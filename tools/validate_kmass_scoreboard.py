#!/usr/bin/env python3
"""Validate KMASS scoreboards against the metric contract's own gate rule.

docs/kmass-metrics-v1.md ends with a Gate implication:

    No phase should be marked complete unless the metrics for that phase are
    attached to: a named measurement protocol, evidence artifacts, an
    acceptance threshold, and a reproducible run log.

That sentence has never been enforced by anything. This is the enforcement.
It is deliberately fail-closed: a scoreboard that is silent about a metric,
or that claims a phase without the four required attachments, is a FAILURE --
not a warning -- because the failure mode this program is trying to cure is
exactly "declared but never verified".

Two rules carry most of the weight:

  * COVERAGE. Every metric id in the contract must appear in the scoreboard.
    Omitting an inconvenient metric is the cheapest way to fake progress, so
    a missing row fails rather than passes quietly.

  * NO VACUOUS PHASE CLAIMS. A metric whose measured value meets a target but
    whose result is not meaningful (latency over an empty corpus, accuracy
    over an empty result set) must set vacuousPass=true, and may not claim a
    phase. A number that looks like success while measuring nothing is worse
    than a missing number, because it survives review.

Usage:
    python3 tools/validate_kmass_scoreboard.py [scoreboard.json ...]

With no arguments, validates every file in scoreboards/.
Exit 0 = valid; exit 1 = one or more violations.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/kmass-scoreboard.v0.1.schema.json"
CONTRACT = ROOT / "docs/kmass-metrics-v1.md"
SCOREBOARD_DIR = ROOT / "scoreboards"

VALID_STATES = {"MEASURED", "UNMEASURED", "UNBUILT"}
VALID_PHASE_CLAIMS = {"none", "phase1", "phase2", "phase3"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: file not found: {path}")
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path.name} is not valid JSON: {exc}")
        sys.exit(1)


def json_type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    return "object"


def type_matches(value: Any, expected: str) -> bool:
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    return json_type_name(value) == expected


def validate_schema(schema: dict[str, Any], value: Any, path: str, errors: list[str]) -> None:
    """Structural validation driven by the schema file itself.

    Matches the walker convention already used by validate_orggov_scorecard.py
    (stdlib only, no jsonschema dependency). This exists because a schema that
    nothing validates against is documentation wearing a contract's clothes --
    the precise failure this whole scoreboard effort is meant to cure. The
    semantic gate rules below layer on top of this; they do not replace it.
    """
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in enum {schema['enum']!r}")
    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(type_matches(value, t) for t in expected_types):
            errors.append(f"{path}: expected type {expected_types!r}, got {json_type_name(value)!r}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = sorted(set(value) - set(properties))
            if extra:
                errors.append(f"{path}: unexpected properties {extra!r}")
        additional = schema.get("additionalProperties")
        for key, item in value.items():
            child = properties.get(key)
            if child is None and isinstance(additional, dict):
                child = additional
            if child is not None:
                validate_schema(child, item, f"{path}.{key}", errors)
    if isinstance(value, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            errors.append(f"{path}: expected at least {min_items} item(s), got {len(value)}")
        item_schema = schema.get("items")
        if item_schema is not None:
            for i, item in enumerate(value):
                validate_schema(item_schema, item, f"{path}[{i}]", errors)


def contract_metric_ids() -> set[str]:
    """Parse the metric ids out of the contract's canonical metric table.

    Deriving the expected set from the contract rather than hardcoding it here
    means adding a metric to the contract automatically makes every existing
    scoreboard incomplete until it is measured -- which is the intended
    pressure. A hardcoded list would silently drift from the contract.
    """
    if not CONTRACT.exists():
        print(f"FAIL: metric contract missing: {CONTRACT}")
        sys.exit(1)
    text = CONTRACT.read_text(encoding="utf-8")
    ids = set(re.findall(r"`([A-Z]{2,4}(?:\.[A-Z_]+){1,3})`", text))
    if not ids:
        print(f"FAIL: no metric ids parsed from {CONTRACT.name} -- contract format changed?")
        sys.exit(1)
    return ids


def validate(path: Path, expected_ids: set[str], schema: dict[str, Any]) -> list[str]:
    doc = load_json(path)
    errors: list[str] = []

    def err(msg: str) -> None:
        errors.append(msg)

    # Structural pass against the schema file itself, first -- a schema that
    # is never applied is decoration, not a contract. The checks below layer
    # semantic/cross-field gate rules the generic walker can't express
    # (contract-derived coverage, the vacuous-pass rule, phase-claim
    # attachment requirements), so both passes run; neither replaces the other.
    validate_schema(schema, doc, "$", errors)
    if errors:
        return errors

    if doc.get("schemaVersion") != "kmass.scoreboard.v0.1":
        err(f"schemaVersion must be 'kmass.scoreboard.v0.1', got {doc.get('schemaVersion')!r}")
    if doc.get("recordType") != "KmassScoreboard":
        err(f"recordType must be 'KmassScoreboard', got {doc.get('recordType')!r}")

    for field in ("recordId", "metricsContractRef", "measuredAt", "environment", "metrics", "provenance"):
        if field not in doc:
            err(f"missing required top-level field: {field}")
    if errors:
        return errors

    prov = doc.get("provenance", {})
    for field in ("createdBy", "createdAt", "nonSecret", "method"):
        if field not in prov:
            err(f"provenance missing required field: {field}")
    if prov.get("nonSecret") is not True:
        err("provenance.nonSecret must be true -- scoreboards are published artifacts")

    metrics = doc.get("metrics", [])
    if not isinstance(metrics, list) or not metrics:
        err("metrics must be a non-empty array")
        return errors

    seen: set[str] = set()
    for i, m in enumerate(metrics):
        mid = m.get("metricId", f"<index {i}>")
        if mid in seen:
            err(f"{mid}: duplicate metric entry")
        seen.add(mid)

        state = m.get("state")
        if state not in VALID_STATES:
            err(f"{mid}: state must be one of {sorted(VALID_STATES)}, got {state!r}")
            continue

        claim = m.get("phaseClaim", "none")
        if claim not in VALID_PHASE_CLAIMS:
            err(f"{mid}: phaseClaim must be one of {sorted(VALID_PHASE_CLAIMS)}, got {claim!r}")
            continue

        vacuous = bool(m.get("vacuousPass", False))

        if state == "MEASURED":
            if m.get("measuredValue") is None:
                err(f"{mid}: state=MEASURED but measuredValue is null")
            if not m.get("runLog"):
                err(f"{mid}: state=MEASURED requires a reproducible runLog (contract gate rule)")
            if not m.get("evidenceArtifacts"):
                err(f"{mid}: state=MEASURED requires at least one evidenceArtifact (contract gate rule)")
        else:
            # UNMEASURED / UNBUILT must say why, or the gap is invisible.
            if not m.get("blockedBy"):
                err(f"{mid}: state={state} requires a non-empty blockedBy explaining what is missing")
            if claim != "none":
                err(f"{mid}: state={state} cannot carry phaseClaim={claim!r}")

        # The gate rule proper: a phase claim needs all four attachments.
        if claim != "none":
            missing = [
                name for name, present in (
                    ("measurementProtocol", bool(m.get("measurementProtocol"))),
                    ("evidenceArtifacts", bool(m.get("evidenceArtifacts"))),
                    ("runLog", bool(m.get("runLog"))),
                    ("phaseTargets", bool(m.get("phaseTargets"))),
                ) if not present
            ]
            if missing:
                err(f"{mid}: claims {claim} without required attachment(s): {', '.join(missing)} "
                    f"(docs/kmass-metrics-v1.md Gate implication)")
            if vacuous:
                err(f"{mid}: vacuousPass=true cannot be combined with phaseClaim={claim!r} -- "
                    f"a result that meets a target without meaning anything is not a phase claim")

        if vacuous and not m.get("notes"):
            err(f"{mid}: vacuousPass=true requires notes explaining why the pass is not meaningful")

    missing_ids = expected_ids - seen
    if missing_ids:
        err(f"COVERAGE: contract defines metric(s) absent from this scoreboard: "
            f"{', '.join(sorted(missing_ids))} -- every contract metric must be reported, "
            f"even if only as UNMEASURED/UNBUILT")

    unknown_ids = seen - expected_ids
    if unknown_ids:
        err(f"scoreboard reports metric id(s) not present in the contract: {', '.join(sorted(unknown_ids))}")

    return errors


def main(argv: list[str]) -> int:
    if not SCHEMA.exists():
        print(f"FAIL: schema missing: {SCHEMA}")
        return 1
    schema = load_json(SCHEMA)

    expected = contract_metric_ids()

    if argv:
        paths = [Path(a) for a in argv]
    else:
        paths = sorted(SCOREBOARD_DIR.glob("*.json")) if SCOREBOARD_DIR.exists() else []

    if not paths:
        print("FAIL: no scoreboards found to validate. A program with a metric "
              "contract and zero scoreboards has never measured itself.")
        return 1

    total_errors = 0
    for p in paths:
        errs = validate(p, expected, schema)
        if errs:
            total_errors += len(errs)
            print(f"\nFAIL {p.name} -- {len(errs)} violation(s):")
            for e in errs:
                print(f"  - {e}")
        else:
            doc = load_json(p)
            ms = doc.get("metrics", [])
            measured = sum(1 for m in ms if m.get("state") == "MEASURED")
            vac = sum(1 for m in ms if m.get("vacuousPass"))
            claims = sum(1 for m in ms if m.get("phaseClaim", "none") != "none")
            print(f"OK   {p.name}: {len(ms)} metrics ({measured} measured, "
                  f"{vac} vacuous, {claims} phase claims), contract coverage complete")

    if total_errors:
        print(f"\n{total_errors} violation(s) across {len(paths)} scoreboard(s).")
        return 1
    print(f"\nAll {len(paths)} scoreboard(s) valid against {CONTRACT.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

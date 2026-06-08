#!/usr/bin/env python3
"""Validate IOES delivery outcome record schema and fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/ioes-delivery-outcome-record.schema.json"
VALID_EXAMPLE = ROOT / "examples/ioes-delivery-outcome-record.valid.json"
REJECTED_EXAMPLE = ROOT / "examples/ioes-delivery-outcome-record.rejected.productivity-only.json"

REQUIRED_METRIC_NAMES = {
    "stewardship_debt_count",
    "successor_coverage_ratio",
    "evidence_completeness_ratio",
    "human_agency_preserved",
    "surveillance_use_prohibited",
}

FORBIDDEN_HUMAN_VALUE_METRICS = {
    "hours_online",
    "tickets_closed",
    "messages_sent",
    "velocity_points",
    "engagement_time",
    "rank_score",
}

PRIVILEGED_SAFETY_CLASSES = {"privileged", "prohibited"}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def json_type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def type_matches(value: Any, expected: str) -> bool:
    actual = json_type_name(value)
    if expected == "number":
        return actual in {"integer", "number"}
    return actual == expected


def validate_schema(schema: dict[str, Any], value: Any, path: str = "$") -> None:
    if "const" in schema and value != schema["const"]:
        fail(f"{path}: expected const {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        fail(f"{path}: {value!r} not in enum {schema['enum']!r}")
    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(type_matches(value, item) for item in expected_types):
            fail(f"{path}: expected type {expected_types!r}, got {json_type_name(value)!r}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                fail(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = sorted(set(value) - set(properties))
            if extra:
                fail(f"{path}: unexpected properties {extra!r}")
        additional = schema.get("additionalProperties")
        for key, item in value.items():
            child_schema = properties.get(key)
            if child_schema is None and isinstance(additional, dict):
                child_schema = additional
            if child_schema is not None:
                validate_schema(child_schema, item, f"{path}.{key}")
    if isinstance(value, list):
        min_items = schema.get("minItems", 0)
        if len(value) < min_items:
            fail(f"{path}: expected at least {min_items} items, got {len(value)}")
        item_schema = schema.get("items")
        if item_schema is not None:
            for index, item in enumerate(value):
                validate_schema(item_schema, item, f"{path}[{index}]")
    minimum = schema.get("minimum")
    maximum = schema.get("maximum")
    if minimum is not None and isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < minimum:
            fail(f"{path}: value {value} is below minimum {minimum}")
    if maximum is not None and isinstance(value, (int, float)) and not isinstance(value, bool):
        if value > maximum:
            fail(f"{path}: value {value} exceeds maximum {maximum}")


def validate_invariants(record: dict[str, Any]) -> None:
    if record.get("metricSet") != "ioes-delivery-outcome-v0":
        fail("metricSet must be ioes-delivery-outcome-v0")

    if not record.get("evidenceRefs"):
        fail("evidenceRefs must be non-empty")
    if not record.get("policyRefs"):
        fail("policyRefs must be non-empty")
    if not record.get("stewardshipRefs"):
        fail("stewardshipRefs must be non-empty")

    metrics = record.get("metrics", [])
    metric_names = {m["name"] for m in metrics if isinstance(m, dict)}

    forbidden = sorted(metric_names & FORBIDDEN_HUMAN_VALUE_METRICS)
    if record.get("humanImpacting") and forbidden:
        fail(f"human-impacting IOES records must not use productivity-only human value metrics: {forbidden!r}")

    missing = REQUIRED_METRIC_NAMES - metric_names
    if missing:
        fail(f"missing required IOES delivery metrics: {sorted(missing)!r}")

    rollup = record.get("rollup", {})
    evidence_completeness = rollup.get("evidenceCompleteness")
    if evidence_completeness is not None and not (0.0 <= evidence_completeness <= 1.0):
        fail(f"rollup.evidenceCompleteness must be in [0, 1], got {evidence_completeness}")

    if record.get("humanImpacting"):
        posture = record.get("humanAgencyPosture", {})
        for key in [
            "consentMaintained",
            "appealOrRepairPath",
            "explanationAvailable",
            "automationBounded",
            "surveillanceUseProhibited",
        ]:
            if posture.get(key) is not True:
                fail(f"human-impacting IOES records require humanAgencyPosture.{key}=true")
        if rollup.get("humanAgencyStatus") != "preserved":
            fail("human-impacting IOES records require rollup.humanAgencyStatus='preserved'")

    if record.get("safetyClass") in PRIVILEGED_SAFETY_CLASSES and rollup.get("promotionStatus") == "promoted":
        evidence_refs = record.get("evidenceRefs", [])
        human_review_present = any("review" in ref.lower() or "approval" in ref.lower() for ref in evidence_refs)
        if not human_review_present:
            fail("privileged/prohibited IOES records cannot be promoted without explicit review evidence")

    non_claims = " ".join(record.get("nonClaims", [])).lower()
    if "human worth" not in non_claims:
        fail("nonClaims must state that the record is not a measure of human worth")
    if "productivity" not in non_claims:
        fail("nonClaims must reject productivity-score interpretation")


def validate_expected_valid(schema: dict[str, Any], path: Path) -> None:
    doc = load_json(path)
    validate_schema(schema, doc)
    validate_invariants(doc)


def validate_expected_rejected(schema: dict[str, Any], path: Path) -> str:
    try:
        doc = load_json(path)
        validate_schema(schema, doc)
        validate_invariants(doc)
    except ValidationError as exc:
        return str(exc)
    fail(f"rejected fixture unexpectedly passed: {path.relative_to(ROOT)}")


def main() -> int:
    try:
        schema = load_json(SCHEMA)
        validate_expected_valid(schema, VALID_EXAMPLE)
        rejected_reason = validate_expected_rejected(schema, REJECTED_EXAMPLE)
    except ValidationError as exc:
        print(f"ERR: {exc}", file=sys.stderr)
        return 2
    print("ok: examples/ioes-delivery-outcome-record.valid.json validates")
    print(f"ok: rejected fixture failed as expected: {rejected_reason}")
    print("OK: IOES delivery outcome validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

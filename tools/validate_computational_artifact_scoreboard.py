#!/usr/bin/env python3
"""Validate computational artifact scoreboard schema and example payload."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/computational-artifact-scoreboard.schema.json"
EXAMPLE = ROOT / "examples/computational-artifact-scoreboard.example.json"

# Metrics required for the computational-artifact-v0 metric set
REQUIRED_METRIC_NAMES = {
    "reproducibility_score",
    "validation_status",
    "feature_count",
    "invalid_feature_count",
    "ingest_latency_ms",
    "artifact_size_bytes",
    "evidence_completeness",
    "promotion_status",
}

# Safety classes that require explicit human review evidence before promotion
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
    if not record.get("evidenceRefs"):
        fail("evidenceRefs must be non-empty")

    metrics = record.get("metrics", [])
    metric_names = {m["name"] for m in metrics if isinstance(m, dict)}
    missing = REQUIRED_METRIC_NAMES - metric_names
    if missing:
        fail(f"missing required metrics for computational-artifact-v0: {sorted(missing)!r}")

    rollup = record.get("rollup", {})

    # Reproducibility score must be in [0, 1]
    repro = rollup.get("reproducibilityScore")
    if repro is not None and not (0.0 <= repro <= 1.0):
        fail(f"rollup.reproducibilityScore must be in [0, 1], got {repro}")

    # evidence_completeness metric must be in [0, 1]
    for m in metrics:
        if isinstance(m, dict) and m.get("name") == "evidence_completeness":
            val = m.get("value")
            if isinstance(val, (int, float)) and not isinstance(val, bool):
                if not (0.0 <= val <= 1.0):
                    fail(f"metrics.evidence_completeness value must be in [0, 1], got {val}")

    # Privileged/prohibited artifacts cannot be promoted without human review evidence
    safety_class = record.get("safetyClass")
    promotion_status = rollup.get("promotionStatus")
    if safety_class in PRIVILEGED_SAFETY_CLASSES and promotion_status == "promoted":
        evidence_refs = record.get("evidenceRefs", [])
        human_review_present = any("review" in ref.lower() or "approval" in ref.lower() for ref in evidence_refs)
        if not human_review_present:
            fail(
                f"artifact with safetyClass={safety_class!r} cannot have promotionStatus='promoted' "
                "without explicit human review evidence in evidenceRefs (ref containing 'review' or 'approval')"
            )


def main() -> int:
    try:
        schema = load_json(SCHEMA)
        example = load_json(EXAMPLE)
        validate_schema(schema, example)
        validate_invariants(example)
    except ValidationError as exc:
        print(f"ERR: {exc}", file=sys.stderr)
        return 2
    print("ok: examples/computational-artifact-scoreboard.example.json validates")
    print("OK: Computational artifact scoreboard validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

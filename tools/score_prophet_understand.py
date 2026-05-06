#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    print(f"ERR: {message}", file=sys.stderr)
    raise SystemExit(2)


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing artifact: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid artifact JSON: {exc}")
    if not isinstance(value, dict):
        fail("artifact root must be an object")
    return value


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def score(artifact: dict[str, Any]) -> dict[str, Any]:
    nodes = [item for item in as_list(artifact.get("nodes")) if isinstance(item, dict)]
    edges = [item for item in as_list(artifact.get("edges")) if isinstance(item, dict)]
    receipts = [item for item in as_list(artifact.get("provenance_receipts")) if isinstance(item, dict)]
    facts: list[dict[str, Any]] = []
    for family in ["nodes", "edges", "summaries", "tours", "diff_impact_sets"]:
        facts.extend([item for item in as_list(artifact.get(family)) if isinstance(item, dict)])

    factual_nodes = [node for node in nodes if node.get("kind") not in {"repo", "directory"}]
    anchored_nodes = [node for node in factual_nodes if isinstance(node.get("source_anchor"), dict)]
    facts_with_receipts = [fact for fact in facts if as_list(fact.get("provenance_receipt_ids"))]

    diff_radius = 0
    for diff in [item for item in as_list(artifact.get("diff_impact_sets")) if isinstance(item, dict)]:
        diff_radius += len(as_list(diff.get("affected_nodes")))
        diff_radius += len(as_list(diff.get("affected_edges")))
        diff_radius += 2 * len(as_list(diff.get("affected_tests")))
        diff_radius += len(as_list(diff.get("affected_docs")))
        diff_radius += 3 * len(as_list(diff.get("affected_policies")))

    policy = artifact.get("policy_status", {}) if isinstance(artifact.get("policy_status"), dict) else {}
    policy_checks = [check for check in as_list(policy.get("checks")) if isinstance(check, dict)]
    warning_count = sum(1 for check in policy_checks if check.get("state") in {"warn", "require_review"})
    deny_count = sum(1 for check in policy_checks if check.get("state") == "deny")

    anchor_ratio = len(anchored_nodes) / len(factual_nodes) if factual_nodes else 1.0
    provenance_ratio = len(facts_with_receipts) / len(facts) if facts else 1.0
    schema_valid = artifact.get("schema_version") == "prophet-understanding.v0"

    if not schema_valid or deny_count:
        state = "red"
    elif warning_count or anchor_ratio < 0.95 or provenance_ratio < 0.95:
        state = "yellow"
    else:
        state = "green"

    repo = artifact.get("repo", {}) if isinstance(artifact.get("repo"), dict) else {}
    return {
        "repo_full_name": repo.get("full_name", "unknown"),
        "repo_commit": repo.get("commit", "unknown"),
        "schema_version": artifact.get("schema_version", "unknown"),
        "repo_graph_present": 1,
        "repo_graph_schema_valid": 1 if schema_valid else 0,
        "repo_graph_node_count": len(nodes),
        "repo_graph_edge_count": len(edges),
        "repo_graph_anchor_coverage_ratio": round(anchor_ratio, 4),
        "repo_graph_provenance_coverage_ratio": round(provenance_ratio, 4),
        "repo_graph_policy_warning_count": warning_count,
        "repo_graph_policy_deny_count": deny_count,
        "repo_pr_impact_radius": diff_radius,
        "repo_ownership_gap_count": sum(1 for node in nodes if node.get("kind") in {"service", "contract", "policy", "schema", "runtime"} and not node.get("metadata", {}).get("owner")),
        "provenance_receipt_count": len(receipts),
        "scorecard_state": state,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score Prophet Understand repo graph artifact for Delivery Excellence.")
    parser.add_argument("--artifact", required=True, help="Path to prophet-understanding.json")
    parser.add_argument("--out", default=None, help="Optional scorecard output path")
    args = parser.parse_args()

    result = score(load(Path(args.artifact)))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()

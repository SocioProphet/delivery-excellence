#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCORER = ROOT / "tools/score_prophet_understand.py"


def fail(message: str) -> None:
    print(f"ERR: {message}", file=sys.stderr)
    raise SystemExit(2)


def artifact() -> dict[str, Any]:
    return {
        "schema_version": "prophet-understanding.v0",
        "repo": {"full_name": "SocioProphet/delivery-fixture", "default_branch": "main", "commit": "abcdef1", "generated_at": "2026-05-05T00:00:00Z", "artifact_hash": "sha256:fixture"},
        "generator": {"name": "smart-tree", "version": "fixture", "parser_versions": {"fixture": "v0"}},
        "agent_identity": {"kind": "fixture", "id": "agent://fixture", "did": None},
        "nodes": [
            {"id": "repo:SocioProphet/delivery-fixture", "kind": "repo", "label": "repo", "path": ".", "confidence": 1.0, "provenance_receipt_ids": ["receipt:run"], "metadata": {}},
            {"id": "contract:demo", "kind": "contract", "label": "demo contract", "path": "contracts/demo.json", "source_anchor": {"path": "contracts/demo.json", "start_line": 1, "end_line": 1, "content_hash": "sha256:contract"}, "confidence": 1.0, "provenance_receipt_ids": ["receipt:contract"], "metadata": {}},
            {"id": "test:demo", "kind": "test", "label": "demo test", "path": "tests/demo_test.py", "source_anchor": {"path": "tests/demo_test.py", "start_line": 1, "end_line": 1, "content_hash": "sha256:test"}, "confidence": 1.0, "provenance_receipt_ids": ["receipt:test"], "metadata": {}},
        ],
        "edges": [{"id": "edge:test-covers-contract", "kind": "tests", "source": "test:demo", "target": "contract:demo", "confidence": 1.0, "provenance_receipt_ids": ["receipt:test"], "metadata": {}}],
        "summaries": [{"id": "summary:demo", "node_id": "contract:demo", "text": "demo contract", "confidence": 0.9, "provenance_receipt_ids": ["receipt:contract"]}],
        "tours": [],
        "diff_impact_sets": [{"id": "diff-impact:demo", "base": "aaa", "head": "bbb", "changed_paths": ["contracts/demo.json"], "affected_nodes": ["contract:demo"], "affected_edges": ["edge:test-covers-contract"], "affected_tests": ["test:demo"], "affected_docs": [], "affected_policies": [], "risk": "low", "requires_review": False, "provenance_receipt_ids": ["receipt:contract"]}],
        "provenance_receipts": [
            {"id": "receipt:run", "claim_type": "repo-scan", "generator": "smart-tree", "parser_version": "fixture", "input_source_hash": "sha256:run", "generated_at": "2026-05-05T00:00:00Z", "confidence": 1.0, "validation_state": "valid", "warnings": []},
            {"id": "receipt:contract", "claim_type": "contract-node", "generator": "smart-tree", "parser_version": "fixture", "input_source_hash": "sha256:contract", "generated_at": "2026-05-05T00:00:00Z", "confidence": 1.0, "validation_state": "valid", "warnings": []},
            {"id": "receipt:test", "claim_type": "test-node", "generator": "smart-tree", "parser_version": "fixture", "input_source_hash": "sha256:test", "generated_at": "2026-05-05T00:00:00Z", "confidence": 1.0, "validation_state": "valid", "warnings": []}
        ],
        "validation_results": [],
        "policy_status": {"state": "allow", "checks": [{"id": "policy:fixture", "state": "allow", "message": "fixture", "evidence_receipt_ids": ["receipt:run"]}]}
    }


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="delivery-prophet-understand-") as raw_tmp:
        tmp = Path(raw_tmp)
        artifact_path = tmp / "prophet-understanding.json"
        out = tmp / "scorecard.json"
        artifact_path.write_text(json.dumps(artifact(), indent=2, sort_keys=True), encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCORER), "--artifact", str(artifact_path), "--out", str(out)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        if result.returncode != 0:
            print(result.stdout, file=sys.stderr)
            fail("score helper exited nonzero")
        payload = json.loads(out.read_text(encoding="utf-8"))
        if payload.get("scorecard_state") != "yellow":
            # yellow is expected because the contract/schema node has no owner metadata yet.
            fail(f"expected yellow scorecard state, got {payload.get('scorecard_state')}")
        if payload.get("repo_graph_schema_valid") != 1:
            fail("schema validity metric not set")
        if payload.get("repo_pr_impact_radius") != 4:
            fail(f"unexpected impact radius: {payload.get('repo_pr_impact_radius')}")
        print("OK: Delivery Excellence Prophet Understand score smoke passed")


if __name__ == "__main__":
    main()

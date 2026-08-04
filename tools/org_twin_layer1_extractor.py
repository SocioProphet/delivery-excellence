#!/usr/bin/env python3
"""Org digital twin, Layer 1 -- the inventory graph.

See docs/design/org-digital-twin-v0.md. This is the "first concrete step": a
read-only extractor over workspace-inventory/repos.yaml plus a live `gh` probe,
producing a graph and the |K| / |E| variables for the SYS.SCALE metric row.

Layer 1 is deliberately narrow. It does NOT model tasks, policies, roles, or
throughput (that is Layer 2). It models exactly what repos.yaml already
declares -- repos, their declared capabilities (`provides`), and their declared
relationships (`related_repos`) -- and then checks each repo against the real
GitHub API rather than trusting the declaration.

Declared vs verified (docs/design/org-digital-twin-v0.md's honesty constraint):
a repo node that repos.yaml lists but that does not actually exist on GitHub is
a hypothesis, not a fact. This extractor renders that distinction explicitly
rather than silently trusting the file. |K| and |E| are reported for the FULL
declared graph and separately for the VERIFIED-only subgraph -- the scoreboard
should cite the verified numbers, not the declared ones, exactly as the design
doc requires ("An edge that has never been probed is a hypothesis, not a
fact").
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Callable

import yaml


def load_repos_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def gh_repo_exists(org: str, name: str) -> bool:
    """Live probe: does this repo actually exist on GitHub? Fail-closed --
    anything other than a clean success (network error, auth error, timeout)
    is treated as NOT verified, never silently assumed to exist."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{org}/{name}"],
            capture_output=True,
            timeout=30,
            check=False,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, OSError):
        return False


def build_graph(data: dict, probe: Callable[[str, str], bool]) -> dict:
    """Build the Layer 1 graph. `probe` is injectable so tests can run without
    hitting the network."""
    default_org = data.get("org", "")
    repos = data.get("repos", [])

    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    for r in repos:
        name = r["name"]
        org = r.get("org", default_org)
        repo_key = f"repo:{org}/{name}"
        verified = probe(org, name)
        nodes[repo_key] = {
            "id": repo_key,
            "type": "repo",
            "name": name,
            "org": org,
            "authority_role": r.get("authority_role"),
            "status": r.get("status"),
            "declared": True,
            "verified": verified,
        }

        for cap in r.get("provides", []) or []:
            cap_key = f"capability:{cap}"
            if cap_key not in nodes:
                nodes[cap_key] = {
                    "id": cap_key,
                    "type": "capability",
                    "name": cap,
                    "declared": True,
                    # A capability node's "verification" is inherited from
                    # whether the repo that provides it was itself verified --
                    # a capability declared by a nonexistent repo is exactly as
                    # much a hypothesis as the repo is.
                    "verified": False,
                }
            if verified:
                nodes[cap_key]["verified"] = True
            edges.append(
                {
                    "from": repo_key,
                    "to": cap_key,
                    "type": "provides",
                    "declared": True,
                    "verified": verified,
                }
            )

        for related in r.get("related_repos", []) or []:
            # related_repos entries are bare names (same org, per schema.json);
            # the target may or may not itself be a repo declared elsewhere in
            # this file -- resolve lazily below, once every repo is loaded.
            edges.append(
                {
                    "from": repo_key,
                    "to": f"repo:{org}/{related}",
                    "type": "related_to",
                    "declared": True,
                    "verified": None,  # resolved below
                }
            )

    # Resolve related_to edge verification now that all repo nodes exist:
    # verified only if BOTH endpoints are verified repo nodes.
    for e in edges:
        if e["type"] == "related_to":
            target = nodes.get(e["to"])
            source = nodes.get(e["from"])
            e["verified"] = bool(
                source and source.get("verified") and target and target.get("verified")
            )
            if target is None:
                # related_repos pointed at a name repos.yaml never declared as
                # its own entry -- record it as an unresolved reference, not a
                # silent drop.
                e["to_unresolved"] = True

    return {"nodes": list(nodes.values()), "edges": edges}


def summarize(graph: dict) -> dict:
    nodes = graph["nodes"]
    edges = graph["edges"]
    verified_nodes = [n for n in nodes if n["verified"]]
    verified_edges = [e for e in edges if e.get("verified")]
    return {
        "declared": {"K": len(nodes), "E": len(edges)},
        "verified": {"K": len(verified_nodes), "E": len(verified_edges)},
        "by_type": {
            "repo_nodes": len([n for n in nodes if n["type"] == "repo"]),
            "capability_nodes": len([n for n in nodes if n["type"] == "capability"]),
            "provides_edges": len([e for e in edges if e["type"] == "provides"]),
            "related_to_edges": len([e for e in edges if e["type"] == "related_to"]),
        },
        "unresolved_related_repos": [e["to"] for e in edges if e.get("to_unresolved")],
        "unverified_repos": [n["id"] for n in nodes if n["type"] == "repo" and not n["verified"]],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--repos-yaml",
        type=Path,
        default=Path.home() / "dev" / "workspace-inventory" / "inventory" / "repos.yaml",
        help="Path to workspace-inventory's repos.yaml",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Write the full graph JSON here (nodes+edges). Prints the summary to stdout regardless.",
    )
    ap.add_argument(
        "--offline",
        action="store_true",
        help="Skip live gh probes; treat nothing as verified (for local dry runs without network/auth).",
    )
    args = ap.parse_args()

    if not args.repos_yaml.exists():
        print(f"::error::repos.yaml not found at {args.repos_yaml}", file=sys.stderr)
        return 1

    data = load_repos_yaml(args.repos_yaml)
    probe = (lambda org, name: False) if args.offline else gh_repo_exists
    graph = build_graph(data, probe)
    summary = summarize(graph)

    print(json.dumps(summary, indent=2))

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump({"graph": graph, "summary": summary}, f, indent=2)
        print(f"wrote full graph to {args.out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Adversarial proof that org_twin_layer1_extractor distinguishes declared from
verified -- the honesty constraint docs/design/org-digital-twin-v0.md requires.
Fires both ways: a repo that exists must be verified, one that doesn't must not,
and a capability's/edge's verification must depend on its actual repo's
verification, not on the declaration alone.

Local-only, stdlib + the module under test. Does not touch the network -- the
`gh` probe is injected as a fake.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from org_twin_layer1_extractor import build_graph, summarize  # noqa: E402

FIXTURE = {
    "workspace_inventory_version": 1,
    "org": "SocioProphet",
    "repos": [
        {
            "name": "real-repo",
            "kind": "tool",
            "manifest": "WORKSPACE.yaml",
            "authority_role": "test",
            "provides": ["shared-capability", "real-only-capability"],
            "related_repos": ["ghost-repo"],
        },
        {
            "name": "ghost-repo",  # declared here AND as a related_repos target,
            # but the fake probe will report it does not exist -- proves an
            # entry in repos.yaml itself can be unverified, not just a dangling
            # reference.
            "kind": "tool",
            "manifest": "WORKSPACE.yaml",
            "authority_role": "test",
            "provides": ["shared-capability"],
        },
    ],
}


def fake_probe_real_only(org: str, name: str) -> bool:
    return name == "real-repo"


def test_verified_and_declared_diverge_correctly():
    graph = build_graph(FIXTURE, fake_probe_real_only)
    nodes = {n["id"]: n for n in graph["nodes"]}

    assert nodes["repo:SocioProphet/real-repo"]["verified"] is True
    assert nodes["repo:SocioProphet/ghost-repo"]["verified"] is False

    # A capability provided ONLY by the ghost repo must not be verified.
    assert nodes["capability:real-only-capability"]["verified"] is True
    assert nodes["capability:shared-capability"]["verified"] is True  # real-repo also provides it

    # related_to edge from real-repo -> ghost-repo must be unverified: BOTH
    # endpoints must be verified for the edge to be verified, not just one.
    related_edges = [e for e in graph["edges"] if e["type"] == "related_to"]
    assert len(related_edges) == 1
    assert related_edges[0]["verified"] is False


def test_summary_counts_declared_vs_verified_separately():
    graph = build_graph(FIXTURE, fake_probe_real_only)
    summary = summarize(graph)

    # Declared: 2 repos + 2 capability nodes (shared, real-only) = 4 nodes.
    assert summary["declared"]["K"] == 4
    # Verified: only real-repo's repo node + both capabilities it provides
    # (shared-capability is verified because real-repo, a verified repo, also
    # provides it) = 3.
    assert summary["verified"]["K"] == 3
    assert "repo:SocioProphet/ghost-repo" in summary["unverified_repos"]
    assert "repo:SocioProphet/real-repo" not in summary["unverified_repos"]


def fake_probe_none_exist(org: str, name: str) -> bool:
    return False


def test_fires_when_nothing_verifies():
    """The other direction: if the probe reports nothing exists (e.g. the
    --offline mode, or a real outage), verified counts must drop to zero, not
    silently fall back to "assume declared == verified"."""
    graph = build_graph(FIXTURE, fake_probe_none_exist)
    summary = summarize(graph)
    assert summary["verified"]["K"] == 0
    assert summary["verified"]["E"] == 0
    assert set(summary["unverified_repos"]) == {
        "repo:SocioProphet/real-repo",
        "repo:SocioProphet/ghost-repo",
    }


def fake_probe_all_exist(org: str, name: str) -> bool:
    return True


def test_fires_when_everything_verifies():
    graph = build_graph(FIXTURE, fake_probe_all_exist)
    summary = summarize(graph)
    assert summary["verified"]["K"] == summary["declared"]["K"]
    assert summary["verified"]["E"] == summary["declared"]["E"]
    assert summary["unverified_repos"] == []


def test_unresolved_related_repos_target_is_flagged_not_silently_dropped():
    fixture = {
        "org": "SocioProphet",
        "repos": [
            {
                "name": "lonely-repo",
                "kind": "tool",
                "manifest": "WORKSPACE.yaml",
                "related_repos": ["never-declared-anywhere"],
            }
        ],
    }
    graph = build_graph(fixture, fake_probe_all_exist)
    summary = summarize(graph)
    assert "repo:SocioProphet/never-declared-anywhere" in summary["unresolved_related_repos"]


if __name__ == "__main__":
    failures = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL {name}: {e}")
    raise SystemExit(1 if failures else 0)

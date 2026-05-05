# Prophet Understand Metrics

## Purpose

Delivery Excellence measures Prophet Understand / Repo Intelligence v0 adoption, freshness, coverage, drift, PR impact radius, ownership gaps, validation failures, and agent evidence quality.

This metric lane prevents repo graphs from becoming decorative artifacts. The graph must stay fresh, evidence-backed, and operationally useful.

## Metric definitions

### `repo_graph_present`

Boolean. `1` when `.prophet/prophet-understanding.json` exists for the repo/ref being assessed.

### `repo_graph_schema_valid`

Boolean. `1` when the artifact validates against `prophet-understanding.v0`.

### `repo_graph_freshness_seconds`

Current assessment time minus artifact `repo.generated_at`.

### `repo_graph_commit_match`

Boolean. `1` when artifact `repo.commit` matches the assessed commit or is explicitly declared compatible with it.

### `repo_graph_node_count`

Number of graph nodes.

### `repo_graph_edge_count`

Number of graph edges.

### `repo_graph_anchor_coverage_ratio`

Factual non-repo and non-directory nodes with source anchors divided by total factual non-repo and non-directory nodes.

### `repo_graph_provenance_coverage_ratio`

Nodes, edges, summaries, tours, and diff-impact records with at least one provenance receipt divided by all such graph facts.

### `repo_graph_policy_warning_count`

Count of policy checks with `warn` or `require_review` state.

### `repo_pr_impact_radius`

Weighted count of affected nodes, edges, tests, docs, and policies in a diff impact set.

Suggested v0 formula:

```text
impact_radius = affected_nodes + affected_edges + 2*affected_tests + affected_docs + 3*affected_policies
```

### `repo_ownership_gap_count`

Count of service, contract, policy, schema, or runtime nodes without ownership metadata or ownership edge.

### `agent_graph_claims_with_evidence_ratio`

Agent graph-backed claims with node/edge/source/provenance citations divided by total graph-backed claims in the work output.

## Scorecard states

- `green`: valid, fresh, high provenance and source-anchor coverage, no high-risk policy state.
- `yellow`: valid but stale, partial coverage, or policy warnings.
- `red`: invalid schema, missing provenance, unsafe hooks, high impact without review, or denied policy state.
- `gray`: graph artifact missing or not yet onboarded.

## Reporting rules

Do not reward graph size by itself. Large node/edge counts without source anchors and provenance are lower quality than smaller validated graphs.

Warnings and hard failures must be reported separately. v0 graph absence should not become universal failure until scanner adoption is real.

## First adoption targets

Track these lanes independently:

- platform contract: `prophet-platform`
- scanner/emitter: `smart-tree`
- local index: `lampstand`
- search: `sherlock-search`
- ontology: `ontogenesis`
- agent skills: `agent-registry`
- graph-aware dispatch: `agentplane`
- policy gates: `policy-fabric`
- UI workbench: `socioprophet`

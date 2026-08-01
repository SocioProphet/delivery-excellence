# Org Digital Twin v0 — the SYS.SCALE instrument

**Status:** design, not built
**Unblocks:** `SYS.SCALE.TBD` in [`docs/kmass-metrics-v1.md`](../kmass-metrics-v1.md)
**Work order:** [`WO-KMASS-01.09`](../work-orders/WO-KMASS-01-close-the-baseline.md)

## Why this is not a side quest

`SYS.SCALE.TBD` is the only row in the metric contract whose phase targets are `TBD / TBD / TBD`. That is usually a sign a metric was hard to specify. Read its variables, though, and the reason is clearer — they are not product measurements at all:

> `|K|` knowledge elements · `|E|` relations or provenance edges · `|P(task)|` policies per task · `|CoP|` communities of practice and role distributions · task throughput by role and CoP

Every one of those describes **the organization**, not the software. There is no way to fill this row by instrumenting a service. It requires a model of the org itself: what it knows, who does what, which policies bind which tasks, and how work actually flows between roles.

That model is the digital twin. So the twin isn't an adjacent ambition to bolt on after the metrics work — it is the missing instrument for the one metric the contract couldn't specify. Building it closes the last row and, in the same move, gives you the thing you actually want: a substrate to run scenarios against before committing roadmap decisions.

## What the twin has to be to be useful

A digital twin that is merely a diagram of the org is a wall poster. To be an instrument it has to satisfy three properties, in increasing order of difficulty:

**1. It is derived, not authored.** If the twin is hand-maintained it will drift from reality within a quarter and quietly become fiction — the same failure as a hand-maintained architecture diagram, and the same failure the estate already has a name for. Its nodes and edges must be *extracted* from systems that are already load-bearing: repos and their manifests, `workspace-inventory`'s `repos.yaml` authority roles, `agent-registry` identities and grants, `policy-fabric` policy bindings, `ontogenesis` semantics, CI run history, PR and review flow. A fact that has no upstream system to derive it from does not belong in the twin.

**2. It is measured against the same gate as everything else.** The twin emits a `SYS.SCALE` value into a KMASS scoreboard and is subject to `validate_kmass_scoreboard.py` like any other metric. If the twin cannot produce evidence artifacts and a reproducible run log, it doesn't get to make a claim. No exemption for the instrument.

**3. It is counterfactual.** A twin you can only read is a dashboard. The point is to ask *what if* — and get a defensible answer. That is the third property and the hardest, so it comes last, not first.

## Layering

Build in this order. Each layer is independently useful, which matters because the estate's characteristic failure is large designs that never reach enforcement.

### Layer 1 — Inventory graph (derived, static)

Nodes: repos, services, capabilities, policies, contracts, roles, agents.
Edges: `provides`, `consumes`, `governed_by`, `owned_by`, `depends_on`.

Almost all of this already exists in fragments. `workspace-inventory/inventory/repos.yaml` is the strongest seed — it already carries `authority_role`, `provides`, `consumes`, `consumed_by`, `adoption_state`, `validation_state`, and `drift_risk` per repo. That file is a partial org twin that nobody has called one.

Yields immediately: `|K|` (knowledge elements) and `|E|` (provenance/relation edges) — the first two `SYS.SCALE` variables, from data that exists today.

### Layer 2 — Work and policy overlay (derived, dynamic)

Overlay onto Layer 1: tasks in flight, which policies bind which task types, which roles are permitted which actions, throughput and cycle time per role.

Sources: `delivery-excellence` work-item schemas and boards, `policy-fabric` bindings, `agent-registry` grants, CI/PR history for real throughput rather than declared throughput.

Yields: `|P(task)|`, `|CoP|`, role distributions, task throughput by role — completing the `SYS.SCALE` variable set.

**This is the point at which the row can be filled and phase targets can finally be set with real numbers instead of TBD.** Targets set from a measured baseline are defensible; targets set from imagination are the thing that produced TBD in the first place.

### Layer 3 — Scenario engine (counterfactual)

Only now does simulation make sense, because only now is there a calibrated model to perturb.

Questions worth being able to answer:

- *If the corpus reaches 20k documents, where does the first bottleneck appear — retrieval latency, policy evaluation, or human review throughput?*
- *If a CoP doubles in size, which policies become the constraint?*
- *If we descope video (WO-01.08), what does the achievable Phase-2 envelope look like?*
- *Which single unblocking action moves the most `UNMEASURED` rows to `MEASURED`?* — the twin should be able to re-derive the work order's own dependency ordering, and if it disagrees with the hand-written ordering, that disagreement is information.

Existing substrate worth reusing rather than rebuilding: `hellgraph` (typed atoms, append-only valuations, deterministic replay) is a good fit for a twin that must be re-runnable and auditable. `meshrush` and `cairnpath-mesh` already describe graph-native traversal over a hypergraph world model. The GBRG blast-radius work is essentially scenario propagation over a dependency graph — the same shape as "what breaks if X changes."

## Honest constraints

- **Layer 3 is not near-term.** Layers 1 and 2 are extraction and aggregation over data that mostly exists. Layer 3 requires a calibrated model, and calibration requires the measured baselines that WO-KMASS-01 is producing. Attempting simulation before the baseline exists produces confident, wrong answers — strictly worse than no answers.
- **A twin derived from declarations inherits their inaccuracy.** `workspace-inventory` records `adoption_state: partial` and `validation_state: unknown` across many entries, and today's baseline found several services whose declared state and measured state diverged sharply. The twin must distinguish *declared* from *verified* edges and render them differently. An edge that has never been probed is a hypothesis, not a fact — the same discipline the scoreboard applies with `MEASURED` vs `UNMEASURED`.
- **Scope the twin to what has an upstream source.** The temptation is to model the org as you wish it were. Every node must trace to a system of record, or it is decoration.

## First concrete step

Build Layer 1 as a read-only extractor that emits a graph from `workspace-inventory/repos.yaml` plus live `gh` repo metadata, and report `|K|` and `|E|` into a `SYS.SCALE` row. Small, entirely derived from existing sources, and it converts the contract's only TBD row into a partial measurement — which is what earns the right to build Layer 2.

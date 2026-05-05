# Agent Harness Absorption Readout — 2026-05-05

Status: v0.1 management readout  
Owner plane: Delivery Excellence  
Scope: cross-estate absorption of Aden/Hive production-agent lessons into SocioProphet, SourceOS, and SociOS-Linux

## Executive summary

The Aden/Hive lessons are now routed into the estate as a cross-plane operating model rather than a development-only framework copy.

The key absorption decision is stable:

- Delivery Excellence owns the performance stack: KPI/OKR definitions, scoreboards, work packaging, cadence, proof-of-value, customer-safe readouts, and agent/human collaboration metrics.
- SocioSphere owns topology and routing, but does not duplicate scoreboards.
- AgentPlane owns runtime execution, run/session evidence, replay, failure diagnosis, evolution patches, and promotion artifacts.
- Policy Fabric / Guardrail Fabric own admission, grants, guardrails, judges, human-control gates, and promotion gates.
- Memory Mesh owns artifact pointers, message-native ledgers, memory snapshots, recall/writeback evidence, and safe metric projections.
- SourceOS owns local execution receipt boundaries across local runtime, shell, browser, model carry, host mutation, and downloads.
- BearBrowser owns governed browser receipts and credential/browser action evidence.
- TurtleTerm owns governed terminal receipts and operator approval evidence.
- SCOPE-D owns defensive validation for skills, MCP servers, browser actions, terminal actions, memory flows, graph robustness, and evolution patches.

## Open absorption PRs

| Repo | PR | Purpose | Status |
|---|---:|---|---|
| `SocioProphet/delivery-excellence` | #9 | Agent harness delivery operating model | Open |
| `SocioProphet/delivery-excellence-automation` | #7 | Agent harness metric contracts and examples | Open |
| `SocioProphet/sociosphere` | #273 | Cross-estate routing to Delivery Excellence | Open |
| `SocioProphet/agentplane` | #107 | Runtime contract vocabulary | Open |
| `SocioProphet/policy-fabric` | #60 | Policy/admission/promotion gate model | Open |
| `SocioProphet/memory-mesh` | #23 | Memory ledger, artifact pointer, and recall/writeback contract | Open |
| `SourceOS-Linux/sourceos-spec` | #93 | SourceOS local execution receipt boundary | Open |
| `SourceOS-Linux/BearBrowser` | #22 | Browser receipt surface | Open |
| `SourceOS-Linux/TurtleTerm` | #5 | Terminal/operator receipt surface | Open |
| `SocioProphet/SCOPE-D` | #1 | Agent harness defensive risk-control lanes | Open |

## Absorbed lessons

### Outcome-first operating model

The unit of management is no longer a task alone. It is an outcome with measurable value, success criteria, risk tier, evidence requirements, policy gates, execution plan, proof artifacts, and review cadence.

### Graph-first visibility

Generated plan graphs and executable graphs become operational visibility artifacts. They support plan review, approval gates, failure-path reasoning, dependency mapping, and Delivery Excellence scoreboards.

### Evidence over logs

Logs are diagnostic, not sufficient proof. The estate now routes toward validated evidence packs, receipt artifacts, replay pointers, policy decisions, human-control events, and artifact hashes.

### Human control as measurable data

Approvals, rejections, overrides, clarifications, risk acceptances, credential grants, scope changes, and promotion approvals are typed control events. They become governance evidence and Delivery Excellence metrics.

### Skills and MCP servers as governed assets

Skills, MCP servers, tool packs, and templates are not incidental helper files. They are capability assets with trust tiers, tests, grants, risk scores, install/readiness state, and deprecation/revocation paths.

### Browser and terminal surfaces as production evidence sources

BearBrowser and TurtleTerm now have explicit receipt responsibilities. Browser and terminal work are not opaque side effects; they produce evidence for AgentPlane, Policy Fabric, Memory Mesh, SCOPE-D, and Delivery Excellence.

### Local-first execution receipts

SourceOS receipt boundaries make local runtime, shell, browser, model carry, host mutation, credential use, downloads, offline posture, and replay eligibility measurable and auditable.

### Defensive validation as delivery metric

SCOPE-D risk checks become scoreboard inputs: skill risk, MCP risk, browser automation risk, terminal action risk, memory risk, graph robustness, evolution-patch risk, blocked promotion count, verified-run count, and control coverage.

## Current coverage scorecard

| Plane | Current score | Status | Rationale |
|---|---:|---|---|
| Delivery model | 80 | Green | Operating model PR is open; needs merge and first generated readout. |
| Metrics automation | 70 | Yellow | Schemas/examples are open; generator still missing. |
| Topology routing | 75 | Yellow | SocioSphere PR is open; some branches may need update/rebase. |
| Runtime contracts | 70 | Yellow | AgentPlane vocabulary exists; schemas and emitters remain. |
| Policy gates | 70 | Yellow | Gate model exists; machine-readable decisions remain. |
| Memory ledger | 65 | Yellow | Spec exists; schemas/validators and runtime export remain. |
| SourceOS receipts | 65 | Yellow | Boundary exists; typed schemas and conformance remain. |
| Browser receipts | 65 | Yellow | Surface exists; policy-enforced examples/verifiers remain. |
| Terminal receipts | 65 | Yellow | Surface exists; command/mutation examples and verifiers remain. |
| Defensive validation | 60 | Yellow | Risk-control lanes exist; fixtures and verified reporting extension remain. |
| Product/customer proof | 45 | Red | Readout contract exists, but live customer-safe projection is not generated yet. |

Overall absorption baseline: **~68%**.

Interpretation: the estate has absorbed the operating model and plane boundaries. It has not yet completed machine-readable implementation, generators, validators, dashboards, or live metric production.

## Immediate next tranche

1. Merge or update/rebase the open absorption PRs.
2. Add generator in `delivery-excellence-automation` for recent repo activity reports from GitHub activity.
3. Add AgentPlane schemas/examples for `OutcomeSpec`, `GraphSpec`, `SessionEnvelope`, `EvidencePack`, `EvolutionPatch`, and `PromotionGate`.
4. Add Policy Fabric machine-readable decision schemas for skill, MCP, browser, terminal, memory, judge, human-control, and promotion gates.
5. Add Memory Mesh schemas/examples and validators for `ArtifactPointer`, `MessageLedgerEvent`, `MemorySnapshot`, and `RecallWritebackEvidence`.
6. Add SourceOS/BearBrowser/TurtleTerm examples and verifiers for receipt classes.
7. Add SCOPE-D safe synthetic fixtures for skill, MCP, browser, terminal, memory, graph, and evolution-patch risks.
8. Generate the first Delivery Excellence scoreboard from real GitHub/repo signals.

## Remaining gaps we should not miss

- Live scoreboards are not generated yet.
- Open PRs are not merged yet.
- Several branches were reported as behind current `main`; they may need update/rebase before merge.
- Runtime emitters do not yet produce all new contract objects.
- Policy gates are still described, not fully enforced for all surfaces.
- Skill/MCP registry implementation remains future work.
- Customer-safe proof-of-value readouts are defined but not generated from evidence packs yet.
- Dashboard/UI presentation remains future work.
- Windows/native portability remains a later adoption lane.
- Billing/usage-ledger hooks remain future work.

## Done criteria for absorption baseline

The absorption baseline is complete when:

- all listed PRs are merged or superseded by equivalent merged work;
- Delivery Excellence can generate at least one cross-estate scoreboard snapshot;
- AgentPlane can emit or reference the core runtime contract artifacts;
- Policy Fabric can validate at least one agent-harness gate decision fixture;
- Memory Mesh can validate at least one artifact pointer / memory snapshot fixture;
- SourceOS/BearBrowser/TurtleTerm can validate at least one local/browser/terminal receipt fixture;
- SCOPE-D can validate at least one safe agent-harness risk fixture;
- a customer-safe proof-of-value readout can be generated from non-sensitive evidence.

# Agent Harness Absorption Readout — 2026-05-05

Status: v0.2 management readout  
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
| `SocioProphet/delivery-excellence` | #9 | Agent harness delivery operating model and management readout | Open |
| `SocioProphet/delivery-excellence-automation` | #7 | Agent harness metric contracts, examples, validator, generator, CI | Open / mergeable |
| `SocioProphet/sociosphere` | #273 | Cross-estate routing to Delivery Excellence | Open |
| `SocioProphet/agentplane` | #107 | Runtime contract vocabulary, schema, example, validator, CI | Open / mergeable |
| `SocioProphet/policy-fabric` | #60 | Policy/admission/promotion gate model, schema, example, validator | Open |
| `SocioProphet/memory-mesh` | #23 | Memory ledger, artifact pointer, schema, example, validator, CI | Open / mergeable |
| `SourceOS-Linux/sourceos-spec` | #93 | SourceOS local execution receipt boundary, schema, example, validator, CI | Open / mergeable |
| `SourceOS-Linux/BearBrowser` | #22 | Browser receipt surface, schema, example, verifier, CI | Open / mergeable |
| `SourceOS-Linux/TurtleTerm` | #5 | Terminal/operator receipt surface, schema, example, verifier, CI | Open / mergeable |
| `SocioProphet/SCOPE-D` | #1 | Agent harness defensive risk-control lanes, schema, example, validator wiring | Open / mergeable |

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
| Delivery model | 85 | Green | Operating model and management readout exist; merge still pending. |
| Metrics automation | 82 | Green | Schemas, examples, validator, generator, and CI workflow are open in PR #7. Live GitHub ingestion remains. |
| Topology routing | 78 | Yellow | SocioSphere routing PR exists; branch may require update before merge. |
| Runtime contracts | 80 | Green | AgentPlane now has docs, composite schema, example, validator, and CI. Runtime emitters remain. |
| Policy gates | 78 | Yellow | Gate model plus first decision schema/example/validator exists; full gate family remains. |
| Memory ledger | 80 | Green | Memory Mesh now has spec, schema, example, validator, and CI. Runtime export remains. |
| SourceOS receipts | 80 | Green | SourceOS spec now has receipt boundary, schema, example, validator, and CI. Runtime producers remain. |
| Browser receipts | 80 | Green | BearBrowser now has receipt surface, schema, example, verifier, and CI. Runtime emission remains. |
| Terminal receipts | 80 | Green | TurtleTerm now has receipt surface, schema, example, verifier, and CI. Runtime emission remains. |
| Defensive validation | 78 | Yellow | SCOPE-D now has risk-control docs, schema, example, and validator wiring. More fixtures remain. |
| Product/customer proof | 62 | Yellow | Customer-proof contract and generator exist; live evidence-pack projection remains. |

Overall absorption baseline: **~79%**.

Interpretation: the estate has moved from routing/prose absorption to first executable validation across the main planes. It still needs merges, rebases where branches are behind, live emitters, recurring scoreboards, and customer-safe readouts generated from real evidence packs.

## Completed this tranche

1. Added Delivery Excellence metric generator for example activity reports.
2. Added AgentPlane runtime contract schema, example, validator, and CI workflow.
3. Added Policy Fabric agent-harness gate-decision schema, example, validator, and Makefile validation wiring.
4. Added Memory Mesh memory-ledger schema, example, validator, and CI workflow.
5. Added SourceOS execution-receipt schema, example, validator, and CI workflow.
6. Added BearBrowser browser-receipt schema, example, verifier, and CI workflow.
7. Added TurtleTerm terminal-receipt schema, example, verifier, and CI workflow.
8. Added SCOPE-D agent-harness risk-assessment schema, example, and validator integration.

## Immediate next tranche

1. Update/rebase branches that are behind current `main`, especially fast-moving SourceOS, BearBrowser, TurtleTerm, SCOPE-D, AgentPlane, and Policy Fabric branches.
2. Merge or supersede the open absorption PRs.
3. Replace example-file input in `delivery-excellence-automation` with live GitHub/repo activity ingestion.
4. Emit AgentPlane `EvidencePack` artifacts using the new runtime contract references.
5. Emit Memory Mesh artifact pointer and snapshot records from real AgentPlane runs.
6. Emit BearBrowser and TurtleTerm receipts from actual verifier/smoke paths.
7. Extend SCOPE-D with additional safe synthetic fixtures for skills, MCP servers, memory poisoning, graph robustness, and evolution-patch risk.
8. Generate the first recurring Delivery Excellence scoreboard from real repository and evidence signals.

## Remaining gaps we should not miss

- Open PRs are not merged yet.
- Several branches are behind current `main`; they may need update/rebase before merge.
- Runtime emitters do not yet produce all new contract objects.
- Policy gates are only partially represented by one decision fixture.
- Skill/MCP registry implementation remains future work.
- Customer-safe proof-of-value readouts are generated from example reports, not real evidence packs yet.
- Dashboard/UI presentation remains future work.
- Windows/native portability remains a later adoption lane.
- Billing/usage-ledger hooks remain future work.

## Done criteria for absorption baseline

The absorption baseline is complete when:

- all listed PRs are merged or superseded by equivalent merged work;
- Delivery Excellence can generate at least one cross-estate scoreboard snapshot from live repo/evidence signals;
- AgentPlane emits or references the core runtime contract artifacts;
- Policy Fabric validates representative gate decision fixtures across browser, terminal, memory, skill/MCP, and promotion gates;
- Memory Mesh validates and emits artifact pointer / memory snapshot fixtures from real runs;
- SourceOS/BearBrowser/TurtleTerm validate and emit at least one local/browser/terminal receipt fixture from actual smoke paths;
- SCOPE-D validates safe agent-harness risk fixtures across at least skill, MCP, browser, terminal, memory, and graph lanes;
- a customer-safe proof-of-value readout is generated from non-sensitive evidence.

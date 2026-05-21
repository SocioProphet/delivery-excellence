# Workspace Operation Plane — Delivery Governance Plan

## Purpose

This document makes DelEx-OS the delivery governance spine for the Workspace Operation Plane integration program. It covers contracts, runtime, ledger, policy, agents, agent registry, zero-trust interop, workspace UI, workstation contracts, SourceOS spec, sourceos-syncd, SourceOS shell, TurtleTerm, BearBrowser, sourceos-devtools, agent-machine, memory/search, superconscious cognition loop, HolographMe identity/delegation, SCOPE-D security exercises, storage/knowledge standards, and package release evidence.

DelEx does not own product runtime or policy authority. DelEx owns the way work enters, moves, proves itself, and gets accepted across the repo estate.

Hard rule: no coding lane can mark complete without a conformance fixture or validation evidence.

---

## Lanes

### Lane 1 — Contracts and conformance
- **Owner repo:** `SocioProphet/prophet-core-contracts#1`
- **Scope:** Canonical contract definitions and conformance test fixtures for the Workspace Operation Plane.
- **Dependencies:** None (foundational layer).
- **Acceptance criteria:** Contract schema published; conformance test fixtures cover all defined contract types; downstream lanes reference pinned contract version.
- **Evidence requirements:** Schema validation report; conformance fixture run log; downstream reference manifest.

### Lane 2 — Runtime
- **Owner repo:** `SocioProphet/prophet-platform#376`
- **Scope:** Runtime skeleton and boot sequence for Workspace Operation Plane integration.
- **Dependencies:** Lane 1 (contracts), Lane 4 (policy gate interface).
- **Acceptance criteria:** Runtime skeleton boots against contracted interface; smoke test passes; no hard-coded policy bypass.
- **Evidence requirements:** Smoke test log; conformance fixture or contract validation receipt.

### Lane 3 — Ledger/evidence
- **Owner repo:** `SocioProphet/prophet-core-ledger#1`
- **Scope:** Evidence plane — emit, store, and query ledger records for workspace operation events.
- **Dependencies:** Lane 1 (contracts).
- **Acceptance criteria:** Ledger schema published; write and query paths validated; records link to originating lane and PR.
- **Evidence requirements:** Schema validation report; example ledger record; read-back test log.

### Lane 4 — Policy
- **Owner repo:** `SocioProphet/policy-fabric#46`
- **Scope:** Policy gate interface for workspace operation admission, redaction, and obligation enforcement.
- **Dependencies:** Lane 1 (contracts), Lane 3 (ledger).
- **Acceptance criteria:** Policy decision schema published; at least one policy rule covers workspace admission; redaction coverage metric reported.
- **Evidence requirements:** Policy decision schema validation; rule fixture run log; redaction coverage report.

### Lane 5 — Agent execution
- **Owner repo:** `SocioProphet/agentplane#85`
- **Scope:** Agent operation compliance — tool grants, authority boundary, replay, and evidence emission for workspace operations.
- **Dependencies:** Lane 1 (contracts), Lane 4 (policy), Lane 20 (agent registry).
- **Acceptance criteria:** Agent workflow bundle references workspace contracts; tool grants scoped; evidence receipt emitted per run.
- **Evidence requirements:** Workflow bundle validation; tool grant fixture; evidence receipt sample.

### Lane 6 — Workspace UI/controller
- **Owner repo:** `SocioProphet/sociosphere#259`
- **Scope:** UI and controller surface for Workspace Operation Plane visibility.
- **Dependencies:** Lane 2 (runtime), Lane 1 (contracts).
- **Acceptance criteria:** UI surfaces workspace state; controller binds to contracted runtime interface; demo playbook shows workspace effect.
- **Evidence requirements:** Demo screenshot or recording; UI contract binding validation.

### Lane 7 — Workstation contracts
- **Owner repo:** `SociOS-Linux/workstation-contracts#28`
- **Scope:** Workstation-level contract definitions for device/session integration with the Workspace Operation Plane.
- **Dependencies:** Lane 1 (contracts).
- **Acceptance criteria:** Workstation contract schema published; at least one conformance example per contract type.
- **Evidence requirements:** Schema validation report; conformance example.

### Lane 8 — SourceOS spec
- **Owner repo:** `SourceOS-Linux/sourceos-spec#87`
- **Scope:** Operating system specification for SourceOS in the Workspace Operation Plane context.
- **Dependencies:** Lane 7 (workstation contracts), Lane 1 (contracts).
- **Acceptance criteria:** Spec document complete for workspace-relevant surfaces; open questions resolved and recorded.
- **Evidence requirements:** Spec document review sign-off; ADR or recorded decision for any open question.

### Lane 9 — Storage standards
- **Owner repo:** `SocioProphet/socioprophet-standards-storage#79`
- **Scope:** Storage standards for workspace operation data persistence and retrieval.
- **Dependencies:** Lane 1 (contracts), Lane 3 (ledger).
- **Acceptance criteria:** Storage standard published; conformance example exists; referenced by memory/search lane.
- **Evidence requirements:** Standard document; conformance example; reference from Lane 12.

### Lane 10 — Knowledge standards
- **Owner repo:** `SocioProphet/socioprophet-standards-knowledge#54`
- **Scope:** Knowledge representation and graph standards for workspace intelligence surfaces.
- **Dependencies:** Lane 1 (contracts), Lane 12 (memory/search).
- **Acceptance criteria:** Knowledge standard published; semantic graph schema validated; referenced by Lane 12.
- **Evidence requirements:** Standard document; schema validation report; reference from Lane 12.

### Lane 11 — SourceOS local surfaces
- **Owner repo:** `SocioProphet/workspace-inventory#4`
- **Scope:** SourceOS local surface inventory and compliance mapping for the Workspace Operation Plane.
- **Dependencies:** Lane 8 (SourceOS spec), Lane 7 (workstation contracts).
- **Acceptance criteria:** Surface inventory complete; each surface maps to a contract or spec entry; compliance status recorded.
- **Evidence requirements:** Inventory document; compliance matrix row per surface.

### Lane 12 — Memory/search/semantic graph
- **Owner repo:** `SocioProphet/workspace-inventory#5`
- **Scope:** Memory, search, and semantic graph admission compliance for workspace operations.
- **Dependencies:** Lane 9 (storage standards), Lane 10 (knowledge standards), Lane 3 (ledger).
- **Acceptance criteria:** Memory/search schema validated; semantic graph admission rule exists; admission compliance metric reported.
- **Evidence requirements:** Schema validation; admission rule fixture; compliance metric sample.

### Lane 13 — Devtools
- **Owner repo:** `SourceOS-Linux/sourceos-devtools#19`
- **Scope:** Developer tooling for workspace operation plane integration — build, test, and validate surfaces.
- **Dependencies:** Lane 8 (SourceOS spec), Lane 7 (workstation contracts).
- **Acceptance criteria:** Devtools integrate with workspace contracts; at least one validation command exercises a lane contract.
- **Evidence requirements:** Validation command run log; contract integration evidence.

### Lane 14 — BearBrowser
- **Owner repo:** `SourceOS-Linux/BearBrowser#20`
- **Scope:** Browser surface integration for workspace operations and SourceOS local UI.
- **Dependencies:** Lane 8 (SourceOS spec), Lane 6 (workspace UI).
- **Acceptance criteria:** Browser surface binds to workspace contracts; policy gate checked before sensitive operation.
- **Evidence requirements:** Contract binding validation; policy check receipt.

### Lane 15 — Agent-machine
- **Owner repo:** `SourceOS-Linux/agent-machine#18`
- **Scope:** Agent-machine integration — device-level agent runtime and workspace operation compliance.
- **Dependencies:** Lane 5 (agent execution), Lane 7 (workstation contracts), Lane 20 (agent registry).
- **Acceptance criteria:** Agent-machine runtime references workspace contracts; tool grants scoped to device context.
- **Evidence requirements:** Contract reference validation; tool grant fixture.

### Lane 16 — SourceOS sync/state integrity
- **Owner repo:** `SourceOS-Linux/sourceos-syncd#3`
- **Scope:** Sync daemon and state integrity for SourceOS workspace operations.
- **Dependencies:** Lane 8 (SourceOS spec), Lane 9 (storage standards), Lane 3 (ledger).
- **Acceptance criteria:** Sync daemon references workspace contracts; state integrity check emits ledger record on failure; rollback path tested.
- **Evidence requirements:** Contract reference validation; ledger record sample; rollback test log.

### Lane 17 — Governed cognition loop
- **Owner repo:** `SocioProphet/superconscious#2`
- **Scope:** Governed cognition loop integration — ensuring superconscious operations comply with workspace policy and evidence requirements.
- **Dependencies:** Lane 4 (policy), Lane 3 (ledger), Lane 5 (agent execution).
- **Acceptance criteria:** Cognition loop checks policy gate before action; evidence receipt emitted; no unlogged cognition cycle touches workspace state.
- **Evidence requirements:** Policy check receipt; evidence receipt sample; cognition loop fixture run log.

### Lane 18 — Human digital twin / delegation / competency
- **Owner repo:** `SocioProphet/HolographMe#3`
- **Scope:** Human digital twin, delegation, and competency model integration with the Workspace Operation Plane.
- **Dependencies:** Lane 4 (policy), Lane 20 (agent registry), Lane 3 (ledger).
- **Acceptance criteria:** Delegation model references workspace contracts; competency assertion linked to evidence; revocation path tested.
- **Evidence requirements:** Contract reference validation; delegation fixture; revocation test log.

### Lane 19 — SCOPE-D cyber range / purple-team
- **Owner repo:** `SocioProphet/workspace-inventory#7` (tracked here because `SocioProphet/SCOPE-D` has Issues disabled — see also risk R-05)
- **Scope:** Cyber range and purple-team exercises for Workspace Operation Plane security posture validation.
- **Dependencies:** Lane 4 (policy), Lane 21 (MCP/A2A zero-trust interop), Lane 16 (sync/state integrity).
- **Acceptance criteria:** At least one exercise scenario defined; scenario references workspace policy gates; findings feed risk register.
- **Evidence requirements:** Exercise scenario document; policy gate reference; risk register update.

### Lane 20 — Agent registry capability/delegation/revocation
- **Owner repo:** `SocioProphet/agent-registry#16`
- **Scope:** Agent capability registration, delegation grants, and revocation records for workspace operations.
- **Dependencies:** Lane 1 (contracts), Lane 4 (policy), Lane 3 (ledger).
- **Acceptance criteria:** Capability schema published; delegation and revocation records validated; workspace-scoped tool grants enforced.
- **Evidence requirements:** Schema validation; delegation fixture; revocation record sample.

### Lane 21 — MCP/A2A zero-trust interop
- **Owner repo:** `SocioProphet/mcp-a2a-zero-trust#4`
- **Scope:** MCP and Agent-to-Agent zero-trust interoperability for workspace operation boundaries.
- **Dependencies:** Lane 1 (contracts), Lane 4 (policy), Lane 20 (agent registry).
- **Acceptance criteria:** Zero-trust interop schema published; at least one cross-agent call validated against policy gate; conformance fixture passes.
- **Evidence requirements:** Schema validation; cross-agent call fixture log; policy check receipt.

### Lane 22 — SourceOS shell UX projection
- **Owner repo:** `SourceOS-Linux/sourceos-shell#10`
- **Scope:** Shell UX projection for workspace operations — command surface, context display, and workspace effect visibility.
- **Dependencies:** Lane 8 (SourceOS spec), Lane 6 (workspace UI), Lane 11 (SourceOS local surfaces).
- **Acceptance criteria:** Shell surface binds to workspace contracts; context display references live workspace state; demo shows workspace effect.
- **Evidence requirements:** Contract binding validation; demo screenshot or recording.

### Lane 23 — SourceOS packaging/release evidence
- **Owner repo:** `SourceOS-Linux/homebrew-tap#1`
- **Scope:** Packaging and release evidence for SourceOS workspace operation plane artifacts.
- **Dependencies:** All other SourceOS lanes (8, 11, 13, 14, 16, 22).
- **Acceptance criteria:** Release artifact references validated contract versions; release checklist complete; rollback path documented.
- **Evidence requirements:** Release checklist; contract version reference; rollback plan document.

### Cross-lane reference — Estate correction
- **Tracking issue:** `SocioProphet/workspace-inventory#6`
- **Scope:** Estate-level correction and alignment for workspace inventory. Cross-linked from Lane 11, 12, and 19.

---

## Work breakdown by lane

| # | Lane | Owner Repo | DoD Gate | Key Dependency |
|---|------|-----------|----------|----------------|
| 1 | Contracts and conformance | `SocioProphet/prophet-core-contracts#1` | Schema + fixture | — |
| 2 | Runtime | `SocioProphet/prophet-platform#376` | Smoke test | 1, 4 |
| 3 | Ledger/evidence | `SocioProphet/prophet-core-ledger#1` | Schema + read-back | 1 |
| 4 | Policy | `SocioProphet/policy-fabric#46` | Policy decision + redaction | 1, 3 |
| 5 | Agent execution | `SocioProphet/agentplane#85` | Workflow bundle + evidence | 1, 4, 20 |
| 6 | Workspace UI/controller | `SocioProphet/sociosphere#259` | Demo playbook + contract binding | 1, 2 |
| 7 | Workstation contracts | `SociOS-Linux/workstation-contracts#28` | Schema + example | 1 |
| 8 | SourceOS spec | `SourceOS-Linux/sourceos-spec#87` | Spec sign-off + ADR | 1, 7 |
| 9 | Storage standards | `SocioProphet/socioprophet-standards-storage#79` | Standard + example | 1, 3 |
| 10 | Knowledge standards | `SocioProphet/socioprophet-standards-knowledge#54` | Standard + schema | 1, 12 |
| 11 | SourceOS local surfaces | `SocioProphet/workspace-inventory#4` | Inventory + compliance map | 7, 8 |
| 12 | Memory/search/semantic graph | `SocioProphet/workspace-inventory#5` | Schema + admission fixture | 3, 9, 10 |
| 13 | Devtools | `SourceOS-Linux/sourceos-devtools#19` | Validation command log | 7, 8 |
| 14 | BearBrowser | `SourceOS-Linux/BearBrowser#20` | Policy check receipt | 6, 8 |
| 15 | Agent-machine | `SourceOS-Linux/agent-machine#18` | Contract ref + tool grant | 5, 7, 20 |
| 16 | SourceOS sync/state integrity | `SourceOS-Linux/sourceos-syncd#3` | Ledger record + rollback | 3, 8, 9 |
| 17 | Governed cognition loop | `SocioProphet/superconscious#2` | Policy check + evidence | 3, 4, 5 |
| 18 | Human digital twin / delegation | `SocioProphet/HolographMe#3` | Delegation fixture + revocation | 3, 4, 20 |
| 19 | SCOPE-D cyber range | `SocioProphet/workspace-inventory#7` | Scenario doc + risk update | 4, 16, 21 |
| 20 | Agent registry | `SocioProphet/agent-registry#16` | Schema + delegation + revocation | 1, 3, 4 |
| 21 | MCP/A2A zero-trust | `SocioProphet/mcp-a2a-zero-trust#4` | Schema + cross-agent fixture | 1, 4, 20 |
| 22 | SourceOS shell UX | `SourceOS-Linux/sourceos-shell#10` | Demo screenshot + contract binding | 6, 8, 11 |
| 23 | SourceOS packaging/release | `SourceOS-Linux/homebrew-tap#1` | Release checklist + rollback | 8, 11, 13, 14, 16, 22 |

---

## Definition of Done per lane

A lane is complete when **all** of the following hold:

1. The owner repo issue is closed or the tracking PR is merged.
2. A conformance fixture or validation evidence file exists and is linked in the PR body.
3. The lane entry in the conformance matrix (below) shows **PASS**.
4. Any cross-lane dependency this lane introduces is recorded in the dependency map (below).
5. Evidence is linked to a ledger record in `prophet-core-ledger` or an equivalent evidence artifact.
6. The lane's delivery metrics (see Delivery metrics section) show a non-zero reading.
7. Rollback or revert path has been tested or documented.

No lane may be marked **Done** based solely on a code merge. Conformance fixture or equivalent validation evidence is mandatory.

---

## Cross-repo dependency map

```
prophet-core-contracts (Lane 1)
  ├── prophet-platform (Lane 2)
  ├── prophet-core-ledger (Lane 3)
  ├── policy-fabric (Lane 4)
  ├── agentplane (Lane 5)
  ├── sociosphere (Lane 6)
  ├── workstation-contracts (Lane 7)
  ├── standards-storage (Lane 9)
  ├── agent-registry (Lane 20)
  └── mcp-a2a-zero-trust (Lane 21)

workstation-contracts (Lane 7)
  ├── sourceos-spec (Lane 8)
  ├── workspace-inventory/local-surfaces (Lane 11)
  ├── sourceos-devtools (Lane 13)
  ├── BearBrowser (Lane 14)
  └── agent-machine (Lane 15)

sourceos-spec (Lane 8)
  ├── workspace-inventory/local-surfaces (Lane 11)
  ├── sourceos-devtools (Lane 13)
  ├── BearBrowser (Lane 14)
  ├── sourceos-syncd (Lane 16)
  ├── sourceos-shell (Lane 22)
  └── homebrew-tap (Lane 23)

prophet-core-ledger (Lane 3)
  ├── policy-fabric (Lane 4)
  ├── standards-storage (Lane 9)
  ├── workspace-inventory/memory-search (Lane 12)
  ├── sourceos-syncd (Lane 16)
  ├── superconscious (Lane 17)
  ├── HolographMe (Lane 18)
  └── agent-registry (Lane 20)

policy-fabric (Lane 4)
  ├── agentplane (Lane 5)
  ├── superconscious (Lane 17)
  ├── HolographMe (Lane 18)
  ├── workspace-inventory/SCOPE-D (Lane 19)
  ├── agent-registry (Lane 20)
  └── mcp-a2a-zero-trust (Lane 21)

agent-registry (Lane 20)
  ├── agentplane (Lane 5)
  ├── agent-machine (Lane 15)
  ├── HolographMe (Lane 18)
  └── mcp-a2a-zero-trust (Lane 21)

standards-storage (Lane 9)
  └── workspace-inventory/memory-search (Lane 12)

standards-knowledge (Lane 10)
  └── workspace-inventory/memory-search (Lane 12)

workspace-inventory/memory-search (Lane 12) [consumes ledger + standards]

sourceos-syncd (Lane 16)
  └── homebrew-tap (Lane 23)

sourceos-devtools (Lane 13)
  └── homebrew-tap (Lane 23)

BearBrowser (Lane 14)
  └── homebrew-tap (Lane 23)

sourceos-shell (Lane 22)
  └── homebrew-tap (Lane 23)

workspace-inventory/local-surfaces (Lane 11)
  └── homebrew-tap (Lane 23)

mcp-a2a-zero-trust (Lane 21)
  └── workspace-inventory/SCOPE-D (Lane 19)

sourceos-syncd (Lane 16)
  └── workspace-inventory/SCOPE-D (Lane 19)

Cross-lane reference: workspace-inventory#6 (estate correction) cross-linked from Lanes 11, 12, 19
```

---

## Conformance matrix

Status values: `NOT STARTED` | `IN PROGRESS` | `FIXTURE EXISTS` | `PASS` | `BLOCKED`

| # | Lane | Owner Repo Issue | Conformance Fixture | Status |
|---|------|-----------------|---------------------|--------|
| 1 | Contracts and conformance | `prophet-core-contracts#1` | — | NOT STARTED |
| 2 | Runtime | `prophet-platform#376` | — | NOT STARTED |
| 3 | Ledger/evidence | `prophet-core-ledger#1` | — | NOT STARTED |
| 4 | Policy | `policy-fabric#46` | — | NOT STARTED |
| 5 | Agent execution | `agentplane#85` | — | NOT STARTED |
| 6 | Workspace UI/controller | `sociosphere#259` | — | NOT STARTED |
| 7 | Workstation contracts | `workstation-contracts#28` | — | NOT STARTED |
| 8 | SourceOS spec | `sourceos-spec#87` | — | NOT STARTED |
| 9 | Storage standards | `standards-storage#79` | — | NOT STARTED |
| 10 | Knowledge standards | `standards-knowledge#54` | — | NOT STARTED |
| 11 | SourceOS local surfaces | `workspace-inventory#4` | — | NOT STARTED |
| 12 | Memory/search/semantic graph | `workspace-inventory#5` | — | NOT STARTED |
| 13 | Devtools | `sourceos-devtools#19` | — | NOT STARTED |
| 14 | BearBrowser | `BearBrowser#20` | — | NOT STARTED |
| 15 | Agent-machine | `agent-machine#18` | — | NOT STARTED |
| 16 | SourceOS sync/state integrity | `sourceos-syncd#3` | — | NOT STARTED |
| 17 | Governed cognition loop | `superconscious#2` | — | NOT STARTED |
| 18 | Human digital twin / delegation | `HolographMe#3` | — | NOT STARTED |
| 19 | SCOPE-D cyber range | `workspace-inventory#7` | — | NOT STARTED |
| 20 | Agent registry | `agent-registry#16` | — | NOT STARTED |
| 21 | MCP/A2A zero-trust | `mcp-a2a-zero-trust#4` | — | NOT STARTED |
| 22 | SourceOS shell UX | `sourceos-shell#10` | — | NOT STARTED |
| 23 | SourceOS packaging/release | `homebrew-tap#1` | — | NOT STARTED |

*Update the Conformance fixture column with a link to the fixture or validation artifact when it is created. Update Status as work progresses.*

---

## Evidence checklist for each PR

Every PR against a lane-tracked issue must include the following checklist in the PR body:

```
## Delivery Governance Evidence Checklist

- [ ] Lane number and owner repo issue linked (e.g., Lane 1 — `prophet-core-contracts#1`)
- [ ] Capability area mapped (contracts | runtime | ledger | policy | agent | ui | devtools | standards | packaging)
- [ ] Conformance fixture or validation evidence file created or updated
- [ ] Fixture run log or validation output attached or linked
- [ ] Cross-repo dependencies identified and recorded in the dependency map
- [ ] Conformance matrix row updated (or PR author requests update)
- [ ] Delivery metrics impacted: which metric(s) and expected movement
- [ ] Risk register checked: no new risk introduced without a registered entry
- [ ] Rollback or revert path documented
- [ ] Demo impact noted (none | prerequisite | demo-ready)
- [ ] Downstream repos to notify: [list]
- [ ] Lane DoD items satisfied: [list satisfied items]
```

No coding PR may be merged without the evidence checklist present and the conformance fixture item checked.

---

## Risk register

| ID | Risk | Lanes affected | Likelihood | Impact | Mitigation | Owner | Status |
|----|------|---------------|-----------|--------|-----------|-------|--------|
| R-01 | Contracts not stabilized before downstream lanes begin implementation | 2, 5, 6, 7, 20, 21 | High | High | Lane 1 (contracts) must reach FIXTURE EXISTS before any downstream coding lane PRs merge. Lanes with demo/playbook DoD gates (6, 22) must have contract binding validated before demo is accepted. | Lane 1 owner | Open |
| R-02 | Policy gate interface changes break agent execution conformance | 5, 15, 17, 18 | Medium | High | Policy schema versioned; downstream lanes pin to contract version | Lane 4 owner | Open |
| R-03 | Cross-org repo coordination friction (SourceOS-Linux vs SocioProphet) | 7, 8, 11, 13, 14, 15, 16, 22, 23 | High | Medium | Weekly cross-org sync; dependency map reviewed each milestone | Delivery governance | Open |
| R-04 | Evidence/ledger not ready before coding lanes reach DoD | 3, 5, 12, 16, 17, 18 | Medium | High | Lane 3 (ledger) must reach FIXTURE EXISTS before any lane requiring evidence emission merges | Lane 3 owner | Open |
| R-05 | SCOPE-D issues disabled; purple-team findings tracked through workspace-inventory#7 only | 19 | Low | Medium | Ensure workspace-inventory#7 is the single source of truth; link from risk register | Lane 19 owner | Open |
| R-06 | Conformance fixtures exist but are not executed in CI | All | Medium | High | Each lane adds CI step; delivery governance audits CI status at each weekly milestone | Delivery governance | Open |
| R-07 | Release packaging (Lane 23) attempted before upstream lanes are complete | 23 | Medium | High | Lane 23 is gated on all SourceOS lanes reaching FIXTURE EXISTS | Lane 23 owner | Open |
| R-08 | Delegation/revocation model in HolographMe and agent-registry diverges | 18, 20 | Medium | Medium | Lanes 18 and 20 must coordinate schema; joint review before either reaches PASS | Lanes 18 + 20 owners | Open |
| R-09 | Zero-trust interop (Lane 21) not validated before SCOPE-D exercises run | 19, 21 | Medium | High | Lane 21 must reach FIXTURE EXISTS before Lane 19 scenario exercise runs | Lane 21 owner | Open |
| R-10 | Memory/search semantic graph admission diverges from storage/knowledge standards | 9, 10, 12 | Medium | Medium | Lane 12 must reference Lane 9 and Lane 10 standards explicitly; joint review | Lanes 9, 10, 12 owners | Open |

---

## Release/rollback plan

### Release stages

**Stage 0 — Foundation**
Gates: Lanes 1, 3, 4, 20 reach FIXTURE EXISTS.
Release artifact: Contract schema bundle + ledger schema + policy decision schema + agent registry schema.
Rollback: Remove published schemas; revert to prior version if any downstream lane has pinned.

**Stage 1 — Core integration**
Gates: Lanes 2, 5, 6, 7, 8, 9, 10 reach FIXTURE EXISTS.
Release artifact: Runtime skeleton + workstation contracts + SourceOS spec + storage/knowledge standards.
Rollback: Runtime revert via platform rollback plan; contracts versioned rollback.

**Stage 2 — SourceOS surface integration**
Gates: Lanes 11, 12, 13, 14, 15, 16, 22 reach FIXTURE EXISTS.
Release artifact: SourceOS local surface inventory + memory/search admission + devtools + BearBrowser + agent-machine + sync daemon + shell UX.
Rollback: Each SourceOS component rolls back independently; sync daemon rollback requires state integrity check.

**Stage 3 — Advanced capabilities**
Gates: Lanes 17, 18, 19, 21 reach FIXTURE EXISTS.
Release artifact: Governed cognition loop + HolographMe delegation + SCOPE-D scenario pack + MCP/A2A zero-trust bundle.
Rollback: Each component rolls back independently; SCOPE-D exercise scenarios archived not deleted.

**Stage 4 — Release packaging**
Gates: All lanes reach PASS; Lane 23 release checklist complete.
Release artifact: SourceOS packaging release via homebrew-tap.
Rollback: homebrew-tap version pinned; prior tap version restored; downstream consumers notified.

### Rollback triggers

- Any conformance fixture regression across 2 or more lanes in the same stage → stage rollback.
- Policy gate breach detected in any lane → immediate hold; Lane 4 owner review before any release continues.
- Ledger write failure in production-equivalent environment → hold Stage 1+ releases; Lane 3 owner escalation.
- Security finding from SCOPE-D exercise rated high or critical → hold Stage 3+ releases; risk register updated.

---

## Weekly demo milestone plan

### Milestone M1 (Week 1–2)
**Objective:** Governance structure in place.
- Delivery governance plan published (this document).
- Lane owners identified.
- Conformance matrix populated with current status.
- Risk register reviewed.
- Evidence checklist adopted by at least one lane PR.

**Demo:** Walk through this governance plan and identify at least one lane with a draft conformance fixture.

### Milestone M2 (Week 3–4)
**Objective:** Foundation lanes started.
- Lane 1 (contracts): draft schema published.
- Lane 3 (ledger): draft schema published.
- Lane 4 (policy): draft policy decision schema published.
- Lane 20 (agent registry): draft capability schema published.
- Conformance matrix updated.

**Demo:** Show schema drafts with at least one validation run per lane.

### Milestone M3 (Week 5–6)
**Objective:** Foundation lanes at FIXTURE EXISTS.
- Lanes 1, 3, 4, 20: conformance fixtures passing.
- Stage 0 release readiness check complete.
- Lane 2 (runtime) and Lane 5 (agent execution) started.

**Demo:** Show conformance fixture runs for Lanes 1, 3, 4, 20. Show runtime skeleton boot (even if partial).

### Milestone M4 (Week 7–8)
**Objective:** Core integration lanes started.
- Lanes 2, 5, 6, 7, 8 in progress.
- Lanes 9, 10 drafts published.
- Dependency map updated to reflect in-progress state.
- Risk register reviewed; any new risks registered.

**Demo:** Show runtime skeleton integrating with contract layer. Show policy gate check in agent execution path.

### Milestone M5 (Week 9–10)
**Objective:** Core integration lanes at FIXTURE EXISTS.
- Lanes 2, 5, 6, 7, 8, 9, 10 conformance fixtures passing.
- Stage 1 release readiness check complete.
- SourceOS surface lanes (11–16, 22) started.

**Demo:** End-to-end trace from runtime boot → policy check → agent run → ledger record. Show workspace UI surface.

### Milestone M6 (Week 11–12)
**Objective:** SourceOS surface integration at FIXTURE EXISTS.
- Lanes 11, 12, 13, 14, 15, 16, 22 conformance fixtures passing.
- Stage 2 release readiness check complete.
- Advanced capability lanes (17, 18, 19, 21) started.

**Demo:** Show SourceOS local surface rendering workspace state. Show memory/search admission check. Show sync daemon ledger record.

### Milestone M7 (Week 13–14)
**Objective:** Advanced capabilities at FIXTURE EXISTS.
- Lanes 17, 18, 19, 21 conformance fixtures passing.
- Stage 3 release readiness check complete.
- Lane 23 (packaging) release checklist drafted.

**Demo:** Show governed cognition loop with policy check and evidence receipt. Show zero-trust interop between agents. Show SCOPE-D scenario run summary.

### Milestone M8 (Week 15–16)
**Objective:** All lanes at PASS; release packaging complete.
- All 23 lanes at PASS in conformance matrix.
- Stage 4 release readiness check complete.
- homebrew-tap release artifact published.
- Rollback tested for each stage.

**Demo:** Full end-to-end Workspace Operation Plane demo covering all 23 lanes. Show release artifact and rollback test result.

---

## Delivery metrics

| Metric | Lane(s) | Measurement | Target |
|--------|---------|-------------|--------|
| Contract completeness | 1, 7 | % of contract types with published schema and passing fixture | 100% at Stage 0 |
| Runtime skeleton completeness | 2 | % of defined runtime interfaces with smoke test passing | 100% at Stage 1 |
| Policy gate interface completeness | 4, 21 | % of policy decision types with validated schema | 100% at Stage 0 |
| Agent operation compliance | 5, 15, 17 | % of agent workflow bundles with evidence receipt | 100% at Stage 2 |
| UI visibility completeness | 6, 22 | % of workspace state surfaces rendered in UI demo | 100% at Stage 2 |
| SourceOS local surface compliance | 11, 13, 14, 16 | % of SourceOS surfaces mapped to contract or spec | 100% at Stage 2 |
| Memory/search admission compliance | 12 | % of admission paths with fixture-validated rule | 100% at Stage 2 |
| Redaction coverage | 4 | % of sensitive field types covered by redaction rule | 100% at Stage 1 |
| Conformance pass rate | All | % of lanes at PASS in conformance matrix | 100% at Stage 4 |

---

## Hygiene rules

1. Every lane change maps to a tracked issue in the owner repo.
2. Every PR against a lane issue includes the evidence checklist (see above).
3. No lane is marked Done without a conformance fixture or validation evidence.
4. The conformance matrix is updated each time a lane changes status.
5. The risk register is reviewed at each weekly demo milestone.
6. Cross-org dependencies (SourceOS-Linux ↔ SocioProphet) are flagged in the dependency map and reviewed weekly.
7. Delivery governance does not own product runtime, policy authority, or agent implementation. It owns inspectability, evidence requirements, and gate decisions.

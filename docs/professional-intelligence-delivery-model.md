# Professional Intelligence Delivery Model

## Purpose

This document makes DelEx-OS the delivery governance spine for the SocioProphet Professional Intelligence OS program.

DelEx does not own product runtime. DelEx owns the way work enters, moves, proves itself, and gets accepted across the repo estate.

## Delivery chain

Professional Intelligence OS work follows this chain:

```
Signal -> Intake -> Board Item -> ADR / Spec -> Repo Work Order -> PR -> Validation -> Evidence -> Demo Acceptance -> KPI Update
```

## Control points

### 1. Signal

Sources may include customer discovery, competitive analysis, architecture gaps, repo audits, incidents, interview prep, platform demos, or agent findings.

Required fields:
- signal id
- source type
- confidence
- impacted capability
- impacted repos
- decision required

### 2. Intake

Intake normalizes the signal into a DelEx work item.

Required fields:
- title
- problem statement
- desired outcome
- capability area
- owner repo
- runtime repo
- governance repo
- acceptance evidence
- demo impact
- risk class

### 3. Board item

The board item is the visible delivery unit. It must map to a Professional Intelligence OS capability in `SocioProphet/prophet-platform/professional-intelligence.manifest.yaml`.

Allowed capability classes:
- institution-context-engine
- institution-graph
- agent-fabric
- conflict-engine
- obligation-ledger
- ethical-walls
- workspace-os
- adoption-telemetry
- evidence-plane
- revenue-integrity
- vertical-pack
- delivery-governance

### 4. ADR / Spec

Any cross-repo or irreversible decision requires an ADR or spec.

ADR/spec must state:
- decision
- repos affected
- rejected alternatives
- implementation owner
- validation path
- rollback path
- evidence requirements

### 5. Repo work order

A repo work order gives an agent or human contributor a bounded implementation target.

A valid work order includes:
- branch name
- files to create or modify
- commands to validate
- acceptance evidence
- related playbook
- related schema or contract
- expected PR target

### 6. PR

Every PR should include:
- capability mapping
- validation performed
- evidence artifacts produced or updated
- demo impact
- risk/rollback notes
- downstream repos to update

### 7. Validation

Validation must include repository-local checks and, when relevant, cross-repo manifest checks.

Minimum validation tiers:
- docs-only: link and manifest sanity
- contracts: schema validation and examples
- service: unit/smoke checks
- platform: runtime smoke and GitOps surface checks
- demo: playbook-driven evidence and adoption event

### 8. Evidence

Evidence must be machine-readable where possible.

Evidence may include:
- validation report
- adoption event
- policy check receipt
- agent action receipt
- replay artifact
- demo acceptance receipt
- repo readiness report

### 9. Demo acceptance

A demo is accepted only when it can show:
- an executable playbook or equivalent scripted workflow
- institution context resolution
- governed agent/tool action
- policy or obligation check
- workspace effect
- adoption event
- evidence receipt
- KPI movement or measurable proxy

### 10. KPI update

DelEx KPIs should track:
- demo readiness
- repo readiness
- playbook coverage
- validation pass rate
- evidence coverage
- adoption telemetry coverage
- cycle-time reduction
- risk closure
- customer/value hypothesis coverage

## Repo family alignment

- `delivery-excellence`: mandate, KPI/OKR definitions, governance model, templates, acceptance rules.
- `delivery-excellence-automation`: group/RBAC bindings, CI validation, generated ledgers, meeting/audience automation.
- `delivery-excellence-boards`: idea intake, roadmap, delivery boards, portfolio state.
- `delivery-excellence-innersource`: playbooks, repo readiness, contribution routes, portal/index specs.
- `delivery-excellence-bounties`: acceleration policy, scoring, escrow/payout gates.

## Initial program board lanes

1. Runtime spine
   - `prophet-platform`, `TriTRPC`, `tritfabric`, `prophet-cli`.

2. Work surface
   - `prophet-workspace`, `sherlock-search`, `speechlab`, `orion-field-intelligence`.

3. Governed AI execution
   - `agentplane`, `agent-registry`, `model-router`, `guardrail-fabric`, `model-governance-ledger`, `memory-mesh`.

4. Policy, obligations, and risk
   - `policy-fabric`, `contractforge`, `regis-entity-graph`, `ontogenesis`.

5. Domain packs
   - legal, private capital, real assets, revenue integrity, public-sector/research.

## Non-negotiables

- No orphan repo work. Every meaningful change maps to a capability and an acceptance path.
- No platform feature without evidence and adoption telemetry.
- No agent action without tool grants, authority boundary, and replay/evidence posture.
- No playbook without policy/obligation and KPI hooks.
- No demo that bypasses governance for speed.

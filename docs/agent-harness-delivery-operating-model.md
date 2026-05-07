# Agent Harness Delivery Operating Model

Status: v0.1 planning baseline  
Owner plane: Delivery Excellence / DelEx-OS  
Scope: cross-estate performance stack, delivery metering, corporate scoreboards, operating cadence, customer proof, and agent/human work packaging

## Why this exists

Aden/Hive is useful as a competitive reference because it frames production agents as business-process infrastructure: describe an outcome, generate a plan/graph, run governed workers, observe cost and failure, preserve memory, involve humans, and evolve the process. That pattern is broader than software development. It applies to product delivery, security operations, customer proof, corporate reporting, bounty work, inner-source contribution, support workflows, finance/admin workflows, research production, and field operations.

Delivery Excellence owns the operating and performance layer for this pattern. AgentPlane, Policy Fabric, SourceOS, BearBrowser, TurtleTerm, Memory Mesh, SCOPE-D, SocioSphere, and platform repos emit signals and evidence. Delivery Excellence turns those signals into scoreboards, operating cadence, work packaging, service-level expectations, executive readouts, and improvement loops.

## Boundary

Delivery Excellence owns:

- KPI/OKR definitions and scoreboards.
- Work-order and acceptance templates.
- Delivery cadence, escalation, and operating reviews.
- Performance readouts for agent/human work.
- Customer-safe proof-of-value projections.
- Bounty and inner-source work packaging rules.
- Cross-estate readiness, hygiene, and completion metrics.
- Management-system language for product, operations, support, and security teams.

Delivery Excellence does not own:

- Agent runtime execution. That remains AgentPlane.
- Policy compilation and admission. That remains Policy Fabric / Guardrail Fabric.
- Workspace topology authority. That remains SocioSphere.
- SourceOS host/runtime implementation. That remains SourceOS / SociOS / Agent Machine repos.
- Browser and terminal runtime behavior. That remains BearBrowser, TurtleTerm, and agent-term.
- Security test execution. That remains SCOPE-D and security-specific repos.
- Memory runtime implementation. That remains Memory Mesh.

## Integration loop

The cross-estate operating loop is:

```text
Outcome -> Work Item -> Plan Graph -> Policy Gate -> Run -> Evidence -> Scoreboard -> Review -> Evolution Patch -> Promotion Gate
```

Delivery Excellence owns the translation from evidence to management control:

```text
EvidencePack -> DeliveryMetric -> KPI/OKR -> Readout -> Decision -> Follow-up Work Item
```

## Core objects

### Outcome

A measurable business or platform result, not just a task. Required fields:

- outcome id
- owner
- customer or stakeholder
- expected value
- success criteria
- risk tier
- due date or cadence
- evidence requirements
- linked repos
- linked policy gates
- linked run/evidence artifacts

### Work Item

A scoped unit of human or agent work. Required fields:

- work item id
- outcome ref
- repo refs
- execution mode: human, agent, paired, review-only, dry-run, autonomous-with-gate
- assignee or worker class
- acceptance criteria
- validation path
- rollback/abandon rule
- evidence refs
- readout lane

### Delivery Metric

A stable performance signal derived from evidence. Initial metric families:

- throughput: completed work items, merged PRs, accepted patches, shipped templates
- flow: cycle time, blocked time, review latency, gate latency, reopen rate
- quality: validation pass rate, rollback rate, defect escape rate, evidence completeness
- governance: policy gate pass/fail, exception count, human approval count, revocation count
- cost: model cost, compute cost, human approval load, retry cost, wasted-run cost
- reliability: run success rate, replay success rate, session resume rate, tool failure rate
- safety/security: SCOPE-D findings, prompt/tool/skill/MCP risk count, secret/network violations
- customer proof: value delivered, time saved, artifact count, approved outputs, SLA contribution

### Readout

A management-facing projection of delivery state. Required readout types:

- operator readout: what changed, what passed, what failed, what is blocked
- executive readout: outcome progress, risk, cost, confidence, next decision
- customer-safe readout: work performed, evidence, value, approvals, known limits
- repo readiness readout: maturity, validation, CI, hygiene, docs, open blockers
- agent performance readout: agent class, tool grants, cost, success, intervention rate

## Cross-estate signal producers

### AgentPlane

Emits validation, placement, run, replay, session, promotion, and reversal artifacts. Delivery Excellence consumes these as run success, replay readiness, cycle time, cost, and promotion-readiness signals.

### Policy Fabric / Guardrail Fabric

Emit policy decisions, guardrail evaluations, validation reports, exceptions, and replay reports. Delivery Excellence consumes these as governance pass/fail, exception burden, risk exposure, and approval latency.

### SourceOS / Agent Machine / sourceos-spec

Emit local-first service manifests, activation decisions, boot/release evidence, host readiness, signed release envelopes, and runtime receipts. Delivery Excellence consumes these as installability, bootstrap readiness, supply-chain posture, and local-first operational maturity.

### BearBrowser

Emits browser history/events, credential posture, automation-surface validation, build readiness, and governed browser action evidence. Delivery Excellence consumes these as browser automation reliability, credential safety, and workflow coverage.

### TurtleTerm / agent-term / workstation contracts

Emit shell receipts, operator smoke records, IPC conformance, terminal action evidence, and durable operator state. Delivery Excellence consumes these as operator UX readiness, terminal workflow reliability, and developer/operator parity.

### Memory Mesh

Emits context-pack refs, recall/writeback evidence, memory profile posture, sensitive-payload storage decisions, and retrieval behavior. Delivery Excellence consumes these as memory reliability, context quality, retention posture, and evidence traceability.

### SCOPE-D

Emits defensive security assessments for cloud, GitHub, Kubernetes, local hosts, MCP/tool servers, skills, memory stores, vector stores, graph robustness, detections, and threat intelligence. Delivery Excellence consumes these as security readiness, validation coverage, and risk burndown.

### SocioSphere

Emits workspace topology, repo inventory, dependency direction, source-exposure governance, integration status, and cross-repo hardening rules. Delivery Excellence consumes these as estate coverage, topology compliance, source exposure posture, and integration completeness.

### Product/web/workspace surfaces

SocioProphet product repos, SocioSphere, Prophet Workspace, and web surfaces expose customer/operator-facing status. Delivery Excellence consumes their evidence to produce proof-of-value, demo readiness, and public-product readiness scoreboards.

## Recent active repo watchlist

The operating model must track newly active or recently contributed repos, not only the older dossier baseline. As of the May 2026 alignment pass, include at least:

- SocioProphet/superconscious
- SocioProphet/agentplane
- SocioProphet/policy-fabric
- SocioProphet/guardrail-fabric
- SocioProphet/model-router
- SocioProphet/functional-model-surfaces
- SocioProphet/model-governance-ledger
- SocioProphet/prophet-platform
- SocioProphet/prophet-workspace
- SocioProphet/workspace-inventory
- SocioProphet/ProCybernetica
- SocioProphet/HolographMe
- SocioProphet/semantic-serdes
- SocioProphet/ontogenesis
- SocioProphet/socioprophet-agent-standards
- SocioProphet/SCOPE-D
- SocioProphet/memory-mesh
- SourceOS-Linux/agent-machine
- SourceOS-Linux/BearBrowser
- SourceOS-Linux/TurtleTerm
- SourceOS-Linux/agent-term
- SourceOS-Linux/sourceos-spec
- SourceOS-Linux/homebrew-tap
- SourceOS-Linux/sourceos-syncd
- SociOS-Linux/source-os
- SociOS-Linux/socios
- SociOS-Linux/workstation-contracts
- SociOS-Linux/embeddinglab
- SociOS-Linux/graphlab
- SociOS-Linux/nlplab
- SociOS-Linux/timeserieslab
- SociOS-Linux/translationlab
- mdheller/socioprophet-web

This list should become machine-generated by delivery-excellence-automation using recent commit, PR, issue, and workspace-inventory signals.

## Aden/Hive lessons absorbed

### Outcome-first delivery

Do not track only tasks. Track business/platform outcomes and required evidence.

### Graph-first operating model

Plan graphs are useful for management visibility, not only runtime execution. Delivery boards should expose workstream graphs, dependency edges, approval gates, and live status.

### Human-in-the-loop accounting

Human approvals, rejections, overrides, clarifications, risk acceptances, and credential grants are not invisible interruptions. They are signed control events and must be counted.

### Cost and failure as first-class signals

Agent cost, retry cost, wasted-run cost, escalation load, tool failure, and replay failure must be visible in scoreboards.

### Skill/MCP marketplace discipline

Skills and MCP servers should be measured as reusable assets: installs, tests, trust tier, defects, risk findings, evidence examples, adoption, and deprecation status.

### Proof-of-value

Every significant workflow should have an internal and customer-safe readout: what work was done, what artifacts changed, what approvals occurred, what value was delivered, what risks remain, and what should happen next.

## Initial scoreboards

### Estate readiness scoreboard

- repo has README
- repo has AGENTS.md or equivalent agent instructions
- repo has validation command
- repo has CI validation
- repo has maturity/status file
- repo has security/reporting policy when relevant
- repo is registered in SocioSphere/workspace-inventory
- repo emits or consumes evidence
- repo has owner and boundary statement

### Agent harness scoreboard

- outcome spec exists
- plan graph exists
- policy gate exists
- run evidence exists
- replay evidence exists
- human approval events recorded
- cost/budget recorded
- failure diagnosis recorded
- evolution patch or follow-up work item recorded
- promotion decision recorded

### Product proof scoreboard

- demo path exists
- one-command smoke path exists
- stakeholder-readable summary exists
- customer-safe summary exists
- artifact index exists
- digest/provenance present
- known gaps documented
- next decision documented

### Skill/MCP scoreboard

- manifest exists
- trust tier assigned
- policy grants declared
- evals exist
- risk/threat model exists
- install/doctor command exists
- evidence fixture exists
- deprecation/revocation path exists

## Cadence

Weekly operating review:

- top outcomes
- completion percent by workstream
- blockers and gate latency
- failed validations and regressions
- agent cost and intervention load
- customer-safe proof updates
- security/risk deltas
- next 7-day decisions

Daily lightweight review:

- merged PRs
- open high-risk PRs
- failed CI
- blocked work items
- overdue approvals
- stale evidence

Release review:

- outcome completion
- validation and replay status
- evidence completeness
- SCOPE-D/security posture
- rollback readiness
- proof-of-value summary
- promotion decision

## Delivery Excellence automation requirements

The automation repo should add or extend contracts for:

- `recent-repo-activity-report`
- `agent-harness-work-item`
- `delivery-metric-event`
- `scoreboard-snapshot`
- `customer-proof-readout`
- `human-control-event`
- `skill-mcp-asset-score`
- `repo-readiness-score`

These contracts should allow CI and GitHub automation to ingest AgentPlane, Policy Fabric, SourceOS, SCOPE-D, Memory Mesh, BearBrowser, TurtleTerm, and SocioSphere signals without making Delivery Excellence a runtime authority.

## Non-goals

- Do not turn Delivery Excellence into an agent runtime.
- Do not move Policy Fabric gates into this repo.
- Do not move SocioSphere topology authority into this repo.
- Do not make dashboards depend on proprietary cloud services.
- Do not track vanity metrics without evidence.
- Do not count generated artifacts as complete unless validation and acceptance criteria pass.

## Done criteria for v0.1

- Delivery Excellence has this operating model.
- delivery-excellence-automation has machine-readable contracts for scoreboards and recent repo activity.
- SocioSphere references this model as the delivery/performance authority.
- AgentPlane and Policy Fabric expose enough stable evidence for scoreboard ingestion.
- At least one cross-estate weekly readout can be generated from repo and evidence signals.
- At least one customer-safe proof-of-value readout can be generated from an evidence pack.

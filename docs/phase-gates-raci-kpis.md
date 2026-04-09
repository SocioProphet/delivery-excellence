# Phase Gates, RACI, and KPI Structure

## Phase gates

### Gate 0 — Mobilization
Required before build work starts:
- named sponsor
- named process owner
- named system owner
- named data/knowledge owner
- named policy/risk owner
- named operator representative
- initial use-case shortlist
- access request list

### Gate 1 — Readiness Baseline
Required artifacts:
- process map
- dependency register
- data and knowledge inventory
- initial action-class matrix
- baseline KPI pack

### Gate 2 — Control-Loop Design Freeze
Required artifacts:
- target workflow decomposition
- approval rules
- exception taxonomy
- KPI definitions
- v0 policy model
- v0 evaluation harness

### Gate 3 — Shadow Readiness
Required artifacts:
- connected system
- review surfaces
- offline benchmarks
- telemetry and logging
- failure taxonomy

### Gate 4 — Controlled Action Pilot
Required artifacts:
- approved low-risk reversible action subset
- rollback test evidence
- staffed exception queue
- live audit and intervention telemetry

### Gate 5 — Scale Decision
Required artifacts:
- KPI movement analysis
- intervention trend review
- policy violation review
- dependency stability review
- proposed autonomy or scope expansion

## Minimum accountability mapping

Business outcome definition:
- Accountable: sponsor
- Responsible: delivery control office + process owner

Workflow decomposition:
- Accountable: process owner
- Responsible: process and decision engineering

System dependency readiness:
- Accountable: architect + client system owner
- Responsible: integration/orchestration

Knowledge and corpus readiness:
- Accountable: data/knowledge owner
- Responsible: knowledge/data engineering

Permissions and action policy:
- Accountable: risk/policy owner
- Responsible: security/identity/policy

Evaluation harness and release gates:
- Accountable: evaluation lead
- Responsible: assurance/runtime operations

Override and exception operations:
- Accountable: operations owner
- Responsible: experience/intervention + runtime ops

## KPI structure

Operational:
- time to first action
- time to first meaningful response
- cycle time
- backlog age
- routing accuracy

Quality and assurance:
- groundedness score
- disagreement rate
- intervention rate
- policy-escape rate
- hallucination rate

Knowledge and evidence:
- citation coverage
- freshness lag
- evidence completeness
- missing-source frequency

Adoption and value:
- operator acceptance rate
- fallback rate
- cases touched by system
- CSAT or internal stakeholder satisfaction

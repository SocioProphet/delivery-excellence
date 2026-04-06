# Action Classes and Autonomy Gates

## Principle

We do not contract or operate against vague claims of autonomy. We define explicit action classes, approval rules, and gate criteria.

## Action classes

### A0 — Observe and summarize
Read-only synthesis, monitoring, clustering, extraction, and internal evidence packaging.

Examples:
- call summaries
- incident digests
- requirements clustering
- KPI summaries

Default control:
- automation allowed
- sampled review
- no external commitment

### A1 — Draft and recommend
Agents produce proposed responses, plans, classifications, or next-best actions.

Examples:
- customer reply drafts
- success-plan drafts
- roadmap or backlog suggestions
- escalation summaries

Default control:
- human reviews before use on consequential outputs
- no unsupervised external commitments

### A2 — Approval-gated reversible action
Agents stage or propose low-risk internal actions that a human approves.

Examples:
- task creation
- routing changes
- internal reminders
- CRM note updates
- low-risk metadata changes

Default control:
- 100% human approval until evidence supports narrowing

### A3 — Policy-bounded reversible execution
Agents execute selected internal low-risk reversible actions inside a pre-approved policy boundary.

Examples:
- internal routing
- tagging
- reminder issuance
- checklist progression
- status synchronization

Default control:
- all exceptions routed to humans
- sampled audits remain mandatory
- rollback must be tested

### A4 — Consequential or binding action
Externally binding, destructive, financially material, legally sensitive, or weakly reversible action.

Examples:
- compensation
- pricing change
- contract promise
- policy exception
- production-risk instruction
- destructive account or environment change

Default control:
- human-owned
- explicit approval required

## Gate logic

Permitted autonomy is capped by the weakest maturity axis:
- requirements maturity
- dependency readiness
- knowledge/data readiness
- evaluation maturity
- governance maturity

A project does not move to a higher action class merely because the model seems fluent.

## Evidence required to widen autonomy

A move from A1 to A2/A3 should require evidence for:
- acceptable intervention rate
- acceptable grounding quality
- known exception taxonomy
- tested rollback path
- named accountable owner
- policy review and sign-off
- stable runtime telemetry

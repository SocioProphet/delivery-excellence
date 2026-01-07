# Roles and Purpose-Based Enforcement

Groups define the ecosystem’s address space; roles define authority. Purpose-based enforcement binds roles to governance surfaces (ADRs, automation, standards, scoreboards, calendars, email lists) and then enforces these bindings through merge gates and CI validation.

Canonical roles: owner, approver, reviewer, escalation_target, publisher, gatekeeper, custodian, auditor.

Escalation semantics are time- and priority-bounded:
- P0 blocked > 4h → on-call escalation target + governance escalation target
- P1 blocked > 24h → escalation target (domain) + DelEx Core
- P2 blocked > 72h → escalation target + PMO
- P3 blocked > 7d → PMO + DelEx Core

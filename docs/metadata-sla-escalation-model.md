# Metadata SLA and Escalation Model

## Purpose

This document defines the service-level and escalation model for metadata operations inside DelEx.

The objective is to turn report-driven remediation into a governed service with explicit response expectations, breach logic, and escalation discipline.

## Service-level model

Each metadata finding class should carry:
- severity
- owner role
- response SLA
- remediation SLA
- evidence required for closure
- escalation trigger

## Default severity model

### Critical
Use when the issue blocks production use, gate progression, or materially affects enterprise risk.

### High
Use when the issue materially affects delivery quality, business metadata trust, or sync correctness.

### Medium
Use when the issue degrades metadata quality but has workarounds.

### Low
Use when the issue is informational, cosmetic, or deferred by policy.

## Example SLA posture

| Severity | Response SLA | Remediation SLA | Escalation |
|---|---|---|---|
| Critical | 1 business day | 1 sprint or immediate hot-path action | immediate management escalation |
| High | 2 business days | 1 to 2 sprints | escalate on missed response or low engagement |
| Medium | 5 business days | backlog-managed | escalate on aging or repeated reopen |
| Low | next planning cycle | discretionary | usually none unless trend worsens |

## Engagement-based escalation rule

Escalation should not be triggered solely by red or yellow status. It should be triggered when:
- there is sustained red or yellow status
- metadata contact is not verified
- onboarding or engagement indicators are absent
- response SLA is breached
- remediation SLA is breached
- the same issue reopens repeatedly

## Closure evidence

A finding should not be closed unless there is auditable evidence of:
- ownership confirmation
- corrective action
- status change in the source system or metadata registry
- report revalidation or dashboard confirmation

## BTNR and glossary notes

BTNR and glossary-related issues require separate policy interpretation, but they should still inherit:
- severity
- owner role
- closure evidence
- escalation trigger

## Governance rule

Escalation is part of service management, not interpersonal escalation theater. The goal is to recover delivery and metadata quality, not merely to signal dissatisfaction.

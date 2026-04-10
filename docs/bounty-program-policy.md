# Bounty Program Policy

## Purpose

This document defines the policy object that constrains how bounty and incentive programs may operate inside DelEx.

A bounty program is not an autonomous market. It is a governed incentive surface that must remain subordinate to engagement, gate, evidence, and approval state.

## Additional core object

### 13. Bounty Program Policy
A machine-readable policy object that defines what reward signals are allowed, what reward signals are forbidden, what delivery gates must be satisfied, who must approve rewards, and what ceilings or constraints apply.

Minimum fields:
- policy id
- policy name
- linked service offer id
- linked engagement id, if scoped to a specific engagement
- allowed reward signals
- prohibited reward signals
- gate requirements
- required approver role
- payout ceiling amount and currency, if applicable
- evidence validation requirement
- gate approval requirement
- notes

## Hard boundaries

A bounty program policy must not permit rewards for:
- raw activity without evidence
- work that bypassed approvals
- work invalidated by failed gate review, severe exception, or rollback
- widening autonomy without gate approval

## Repo consumption rules

### `delivery-excellence`
Owns the prose semantics and control boundaries of the bounty program policy.

### `delivery-excellence-automation`
Owns the schema, examples, and validators for bounty program policy objects.

### `delivery-excellence-bounties`
Consumes the validated policy object and applies it downstream to scoring and payout logic.

## Practical implication

If a bounty design conflicts with DelEx gate or evidence rules, the bounty design is wrong and must be changed. Incentives remain downstream of governance.

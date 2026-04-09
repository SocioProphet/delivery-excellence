# Incentive and Payout Objects

## Purpose

This document extends the DelEx shared object model to cover the downstream incentive layer now that payout and escrow semantics have been encoded in `delivery-excellence-automation`.

The rule remains the same: incentive logic is downstream of delivery truth.

## Additional core objects

### 11. Payout Decision
A governed decision object that links incentive release to a real engagement, a real delivery gate, and real evidence.

Minimum fields:
- payout decision id
- linked engagement id
- linked gate id
- decision status
- decision owner
- evidence links
- reusable asset ids, if any
- exception ids, if any
- escrow reference id, if any
- amount and currency
- rationale

### 12. Escrow Reference
A reference object for reserved, released, cancelled, or settled funds or equivalent internal payout instruments.

Minimum fields:
- escrow reference id
- instrument type
- currency
- amount
- status
- external reference, if applicable
- notes

## Consumption rules

### `delivery-excellence`
Owns the prose semantics and control boundaries for payout and escrow objects.

### `delivery-excellence-automation`
Owns the machine-readable schemas, examples, and validators for payout and escrow objects.

### `delivery-excellence-bounties`
Consumes these objects and must not bypass or redefine the upstream link to engagement, gate, evidence, reusable-asset, and exception state.

## Hard boundary

A payout decision is never a substitute for gate completion.
An escrow reference is never a substitute for approval.
A bounty signal is never a substitute for evidence.

## Practical implication

The bounty layer may accelerate or reinforce proof-backed work, but it must never become a parallel governance plane that overrides DelEx controls.

# Cross-Repo Architecture

## Goal

Define one clean dependency order across the DelEx repositories so method, automation, boards, contribution readiness, and incentives do not drift apart.

## Canonical split

### `delivery-excellence`
Human-readable canon for:
- delivery governance method
- agentic services operating model
- GTM/contracting/customer-success method
- action classes and phase gates
- templates and review forms

### `delivery-excellence-automation`
Machine-readable contract and validation layer for:
- group ledger
- RBAC bindings
- autonomy envelope
- delivery gate schema
- client dependency manifest
- executable validation rules

### `delivery-excellence-boards`
Operational portfolio and board surface that should consume the upstream object model, not define it.

### `delivery-excellence-innersource`
Contribution readiness, service asset adoption, maintainer role mapping, and capability-transfer surface.

### `delivery-excellence-bounties`
Incentive and payout layer that must consume delivery evidence and gate completion, not precede them.

## Dependency order

1. Canon (`delivery-excellence`)
2. Contract (`delivery-excellence-automation`)
3. Consumer surfaces (`boards`, `innersource`)
4. Incentive surface (`bounties`)

## Why this ordering matters

- Tool selection should not silently dictate workflow semantics.
- CODEOWNERS and branch protections should not harden before role definitions stabilize.
- Incentives should not be attached before evidence and gate logic are well-defined.

## Immediate implementation tranche

Tranche A:
- establish canon in `delivery-excellence`
- establish machine-readable contracts in `delivery-excellence-automation`

Tranche B:
- map canon into `delivery-excellence-boards`
- map readiness and adoption into `delivery-excellence-innersource`

Tranche C:
- bind `delivery-excellence-bounties` to evidence and payout gates derived from the upstream model

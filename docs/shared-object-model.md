# Shared Object Model

## Purpose

This document defines the minimum cross-repo object model that downstream DelEx systems must consume rather than redefine.

The goal is to prevent `boards`, `innersource`, and `bounties` from drifting into incompatible workflow semantics.

## Core objects

### 1. Service Offer
A commercialized delivery package with defined stages, outcomes, action boundaries, and success metrics.

Minimum fields:
- offer id
- offer name
- buyer problem
- included stages
- excluded actions
- acceptance model
- managed-service follow-on path

### 2. Engagement
A concrete client-specific instantiation of a service offer.

Minimum fields:
- engagement id
- linked service offer
- sponsor and named owners
- target workflow
- current phase/gate
- current autonomy envelope
- KPI baseline

### 3. Control Loop
The governed unit of execution.

Minimum fields:
- control-loop id
- trigger
- context sources
- allowed tools
- action classes in scope
- approval rule
- exception route
- emitted evidence
- KPI targets

### 4. Action Class
The authority model for a unit of work.

Canonical values:
- A0 observe/summarize
- A1 draft/recommend
- A2 approval-gated reversible action
- A3 policy-bounded reversible action
- A4 consequential or binding action

### 5. Delivery Gate
A release/control checkpoint that constrains phase movement.

Minimum fields:
- gate id
- maturity thresholds
- required evidence
- accountable roles
- exit criteria

### 6. Client Dependency
A client-controlled prerequisite that can block readiness or release.

Minimum fields:
- dependency id
- system
- owner
- access state
- criticality
- blockers
- failure modes

### 7. Exception Class
A named class of failure, ambiguity, or escalation condition.

Minimum fields:
- exception id
- severity
- trigger condition
- human owner
- resolution target
- stop-work or rollback implication

### 8. Board Item
The operational projection of work onto portfolio and delivery boards.

Minimum fields:
- item id
- item type
- linked engagement/control loop
- current phase/gate
- owner
- priority
- evidence links
- blocked state

### 9. Reusable Asset
A reusable delivery artifact, playbook, pattern, or automation component.

Minimum fields:
- asset id
- asset type
- owning group
- source engagement(s)
- evidence of reuse value
- readiness status

### 10. Customer Success Review
A post-sale or operating review object tied to value realization.

Minimum fields:
- review id
- review period
- KPI movement
- incident/intervention summary
- trust/adoption signal
- proposed scope or autonomy changes

## Repo consumption rules

### `delivery-excellence`
Owns prose definitions, templates, governance semantics, and change control for these objects.

### `delivery-excellence-automation`
Owns machine-readable schemas, examples, and validation logic for these objects.

### `delivery-excellence-boards`
Must consume `Engagement`, `Control Loop`, `Delivery Gate`, `Board Item`, and `Client Dependency` objects.

### `delivery-excellence-innersource`
Must consume `Reusable Asset`, `Board Item`, `Delivery Gate`, and role/readiness semantics.

### `delivery-excellence-bounties`
Must consume `Delivery Gate`, `Reusable Asset`, and evidence completion semantics before assigning payout or incentive logic.

## Change rule

Any new downstream object that changes control, approval, release, or payout semantics must first be added here and then encoded in `delivery-excellence-automation` before downstream repos adopt it.

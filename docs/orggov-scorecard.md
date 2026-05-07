# OrgGov Scorecard v0.1

## Purpose

OrgGov Scorecard v0.1 makes Delivery Excellence the operating-metrics lane for Organization Governance Control Plane v0.

The scorecard tracks whether governed human-agent institutional work is legible, policy-covered, evidence-backed, replay-ready, reviewed, and improving.

## Dimensions

The v0 scorecard uses normalized 0.0 to 1.0 dimensions:

- `evidenceCompleteness`
- `policyCoverage`
- `replayReadiness`
- `operatorLegibility`
- `productCompression`
- `cycleTimeRisk`
- `reviewReadiness`
- `learningClosure`

`cycleTimeRisk` is inverted relative to most dimensions: higher means greater delivery/cycle risk.

## Contract files

- `schemas/orggov-scorecard.v0.1.schema.json`
- `examples/orggov-scorecard.v0.1.example.json`
- `tools/validate_orggov_scorecard.py`

## Invariants

- Every scorecard references objective, workroom, work order, outcome, evidence, and metric period.
- Every scorecard preserves non-secret provenance.
- Every dimension is normalized to the range 0.0 to 1.0.
- Every scorecard includes recommendations for the next operational loop.

## Cross-repo links

- Parent: `SocioProphet/prophet-platform#406`
- Delivery workstream: `SocioProphet/delivery-excellence#14`
- Policy decision: `SocioProphet/policy-fabric#57`
- Evidence binding: `SocioProphet/agentplane#104`
- Workspace control room: `SocioProphet/prophet-workspace#15`

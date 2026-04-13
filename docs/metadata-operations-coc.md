# Metadata Operations CoC

## Purpose

This document integrates operational metadata work into the DelEx Center of Capability model as a recurring service, not a one-time cleanup activity.

It formalizes how metadata completeness, inconsistency remediation, contact verification, glossary quality, and BTNR handling should operate inside the broader governance, delivery, and continuous-improvement system.

## Why metadata operations belong in the CoC

The CoC success criteria require:
- customer service focus and business-community buy-in
- early planning in the implementation lifecycle
- service-level expectations and measurement
- explicit central-versus-distributed ownership
- formal documentation and knowledge capture
- strong governance to control cost and demonstrate value
- motivated and coached staff
- use of technology to reduce friction

Operational metadata work directly serves those goals when treated as a governed service line.

## Service placement in the CoC model

### Engagement
- verify metadata contacts
- onboard metadata focals
- run intro package and AMG demo sessions
- collect engagement and adoption signals

### Strategy and Planning
- define metadata operating model
- define central vs distributed ownership
- define metadata SLA and escalation policy
- define glossary and BTNR governance
- plan staffing and retention for metadata capability

### Information Technology and Solution Design
- define report taxonomies and finding classes
- define sync, schema, and naming inconsistency handling
- define metadata quality dashboards
- design validators and automation around findings

### Transformation
- connect metadata quality to benefit cases and funding readiness
- prioritize use cases and sources based on business value and operational risk
- create backlog and sprint packages from report findings

### Delivery / Run and Maintain
- execute remediation stories and subtasks
- track completeness, inconsistency backlog, aging, SLA attainment, and reopen rates
- run glossary quality and BTNR disposition routines
- operate escalation path when engagement breaks down

## Operational streams

### Completeness stream
Focus on metadata presence and coverage.

Canonical checks:
- metadata contacts verified
- technical metadata present
- business metadata present
- red/yellow/green status assigned

### Inconsistency stream
Focus on structural, sync, and record-integrity discrepancies.

Canonical finding classes include:
- tabs_without_columns
- schema_without_app
- schema_without_table
- schema_without_table_oos
- schemas_missing_in_igc
- out_of_sync_column
- metadata_contact_inconsistency
- data_artifact_inconsistency
- glossary_quality_issue
- btnr_candidate

## TMD and BMD definitions

### TMD
Technical metadata is present when required technical description fields are populated, such as long and short descriptions.

### BMD
Business metadata is present when required business-term assignments are populated.

## Governance rule

Metadata operations are not a side queue. They are part of the governed delivery system and must be visible in:
- service catalog
- gate evidence requirements
- dashboard snapshots
- backlog and sprint packages
- reusable playbooks and enablement assets

## Evidence expectation

No metadata completion or remediation claim is valid unless it is backed by:
- a report or evaluation snapshot
- a named owner or target role
- a timestamped remediation action
- an auditable status change
- a reproducible dashboard or log artifact

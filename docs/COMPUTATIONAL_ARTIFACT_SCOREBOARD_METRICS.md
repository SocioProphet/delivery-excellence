# Computational Artifact Scoreboard Metrics

## Purpose

Delivery Excellence meters ProphetArtifact execution results through the Computational Artifact Scoreboard lane. This lane captures the signal set needed to score artifact execution, reproducibility, validation, benchmark, and promotion decisions within the Prophet Computational Knowledge Plane.

The scoreboard ensures artifact results are evidence-backed, reproducible, and aligned with the Delivery Excellence operating model before any promotion decision is made. Human review remains a hard gate for privileged and prohibited artifact classes.

## Schema

All scoreboard payloads must validate against:

```
schemas/computational-artifact-scoreboard.schema.json
```

Run local validation with:

```
python3 tools/validate_computational_artifact_scoreboard.py
```

Or via `make`:

```
make validate
```

## Metric definitions

The following metrics form the `computational-artifact-v0` metric set. All are required in every scoreboard payload for this metric set.

### `reproducibility_score`

**Type:** `ratio` (0–1) | **Direction:** maximize | **Threshold:** ≥ 0.95

Fraction of artifact execution attempts that produce byte-identical or semantically equivalent output given the same input and environment pin. A score below 0.95 triggers a `warn` status; below 0.80 triggers `fail`.

High reproducibility is the primary signal that the artifact runner is deterministic and that environment pins are correctly captured.

### `validation_status`

**Type:** `enum` (`pass` / `warn` / `fail` / `unknown`) | **Direction:** informational

Aggregate validation result after running all schema, contract, and output checks on the artifact's produced data. Mirrors the `rollup.validationStatus` field.

### `feature_count`

**Type:** integer ≥ 0 | **Direction:** informational

Total number of geospatial or domain features ingested or emitted by the artifact run. Used to detect silent truncation or runaway expansion across artifact versions.

### `invalid_feature_count`

**Type:** integer ≥ 0 | **Direction:** minimize | **Threshold:** ≤ 500

Count of features that failed schema or geometry validation. A non-zero count is a warning signal. Exceeding the threshold triggers `fail`.

### `ingest_latency_ms`

**Type:** integer ≥ 0 | **Direction:** minimize | **Unit:** ms

Wall-clock elapsed time from first-byte-read to last-byte-write for the artifact's primary ingest pipeline. Used to detect performance regressions across versions and environment configurations.

### `artifact_size_bytes`

**Type:** integer ≥ 0 | **Direction:** informational | **Unit:** bytes

Size of the primary output artifact on disk or in object storage after the run. Used to monitor artifact growth trends and catch runaway output.

### `evidence_completeness`

**Type:** `ratio` (0–1) | **Direction:** maximize | **Threshold:** ≥ 0.90

Fraction of scoreboard metric entries that carry an `evidenceRef` pointing to durable execution evidence (CI run, log, checksum, or audit record). A score below 0.90 blocks candidate promotion.

### `promotion_status`

**Type:** `enum` (`blocked` / `candidate` / `promoted` / `deprecated` / `unknown`) | **Direction:** informational

Current promotion state of the artifact. Emitted as a metric to make promotion history visible in time-series rollups. The authoritative value is `rollup.promotionStatus`.

## Rollup fields

| Field | Type | Meaning |
|---|---|---|
| `reproducibilityScore` | `number` [0, 1] | Overall reproducibility across sampled runs |
| `validationStatus` | `enum` | Aggregate pass/warn/fail/unknown from all validation checks |
| `promotionStatus` | `enum` | Current artifact promotion state |

## Scorecard states (from rollup)

| State | Condition |
|---|---|
| `promoted` | All checks pass, evidence complete, human review recorded (required for `privileged`/`prohibited` classes) |
| `candidate` | Metrics pass thresholds; promotion review pending |
| `blocked` | One or more critical metrics fail, or evidence incomplete |
| `deprecated` | Artifact superseded or retired |
| `unknown` | Scoreboard not yet computed |

## Privilege and promotion gates

**Privileged and prohibited artifacts cannot be marked `promoted` without explicit human review evidence.**

A scoreboard payload for a `privileged` or `prohibited` `safetyClass` artifact must include at least one `evidenceRef` value containing `"review"` or `"approval"` before `rollup.promotionStatus` may be set to `"promoted"`. The validator enforces this invariant.

This aligns with the Delivery Excellence operating model requirement that high-risk artifact execution decisions remain human-in-the-loop.

## How artifact metrics feed delivery metering

Artifact scoreboard signals flow into the Delivery Excellence operating model as follows:

```
Prophet Artifact Runner
        │
        ▼
Scoreboard Payload (computational-artifact-scoreboard.schema.json)
        │
        ├─► Delivery Excellence lane rollup
        │       reproducibility_score → signals deployment confidence
        │       evidence_completeness → gates promotion approval workflow
        │       promotion_status      → feeds phase-gate RACI
        │
        ├─► Outcome-driven agent metering
        │       feature_count / invalid_feature_count → data quality signal
        │       ingest_latency_ms                     → SLA adherence
        │       artifact_size_bytes                   → cost/capacity signal
        │
        └─► Human review queue (privileged/prohibited artifacts)
                promotion_status = candidate → triggers review assignment
                Human approval → sets promotion_status = promoted + evidenceRef
```

This ensures every artifact promotion decision is backed by measured execution evidence rather than subjective assertion.

## GAIA bounded OSM ingest slice

The `artifact://gaia.bounded-osm-ingest@0.1.0` artifact is the first onboarded slice in this lane. Its scoreboard path is:

1. **Runner emits** scoreboard payload after each CI execution (see `examples/computational-artifact-scoreboard.example.json`).
2. **Validator confirms** all eight metric names are present and within thresholds.
3. **Rollup** sets `reproducibilityScore`, `validationStatus`, and `promotionStatus`.
4. **Promotion review** is not required for `bounded` safety class; `promotionStatus: candidate` advances automatically when all thresholds pass.
5. **Delivery Excellence** records the scoreboard in the lane rollup under the GAIA program.

Example payload: `examples/computational-artifact-scoreboard.example.json`

## Payload shape for Prophet Platform emission

After each artifact runner execution the Prophet Platform should emit:

```json
{
  "schemaVersion": "v0.1",
  "scoreboardId": "scoreboard:computational-artifact:<artifactRef>:<YYYY-MM-DD>",
  "generatedAt": "<ISO-8601 timestamp>",
  "artifactRef": "artifact://<name>@<version>",
  "ownerRepo": "<org>/<repo>",
  "runRef": "github://<org>/<repo>/actions/runs/<runId>",
  "runtimeProfile": "<profile-name>",
  "safetyClass": "advisory | bounded | privileged | prohibited",
  "metricSet": "computational-artifact-v0",
  "metrics": [ /* see metric definitions above */ ],
  "rollup": {
    "reproducibilityScore": 0.0,
    "validationStatus": "pass | warn | fail | unknown",
    "promotionStatus": "blocked | candidate | promoted | deprecated | unknown"
  },
  "evidenceRefs": [ /* at least one durable CI/audit ref */ ],
  "lineageRefs": [ /* prior artifact version refs */ ]
}
```

Validate with `python3 tools/validate_computational_artifact_scoreboard.py` before publishing.

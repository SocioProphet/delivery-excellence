# KMASS Metrics v1

## Purpose

This document turns the KMASS framework into a DelEx-governed measurement contract.

The goal is to make outcome, capacity, and friction claims precise enough to be audited, tested, versioned, and attached to phase-gate acceptance.

## Metric contract columns

Each metric entry should define:
- metric id
- figure row / human-readable label
- metric type
- unit
- phase targets
- measurement protocol
- acceptable error or confidence rule
- required evidence artifacts

## Canonical metric set

| Metric ID | Figure Row | Type | Unit | Phase Targets | Evidence Artifact |
|---|---|---|---|---|---|
| `TAB.TEXT.GRAN` | Textual Granularity | Outcome | Top-1 accuracy @ unit | 80% @ {doc, para, sentence} | labeled query set + retrieval logs |
| `TAB.VIDEO.GRAN` | Video Granularity | Outcome | Success@5 or Recall@5 | 65% @ {video, clip, frame} | labeled multimodal queries + ranked outputs |
| `TAB.TEXT.SCALE` | Text Sources | Capacity | count | 20k / 120k / 800k | ingestion manifests + index cardinalities |
| `TAB.VIDEO.SCALE` | Video Sources | Capacity | hours | 40 / 220 / 400 | media catalog + segment index |
| `TAC.CAPTURE.FRICTION` | Easy and Natural | Friction | minutes / fact | 10 / 5 / 2 | timestamped capture traces |
| `TAD.LATENCY.JIT` | Just-in-Time | Outcome | seconds | 60 / 8 / 1 | end-to-end timing traces |
| `TAD.ACTIONS.JE` | Just-enough | Friction | action count | 10 / 5 / 1 | UI or agent action logs |
| `TAD.RELEVANCE.JFM` | Just-for-me | Outcome | percent relevant | 70 / 83 / 98 | human evaluation + rubric |
| `SYS.SPEEDUP` | Speed Improvement | Composite | multiplier | 1.1x / 2x / 5x | time-on-task studies |
| `SYS.SCALE.TBD` | Scale | Composite | multi-dimensional | TBD / TBD / TBD | policy/task/role graph stats |

## Retrieval-unit canon

### Text
- Document: immutable source blob identified by `doc_id` and `doc_rev`
- Paragraph: contiguous text span identified by `span_id = hash(doc_id, start_offset, end_offset)`
- Sentence: linguistic segment with explicit `segmenter_ver`

### Video
- Video: `video_id` with `duration_ms`
- Clip: `clip_id = hash(video_id, start_ms, end_ms)` with approximately 60-second span and explicit tolerance
- Frame: `(video_id, frame_index)` with `fps_assumed` and `decode_method_version`

## Measurement protocols

### Text accuracy
- metric: Top-1 exact match against labeled target set
- granularity: document, paragraph, sentence
- minimum sample size: 30 queries per phase per modality unless explicitly marked preliminary

### Video retrieval success
- metric: Success@5 or Recall@5
- matching rule: overlap against labeled temporal target window, ideally with explicit IoU threshold

### Relevance
- metric: percentage of results scored relevant under blinded human evaluation
- recommended rubric: 0 to 3, where score >= 2 counts as relevant

### Latency and actions
- latency: end-to-end query to answer completion time
- actions: discrete user or agent actions required to reach acceptable answer state

## Architecture commitments by phase

### Phase 1
- coarse indices
- document-level and video-level retrieval
- ranking and timing logs mandatory from day one

### Phase 2
- chunking pipeline with stable paragraph and clip identifiers
- reranking on local context windows
- basic role or task context for personalization

### Phase 3
- sentence-level or frame-level atomic provenance
- aggressive caching and precomputation
- context binding to identity, policy, and task state

## Scale model

Track at minimum:
- `|K|`: number of knowledge elements
- `|E|`: number of relations or provenance edges
- `|P(task)|`: policies per task
- `|CoP|`: communities of practice and role distributions
- task throughput by role and CoP

## Implementation profiles

### Minimal
- document and paragraph text indexing
- clip-level video indexing, frame-level only for cited clips
- stable provenance IDs required

### Maximal
- sentence-level atomic claims and claim normalization
- frame-level indexing with temporal grounding
- precomputation and caching for near-instant response

## Gate implication

No phase should be marked complete unless the metrics for that phase are attached to:
- a named measurement protocol
- evidence artifacts
- an acceptance threshold
- a reproducible run log

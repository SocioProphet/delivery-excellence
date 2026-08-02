# KMASS Baseline Readout — 2026-08-01

First measured instance of the metric contract in [`docs/kmass-metrics-v1.md`](../kmass-metrics-v1.md).

That contract has existed with 10 fully-specified metrics — ids, units, phase targets, measurement protocols, sample-size rules, required evidence artifacts — and a closing Gate implication rule. Prior to this run, **none of its metric ids appeared anywhere else in the repository.** Zero measurements had ever been taken, so the gate rule it declares for itself had never once fired.

Scoreboard: [`scoreboards/kmass-baseline-2026-08-01.json`](../../scoreboards/kmass-baseline-2026-08-01.json)
Validator: `python3 tools/validate_kmass_scoreboard.py`

## Headline

| | |
|---|---|
| Metrics in contract | 10 |
| Measured | **2** |
| Of those, vacuous (meets target but means nothing) | **1** |
| Unmeasured (capability exists, no valid run) | 5 |
| Unbuilt (capability does not exist) | 3 |
| Legitimate phase claims earned | **0** |

Retrievable documents: **12** against a Phase-1 target of 20,000 — 0.06%.

## What is actually working

Two components are load-bearing and real:

- **`embeddings`** — serving `nomic-ai/nomic-embed-text-v1.5` at 768 dimensions, p50 103ms over 10 samples. Healthy.
- **`sherlock-engine`** — tantivy index, p50 6.9ms, returned non-empty results for 14 of 30 queries against its 12 documents. Small, but genuine retrieval.

Everything below is built on the assumption that these two are the foundation to extend, not replace.

## The four findings that matter

### 1. The retrieval tier cannot accumulate a corpus — architectural, not volumetric

Zero PersistentVolumeClaims back any retrieval service.

| Service | Storage | Contents |
|---|---|---|
| `sherlock-engine` | `emptyDir`, 256Mi cap | 12 docs |
| `commons-search` | `store: memory` | 0 |
| `memoryd` | `backend: memory` | 0 resources / 0 events / 0 memories |
| `search-orchestrator` | `mode: in-memory` | 1421 seeded, **not retrievable** |

Every pod restart resets the corpus to zero. The 20k → 120k → 800k growth curve is unreachable by construction. No amount of ingestion effort fixes this before durable storage exists.

### 2. `search-orchestrator` returns zero results for every query

30 diverse queries returned `results: []`. So did generic probes — `a`, `the`, `learning`, `course`, `academy`, `*`, and the empty string — across every mode tried (`default`, `semantic`, `keyword`, `hybrid`, `all`).

Its own counters confirm this is not a client-side parsing artifact: `search_query_total` advanced 0 → 30 while `academy_result_total` stayed at **0**. The 1421 seeded academy records are not connected to the retrieval path.

### 3. The search policy gate has never fired — including during this run

Before the run and after 30 successful queries, all five policy counters read zero:

```
policy_decision_allow_total    0 -> 0
policy_decision_deny_total     0 -> 0
policy_decision_local_total    0 -> 0
policy_decision_remote_total   0 -> 0
policy_decision_fallback_total 0 -> 0
```

A policy gate that does not evaluate on the request path is declared, not enforced. Whether it is short-circuited by the empty result set or simply unwired, the conclusion for a reviewer is identical: there is no evidence this control has ever made a decision.

### 4. Latency "passes" Phase 3 by 113x, and the pass is worthless

p50 of **8.8ms** against a Phase-3 target of 1 second. Recorded as `vacuousPass: true` and claiming no phase, because all 30 queries returned nothing. Measuring the latency of returning an empty set measures nothing.

This is the most dangerous number in the scoreboard — it is the one that would survive a slide review unchallenged. The schema and validator exist specifically so it cannot be promoted into a phase claim.

**Also worth stating plainly, precisely:** `search_query_total` was exactly `0` before this run. The counter is process-local (`mode: in-memory`, like everything else in this tier), and the current pod was 3d2h old with 0 restarts — so this proves at least 3 days with no evidence of query traffic, not that the service has literally never served a query since the Deployment was created (2026-07-13, ~3 weeks earlier); an earlier pod incarnation could have. Either reading lands the same place: green health checks were reporting success on a path with no confirmed traffic for at least three days — the same shape as the Loki incident earlier the same day, where a merged, healthy-looking pipeline had ingested zero bytes for 2.5 days.

## Run log

Probes ran **inside the cluster** from a pod in the `socioprophet` namespace, against ClusterIP service DNS, to exclude ingress and WAN variance from the latency figures. Python stdlib `urllib` only; latency captured with `time.perf_counter()` around the full request/response cycle.

Environment: `gke_socioprophet-platform_us-central1_prophet-platform`

Query set: 30 fixed domain-relevant strings (`governance policy`, `evidence receipt`, `agent registry`, … `scoreboard metric`), meeting the contract's minimum of 30 queries per phase per modality.

Sequence:

1. Read `/healthz` on `memoryd`, `commons-search`, `search-gateway`, `search-orchestrator`, `holmes`, `sherlock-engine`, `embeddings` — captured store backends and document counts.
2. Read `/v1/search/debug/config` and `/v1/search/debug/metrics` on `search-orchestrator` — captured pre-run counters.
3. Issued 30 `POST /v0/search/query` with the correct `SearchRequest` shape (`query_id`, `actor_id`, `text`, `mode`, `limit`), timing each.
4. Issued 30 `GET /search?q=` against `sherlock-engine`, timing each.
5. Issued 10 `POST /v1/embeddings`, timing each.
6. Re-read `/v1/search/debug/metrics` — computed the counter delta.
7. Fairness pass: re-queried with generic terms and all five modes to rule out vocabulary mismatch as the cause of zero results.
8. Checked cluster-wide for video/media/ASR pods and for PVCs backing any retrieval service.

An earlier attempt used `{"query": ...}` and got HTTP 422 across the board. That was a wrong payload shape on my side, not a service fault; the schema was read from `/openapi.json` and the run repeated correctly. Recorded here so the 422s in any captured logs are not mistaken for a defect.

No secrets, file paths, actor identities, or query contents are persisted in the scoreboard's evidence strings.

## Reproducing

```bash
python3 tools/validate_kmass_scoreboard.py
```

The validator is fail-closed and was proven to fire in both directions before being committed. Five adversarial mutations of this scoreboard were each caught: claiming a phase off the vacuous latency pass, deleting an inconvenient metric row, claiming a phase with no run log or evidence, marking a metric measured with a null value, and leaving a gap unexplained.

## What this readout is for

The `UNMEASURED` and `UNBUILT` rows are not gaps in the report. They **are** the program backlog, derived from measurement rather than invented in a planning session. They are worked in [`docs/work-orders/WO-KMASS-01-close-the-baseline.md`](../work-orders/WO-KMASS-01-close-the-baseline.md).

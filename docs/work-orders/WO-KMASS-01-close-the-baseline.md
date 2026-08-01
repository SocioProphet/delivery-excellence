# WO-KMASS-01 — Close the Baseline

**Origin:** [`docs/reports/kmass-baseline-readout-2026-08-01.md`](../reports/kmass-baseline-readout-2026-08-01.md)
**Contract:** [`docs/kmass-metrics-v1.md`](../kmass-metrics-v1.md)
**Status:** open
**Objective:** move every metric in the contract from `UNBUILT`/`UNMEASURED` to `MEASURED`, and earn the first legitimate Phase-1 claim.

This work order is derived from measurement, not planning. Every task below exists because a specific metric could not be measured on 2026-08-01, and each carries the metric id it unblocks.

## Dependency shape

Most of the backlog is blocked behind two root causes, not ten independent gaps:

```
  WO-01  durable retrieval tier ──┬── WO-02 reconnect orchestrator retrieval
                                  │        └── WO-03 policy gate on the request path
                                  │        └── WO-04 labeled eval set ── WO-05 non-vacuous latency/actions
                                  └── WO-06 corpus ingestion to 20k
  WO-07  capture instrumentation (independent)
  WO-08  media/ASR tier (independent, largest)
  WO-09  org twin ── unblocks SYS.SCALE (see design note)
  WO-10  wire the gate into CI (independent, do first — it is cheap)
```

Sequencing consequence: **WO-01 gates six other items.** Nothing in TA B or TA D can produce a durable number until storage is durable. Do not parallelise the dependents ahead of it.

---

## WO-KMASS-01.10 — Wire the scoreboard gate into CI

**Unblocks:** the enforcement of every row below
**Effort:** hours
**Owner repo:** `delivery-excellence`

`tools/validate_kmass_scoreboard.py` exists and is proven fail-closed in both directions, but nothing runs it automatically yet. Until it is a required check, the gate rule remains advisory — the exact condition this program is trying to cure.

**Acceptance:**
- [ ] `.github/workflows/kmass-scoreboard.yml` runs the validator on every PR touching `scoreboards/**`, `schemas/kmass-scoreboard.*`, or `docs/kmass-metrics-v1.md`
- [ ] The check is marked **required** in branch protection, matching the `gate / check` pattern already required across six estate repos
- [ ] Adding a new metric id to the contract makes existing scoreboards fail until measured (already implemented — verify it in CI, don't assume)

**Do this first.** It is the cheapest item and it makes every later claim falsifiable.

---

## WO-KMASS-01.01 — Give the retrieval tier durable storage

**Unblocks:** `TAB.TEXT.SCALE`, and transitively `TAB.TEXT.GRAN`, `TAD.RELEVANCE.JFM`, `TAD.ACTIONS.JE`, `SYS.SPEEDUP`
**Effort:** days
**Owner repo:** `prophet-platform` (`infra/k8s/`)
**Severity:** critical — this is the single highest-leverage item in the work order

Every store in the retrieval tier is non-durable: `sherlock-engine` on a 256Mi `emptyDir`, `commons-search` and `memoryd` on in-memory backends, `search-orchestrator`'s academy repository in-memory with no configured file or carrier source. Corpus resets to zero on every pod restart.

**Acceptance:**
- [ ] `sherlock-engine`'s tantivy index is on a PVC sized for the Phase-2 target (120k docs), not an `emptyDir`
- [ ] `memoryd` runs against a persistent backend (Qdrant is already the documented intent) rather than `backend: memory`
- [ ] `commons-search` either gets a durable store or is explicitly retired as duplicative of `sherlock-engine` — decide, don't leave two empty in-memory indices
- [ ] **Proof of durability:** delete each pod, confirm document count survives. A green `/healthz` is not evidence; the count after a restart is.
- [ ] Note the GKE Autopilot constraint learned this week: write-mode `hostPath` is rejected outright by the Warden admission webhook. Use PVCs.

---

## WO-KMASS-01.02 — Reconnect the orchestrator's retrieval path

**Unblocks:** `TAB.TEXT.GRAN`, `TAD.RELEVANCE.JFM`, and de-vacuums `TAD.LATENCY.JIT`
**Effort:** days
**Owner repo:** `prophet-platform` (`apps/search-orchestrator`)
**Severity:** critical

`search-orchestrator` holds 1421 seeded academy records and returns `results: []` for every query in every mode, including wildcard and empty string. `academy_result_total` stayed at 0 across 30 successful queries. The seeded corpus is not wired to the query path.

**Acceptance:**
- [ ] A query matching known seeded content returns a non-empty result set
- [ ] `academy_result_total` advances when results are returned
- [ ] `academy_ingest_total` advances when content is ingested (currently permanently 0 — ingestion has never run)
- [ ] One of `json_file` / `lampstand_jsonl` / `lampstand_carrier` is configured `true` in `/v1/search/debug/config`, so the corpus has a real source rather than a seed
- [ ] **Regression test:** a test that fails if any query path returns the empty set for a term known to be in the corpus. This defect was invisible because nothing asserted non-emptiness.

---

## WO-KMASS-01.03 — Put the policy gate on the request path

**Unblocks:** credible TA D governance claims; no metric directly, which is exactly why it has gone unnoticed
**Effort:** days
**Owner repo:** `prophet-platform` + `policy-fabric`
**Severity:** critical

All five `policy_decision_*` counters read zero before and after 30 real queries. `policy_fabric_endpoint` is `false`; the service runs in `local-fallback` mode and even the fallback counter never increments.

**Acceptance:**
- [ ] A query produces a non-zero increment on exactly one of `allow` / `deny` counters
- [ ] `policy_fabric_endpoint` is configured, and `remote` vs `local` vs `fallback` counters distinguish which path served the decision
- [ ] **Prove teeth both ways:** a query that must be denied is denied and increments `deny_total`. A gate only ever observed allowing is not distinguishable from an absent gate.
- [ ] Add a liveness alert on "zero policy decisions over a period in which queries were served" — the condition that hid this for the service's entire lifetime

---

## WO-KMASS-01.04 — Build the labeled evaluation set

**Unblocks:** `TAB.TEXT.GRAN` (and is a prerequisite for any accuracy claim at all)
**Effort:** days
**Owner repo:** new, or `delivery-excellence/fixtures/`
**Depends on:** WO-01.02

The contract requires Top-1 exact match against a labeled target set, minimum 30 queries per phase per modality. No such set exists anywhere in the estate.

**Acceptance:**
- [ ] ≥30 labeled query/target pairs at document granularity (Phase 1)
- [ ] Targets addressed by the contract's canonical retrieval-unit ids — `doc_id`+`doc_rev` for documents, `span_id = hash(doc_id, start, end)` for paragraphs, explicit `segmenter_ver` for sentences
- [ ] A harness that computes Top-1 accuracy and emits a scoreboard-compatible evidence artifact
- [ ] Labeled set is versioned and reviewable; an eval set that can be silently edited to make a number go up is not evidence

---

## WO-KMASS-01.05 — Re-measure latency and actions non-vacuously

**Unblocks:** legitimate `TAD.LATENCY.JIT` and `TAD.ACTIONS.JE` claims
**Effort:** hours (once dependencies land)
**Depends on:** WO-01.02, WO-01.04

Current latency of p50 8.8ms nominally beats the Phase-3 target by 113x and is recorded `vacuousPass: true` because every query returned nothing.

**Acceptance:**
- [ ] Latency re-measured with `nonzero-result ≥ 90%` of the sample, `vacuousPass` set false
- [ ] `TAD.ACTIONS.JE` defined against a concrete "acceptable answer state" and counted on a real surface
- [ ] Expect the honest number to be **worse** than 8.8ms. That is the point; a regression against a vacuous baseline is progress.

---

## WO-KMASS-01.06 — Ingest to the Phase-1 corpus target

**Unblocks:** `TAB.TEXT.SCALE` Phase-1 claim
**Effort:** weeks
**Depends on:** WO-01.01, WO-01.02

12 retrievable documents against a 20,000 target.

**Acceptance:**
- [ ] ≥20,000 documents retrievable and surviving a pod restart
- [ ] Ingestion manifests + index cardinalities as evidence artifacts, per the contract
- [ ] Stable `doc_id` / `doc_rev` provenance on every document — the contract's Phase-1 architecture commitment requires ranking and timing logs mandatory from day one

---

## WO-KMASS-01.07 — Instrument capture friction

**Unblocks:** `TAC.CAPTURE.FRICTION`
**Effort:** days
**Owner repo:** `goose-notes`
**Independent of the retrieval chain — can run in parallel**

`goose-notes` is the designated capture surface but is not deployed to the measured environment and emits no timing traces. The metric needs minutes-per-fact over n=30.

**Acceptance:**
- [ ] Capture surface emits timestamped traces: capture-initiated → fact-committed
- [ ] n≥30 traces collected under realistic task conditions, not a synthetic loop
- [ ] Baseline number recorded even if it is far worse than the 10-minute Phase-1 target
- [ ] **Phase-3 scope note:** the target trajectory ends at cell-phone / personal-sensor capture. Nothing in the estate addresses mobile capture today. Flag now whether that is in scope, because it is a build, not an instrumentation task.

---

## WO-KMASS-01.08 — Media / ASR tier

**Unblocks:** `TAB.VIDEO.GRAN`, `TAB.VIDEO.SCALE`
**Effort:** weeks — largest single item
**Owner repos:** `videolab`, `imagelab`, `speechlab` (currently lab repos, not deployed services)
**Independent of the retrieval chain**

No video, media, ASR, or transcode capability exists in the cluster. Verified: zero matching pods across all namespaces. Both video metrics are `UNBUILT`, not merely unmeasured.

**Acceptance:**
- [ ] Media ingest + catalog with `video_id` and `duration_ms`
- [ ] Segment index using the contract's canonical ids: `clip_id = hash(video_id, start_ms, end_ms)` at ~60s spans with explicit tolerance; frames as `(video_id, frame_index)` with `fps_assumed` and `decode_method_version`
- [ ] ≥40 hours catalogued (Phase-1 target)
- [ ] Success@5 or Recall@5 measurable with an explicit IoU threshold

**Recommend a scope decision before starting.** This is the most expensive item in the work order and the estate currently has zero of it. If video is not near-term, mark both metrics out-of-scope explicitly in the contract rather than carrying them as perpetual `UNBUILT` — an honest descoping is better than a permanent red row.

---

## WO-KMASS-01.09 — Org digital twin

**Unblocks:** `SYS.SCALE.TBD`, plus scenario simulation for roadmap choices
**Effort:** weeks
**Design:** [`docs/design/org-digital-twin-v0.md`](../design/org-digital-twin-v0.md)

`SYS.SCALE.TBD` is the only row whose phase targets are themselves undefined, and its variables are organizational rather than product: knowledge elements, distinct tasks, policies per task, communities of practice, roles within CoPs, tasks per CoP. It is an org model by definition. See the design note.

---

## Definition of done for this work order

- [ ] Every contract metric reads `MEASURED` with a real number, or is explicitly and deliberately descoped in the contract itself
- [ ] Zero rows carry `vacuousPass: true`
- [ ] At least one metric carries a legitimate `phaseClaim` with all four gate attachments
- [ ] The scoreboard validator is a required CI check
- [ ] A second scoreboard exists, so trend is visible — a single point is a measurement, two points are a program

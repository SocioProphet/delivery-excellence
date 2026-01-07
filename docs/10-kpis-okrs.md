# KPIs and OKRs

We separate instruments (KPIs) from goals (OKRs). KPIs are continuously measured signals; OKRs are time-boxed bets.

## Core KPIs (always-on)

Delivery flow:
- Lead Time (median / p90): request created → done
- Cycle Time (median / p90): started → done
- Throughput: items done per week (by stream + GEO)
- WIP: active items per stream (and WIP aging buckets)
- Blocked Time: % of cycle time in blocked state; count of items blocked > 24h/72h/7d
- Predictability: planned vs completed per week (and per sprint/quarter)

Quality / correctness:
- Reopen Rate: % items reopened within 14 days
- Escaped Defects: defects found after “done” / release
- Evidence Completeness: % done items with required evidence links present
- Review Latency: median time to first review; median time to approval (ADRs + PRs)

Reliability / ops (if applicable):
- Change Failure Rate: % changes causing incidents/rollback
- MTTR: mean time to restore for incidents tied to delivery changes
- Recurrence Rate: repeated incidents with same root cause within 90 days

Governance adoption:
- Template Compliance: % WoW items using required template fields
- ADR Coverage: % architecture-impacting changes with ADR recorded

## Recommended Quarterly OKRs (v1)

O1: Reduce delivery uncertainty and unblock work faster.
- KR1: Reduce p90 lead time by 20% vs prior quarter.
- KR2: Cut items blocked >72h by 50%.
- KR3: Maintain predictability ≥ 85% (planned vs done).

O2: Increase quality and auditability without slowing flow.
- KR1: Evidence completeness ≥ 95% for “done” items.
- KR2: Reopen rate ≤ 5%.
- KR3: ADR coverage ≥ 90% for architecture-impacting changes.

O3: Make enablement compounding, not rediscovery.
- KR1: Publish ≥ 8 reusable patterns/playbooks with proof artifacts.
- KR2: Run ≥ 6 enablement sessions (tech + sales) with ≥ 80% positive feedback.
- KR3: Decrease repeat “how do we…” questions by 30% (tracked via tagged issues/threads).

All thresholds are policy knobs; the point is tight feedback loops plus auditable evidence.

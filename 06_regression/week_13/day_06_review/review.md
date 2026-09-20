# Day 6 Review — Week 13 Consolidation

## Retrieval (spot-check the cold list)

The day's lesson.md cold list IS the review — if any item needed a peek,
it goes on YOUR spaced-repetition schedule for +1 week. The five that
matter most long-term (course-wide spaced schedule):

1. SE(β̂) = σ̂_e/(σ̂_x√n) and its three levers.
2. A2 vs A4/A5 vs A6: the failure hierarchy.
3. The sandwich: (XᵀX)⁻¹ meat (XᵀX)⁻¹; White meat = Σ e_t² x_tx_t′.
4. OVB: bias = γ · (regression of omitted on included).
5. R² calibration bands (0.9 twins / 0.2–0.5 stock-market / ~0 honest
   predictive).

## Interleaved problem

Take any regression you ran this week. Fill this block without code:

- β̂ ± 95% CI (from the printed SE): ____
- The one assumption audit that worries you most, and why: ____
- The SE flavor you would report, and the one-line defense: ____
- The sentence starting "This estimate could mislead because…": ____

<details><summary>What a strong answer looks like</summary>

Specific numbers in slot 1; a named assumption (not "the assumptions") in
slot 2 with a *reason tied to your data's structure* (e.g. "A4 — the
2020 bucket's variance was 5× 2019's; White repairs it, repair verified:
ratio 1.18"); slot 3 defended by the audit, not by habit; slot 4 pointing
at a *future* failure (window change, regime change, omitted factor),
not a past one. Glib answers ("multiple testing", "outliers") score zero
— the course's question is always "how could THIS be wrong, specifically?"
</details>

## Spaced-repetition scheduling (add to PROGRESS.md)

| Concept | Revisit | Method |
|---|---|---|
| Normal equations / closed forms | +1 week | rebuild ols_fit from blank |
| SE closed form + sandwich | +1 week | re-derive; hand-compute SE from summary stats |
| GM assumptions + hierarchy | +1 month | cold dump, grade vs lesson 4 §2 |
| White vs NW reach | +1 month | one-paragraph each: what it fixes, what it misses |
| OVB formula | +3 months | compute implied bias on a real regression of yours |

## Self-grade

- Cold list: 10/10 without notes? (Log the misses.)
- The 20-minute build: made the box? (Log the time.)
- The table-you-refuse-to-publish comment: could a busy PM act on it?

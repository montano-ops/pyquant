# Day 4 Review — Building a Panel

## Retrieval (answers)

1. Outer join = union of dates, NaN where not trading — the honest
   panel; inner = intersection — shrinks to common days, over-weights
   liquid/calm; fillna(0) fabricates calm; ffill inside gaps
   fabricates flat returns then jumps.
2. NaN lattice: leading = pre-IPO (didn't exist); trailing = delisted
   (stopped); interior = halts/vendor gaps/holidays; all-NaN = bad
   ticker/vendor failure (loud, by design).
3. Phantom return: pct_change across a gap = multi-day "return";
   adjusted staleness: mixed pulls rewrite history on action dates.
4. Panel hygiene: one frozen pull; outer+NaN; phantom flag;
   per-ticker scans; panel_info ID card.

## Elaboration prompts

- Your colleague proposes backfilling leading NaNs with each stock's
   first price "so the matrix is dense." Write the two-sentence
  refusal (fabricated zero returns pre-existence; survivorship
  laundering via dense panel).
- The panel_info ID card: which 3 fields would you ADD for a
  strategies panel (turnover, cost estimate, capacity per name)?

## Interleaved problem

Panel of 4 stocks, 1000 days. A: all days. B: first 400 only
(acquired). C: last 600 only (IPO 2017). D: all days but a 5-day
halt at day 500. (a) Shape after outer join? (b) Rows surviving
dropna? (c) Compute cross-sectional mean return per day correctly
(mean of available names, NaN-aware) vs the dropna version — how
biased is 2016 in the dropna version?

<details><summary>Reference answer</summary>

(a) 1000 × 4 with NaNs: B trailing (days 400–999), C leading (0–399),
D interior (500–504). (b) dropna keeps only days where all four have
data: days 0–399 minus nothing... A all, B until 400, C from 400, D
minus 500–504: the intersection is EMPTY for C (C starts where B
ends) — dropna returns ~0 rows! The panel vanishes. (c) NaN-aware
mean: day 300 uses A, B, D (3 names); 2016 (days ~250–400) drops C
from the cross-section — the dropna version drops the whole DAY,
deleting A/B/D's information. **Survivorship via cleaning: one
delisted ticker deletes the entire market's days — this is why
`dropna()` on panels is a research sin.**
</details>

## Self-grade

- The four NaN patterns + meanings, cold?
- Could you state the phantom-return bug and its two fixes in one
  breath?

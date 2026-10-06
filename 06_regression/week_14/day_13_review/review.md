# Day 13 Review — Week 14 Consolidation

## Retrieval (spot-check)

The lesson's cold list is the review; misses go on your +1-week schedule.
The four worth never losing:

1. Overlap → ramp ACF → NW with L ≥ q (and under-lagging = false comfort).
2. Multicollinearity signature: small t's, big joint F, stable sums.
3. Phenomenon tails are not outliers: winsorize characteristics, not
   returns; delete provable errors, log by name.
4. Interactions are questions: δ̂ with t(δ̂), thresholds declared ex ante.

## Interleaved problems — reference answers

**P1.** ACF(10) = 0.84, ACF(63) = 0, L ≥ 63. A lag-1 spike ABOVE the ramp:
an MA(1)/bid-ask-bounce-type microstructure effect or stale pricing
(day-specific), i.e. overlapping isn't your only A5 violator — L covers
it (≥ max lag present), but daily microstructure noise in the *predictor*
raises an errors-in-variables flag for β̂ itself (module 09).

**P2.** Better: report both 12-VIF variables jointly (F-test; CI on their
sum/difference per the research question); or orthogonalize with a
THEORY-stated order and show both orderings. Dropping one prices the
dropped variable's contribution at exactly zero — a research finding made
by silence.

**P3.** Statistical: the shift (>0.5 SE) means those days carry the
signal — report both fits, check the identity of the days (earnings =
real information events, so they fail the module-05 error test and MAY
NOT be deleted). Research: your signal is (partly) an earnings-news
strategy wearing your signal's clothes — the finding that survives is
"effects concentrate in earnings weeks", which is itself publishable-
grade information and changes the execution design (capacity/trading
dates).

**P4.** (a) the calm optimizer: winsorized 0.95 with the bias disclosed
(its MSE is better in-regime); (b) the stress model: raw 1.14 (tails =
mandate). Risk committee quote: "β̂ = 1.14 ± 0.05 raw, with calm-regime
central estimate ≈0.95; we size hedges off the raw number and treat the
gap as the crisis-beta premium."

**P5.** `r_nextmonth ~ mom_12_2 + D_crisis·mom_12_2`: β̂ = calm momentum
loading, δ̂ = crash-regional change (expect δ̂ < 0, JT/DM-flavored), t(δ̂)
the test. Threshold: pre-declared ex-ante — e.g. market 21-day realized
vol above its 90th historical percentile, written in the log BEFORE the
fit, and (this is day 07.18's seed) crisis defined by ex-post minus-20%
drawdowns is FORBIDDEN (look-ahead flavor).

## Spaced repetition

| Item | When | How |
|---|---|---|
| The SE decision path (fan? overlap? → flavor) | +1 week | redraw the routing, one regression end-to-end |
| VIF + joint-F reading | +1 month | cold on a 3-factor fit |
| Winsor y/x asymmetry | +1 month | the four-column clip matrix from memory |
| Interaction grammar | +3 months | crisis-beta fit from blank |

## Self-grade

- The 25-minute build made the box? (Log it honestly.)
- The dress-rehearsal two-sentence finding: would you sign it?
- R5's four questions: could you write them for a stranger's report?

# Day 13 — Review: Days 8–12

Cold retrieval, then problems. Commit to answers before checking. NO NOTES.

## Cold retrieval

1. The overlap arithmetic: forward q-sums at daily frequency → ACF shape
   and where it dies. The SE inflation scale factor, and why √q.
2. Newey–West meat: the two added pieces vs White (lag terms, weights),
   and the lag-selection rule for overlap q and for non-overlapped series.
3. Multicollinearity: the signature trio (t's, joint F, R²), the VIF
   formula, why pairwise-correlation inspection is insufficient.
4. The four-panel diagnostic page: panels, policed assumptions, triggered
   repairs.
5. Leverage vs influence: h_tt and Cook's D definitions, thresholds, the
   dangerous quadrant, and the delete-and-report protocol.
6. Trim vs winsor; the stability-vs-bias trade numbers from the
   tournament; the y-vs-x asymmetry rule.
7. Interaction grammar: β̂, γ̂, δ̂, β̂+δ̂, t(δ); the dummy trap; main-
   effect reading with interactions present.
8. Logs: per-dollar vs per-doubling theory; the leverage rescue; the
   elasticity case.
9. Threshold mining: why search-max t is not evidence and what the
   two-column honest report looks like.
10. The full SE decision path so far: classical → White → NW, and the two
    questions (fan? overlap?) that route you.

## Interleaved problems

**P1.** Forward 63-day sums at daily frequency: predict ACF(10), ACF(63),
and the L you'd pass to `se_nw`. Then the surprise: your residual ACF
also shows a spike at lag 1 ABOVE the ramp. What second mechanism could
add that?

**P2.** VIFs: [1.1, 12, 12, 1.3]. The PM says "drop one of the 12s and
ship." Two better dispositions.

**P3.** Cook's D top-3 days: all the same earnings week. Deleting them
moves your signal's t from 2.2 to 1.3. Write both the statistical and the
research dispositions.

**P4.** Winsorized-y beta 0.95 (SE 0.03) vs raw beta 1.14 (SE 0.05):
which enters (a) the calm-regime optimizer, (b) the stress-loss model,
and what do you quote to the risk committee?

**P5.** Write the interaction model for "momentum works except in
crashes", name each coefficient's reading, and state the ex-ante
threshold rule you'd declare.

## Build (25 min)

From blank: `ols_multi` + `se_nw` + one overlapped-series fit with
classical/NW t's, a VIF report on three (deliberately) correlated
regressors, and a crash-interaction fit with declared threshold. If this
takes >25 minutes, the log notes which piece needed rebuilding — day 14
assumes all of it.

## Error log

One line: this week's repairs each charge a price (NW: noisy SEs; White:
efficiency; winsor: bias; orthogonalization: a theory claim). Which price
were you most tempted to pretend wasn't being charged?

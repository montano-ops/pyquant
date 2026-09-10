# Day 14 — Mini-Project: The Portfolio Variance Laboratory

## The brief

A complete small study of diversification, using everything from weeks 1–2.
Universe: as many of the course ETFs as you can (or `research50` if you want
ambition; synthetic fallback is fine and seeded).

**Part 1 — The diversification curve.** Randomly select (seed!) groups of
$n$ assets for $n = 1, 2, 4, 8, 16, 32$ (repeat each 20 times, average the
vols). Plot portfolio vol vs $n$ with the theoretical floors: average
variance / n, and average covariance, overlaid. Does the curve flatten at
$\bar{\text{cov}}$? (Day 10's formula says it must — your data says how
fast.)

**Part 2 — The correlation regime.** Split the sample into high-vol and
low-vol halves (by median of average rolling vol). Rebuild $\Sigma$ and the
curve in each regime. What happens to $\bar{\text{cov}}$ in the stormy half?
What happens to the *practical value* of diversification exactly then?

**Part 3 — Estimation noise.** Split the sample in half by time. Compute the
min-variance weights (day 12) from half A; measure their realized vol on
half B. Compare against: (i) equal weights on half B, (ii) min-variance
computed on half B itself (the "cheating" optimum). The gap between (ii) and
(i) is what perfect covariance knowledge would buy you; the gap between your
A-weights and (i) is what estimation error costs. Report both, in vol points.

**Write-up (one page):** the three exhibits with your reading of each, plus
the reflection questions:

1. What does the flattening curve imply for "just add more stocks"?
2. Regime shift: if covariances double in crises, what happens to the
   risk of a portfolio sized in calm times?
3. Estimation: was your half-A portfolio *better or worse* than naive 1/N
   out of sample? What does that single data point NOT establish (think:
   module 13, multiple testing)?

## Rules

- Every random choice seeded and logged.
- Every portfolio return computed as `rets @ w` (simple returns — you know
  why by now).
- The "cheating" portfolio in Part 3 must be labeled as cheating — in-sample
  optima are for diagnosis, never for reporting as performance.

Done means: three exhibits + one page + a bias-aware reflection you could
defend out loud.

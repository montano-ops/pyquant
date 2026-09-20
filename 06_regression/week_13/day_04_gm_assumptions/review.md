# Day 4 Review — The Gauss–Markov Assumptions

## Retrieval (answers)

1. A1 linearity; A2 exogeneity E[ε|X]=0 (unbiasedness); A3 no perfect
   collinearity (existence); A4 homoskedasticity (Classical SEs +
   efficiency); A5 no autocorrelation (classical SEs); A6 normality
   (small-sample exact inference, optional).
2. Hierarchy of failure: A2 (bias — unfixable by SE choice) → A4/A5
   (inference — sandwich-fixable) → A6 (harmless at research n).
3. OVB formula: plim β̂ = β + γ·cov(x, omitted)/var(x) — bias = omitted
   loading × regression of omitted on included.
4. Heteroskedasticity that *tracks |x|* inflates true SE above the
   classical one; time-only variance variation with an iid regressor
   roughly cancels in the classical estimate.
5. Autocorrelated errors hurt especially with a *persistent regressor*;
   with iid x the cross-products average out.

## Elaboration prompts

- "Robust standard errors cannot fix a broken model." Explain using A2,
  with the precise-wrong-number image.
- Where in YOUR day-to-day data work could an omitted-variable story like
  E2(d) be running right now? Name the omitted variable candidate and the
  sign of the bias it induces.

## Interleaved problem

A colleague regresses next-month stock returns on this month's *volatility
level* (a persistent regressor, AR(1) ≈ 0.95) with pooled daily-resampled
data and reports t = 6.2 under classical SEs. Rank your suspicions with
repairs, and state which single check you run first.

<details><summary>Reference answer</summary>

First suspicion: **A5 failure with a persistent regressor** — the E2(c)
pairing; classical t = 6.2 can be a NW-corrected t ≈ 2 or less. First
check: ACF of the residuals + refit with Newey–West at a lag scale matching
the observation overlap/persistence (day 8). Second suspicion: overlapping
observations if "next-month" is measured at daily frequency — same repair
class. Third: A2 — vol level proxies for known factors (is it vol, or is it
beta? day 16 teaches the FF92 version of this question). And *not* on the
list: non-normality — A6 is the least of this regression's problems.
</details>

## Self-grade

- A1–A6 cold, each with its "buys" and its repair?
- The OVB formula, and its two corollaries?
- The tournament table's four rows from memory — which world broke which
  property?

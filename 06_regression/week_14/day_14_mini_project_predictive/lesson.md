# Day 14 — Mini-Project: The Predictive Regression

**The deliverable:** a one-page honest report on whether lagged
volatility and lagged dollar volume *predict* next-month returns — run on
your module-05 panel (50 names) or a planted synthetic twin. Question →
construction (shift discipline) → regression + SE justification → R² in
economic context → stability → *how could this be wrong?*

## Why this assignment, at this exact point in the course

Every prior regression this module was *contemporaneous*: x and y from
the same period (market model, betas). Prediction is different and
costlier: it needs **shift discipline** (x known strictly before y —
module 08's and module 13's god-term), it meets **persistent regressors**
(vol levels are AR(1) ≈ 0.9 — your day-4 tournament row (c) is now live
ammunition), and its honest R² is 0.00–0.05, which you will now learn to
*read* instead of apologize for. Week 15 exports this whole protocol to
the cross-section (FF92's playground); today you run it end-to-end at the
smallest real scale.

## The build

1. **Question and hypotheses (written first).** E.g.: "High realized vol
   this month is associated with LOWER returns next month (the
   low-volatility anomaly flavor); high dollar volume predicts — what?
   Write the sign you expect for each regressor and WHY before touching
   data." Stale-but-honest priors, in the log.
2. **Construction.** Monthly returns per name (log, month-end sampling);
   predictors computed from data strictly *within* the prior month:
   realized vol σ̂_{i,t} (daily returns, month t), log dollar volume;
   response: return of month t+1. The entire correctness of the study is
   two timestamps: **every predictor's last data point precedes every
   response's first.** Lag/shift audit printed (day
   8's overlap lesson: use NON-overlapped months).
3. **The regression.** Pooled panel *or* per-name time series (your
   choice — defend it): r_{i,t+1} ~ σ̂_{i,t} + logDV_{i,t}. SE flavor:
   justify from the panel structure (cross-correlation across names in
   the same month — day 15's problem preview; accept per-name White as
   the working baseline and say why).
4. **R² in context.** Report it, then calibrate: what would R² = 0.02
   monthly *mean* if real? Convert the fitted coefficient into an
   economic quantity: "moving from the 25th to 75th vol percentile
   changes next-month expected return by __ bp" — that sentence, not R²,
   is the claim.
5. **Stability.** Split-sample sign check (first half vs second half);
   rolling 36-month coefficient plot for ONE regressor; note honestly
   what drifts.
6. **The audit.** Multiple-testing count (how many regressors did you
   try, including the ones you tried in your head?); persistent-regressor
   Stambaugh-bias warning in one sentence; survivorship (research50!)
   in one sentence; and the honest headline: "suggestive of X under
   assumptions Y, worth out-of-sample follow-up Z".

## Method notes

- Pooled-capable but per-name is fine: ~120–360 monthly observations per
  name; state the power implication in the report (module 04.5's shadow:
  small effects × small n = humility).
- Synthetic mode: the generator plants a weak negative vol effect and a
  zero volume effect (you'll be told the signs AFTER fitting — write the
  recovery truthfully, including any wrong-sign results; grader checks
  honesty, not luck).
- All the week's machinery is load-bearing: White/NW justified, VIF on
  the two regressors (σ̂ and logDV correlate — how much?), interaction
  optional stretch (vol effect in high-vol regimes).

## Self-assessment rubric

| Criterion | Bar |
|---|---|
| Shift audit | Printed timestamps proving no look-ahead; non-overlapping months |
| SE justification | Named flavor + reason tied to data structure; both flavors in a footnote |
| Economic sentence | bp-per-IQR number present, sign discussed against the anomaly literature |
| Stability | Split-sample signs + one rolling plot, interpreted |
| Audit | ≥4 named channels with direction; honest headline ends the report |

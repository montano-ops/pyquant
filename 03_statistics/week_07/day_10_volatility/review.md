# Day 10 Review — Volatility

## Retrieval (answers)

1. SPY vol: 7% → 80%+ annualized across the sample — a 10× swing; "the
   vol of SPY" is a process, not a number.
2. √252 from Var(sum of independent) = 252·Var(daily); returns are
   ~uncorrelated so it's approximately right as a *unit translation*;
   it is not a forecast (regimes don't persist a year).
3. Estimators: close-close (default), Parkinson (H/L, ~5× efficient if
   quotes real), EWMA λ=0.94 (fast, exponential memory ≈ 11 days to
   half-weight), realized vol (intraday gold standard).
4. Three blind spots: direction (symmetric), shape/tails (scale not
   shape — equal σ, different VaR), jumps (close-close hides overnight).
5. Regimes: persistent, bimodal-ish; regime membership predicts |r|
   several times better than unconditional σ — THE predictability.

## Elaboration prompts

- You're shown two backtests with equal realized vol. List five
   questions you'd ask before believing they carry equal risk. (Windows
  equal? Estimator? Fat tails? Clustering? Overnight gaps?)
- EWMA λ = 0.97 vs 0.94: trade-offs in one paragraph. When would you
  want which? (Fast reacting = noisier estimate; slow = stable but
  stale at regime turns — risk limits vs P&L attribution answer
  differently.)

## Interleaved problem

An asset's 21-day vol is 25% annualized. Vol-of-vol: the rolling
series' own SD is 10pp. (a) What is the SE of a 21-day vol estimate
(assuming iid, normal)? (b) If vol is 25% and next month it's 40%, is
that "noise" in the estimate or a regime move?

<details><summary>Reference answer</summary>

(a) SE(σ̂) ≈ σ/√(2n) = 25%/√42 ≈ 3.9pp — so a 21-day vol estimate has
a ±7.6pp (95%) band *even in a calm, well-behaved world*. (b) 40% is
15pp above 25% ≈ 3.9 SE — too far for estimation noise alone: a real
level shift (regime). BUT the iid/normal SE understates real-world
vol-of-vol (vol itself clusters and jumps — 2020's vol doubled in a
week), so the honest statement is: 15pp in a month is at the edge of
what estimation noise produces in calm markets and routine for real
regime shifts — the *context* (was there a −4% day this month? vol
estimates are dominated by 1–2 days) decides. That's the deep lesson:
short-window vol estimates are functions of the biggest 1–2 days in
the window.
</details>

## Self-grade

- EWMA memory at λ=0.94: ~11 days — derivable on demand?
- The three blind spots, cold?

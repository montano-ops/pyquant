# Day 7 Review — The t-Statistic Laboratory (debrief)

## Reference results (normal parents; yours match to simulation error)

**E1 — the t-road.** Median t(y) tracks SR√Y (0.5·√y); the 5–95% band
at any y is roughly ±0.9 wide. P(reject), one-sided 5% (t ≥ 1.645):
y=1 → ~13%, y=5 → ~30%, y=10 → ~47%, y=16 → ~64%, y=25 → ~80%.
(Analytic: Φ(0.5√y − 1.645); two-sided 5% is lower — 8%/20%/35%/52%/71%.)

**E2 — the casino.** True SR = 0, rolling annual evaluations monthly:
P(some t ≥ 2 within 5 years) ≈ 35–45% — versus 5% for any single,
pre-specified evaluation. **Optional stopping multiplies false
discoveries ~8×**: "keep testing until significant" is a significance
factory. (With daily peeking it approaches certainty.)

**E3 — fat tails (t(5)).** Under H₀ at fixed horizons: rejection
6–8% instead of 5% (size distortion). Under SR=0.5: power at y=5
drops a few points (the fat right tail of the t-stat occasionally
helps, the fat left tail hurts; net slightly worse). Small n is where
it bites; y≥10 the CLT has mostly repaired it.

**E4 — clustering.** Power drops hardest in the early years (high-vol
draws dominate short samples; n_eff < n makes the effective y
smaller). The 16-year t=2 target quietly becomes ~20–25 years. **A
clustered-vol world is a slower-evidence world — the honest Sharpe
threshold's shadow.**

**E5 — the verdict table (typical values, one-sided 5% rejection)**

| Model | 1y | 5y | 16y | 25y |
|---|---|---|---|---|
| SR=0 (false positive) | 5% | 5% | 5% | 5% |
| SR=0.5, normal | 13% | 30% | 64% | 80% |
| SR=0.5, fat tails | 13% | 28% | 62% | 79% |
| SR=0.5, clustered | 11% | 25% | 55% | 74% |

## The three sentences (reference versions)

1. A significant 3-year record proves almost nothing: under SR=0.5 the
   power is ~22%, under SR=0 the false-positive rate is 5% — the
   likelihood ratio is ~4:1, and the prior of real edges among tried
   strategies eats that margin whole.
2. An insignificant 3-year record disproves almost nothing: SR=0.5
   strategies fail to clear t=2 in ~78% of 3-year runs — absence of
   evidence, again, is not evidence of absence.
3. The monitoring plan for a live SR-0.5 strategy: pre-commit to
   evaluation at fixed, widely-spaced horizons (years, not months —
   E2's casino); define the kill threshold in SEs of the *design*'s
   power, not in P&L drawdowns alone; and log every look, because
   every look is a test.

## The fourth sentence (yours)

If your fourth sentence doesn't mention either (a) how many
strategies/looks produced the t-stat you're reading, or (b) the
SR√Y arithmetic that converts it to an effect size — re-read day 4
and write it again. Those two moves are the module.

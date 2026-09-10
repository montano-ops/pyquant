# Day 6 Review — Week-6 Consolidation

## Cold retrieval (reference answers)

1. Two worlds: population (fixed, unknown F: μ, σ, ν, κ) vs sample
   (random, known: x̄, s, ν̂, k̂). One backtest = one draw.
2. Four biases: survivorship (dead excluded, up), selection (seen
   because good), look-ahead (future info in past sample), snooping
   (many tries, one shown).
3. SE price list at n=252: mean 0.063% (σ=1%), SD 0.045%, skew 0.155,
   kurt 0.31.
4. 1.4826 = Φ(0.75)⁻¹ ≈ 1/0.6745: scales MAD to SD-matching at
   normality.
5. mean > median → right tail drags mean up; mean < median → left.
   (SPY's sign: check the data — it has flipped across decades.)
6. One k-σ point in n: contributes ≈ k⁴/n to kurtosis.
7. Winsorize: cap at quantiles, keep the day; trim: drop the extremes.
8. Protocol: detect robustly → verify externally → report with AND
   without → never delete silently.
9. x̂ ± SE (n, window, source) — or it didn't happen.
10. Masking: the outlier inflates σ̂ (and shifts x̄), shrinking the
    classical z that should flag it; robust statistics don't eat the
    poison.

## Interleaved problems (reference answers)

**P1.** SE = 1.05%/√2520 ≈ 0.021% — a halving of μ (0.04% → 0.02%) is
under 1 SE: invisible in one decade. That's the honest answer: you'd
need ~4 decades for 2 SE at that difference.

**P2.** Skew: −0.2/√(6/1000) = −0.2/0.077 ≈ 2.6 SE. Kurtosis:
8/√(24/1000) = 8/0.155 ≈ 52 SE. Kurtosis is more surprising by 20× —
and it's the one the risk model cares about.

**P3.** High win rate + negative skew + high kurtosis = short-vol
profile (carry, sell-puts, "pennies/steamroller"). Audit first: the
kurtosis/tail of the LOSS distribution (the steamroller's size), then
check whether the worst month is one event or a cluster (ACF of |r|).

**P4.** The 0.72% is winsorized: the reader must ask "what caps? what
does the raw number say? what does the caps-implied VaR hide?" Risk
reports must show both; otherwise the report is marketing.

**P5.** Non-stationarity: pooling assumes one F; decades mix
distributions. More n → more precision about a *mixture average* — a
quantity that may describe no actual regime. You can be confidently
wrong about a thing that changed.

## Build drill check

The 15-minute six-number shape report (mean, median, SD, MAD, skew,
kurt, each ±): could you do it cold? If not — that's tomorrow
morning's first 15 minutes, before the mini-project.

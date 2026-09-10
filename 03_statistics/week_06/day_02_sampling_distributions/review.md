# Day 2 Review — Sampling Distributions

## Retrieval (answers)

1. SE(x̄) = σ/√n: 0.063% at n=252, σ=1%; SE(s) = σ/√(2n); SE(skew) =
   √(6/n); SE(kurt) = √(24/n) — the price list.
2. Center statistics cheap, tail statistics ruinous (SE of a quantile
   ∝ 1/f(q)); moments pay √k per order of sensitivity.
3. Bias-variance: MSE = bias² + variance; shrinkage trades a little bias
   for much variance *deliberately*; unknown bias is never acceptable.
4. The reporting standard: x̂ ± SE (n, window, source). Bare numbers are
   bugs.

## Elaboration prompts

- Why do you think the SE of kurtosis is √(24/n) — twice the skew's
  √(6/n)? (Higher moments of a *normal* sampling distribution: the 4th
  moment of a standard normal is 3, variance of z² is E[z⁴]−E[z²]² = 2;
  kurtosis estimates scale with it. The pattern: sensitivity grows with
  the power.)
- Which statistics in your own work have you been reporting without SEs?
  Make the list; it's your personal audit queue.

## Interleaved problem

You estimate the 1% daily VaR of a strategy from 250 days: the empirical
1st percentile. Simulate its sampling distribution (500 draws from a
fixed fat-tailed parent, e.g., t(5)). What is the interquartile range of
your VaR estimates? What does a ±Xbp band do to a risk-limit
conversation?

<details><summary>Reference answer</summary>

For t(5)-scaled daily returns (σ≈1%), the 1% quantile ≈ −2.9%; the IQR
of 250-day empirical estimates is typically ~0.6–0.9pp — the estimate
wobbles ±30% of its own value. Implication: a risk limit breached/not
breached by less than that band is a *sampling artifact*, not
information. VaR from 250 days is a rough instrument — regulators'
choice of 250 days is a compromise between relevance and stability,
and the band quantifies the compromise. (Exact numbers depend on the
parent — the point is the band's width relative to the estimate.)
</details>

## Self-grade

- Price list from memory? (mean/SD/skew/kurt at n=252.)
- Can you explain masking (tomorrow's outlier theme) as a
  bias-variance story? (Contaminated σ̂: the estimator's own input is
  corrupted by the thing it should catch — bias, unknown.)

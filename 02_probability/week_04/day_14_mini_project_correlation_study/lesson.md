# Day 14 — Mini-Project: The Correlation Study

## The brief

A regime-aware correlation study of a real portfolio — the exact analysis a
risk manager runs before believing any diversification claim.

**Data:** as many of the course ETFs as available (real mode), 2006→ if
possible (to include 2008); synthetic fallback with fixed seed.

**Part 1 — The headline number, honestly.** Full-sample correlation matrix.
Identify the highest pair and the most diversifying pair. Compute the SE of
each pairwise ρ̂ (≈ 1/√T) and state which correlations are actually
distinguishable from zero.

**Part 2 — The rolling window.** 1-year rolling correlations of the top
pair and the best-diversifier pair. For each: min, max, and the share of
time the correlation's *sign* differs from the full-sample value. What does
"the correlation between A and B is 0.3" hide?

**Part 3 — The stress test.** Define SPY's worst 10% of days (by return).
Recompute the correlation matrix on those days only. Report the average
pairwise correlation: all days vs worst days. Quantify the deterioration of
diversification exactly when it matters (the number orientation day 7 only
gestured at).

**Part 4 — The write-up (one page):** three exhibits with your reading; a
paragraph on what this implies for a 60/40-style portfolio sized on
full-sample correlations; and the bias audit (sample period, survivorship
of famous ETFs, the multiple-comparisons point: you just examined
$\binom{N}{2}$ correlations — some extreme ones are noise. Which?)

**Rules:** rolling windows aligned and lag-stated; no shifting bugs (all
correlations use *contemporaneous* returns — that's correct here, and you
should be able to say why this analysis has no look-ahead);
seeds for any sampling.

# Day 19 — Review Week: Consolidation

## The format

Two blocks, no notes:

**Block A — the self-test (12 items, one per module-day range).**
Each item is a *retrieval* question: a formula, a definition, or a
one-sentence judgment. 90 seconds per item; if you can't produce it
in 90 seconds, mark it and move on. The score is not the point — the
*locations* of the misses are.

**Block B — the re-derivations (4 items).** Re-derive, from
assumptions, the four formulas that the whole course stands on:
the t-statistic from the CLT; the Welch–Satterthwaite df; the
Bartlett factor for overlapping data; the gate's death cost.

Then the error-log triage: every miss from the module, sorted into
concept / arithmetic / careless, each with the scheduled re-learn.

## Block A — the self-test

**01 Math**
1. wᵀΣw: the object, and why the off-diagonals are the whole
   diversification story.

**02 Probability**
2. E[portfolio return] in terms of weights and single-asset
   means; why the portfolio *variance* has cross terms the mean
   doesn't.
3. The SE of a sample correlation at ρ = 0.

**03 Statistics**
4. Skewness and excess kurtosis: what each one says about a return
   distribution, and the trading consequence of getting each wrong.
5. Why rolling vol *is* the volatility estimate, and what it can't
   see.

**04 Inference**
6. The p-value, correctly.
7. Consistency vs unbiasedness, each in one sentence.
8. The SE of the mean difference, paired.
9. Bootstrap: what is resampled, what is estimated, block length's
   job.
10. BH's rejection rule.
11. The Bartlett factor for H-day overlap.
12. Death cost, per event.

## Block B — the re-derivations

1. **The t-stat from the CLT.** Start: x̄ is approximately normal
   with SE σ/√n; σ unknown, replaced by s. One page, no skipping.
2. **Welch–Satterthwaite df.** Start: the two variances s₁²/n₁,
   s₂²/n₂ are themselves noisy (χ²-ish, variance 2a²/(n₁−1) etc.);
   match the variance of the estimated SE to a t with df ν. State
   the final formula.
3. **The Bartlett factor.** Start: Var(x̄) = (σ²/n)(1 + 2Σρ_k) for a
   stationary mean; overlapping H-day sums give ρ_k = (H−k)/H.
   Sum it, take the square root.
4. **The death cost.** Start: net per event = gross per event −
   cost; set the annualized net to zero; solve for the cost.

## The triage protocol

For every miss: **concept** (you thought the thing was different —
re-read the lesson section, schedule it at +1 week); **arithmetic**
(you knew it, slipped — recompute by hand twice this week);
**careless** (you knew it, rushed — the checklist fixes it, not
more reading). The module's final deliverable is the triaged log,
not a score.

## What good looks like

A graduate of module 04 can, cold: read a table and decode it in two
minutes; state the design of any SE they see; count the family;
compute the gate. If Block A's misses cluster anywhere, that's the
day to re-read — not the module.

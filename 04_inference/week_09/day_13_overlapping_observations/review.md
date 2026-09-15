# Day 13 Review — Overlapping Observations

## Retrieval (answers)

1. Overlapping H-day returns from iid daily: ACF triangle
   ρ_k = (H−k)/H for k < H, 0 beyond. Bartlett factor = √(1+2Σρ) =
   √H exactly. Corrected t = naive t / √H.
2. Monte-Carlo signature: naive rejects ~25–35% on pure null at H=5;
   corrected ≈ 5%. The correction is *provable*, not optional.
3. Two honest fixes: Newey–West with lags past H−1 (keep N), or
   non-overlapping sampling (N shrinks, SE honest per N).
4. "Monthly"/"weekly" labels say nothing about overlap — read the
   holding period and the sampling frequency, then compute the
   factor.
5. On real data the factor runs a few percent above √H (market
   clustering leaks past the H−1 truncation) — the honest t is
   slightly smaller than the iid theory gives.

## Elaboration prompts

- Explain "N = 1,500 observations, 300 independent" to a non-quant
  stakeholder in two sentences. (A coin that lands heads-tails-
  heads-tails is not 4 independent coins…)
- A colleague argues NW with K = √n lags is "standard, don't
  overthink." You know H = 60 and √n = 30. What do you say? (K must
  exceed H−1 or the correction is too small — the standard rule
  breaks for long holdings; increase K or thin the sample.)
- Write the one-line design disclosure your future strategy papers
  must carry. (Holding H, sampled every s days, overlap ≈ (H−s)/H,
  SE type with lags, N and effective N.)

## Interleaved problem

Daily returns, H = 10 overlapping, N = 3,000. A strategy spread
series has mean 5bp, SD 30bp. (a) Naive t. (b) Bartlett factor,
corrected t. (c) If the same strategy were sampled non-overlappingly
(every 10 days), what N and what t at the same 5bp mean (SD of a
10-day sum ≈ √10 × daily SD)? (d) Which design do you trust more and
why — and what did you give up?

<details><summary>Reference answer</summary>

(a) SE = 30bp/√3000 = 0.55bp → t = 5/0.55 ≈ **9.2**. (b) Factor
√10 ≈ 3.16 → t ≈ **2.9** — significant, but half the drama. (c)
N = 300; the 10-day sum's SD is 30bp (√10 × the 9.5bp daily SD) →
SE = 30/√300 = 1.73bp → t = 5/1.73 ≈ **2.9** — the same
information, told honestly, N = 300. (d) Both are valid; the
overlapping + NW version keeps N = 3,000 and is standard; the
non-overlapping version is easier to defend to a skeptic and is the
right choice when H > √n. What you "give up" in (c) is nothing
statistically — the power is identical; what you give up is the
appearance of a big N, which was never real.
</details>

## Self-grade

- Can you compute the Bartlett factor from an ACF in 30 seconds?
- Did you run the Monte-Carlo proof and read the two rejection rates?
- Can you state the design disclosure line for a strategy in one sentence?

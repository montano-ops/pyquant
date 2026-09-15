# Day 9 Review — The Bootstrap

## Retrieval (answers)

1. Naive bootstrap: resample n units with replacement, B times, stat on
   each; SE_boot = sd of the stats; CI = percentiles [2.5, 97.5].
   Unit test: must reproduce s/√n for the mean.
2. Block bootstrap: resample consecutive blocks of length b, glue to
   length n; keeps within-block dependence. b between the dependence
   horizon and n; flatten point of the SE-vs-b curve ≈ honest b.
3. Naive < block for vol-based stats because clustering makes
   consecutive days more similar than independent days; naive
   resampling scatters clusters → resamples look more iid → less
   variation → SE understated by roughly √(n/n_eff).
4. Percentile CIs lack finite-n corrections: for means, the t CI wins.
   Bootstrap for statistics without clean formulas (Sharpe, GARCH θ,
   VaR, MDD).
5. The two limits: sample ≈ population (blind spots — no 2008 in the
   sample, no 2008 in any resample); and it inherits non-stationarity
   silently.

## Elaboration prompts

- Explain the bootstrap to a skeptical friend in three sentences,
  without the word "distribution." ("Resample your own data to build
  fake parallel histories; measure how much your number moves across
  them; that movement is how much your number would move if you'd
  gotten different data.")
- A colleague reports "bootstrap CI for the Sharpe: [0.4, 1.2], naive
  resampling." What do you ask? (Block length? SE at other block
  lengths? Sample period/regimes? B?)
- Why would a bootstrap CI be *wider* than the t CI for the same mean?
  (Skewness/fat tails the t ignores — the bootstrap sees them; the t
  CI assumes normality and under-covers in fat tails.)

## Interleaved problem

3,000 daily returns, clustered (n_eff ≈ 1,200 by the |r|-ACF rule),
mean 2bp, SD 1.0%. (a) Textbook SE of the mean (both n and n_eff
versions). (b) Which SE would you report, and what does the CI do to
the claim "the mean is positive"? (c) A junior analyst bootstraps the
mean with single-day resampling and gets a CI half as wide as yours.
One sentence on what's wrong.

<details><summary>Reference answer</summary>

(a) s/√n = 1.0%/√3000 = 0.58bp; honest s/√n_eff = 1.0%/√1200 =
0.91bp. (b) Report 0.91bp: CI = 2 ± 1.8bp → [+0.2, +3.8]bp — the mean
is positive but *barely*; the textbook CI would be 2 ± 1.1bp,
confidently positive. (c) Single-day resampling breaks the clusters,
so the resampled means vary less than real sample means would — the CI
is too narrow by roughly √(3000/1200) ≈ 1.6×.
</details>

## Self-grade

- Can you write naive_boot and block_boot from scratch in under 10 minutes?
- Do you know your b for this data, and can you defend it with a sensitivity table?
- Can you state the bootstrap's assumption and one concrete blind spot in one sentence each?

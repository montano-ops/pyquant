# Day 5 Review — Outliers

## Retrieval (answers)

1. Outliers are information: 1987, 2008, 2020 are the phenomenon;
   outlier-free risk models are helmets for pavement-free worlds.
2. 3σ fails: fat tails make |z|>3 real (module 02.11), and σ̂
   contamination *masks* (the outlier inflates the very denominator
   that should flag it). Robust z = (x − median)/(MAD×1.4826).
3. Winsorize = cap at quantiles (keep, shrink); trim = drop the tails.
   The mean moves little, SD and kurtosis collapse — winsorized risk
   numbers are *lower* by construction; disclosure is the difference
   between stabilization and fraud.
4. Protocol: detect (robust scores) → verify (calendar, volume, news)
   → report twice (with/without) → never silently delete.

## Elaboration prompts

- Find your data source's worst single day for an asset you know.
   Verify it three ways (calendar, the price path around it, external
  memory/news). Was it a market event or an artifact?
- The "report twice" rule: which of *your* current beliefs would
  survive the outlier-free version of their evidence? (Most
  performance-chasing beliefs don't — the star year IS the outlier.)

## Interleaved problem

A 10-year daily series (n≈2520) has one −22% day. Compute (or reason)
the change in: mean (assume other days ~ +0.04% ± 1%), SD, excess
kurtosis, 99% VaR (empirical 1st percentile), max drawdown — each
with vs without the day. Which statistic is MOST changed, and which
is *owned* by that single day?

<details><summary>Reference answer</summary>

Mean: −0.22/2520 ≈ −0.009pp — barely moves (≈ +0.04% → +0.031%). SD:
the day is a ~20σ outlier; removing it drops σ by roughly
(0.22²−σ²)/2nσ... numerically ~10–15%. Kurtosis: with it ≈ 15–20+,
without ≈ 5–8 — the single day contributes most of the fourth moment
(0.22⁴ dominates). Empirical 1% VaR: the 25th-worst day — the −22%
day is *beyond* it, so the VaR barely changes (it's the ~−3.5% days
that define p1) — a subtle and important fact: one extreme point does
NOT move the empirical p1 much, it moves what's BEYOND it. Max
drawdown: owned entirely by the single day and its neighbors. Most
changed: kurtosis. Owned: max drawdown. Lesson: different statistics
have different *outlier exposure* — know which is which before you
clean.
</details>

## Self-grade

- Masking explained in one sentence, cold?
- Winsorize vs trim, one sentence each, cold?

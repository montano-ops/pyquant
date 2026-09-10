# Day 3 Review — Descriptive Statistics

## Retrieval (answers)

1. Five-number summary: min, Q1, median, Q3, max — read as worst,
   ordinary-bad, typical, ordinary-good, best.
2. Mean breaks under outliers (z¹ but unbounded exposure); median
   survives (rank only); trimmed/winsorized are the middle path.
3. MAD×1.4826: the 1.4826 calibrates to SD at normality
   (Φ⁻¹(0.75) = 0.6745; 1/1.35 ≈ 0.74; 0.6745⁻¹ ≈ 1.4826) — a robust
   drop-in σ̂.
4. SD vs MAD gap = fat-tail diagnostic; mean-median gap = asymmetry
   signal (direction fights with skew — the data decides).
5. Signal-to-noise: mean/SD ≈ 1:25–35 for daily equities — the number
   that explains all of empirical finance's humility.

## Elaboration prompts

- You must report ONE center statistic to a client for their
  month-to-month P&L. Defend your choice in three sentences (there is
  no universal answer — the reasoning is the answer).
- Design a one-line data test where mean, trimmed mean, and median
  differ by a lot. What real strategy produces it? (Short-vol: 15
  months of +1%, one month of −25%.)

## Interleaved problem

Strategy P&L (monthly): {+1.2, +1.1, +1.3, +0.9, +1.0, +1.1, +1.4, −9.8,
+1.0, +1.2, +1.1, +0.8}%. Compute mean, median, SD, MAD-scaled, skew,
kurtosis (excess). Which statistics scream, which stay quiet? Name the
strategy type.

<details><summary>Reference answer</summary>

Mean ≈ +0.11%/mo; median ≈ +1.05%/mo — the mean lies BELOW every
ordinary month because one month carries −9.8%. SD ≈ 2.9%/mo (dominated
by the crash); MAD-scaled ≈ 0.2% (the honest ordinary-month scale — a
15× gap, screaming fat tails). Skew ≈ −3.0, excess kurtosis ≈ 9.9.
Screaming: skew, kurtosis, SD-vs-MAD gap. Quiet: median, MAD. This is
short-vol / carry / "picking up pennies": 11 wins and one steamroller.
The median tells you what a typical month feels like; ONLY the mean
and the tail tell you what the strategy is worth. Both, always.
</details>

## Self-grade

- 1.4826 from memory, and why?
- Did you check SPY's actual mean-vs-median sign? What was it?

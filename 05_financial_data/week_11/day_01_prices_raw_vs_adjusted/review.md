# Day 1 Review — Raw vs Adjusted

## Retrieval (answers)

1. raw = as-traded; adj = raw × cumulative factor (total return with
   reinvestment); auto-adjusted = split-repaired price return.
   Backtests: adjusted. Execution: raw. Sizing: raw × shares.
2. Dividend: multiply past by (1 − D/P) — cash left, holder keeps it.
   Split: divide past by ratio — the unit changed.
3. adj series are retrospective constructs: new events rewrite
   history; never mix pulls from different dates.
4. The gap: dividend yield compounding — SPY since 1993 ≈ 13–14×
   price vs 18–20× total; long-horizon studies on raw closes delete
   a third of the premium.

## Elaboration prompts

- Pull (or reconstruct) the raw and total-return paths of a
  high-yield stock (e.g., a 4–6% yielder). What fraction of its
  10-year total return is dividends? What does a raw-close
  mean-reversion signal see on its ex-div days?
- The three-price-universe bug (signal on adj, fill at raw, size at
  adj): write the one-line policy sentence that prevents it in your
  own codebase.

## Interleaved problem

A stock: $80, quarterly dividend $1.20, 2:1 split at year-end, price
growth +10%/yr for 2 years (price return). (a) Price-only wealth
multiple (careful with the split — raw closes halve visually). (b)
Holder's total wealth multiple. (c) The annualized gap; (d) what the
provider's adj series shows for day 0 on the day after the split.

<details><summary>Reference answer</summary>

(a) Raw path: 80 → 88 (split → 44) → 48.4: raw-close wealth = 48.4/80
× 2 (you own 2 shares after the split!) — the naive division forgets
the doubled share count: price-only multiple = 1.1² = 1.21 either way
IF the split is handled; a naive raw-close backtest that ignores the
split computes 48.4/80 = 0.605 — a −39% "loss" that never happened.
(b) Dividends: $1.20 × 8 quarters ≈ 1.5%/quarter yield on ~$80–90 →
holder multiple ≈ 1.21 × (1 + 0.015)⁸ ≈ 1.21 × 1.126 ≈ 1.36.
(c) Gap ≈ 6%/2y ≈ 3%/yr. (d) On the day after the split, adj_close
for day 0 is halved relative to the pre-split pull — the factor
absorbed the 2:1; the RETURN series is unchanged.
</details>

## Self-grade

- The three series' purposes, cold?
- Could you explain to a colleague why adj_close for 2010 changed
  value between two downloads, without notes?

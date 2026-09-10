# Day 3 Review — OHLC, Volume, Liquidity

## Retrieval (answers)

1. Dollar volume = P × volume (the comparable liquidity unit);
   Amihud = mean(|r|/dollar volume) — price impact per dollar
   traded; turnover = volume/shares.
2. Screens: price > $5 (microstructure/data quality), ADV > $1M
   (tradability), history ≥ 12m (formation data), exchange (quality/
   convention). Each selects away a literature: penny/distressed
   (reversal), small caps (size), IPOs (first-year effects).
3. Volume-vol correlation (|r| vs log DV): +0.3 to +0.5 — activity
   tracks risk (Cont fact 6).
4. Liquidity is regime-dependent: size positions on worst-decile ADV
   participation, not the mean.

## Elaboration prompts

- Compute Amihud for three assets you can fetch (an ETF, a large
  stock, a small stock). The spread should be orders of magnitude —
  write the sentence "my order moves X by Y bp per $Z."
- Your strategy's capacity: positions sized at 5% participation of
  20-day ADV. Compute the capacity in dollars for your three assets.
  Which one caps the strategy?

## Interleaved problem

Signal strength by liquidity bucket (ADV terciles): top $2.1%/mo,
middle $3.4%/mo, bottom $6.8%/mo. Costs: 5/12/35bp per month
respectively. (a) Net returns by bucket. (b) Which bucket do you
trade? (c) What claim does the paper's headline (gross, all buckets)
support?

<details><summary>Reference answer</summary>

(a) Net: top 2.05%, middle 3.28%, bottom 6.45%/mo — all positive
(liquidity premium dominating costs even at the bottom, unusually).
(b) All three — but capacity: the bottom bucket's ADV caps size, and
its costs are estimates with fat error bars (35bp assumed; stress
week doubles it). The honest trade is top+middle at size, bottom as
satellite. (c) The gross headline supports "the signal exists across
the liquidity spectrum"; it does NOT support "it is tradable at
scale" — that needs the cost-adjusted, capacity-weighted number,
which is a DIFFERENT (smaller) statistic. **Gross-by-bucket is the
paper's table; net-by-bucket-at-capacity is the fund's table.**
</details>

## Self-grade

- Amihud from memory, with units?
- The screens table with each one's cost: cold?

# Review — Day 4: Prices and Returns

## Retrieval

1. Define simple and log returns, both ways (price ratio, and one in terms of the other).
2. Which aggregates across time by addition? Across assets by weighting?
3. What does `Adj Close` approximate, and by what mechanism?
4. Convert a −50% simple return to a log return. And +100%?

<details><summary>Answers</summary>

1. r = P_t/P_{t−1} − 1; r_log = ln(P_t/P_{t−1}) = ln(1 + r).
2. Log returns add over time; simple returns weight across assets.
3. Total return with dividends reinvested; historical prices are scaled by
   split and dividend adjustment factors (module 05 builds it from scratch).
4. ln(0.5) = −0.693; ln(2) = +0.693. (Note the asymmetry: same-magnitude
   simple moves give equal-magnitude log moves only in one direction pairing
   — −50% and +100% both give ∓0.693.)

</details>

## Elaboration

- Explain to a colleague why a 10-year "price return" on a dividend payer is
  nearly meaningless for an investor, and estimate the annual gap for a 3%
  yielder.
- Give an example of a false trading conclusion caused by using unadjusted
  prices for a split-heavy stock.

## Spaced repetition

- The two return definitions and their aggregation rules: re-derive at +1
  week (module 01 day 3 does this formally), self-quiz at +1 month.

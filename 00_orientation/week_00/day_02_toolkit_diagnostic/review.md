# Review — Day 2: Your Toolkit, Tested

## Retrieval

1. Why resample prices and *then* take returns, rather than resample daily returns?
2. `px.loc["2010":"2020"]` — are both endpoints included? Why does it matter for reproducing a paper?
3. Write the one-liner for annualized 63-day rolling volatility.
4. In the momentum snippet, what exactly was the bug, and what is the fix?

<details><summary>Answers</summary>

1. Because returns compound: the weekly return is the product of daily growth
   factors, so you want the price ratio week-end vs week-end (or sum of daily
   *log* returns). Averaging daily returns is neither.
2. Yes, label slicing is inclusive on both ends. Sample periods must match a
   paper's exactly, or you're studying a different dataset while claiming
   otherwise.
3. `rets.rolling(63).std() * np.sqrt(252)`
4. Today's signal multiplied by today's return — using day-t information to
   profit from day-t returns. Fix: `signal.shift(1)` (decide at close t, earn
   day t+1).

</details>

## Elaboration

- Explain the inner-vs-outer join choice as if to a colleague deciding how to
  build a panel of 50 stocks. Give one concrete false conclusion each choice
  could produce.

## Spaced repetition

- Re-derive the look-ahead fix from a blank page: write the buggy snippet and
  the fixed snippet from memory. +1 week (module 01), +1 month (module 08).

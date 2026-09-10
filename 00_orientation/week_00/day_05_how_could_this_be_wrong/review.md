# Review — Day 5: How Could This Be Wrong?

## Retrieval

1. Name the six biases, each with a one-line example.
2. Which bias does each inflate, and can any bias *deflate* results? (Think: survivorship and short legs.)
3. In the noise-mining experiment, describe the mechanism that produced the
   champion's great in-sample Sharpe.
4. Why does the champion's OOS performance collapse to ≈ 0 rather than to a
   negative number?

<details><summary>Answers</summary>

1. Look-ahead (signal×same-day return); survivorship (today's S&P members in
   a 2010 backtest); selection (reporting the best period); snooping/overfitting
   (200 parameter combos, keep the best); unrealistic costs (reversal net of
   real spreads); multiple testing (100 nulls → ~5 "significant" at 5%).
2. Look-ahead, survivorship (for longs), selection, snooping all inflate.
   Survivorship can *deflate* a short leg (the losers you'd have shorted are
   missing — module 05 quantifies). Costs omitted inflate; costs overdone
   deflate.
3. Selection over 200 random strategies: with noise alone, the maximum of 200
   Sharpe draws is high. The search itself created the champion.
4. A random (zero-true-edge) strategy's expected Sharpe is 0; the champion
   was lucky in-sample, but its *expectation* out-of-sample is still 0.

</details>

## Elaboration

- A colleague says: "I found a 20-day MA rule with Sharpe 1.8 — I tried MA
  windows 5 to 200 in steps of 5." Write your two-sentence reply.
- Give an example of how survivorship bias could make a *published* strategy
  look *worse* than it really is (hint: shorting losers that disappear).

## Spaced repetition

- The six-bias list: reproduce from a blank page at +1 week; revisit every
  project as the audit checklist (it grows a section per module until module
  13 completes it).

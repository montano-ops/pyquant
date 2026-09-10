# Review — Vectors

## Retrieval

1. Compute $[0.25, 0.75]\cdot[0.02, -0.02]$ and name what it is.
2. What does $\sum_i w_i = 0$ mean? = 1?
3. Why must the portfolio return use simple, not log, returns?
4. If two centered return vectors have correlation −1, what's the angle between them?

<details><summary>Answers</summary>

1. 0.005 − 0.015 = −0.01 — the portfolio's return that period.
2. Dollar-neutral (longs finance shorts); fully invested.
3. Log of a weighted sum ≠ weighted sum of logs; simple returns weight linearly.
4. 180° — mirrored directions; a combination exists with (near-)zero variance.

</details>

## Elaboration

- Explain why "risk is not the sum of the weights' sizes" using the
  dollar-neutral example (what carries the risk if not net exposure?).

## Spaced repetition

- Dot products return tomorrow as matrix rows, and in module 12 as the
  backtest engine core. Re-derive `rets @ w` at +1 week.

# Review — Monte Carlo & Bootstrap

## Retrieval

1. Monte Carlo vs bootstrap — the model/data distinction.
2. The resampling detail that makes it a bootstrap.
3. What does plain bootstrap corrupt, and what's the fix?
4. The three-question interrogation of any backtest.

<details><summary>Answers</summary>

1. MC samples from an assumed process; bootstrap resamples the realized
   data with replacement.
2. WITH replacement, same n.
3. Path/time-dependence statistics (drawdowns, vol-managed Sharpe) —
   block bootstrap preserves local dependence.
4. False-alarm rate (simulate null), power (simulate claimed edge),
   statistic variability (resample).

</details>

## Elaboration

- Why can a normal MC never show you a 1987, and what generator choice
  fixes that (qrc.synth's defaults)?

## Spaced repetition

- Bootstrap CIs formalize in module 04.9; block bootstrap in 04.10.

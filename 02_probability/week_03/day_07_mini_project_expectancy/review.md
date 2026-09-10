# Review — Expectancy Simulator

## Retrieval (about your own results)

1. For (0.55, ±1%): what fraction of simulated years lost money? Reconcile
   with positive expectancy in one sentence (√n vs n).
2. Going 0.55 → 0.52: which changed more, the mean path or the
   losing-year probability? Why does that matter for self-evaluation?
3. The asymmetric variant at equal expectancy: how did losing-year
   probability move, and which term of Var = p(1−p)(W+L)² explains it?

<details><summary>Notes</summary>

Typical numbers: (0.55, ±1%) loses ~7% of years — and about 1 month in 3!
— despite clearly positive expectancy; (0.52, ±1%) loses ~31% of years
(~42% of months); the asymmetry (0.55, 1.2%/1%) has *double* the mean
(0.21%/day) plus higher variance — the bigger mean wins: losing years
nearly vanish (~0.2%). The reconciliation: mean grows like n·μ (signal)
but SD of the total grows like √n·σ (noise), so P(loss) decays only as n
grows — slowly, and at the monthly horizon even a real edge loses more
often than not.

</details>

## Elaboration

- Write the "standards upgrade" paragraph from your reflection as three
  testable rules you'll apply to any future backtest (n? SE? losing-year
  probability?). These are your personal research standards v1.

## Spaced repetition

- Re-run your simulator with a fat-tailed loss size (occasional −4% days)
  at +1 month: does the losing-year fraction change? (It will — variance
  is now understated by the two-point model.)

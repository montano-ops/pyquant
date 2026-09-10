# Day 1 Review — Population vs Sample

## Retrieval (answers)

1. **Population**: the full distribution of possible outcomes (all
   possible daily returns under F — fixed, unknown). **Sample**: the
   returns that actually happened (random, known). Market trap: one
   backtest window is one draw, reported as if it were the distribution.
2. The four biases: **survivorship** (dead funds/stocks excluded →
   upward), **selection** (you see the strategy *because* it looks
   good), **look-ahead** (sample contains info the past didn't have),
   **data snooping** (many questions, one sample, one lucky answer).
3. x̄ vs μ: the backtest's Sharpe is a *sample* statistic that *sounds
   like* a property of the strategy.
4. Non-stationarity: the population itself drifts — pooling decades
   mixes populations; you can precisely estimate an average of things
   that no longer exist.

## Elaboration prompts

- Write the "one backtest = one sample" paragraph for your own current
  favorite strategy or belief. What is the population? What drew the
  sample?
- The mutual-fund database example: reconstruct the direction of the
  survivorship bias from first principles (dead funds died of losses →
  excluded → average too high). Could it ever bias *downward*? (Yes —
  think about why closed *winners* might exit too: funds that liquidate
  after a star manager leaves, or merge. The net direction is an
  empirical question; the *classic* case is upward.)

## Interleaved problem

A study computes "average 10-year return of actively managed funds:
7.2%." Name the three filters between "all funds ever started" and "the
funds in the study," and give the direction of each bias.

<details><summary>Reference answer</summary>

(1) Survivorship: funds that closed are gone — closed funds underperformed
(bias up). (2) Backfill/selection: some databases add funds' history only
after they join — often after good runs (bias up, the "backfill bias").
(3) The study's own inclusion rules (minimum history = 10 years) —
selects for survival again (bias up, compounding #1). All three point
the same way: the 7.2% is an overestimate of the *typical* fund
experience. The honest number needs the graveyard.
</details>

## Self-grade

- Can you recite the 2-worlds table? The 4 biases with directions?
- Did your error log gain an entry today? (If not, you weren't
  surprised enough — re-read §5.)

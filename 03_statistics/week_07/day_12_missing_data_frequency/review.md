# Day 12 Review — Missing Data & Frequency

## Retrieval (answers)

1. fillna(0): missing day becomes fake 0% return — vol biased down,
   correlations toward zero, calm fabricated. ffill(prices)→returns:
   gaps become 0% days then a jump on return — honest for *levels*,
   biased for *returns statistics*.
2. Panel dropna: keeps only all-traded days — the intersection
   calendar; over-weights liquid/calm days (MNAR: illiquid names go
   missing exactly in chaos). Choices: intersection for portfolio
   simulation, per-asset calendars for statistics, never impute
   returns.
3. Aggregational Gaussianity: κ collapses daily→weekly→monthly
   (12→3→1 for SPY-ish) — CLT summing tails away, slower than
   independence implies (dependence).
4. Both scaling traps: monthly-built risk scaled to daily understates
   daily tails; daily-built scaled up overstates... precisely: daily
   tail risk does NOT scale by √t under fat tails + clustering —
   crises deliver multi-day runs (2008 Q4: three bad months in a row).
5. Frequency-by-decision: forecast daily risk → daily; test a mean →
   longest/lowest frequency; tail quantiles → daily + EVT; monthly
   rebalance → daily data, monthly decisions.

## Elaboration prompts

- Your data has a 3-day gap in an EM asset during a currency crisis.
   Walk through every option (drop, ffill, interpolate, model) and the
  bias each adds. Which does the *risk* book want? Which does the
  *marketing* deck want?
- Convert a daily strategy's Sharpe to monthly: what can change
   besides the arithmetic? (The distribution's shape — κ drops; serial
  dependence matters more per-observation; the mean's relative SE is
  IDENTICAL — frequency doesn't create information. That last fact is
  under-appreciated: resampling changes the view, not the evidence.)

## Interleaved problem

A vendor series for an illiquid stock shows 30% of days with exactly
0.0% returns. Your colleague computes: vol 18%, skew −0.4, κ 1.2 —
"boring stock, safe." You compute after dropping the zero-days: vol
26%, skew −1.1, κ 6.5. Explain the mechanism; which numbers describe
the risk of *holding* the stock?

<details><summary>Reference answer</summary>

Mechanism: stale marks (no trade → last price repeated → 0% returns).
Those fake zeros are *not* calm days; they're unobserved days whose
risk was postponed, not removed — and it lands in one jump when the
asset finally trades (the true process is "0% for days, then −8%").
The raw statistics average real days with fake days: vol diluted
(σ² averages in zeros → down ~30%), skew/kurtosis compressed toward
calm-normal. After dropping zeros: the *traded-day* distribution —
fatter, more skewed, honest about the days that move. For HOLDING
risk, the second set matters (your P&L realizes the jumps), but
expressed per-*calendar* day: the true per-day vol is between the two
(spread the traded-day risk over the stale days too). The right
answer: model the process (stale-mark + jump), don't average over the
artifact. And note: illiquid strategies' backtests *always* look
better on stale data — a leading killer of "arbitrage" backtests
(module 05).
</details>

## Self-grade

- MNAR vs MAR: definitions cold?
- The two scaling traps, each with its direction of error?

# Day 5 — How Could This Be Wrong?

## Warm-up retrieval (no notes)

1. Simple vs log returns: which aggregates across assets, which across time?
2. What does an adjusted close approximate?
3. State JT93's construction in one sentence (rank by past return, skip a month, buy top / sell bottom decile).

## 1. The question that runs the course

Every result you produce in this course gets one final exam question:

> **How could this be wrong?**

Not as a formality — as a serious search. Today you meet the six standard
answers. You will spend modules 05, 12, and 13 learning to detect and measure
each one, but the *habit* starts now.

## 2. The six ways a backtest lies

**1. Look-ahead bias.** Using information that didn't exist at decision time.
The classic: today's signal × today's return. Subtler: annualizing with a
volatility estimate that used the full sample; screening stocks by *today's*
index membership for a 2010 backtest. *Effect: always inflates results.*

**2. Survivorship bias.** Your dataset contains only firms still alive today.
Dead firms — with their −80% final years — are missing. *Effect: inflates
long-only results, wildly inflates "cheap loser" strategies, and corrupts
short legs.* Free data is survivorship-biased by default; module 05 measures
the damage.

**3. Selection bias / cherry-picking.** Reporting the best asset, period, or
specification; choosing the sample because it worked. Related: stopping
exploration when something looks good.

**4. Data snooping / overfitting.** Trying 50 parameter combinations and
keeping the best. The backtest then measures *your search*, not the market.
Today's exercise manufactures this deliberately.

**5. Unrealistic costs & liquidity.** Ignoring spreads, commissions, market
impact; assuming you can short anything at any size; filling at prices where
size didn't exist. Strategies with high turnover (reversal!) often live
entirely inside the bid-ask spread.

**6. Multiple testing (the meta-bias).** Even with honest methods: run enough
strategies and 5%-significance tests, and pure luck produces "significant"
discoveries. The academic literature itself suffers this — hundreds of
published "factors", many likely false (Harvey, Liu & Zhu; module 13).

## 3. Today's experiment: manufacture a great strategy from noise

The setup (you implement it in the exercise):

1. Take real daily returns of one liquid asset (or the synthetic series).
2. Generate **200 random signals**: each is just noise, drawn independently
   of returns — a random walk of positions in {−1, +1}, or random weights.
3. Backtest all 200. Each is, by construction, worthless.
4. **Pick the best in-sample.** It will show a beautiful equity curve and a
   Sharpe around 1.5+ (with enough tries you can get 2).
5. Now evaluate that champion on data it has never seen. It collapses toward
   zero — its "edge" was luck plus your search.

The point is not that backtests are useless. The point is what a backtest
actually is: *one draw from a distribution of possible histories of one
strategy that itself came from a search across many strategies.* Until you
account for the search (module 13's deflated Sharpe ratio does exactly this),
"Sharpe 1.5" from a mined backtest is a measurement of your selection
process, not of the market.

This is also why the course makes you keep a research log: the log records
the search, so the search can be corrected for.

## 4. A first bias-audit checklist (use it on every project)

- [ ] Would my signals have been computable in real time, at decision time? (look-ahead)
- [ ] Does my universe include firms that later died / were removed? (survivorship)
- [ ] Did I choose this asset/period/specification before or after seeing results? (selection)
- [ ] How many things did I try before this one worked? (snooping)
- [ ] What happens at 10× the transaction costs? (costs)
- [ ] How many hypotheses does this study test in total? (multiplicity)

## 5. Research connection

Everything in module 13 (deflated Sharpe, minimum track record length,
purged cross-validation, the factor zoo) is machinery for taking today's
six-item list seriously. And the professional world echoes it: practitioners
routinely discount beautiful backtests by default — today you learned why
that instinct is correct.

## 6. Reflection

1. In the noise-mining experiment, why does the champion's *out-of-sample*
   Sharpe land near zero rather than near zero *minus costs*? (What is the
   expectation of a random strategy's Sharpe?)
2. A friend shows you a backtest: Sharpe 2.1, 2013–2023, 30 large-cap stocks.
   Write the three questions you'd ask first.

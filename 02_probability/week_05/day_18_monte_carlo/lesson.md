# Day 18 — Monte Carlo and the Bootstrap Preview

## Warm-up retrieval (no notes)

1. The law of small numbers fallacy in one sentence; the SE(p̂) table's n=20 row.
2. The four-step remedy for small-sample delusions.
3. Why does selection-over-noise manufacture gurus?

## 1. Why a quant needs this

You have one historical path. Every strategy, every asset, every regime
gave you exactly one realization. Monte Carlo replaces "what happened" with
"**the distribution of what could have happened**" — and that distribution
is what decisions should be based on. This is the researcher's single most
powerful habit, and today you acquire it.

## 2. Monte Carlo: simulate the process you believe

If you have a model of the data-generating process, sample from it — many
times:

```python
import numpy as np
rng = np.random.default_rng(30)
n_sims, n_days = 5_000, 252
mu, sigma = 0.0004, 0.011

paths = rng.normal(mu, sigma, (n_sims, n_days))
final_wealth = np.prod(1 + paths, axis=1)
print(f"median outcome: {np.median(final_wealth):.3f}")
print(f"5th percentile: {np.percentile(final_wealth, 5):.3f}")
print(f"P(lose money over a year) = {(final_wealth < 1).mean():.1%}")
```

Uses you will make of this weekly:

- **Precision of statistics**: re-estimate your statistic on each simulated
  path → its sampling distribution (tomorrow-adjacent: that's what a
  standard error *is*).
- **Scenario risk**: P(drawdown worse than X), P(strategy dies before
  profitable) — questions with no closed form, trivial by simulation.
- **Method validation**: simulate data where you KNOW the truth (there is /
  is no edge), then check whether your method detects it — the only way to
  know your method's power and false-alarm rate (day 5 of qrc.synth exists
  for exactly this).

## 3. The bootstrap: simulate by resampling the data itself

No model? **Resample the data.** The bootstrap treats your realized returns
as the best available approximation of the distribution, and generates
alternative histories by drawing from it *with replacement*:

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2010-01-01")
r = px["SPY"].pct_change().dropna().values

rng = np.random.default_rng(1)
n_sims = 5_000
idx = rng.integers(0, len(r), (n_sims, len(r)))          # WITH replacement
boot_means = r[idx].mean(axis=1)
lo, hi = np.percentile(boot_means, [2.5, 97.5])
print(f"mean daily return: {r.mean():.5f}")
print(f"bootstrap 95% CI: [{lo:.5f}, {hi:.5f}]")
```

The bootstrap's deep idea: *the sample is to the population as the
resample is to the sample* — so the wobble of statistics across resamples
estimates the wobble of your statistic across samples. It converts
"what's the SE of this weird statistic?" (hard math) into "resample and
look" (easy code). Module 04 turns it into confidence intervals and tests
for quantities with no formulas (Sharpe ratios, drawdowns).

## 4. The i.i.d. fine print (today's honest caveat)

Plain bootstrap resampling *shuffles time* — it destroys any dependence in
the data. For returns, direction is near-i.i.d. (day 16) so means are
roughly fair game, but **anything volatility-sensitive (drawdown
distributions, Sharpe of vol-targeted strategies) is corrupted by plain
resampling**. The fix — block bootstrap (resample contiguous chunks,
preserving local dependence) — is day 19's subject and one of module 04's
workhorses.

## 5. The Monte Carlo → validation mindset (course-critical)

From today forward, every backtest you build gets asked:

1. If the true edge were ZERO, how often would my procedure "find" one?
   (false-alarm rate — simulate null data)
2. If the true edge were exactly what I claim, how often would I detect
   it? (power — simulate with that edge)
3. How variable is my statistic across parallel histories? (resample)

A strategy whose "discovery" you cannot put through these three questions
is a story, not a result.

## 6. Research connection

- The bootstrap is ubiquitous in modern empirical finance precisely
  because return statistics are non-normal and dependent (module 04.9
  formalizes; module 13's CSCV is a block-bootstrap relative).
- GARCH forecasting evaluation (module 09) leans on simulation for VaR
  backtests.
- The "deflated Sharpe ratio" (module 13) is, conceptually, a Monte Carlo
  of your own search process.

## 7. Common mistakes

- Resampling without replacement (that's permutation, a different tool —
  day 19) or with a typo'd range (off-by-one: the classic).
- Bootstrapping a *time-dependent* statistic with plain resampling and
  believing the CI (drawdowns, max streaks — corrupted; use blocks).
- Forgetting that simulation output inherits the model's assumptions: a
  normal Monte Carlo can never show you a 1987. Simulate fat tails when
  tails matter (`qrc.synth` does, by default).

## 8. Reflection

1. Your backtest's Sharpe is 0.8 over 5 years. Describe the three-question
   interrogation in your own words, and which one scares you most.
2. Why is "the sample is to the population as the resample is to the
   sample" the right frame for SEs of weird statistics?

**Self-check:** Monte Carlo vs bootstrap (model vs data); the with-
replacement detail; what plain bootstrap corrupts for time series.

# Day 9 — The Bootstrap

## 1. Warm-up retrieval (no notes)

1. What does a 95% CI mean — in the correct long-run sense, not the
   "95% chance θ is in it" sense?
2. What is the SE of a sample correlation at ρ = 0?
3. You estimated a Sharpe ratio of 0.7 (annual, from 2,500 daily
   returns). What is its SE — and why can't you answer that from
   today's earlier days?

## 2. Why a quant needs this

The t-test gave you CIs for the *mean*. But research lives on
statistics with no clean SE: the **Sharpe ratio**, a GARCH
persistence parameter, a VaR, a factor-loading spread, a backtest's
maximum drawdown. Each has an estimator, but the sampling distribution
is messy — the bootstrap supplies it *from the data*:

> Pretend the sample is the population. Resample from it. The spread
> of the statistic across resamples *is* its sampling distribution.

## 3. Intuition — parallel histories

You have one history: 2,500 days. The bootstrap builds 2,000 fake
histories, each 2,500 days, drawn *with replacement* from the real one.
Each fake history is like "one of the other universes that could have
happened." The distribution of x̂ across universes ≈ the distribution
of x̂ across samples (this is exact as n→∞ under iid, and
reasonably good well before).

Two honest limits:
- The bootstrap can only see the *shape* your sample shows. If your
  2,500 days never contained a 2008, the resamples never contain a
  2008 either. **The bootstrap inherits your sample's blind spots.**
- It assumes observations are exchangeable (iid). Daily returns
  aren't (clustering, 03.10) → naive bootstrap on vol-based statistics
  gives CIs that are too narrow. Fix: **block** resampling (day 02.19
  said *why*; today is *how*).

## 4. The mathematics

**Naive bootstrap.** For sample x₁…xₙ:
1. Draw n indices uniformly at random (with replacement); form x*_b.
2. Compute x̂* on x*_b. Repeat B times (B ≥ 1,000; B = 10,000 for
   publication-grade).
3. SE_boot = sd(x̂* over b). 95% CI = percentile [2.5%, 97.5%] of x̂*.

**Block (moving-block) bootstrap.** Draw *blocks* of b consecutive
observations, glue them until length n. Within a block the time
structure survives; between blocks it doesn't. Choose b so a block is
longer than the dependence you care about: b ≈ 10–22 for clustered
daily returns; rule of thumb b ~ T^(1/3) to T^(1/2). Small b → back to
iid (too narrow); b = n → one resample (no information).

**When to use what.** Mean with normal-ish errors → t-test (finite-n
corrections beat the bootstrap here). Anything else — Sharpe, GARCH
θ, VaR, max drawdown, a spread of two estimates → bootstrap.

## 5. Python implementation

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(11)

def naive_boot(x, stat, B=2000, rng=rng):
    n = len(x)
    idx = rng.integers(0, n, size=(B, n))
    return np.array([stat(x[i]) for i in idx])

def block_boot(x, stat, b=22, B=2000, rng=rng):
    n = len(x)
    out = np.empty(B)
    for bb in range(B):
        nblocks = int(np.ceil(n / b))
        starts = rng.integers(0, n, size=nblocks)
        sample = np.concatenate([x[s:s+b] for s in starts])[:n]
        out[bb] = stat(sample)
    return out

x = rng.standard_t(5, 2500) * 0.01            # fat-tailed "returns"
sharpe = lambda r: r.mean()/r.std()
se_naive = naive_boot(x, sharpe, rng=np.random.default_rng(3)).std()
se_block = block_boot(x, sharpe, b=22, rng=np.random.default_rng(4)).std()
print(f"Sharpe SE: naive {se_naive:.3f} | block(22) {se_block:.3f}")
```

## 6. On real data

SPY daily returns: bootstrap the *Sharpe ratio* (no closed-form SE you
would trust), then the mean (compare bootstrap vs s/√n — they should
agree closely; the bootstrap is not a miracle, it recovers the known
answer when one exists).

```python
from qrc.data import get_prices
r = get_prices("SPY", start="1993-01-01").iloc[:, 0].pct_change().dropna()
sh = r.mean()/r.std()
boot_sh = naive_boot(r.values, lambda v: v.mean()/v.std())
print(f"Sharpe {sh:.3f} | boot 95% CI "
      f"[{np.percentile(boot_sh, 2.5):.3f}, {np.percentile(boot_sh, 97.5):.3f}]")
```

## 7. Research connection

- **GARCH inference** (module 09): analytic SEs for MLE parameters are
  delicate; papers routinely report *bootstrap* CIs (resample
  innovations, refit, repeat).
- **Bailey & López de Prado's deflated Sharpe** (module 13, day
  13.11): the whole test is a bootstrap on the distribution of the
  maximum Sharpe under pure noise. You are building the engine now.
- **VaR backtests** (module 09, day 09.12): violation counts are
  binomial-ish, but the independence test on them uses resampling.

## 8. Common mistakes

1. **Naive bootstrap on clustered data.** Resampling single days breaks
   the volatility clusters; the resampled Sharpe varies less than real
   Sharpe estimates do → CI too narrow → "robust" result that isn't.
   Symptom to check: does the statistic's naive-boot SE agree with a
   block-boot SE? If they differ, trust the block.
2. **Percentile CI as gospel.** For small n or skewed estimators, the
   percentile CI can be badly off-center (the t-test's CI has
   finite-sample corrections the percentile method lacks). For the
   mean, use the t CI; the bootstrap is for statistics *without* a
   clean formula.
3. **Forgetting the blind spots.** A bootstrap CI on a 2015–2024
   backtest says nothing about 2000 or 2008. "The CI contains 0" is
   only as good as the sample's coverage of the relevant regimes.

## 9. Reflection

- The bootstrap's assumption (sample ≈ population) is *weaker* than
  the t-test's (normality) but *stronger* than nothing. Where does
  that put it in your toolbox for a 3-year, high-vol, 1998–2001
  sample?
- Block length is a judgment call with no unique answer. What would
  you *show* in a paper to defend b = 22? (A sensitivity table: CIs
  at b = 1, 5, 10, 22, 63, 252.)

## Self-check

1. Why is the naive bootstrap SE for a Sharpe ratio usually *smaller*
   than the block bootstrap SE on the same data?
2. Your statistic has a known closed-form SE and normal sampling
   distribution. Should you still bootstrap? Why or why not?

---

**Answers:** (1) Clustering means consecutive days are more similar
than independent days; naive resampling scatters the clusters, so the
resampled series look more iid than reality → less variation in the
statistic → SE understated, often 20–50%. (2) Usually no — use the
analytic CI; it has finite-n corrections the percentile bootstrap
lacks. Bootstrap to *check* the analytic answer (if they agree, you
understand both; if they disagree, you've found something).

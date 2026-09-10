# Day 19 — Why You Can't Randomly Shuffle Financial Time Series

## Warm-up retrieval (no notes)

1. Monte Carlo vs bootstrap — model-based vs data-based; what detail makes
   it a bootstrap?
2. What does plain bootstrap corrupt for volatility-sensitive statistics?
3. The three-question interrogation of any backtest?

## 1. Why a quant needs this

The most common statistical reflex — "randomize and see what happens" —
the permutation test — is *quietly invalid* on time series in its naive
form. This day explains exactly why, and what to do instead. It is the
gateway to honest placebo tests (module 13.17) and time-series
cross-validation (module 13.9), and it closes this module's three-day arc
(dependence → simulation → shuffling).

## 2. What shuffling destroys

A permutation (shuffle) of a time series breaks the *temporal order* —
and returns' order carries information, just not the information people
expect:

- **Direction (returns) is near-independent** — shuffling barely changes
  the mean. (This is why shuffling returns for a *mean* test is *less*
  catastrophic than folklore says.)
- **Volatility clustering is order-information** — real return sequences
  have calm stretches and storms; a shuffled sequence relocates every big
  day randomly. Any statistic that touches the *path* — drawdowns,
  max streaks, rolling-vol behavior, Sharpe of vol-managed strategies,
  autocorrelations of |r| — is fundamentally altered by shuffling.

```python
import numpy as np
rng = np.random.default_rng(4)
from qrc.data import get_prices
px = get_prices("SPY", start="2010-01-01")
r = px["SPY"].pct_change().dropna()

shuffled = r.sample(frac=1, random_state=0)   # order destroyed
growth = lambda s: (1 + s.sort_index()).cumprod()
for name, s in [("real", r), ("shuffled", shuffled)]:
    dd = growth(s) / growth(s).cummax() - 1
    print(f"{name:8s}: max drawdown {dd.min():.1%} | "
          f"ACF(|r|) lag1 {s.abs().autocorr(1):.2f}")
```

Same *marginal* distribution (identical returns!), radically different
*path* statistics: the real series keeps its vol clusters and its
drawdown depth; the shuffled one dissolves them. **Shuffling tests the
marginal distribution's null, not the time-series null.**

## 3. The dependence taxonomy (what to preserve, per question)

| Question | What must be preserved | Valid randomization |
|---|---|---|
| Is the mean ≠ 0? | (near-)i.i.d. direction | plain shuffle ≈ OK (with caveats) |
| Is the drawdown/VaR real? | vol clustering | block bootstrap |
| Is the signal's edge real? | signal-return timing | circular block shuffle of signal+returns *jointly* |
| Is this pair cointegrated? | cross-asset levels structure | specialized (module 09) |

The unifying principle: **your placebo must destroy exactly the structure
you're testing for, and preserve everything else.** A placebo that destroys
*more* than the hypothesis over-rejects; one that destroys *less*
under-rejects. Designing placebos is a first-class research skill (module
13.17 gives it a full day).

## 4. Block methods (the standard fix)

**Block bootstrap**: resample contiguous blocks (length L) with
replacement — preserves dependence *within* blocks, sacrifices it across
block boundaries. Rule of thumb: L at least the dependence horizon (for
vol, ~1–3 months of days).

```python
def block_bootstrap(returns, n_blocks, block_len, rng):
    starts = rng.integers(0, len(returns) - block_len, n_blocks)
    idx = np.concatenate([np.arange(s, s + block_len) for s in starts])
    return returns.iloc[idx[:len(returns)]]
```

**Circular blocks** (wrap around) reduce edge effects — module 04.9
implements properly; today you only need the *idea*: keep short-range
dependence, randomize long-range arrangement.

## 5. Effective sample size, quantified (the day's number)

Dependence inflates variance of means: with autocorrelations ρ_k,

$$n_{eff} = \frac{n}{1 + 2\sum_{k=1}^{\infty}\rho_k}$$

For |r|-style clustering the *returns* autocorrelations are ≈0, so mean-
return inference is mildly affected — but for any statistic built on
squared returns (variance, Sharpe), the sum is large and n_eff can be a
*fraction* of n. This is the formula behind "HAC standard errors" that
you'll meet in module 06.

## 6. Research connection

- Momentum papers' overlapping portfolios (JT93) create mechanical
  autocorrelation in strategy returns → naive shuffles/permutation and
  naive SEs are invalid → Newey-West everywhere in the literature
  (module 06.8 derives; today you know *why*).
- Vol-managed portfolios (Moreira & Muir, module 10.23) derive their
  power from the very dependence that shuffling destroys — evaluating
  them with shuffled placebos is meaningless.
- Module 13's purged cross-validation is the supervised-learning
  descendant of today's principle: never let randomized folds leak time
  adjacency.

## 7. Common mistakes

- Shuffling returns and reporting the drawdown distribution "under the
  null" — the null you tested isn't the one you care about.
- Block length chosen by convenience (L=5) when the dependence horizon is
  months — blocks must exceed the horizon or you've shuffled the
  dependence right back in.
- Circular reasoning: tuning the placebo until it confirms your result
  (placebo design is pre-committed, like everything else).

## 8. Reflection

1. Your strategy's Sharpe depends on vol-targeting (position ∝ 1/σ̂). Why
   is a plain shuffle placebo guaranteed to *understate* your Sharpe's
   sampling noise?
2. Explain to a colleague: "same returns, different order, different
   strategy" — with the two statistics that prove it.

**Self-check:** what does shuffling preserve/destroy; the placebo design
principle; block bootstrap in one sentence; n_eff formula intuition.

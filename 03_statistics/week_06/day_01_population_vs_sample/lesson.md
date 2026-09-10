# Day 1 — Population vs Sample

## 1. The two worlds

The **population** is the full set of possibilities — every daily return
that SPY *could ever* produce, governed by some unknown distribution F.
The **sample** is what you actually observed: ~5,000–9,000 daily returns,
one path of history.

| | Population | Sample |
|---|---|---|
| Mean | μ (fixed, unknown, forever) | x̄ (random, known, changes with window) |
| Variance | σ² | s² |
| Skew, kurtosis | ν, κ | ν̂, k̂ |

**The inversion that makes statistics work:** you observe the sample and
make claims about the population. Every claim in every paper you read is
this inversion. Every fraud in every paper you read hides in it.

## 2. One backtest = one sample

```python
from qrc.data import get_prices
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
# the sample mean of daily returns:
print(f"x̄ = {r.mean():.5%}, n = {len(r)}")
```

x̄ ≈ 0.03–0.05%. Is *μ* 0.03%? 0.06%? Could μ be 0? Module 02.12 armed
you: t = x̄/SE with SE = s/√n ≈ 0.011/√7500 ≈ 0.00013 — so x̄ is measured
to ±2.5bp at 95%. The *sample* is precise about itself and fuzzy about
the population. When a paper says "the strategy earned 0.04% per day,"
it is reporting x̄ while sounding like it reports μ.

## 3. Sampling bias: the scarier twin

Noise (module 02) makes x̂ wobble around the truth. **Bias** makes it
wobble *around the wrong place*. The catalog:

- **Survivorship**: the sample contains what survived. "The average
  equity mutual fund returned X" computed on today's existing funds
  drops every fund that died — and dead funds died *because* they lost.
  (Module 05 does this with real consequences.)
- **Selection**: the strategy that reached your desk reached it *because*
  its sample looked good. The population of strategies tried is huge;
  you see a filtered sample.
- **Look-ahead**: the sample includes information the population of
  *that moment* could not have had (index constituents chosen by
  today's membership; fundamentals known only later).
- **Data snooping**: asking many questions of one sample until one
  answer looks good — module 02.17's 500 gurus, now a sampling problem.

## 4. Sampling *with* replacement — the bootstrap preview

```python
import numpy as np
rng = np.random.default_rng(0)
boot = np.array([ rng.choice(r.values, len(r), replace=True).mean()
                  for _ in range(2000) ])
print(f"bootstrap x̄ spread: {boot.std():.6f} vs CLT s/√n = {r.std()/np.sqrt(len(r)):.6f}")
```

The spread of re-sampled means ≈ the SE. This is the bootstrap (module
02.18) re-derived as a *population-vs-sample* device: the empirical
distribution stands in for F, and you watch x̄ behave as a random
variable. Tomorrow we do this for every statistic you'll ever compute.

## 5. Why quants care more than biologists

A drug trial samples 500 patients from a population the trial *defines*.
A quant samples 8 years from a **non-stationary** population — 2009's
return distribution and 2020's are not draws from the same F. The
population itself drifts. This is why "past performance" disclaimers are
not legal decoration: the sample was drawn from a population that no
longer exists. Every module from here on carries this wound.

## Self-check

1. A backtest reports Sharpe 0.8 over 2010–2020. Population or sample
   statistic? What is the claim it *sounds* like?
2. Your fund database contains only funds alive today. Which bias, which
   direction?
3. Why does non-stationarity make the population/sample split *worse*
   for markets than for coin flips?

---

**Answers:** (1) Sample statistic of Sharpe; it sounds like a property of
the strategy (the population parameter). (2) Survivorship; upward — the
dead (losers) are excluded. (3) With coins, more data always sharpens the
estimate of one fixed μ; with markets the μ moves, so pooling 30 years
mixes populations — you can be precisely estimating an average of things
that no longer exist.

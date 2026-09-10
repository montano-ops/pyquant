# Day 9 — Matrices

## Warm-up retrieval (no notes)

1. Compute $[0.25, 0.75] \cdot [0.02, -0.02]$ and say what it is.
2. What does $\sum_i w_i = 0$ mean in trading terms?
3. Why do weights combine simple returns and not log returns?

## 1. Why a quant needs this

Every dataset in this course is a matrix: $T$ dates × $N$ assets. Every
multivariate model — covariance, factor regression, PCA — is matrix
operations on it. Today: the three objects (data matrix, transpose,
covariance matrix) and the one product that turns them into research.

## 2. The data matrix

$$X = \begin{pmatrix} r_{1,1} & \cdots & r_{1,N} \\ \vdots & \ddots & \vdots \\ r_{T,1} & \cdots & r_{T,N} \end{pmatrix}$$

Row $t$ = "one date, all assets" (a cross-section). Column $i$ = "one asset,
all dates" (a time series). *This distinction — cross-section vs time series
— organizes all of quantitative finance*: momentum sorts the cross-section;
GARCH models the time series; Fama–MacBeth (module 06) does both at once.

In pandas this is a wide DataFrame: `rets = px.pct_change().dropna()`, shape
`(T, N)`. `.iloc[t]` is a row (cross-section); `rets[col]` is a column (time
series).

## 3. Matrix–vector product: the whole portfolio history at once

$$ (X\mathbf{w})_t = \sum_{i=1}^{N} x_{t,i}\, w_i $$

Each *row* of $X$ dots with $\mathbf{w}$: yesterday's one-day dot product,
repeated for every day in history. `rets @ w` — you already ran it, on day 8.
Now you know its name: a matrix–vector product.

**Transpose**: $X^\top$ swaps rows and columns ($T{\times}N \to N{\times}T$).
`rets.T` gives "assets as rows" — the shape correlation matrices and
cross-sectional regressions want (module 06's Fama–MacBeth lives there).

## 4. The covariance matrix — the single most important object in portfolio math

$$\Sigma = \text{Cov}(X), \qquad \Sigma_{ij} = \frac{1}{T-1}\sum_{t=1}^{T}(r_{i,t}-\bar{r}_i)(r_{j,t}-\bar{r}_j)$$

Facts to *own* (each is a working tool):

- Shape $N \times N$: one row/column per asset.
- **Symmetric**: $\Sigma_{ij} = \Sigma_{ji}$ — covariance doesn't care about
  order. Check numerically; asymmetry means a bug.
- **Diagonal = variances**: $\Sigma_{ii} = \sigma_i^2$. The diagonal of your
  covariance matrix is each asset's own risk.
- Off-diagonal = pairwise covariances — the *interactions* that decide
  whether diversification works.
- `rets.cov()` computes exactly this (with the T−1, pandas' default — you're
  welcome).

```python
import numpy as np
Sigma = rets.cov().values               # N×N numpy array
assert np.allclose(Sigma, Sigma.T)      # symmetric — always assert
print(np.diag(Sigma))                   # variances; sqrt -> vols
```

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT", "GLD", "XLE", "QQQ"], start="2015-01-01")
rets = px.pct_change().dropna()
Sigma = rets.cov()
print(Sigma.round(6))
```

Read it like a researcher: which asset has the largest diagonal (own risk)?
Which pair has the most positive off-diagonal (co-movement)? Is anything
near zero (independent bets)? This *reading* habit — matrix as a table of
relationships — is what day 10 builds on.

## 6. Research connection

- **Portfolio variance** (tomorrow): $\sigma_p^2 = \mathbf{w}^\top \Sigma \mathbf{w}$.
- **Factor models** (module 07): assert returns are
  $r_i \approx \alpha_i + \beta_i^\top f + \varepsilon_i$ — a *vector* of
  loadings per asset; the covariance structure is then carried by factor
  covariances (this is how risk models handle 3,000 stocks with a 5-factor
  $\Sigma$).
- **PCA** (module 14): decomposes $\Sigma$ into ranked directions of
  variance — "statistical factors."

## 7. Common mistakes

- Building $\Sigma$ from **prices** instead of returns (variance of a random
  walk is nonsense-scale; also non-stationary — module 08).
- Mixing **frequencies**: daily $\Sigma$ for a monthly rebalance strategy —
  covariance is frequency-specific (and period-specific — day 14 measures
  how badly it wanders).
- Trusting $\Sigma$ when $N \approx T$: the sample covariance matrix becomes
  garbage precisely when you have many assets (module 09.15 simulates this
  spectacular failure).

## 8. Reflection

1. Why must a covariance matrix be symmetric, and what would asymmetry tell
   you about your code?
2. If two assets are perfectly correlated, what does $\Sigma$ look like in
   their 2×2 block? What portfolio of the two has zero variance?

**Self-check:** describe $\Sigma$'s shape, diagonal, and symmetry — and what
`rets.cov()` assumed about your data to produce it.

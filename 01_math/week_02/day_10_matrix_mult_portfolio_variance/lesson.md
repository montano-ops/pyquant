# Day 10 — Matrix Multiplication and Portfolio Variance

## Warm-up retrieval (no notes)

1. What are the dimensions of $\Sigma$ for 50 assets, and what's on its diagonal?
2. Row of the data matrix = cross-section or time series? Column?
3. What is $(X\mathbf{w})_t$, in words?

## 1. Why a quant needs this

Today you meet **the most important formula in portfolio mathematics**:

$$\boxed{\ \sigma_p^2 = \mathbf{w}^\top \Sigma\, \mathbf{w}\ }$$

Every risk number, every diversification claim, every hedge ratio, and
(module 11) every "risk parity" and "minimum variance" portfolio is this
expression evaluated, minimized, or decomposed.

## 2. Matrix multiplication = a grid of dot products

$A B$ (shape $m{\times}k$ times $k{\times}n$) has entry $(i,j)$ = row $i$ of
$A$ dotted with column $j$ of $B$. The inner dimensions must match ($k$),
and the result is $m{\times}n$. That's the whole definition:

```python
import numpy as np
A = np.arange(6).reshape(2, 3)      # 2×3
B = np.arange(6).reshape(3, 2)      # 3×2
C = A @ B                           # 2×2 — each entry a dot product
```

Non-negotiable rule: **$AB \neq BA$** in general. Order matters; in finance,
order *encodes meaning* ($\mathbf{w}^\top\Sigma\mathbf{w}$ is a number,
$\mathbf{w}\mathbf{w}^\top\Sigma$ is an $N{\times}N$ matrix).

## 3. Portfolio variance, unpacked one layer at a time

$$\mathbf{w}^\top \Sigma \mathbf{w} = \sum_{i=1}^{N}\sum_{j=1}^{N} w_i\, \Sigma_{ij}\, w_j$$

The double sum says: *every pairwise interaction, weighted by both holdings*.
For two assets it reduces to the formula you must also know cold:

$$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2 w_1 w_2 \rho\, \sigma_1 \sigma_2$$

That last term is the whole game: if $\rho < 1$, it is *less* than
$2w_1w_2\sigma_1\sigma_2$-with-$\rho{=}1$ — the risk that cancels. With
$\rho = 1$ and equal vol, a 50/50 mix has *exactly* the average risk: no
diversification. With $\rho = 0$, the 50/50 risk is average risk divided by
$\sqrt{2}$. **Diversification is a correlation phenomenon.**

```python
def port_var(w, Sigma):
    return float(w @ Sigma @ w)          # one line; understand every symbol

w = np.array([0.5, 0.5])
Sigma = np.array([[0.04, 0.010],          # var=0.04 (vol 20%), cov=0.010
                  [0.010, 0.04]])
print(port_var(w, Sigma), np.sqrt(port_var(w, Sigma)))
```

## 4. The diversification curve (today's centerpiece)

Equal-weight $N$ assets, all with variance $\bar{\sigma}^2$ and average
pairwise covariance $\bar{\text{cov}}$:

$$\sigma_p^2 = \frac{\bar{\sigma}^2}{N} + \frac{N-1}{N}\,\bar{\text{cov}}$$

Read it as $N \to \infty$: the first term dies, and portfolio variance
converges to **average covariance**. You can diversify away *idiosyncratic*
risk, never *common* risk. This one line explains: why index funds work, why
"100 stocks is basically the market", why crisis correlations are lethal
(average covariance is exactly what spikes in a crash), and why long-short
market-neutral strategies target the common factor explicitly (module 11).

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT", "GLD", "XLE", "XLF", "XLK"], start="2015-01-01")
rets = px.pct_change().dropna()
Sigma = rets.cov().values

for n in range(1, len(rets.columns) + 1):
    w = np.zeros(len(rets.columns)); w[:n] = 1 / n
    print(n, np.sqrt(port_var(w, Sigma) * 252))     # annualized vol
```

Notice the curve flattens — and *where* it flattens is the average
covariance of your universe. In today's exercise you draw this curve
properly (with many more assets, shuffled orders, and a written
interpretation).

## 6. Research connection

- **Markowitz**: choose $\mathbf{w}$ to minimize $\mathbf{w}^\top\Sigma\mathbf{w}$
  subject to $\sum w_i = 1$ — day 12, numerically; module 11, seriously.
- **Beta as a covariance object**: $\beta_i = \text{Cov}(r_i, r_m)/\sigma_m^2$
  — module 06/07; notice it is one cell of $\Sigma$ normalized.
- **Hedging**: minimize $\mathbf{w}^\top\Sigma\mathbf{w}$ over hedge ratios;
  the optimal hedge for asset $i$ against the market is (again) beta.
- The **deflated Sharpe ratio** (module 13) is, underneath its brackets, a
  statement about how many $\mathbf{w}$'s you tried.

## 7. Common mistakes

- Annualizing variance by ×252 but volatility by ×√252 inconsistently inside
  one calculation. Pick a convention: compute daily $\sigma_p^2$, annualize
  at the end.
- Using $\Sigma$ from a different period than the backtest (covariances
  wander — day 14 makes you measure it).
- Forgetting the diagonal's contribution: with concentrated weights
  (momentum's deciles), $w_1^2\sigma_1^2$ terms dominate — the double sum's
  "self" terms are not small print.

## 8. Reflection

1. In the 2008 crisis, what happened to $\bar{\text{cov}}$, and therefore to
   every "diversified" portfolio's variance? What does that imply about
   trusting calm-period $\Sigma$?
2. A long-short portfolio is dollar-neutral. Why is its variance not zero?
   Which term of the double sum survives?

**Self-check:** write the two-asset variance formula and the
$N$-equal-weights limit formula from memory, and explain the limit in plain
words.

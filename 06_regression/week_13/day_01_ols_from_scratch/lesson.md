# Day 1 — OLS from Scratch

## 1. Why a quant needs this

Open any empirical asset-pricing paper: the tables are regressions. Beta is
a regression slope. Alpha is a regression intercept. Every factor model you
will meet in module 07, every predictive regression in module 10, and every
backtest evaluation in module 12 is one line:

> regress the thing you care about on the things that might explain it.

If that line is a black box to you, the tables are a black box. Today you
refuse the black box: you fit the line with code you could defend on a
whiteboard, and only then let statsmodels carry the load.

## 2. The problem, in one picture worth drawing

You have $n$ pairs $(x_t, y_t)$ — say, daily market returns ($x$) and daily
returns of one stock ($y$). You want the *best line* $y \approx \alpha +
\beta x$. "Best" needs a definition. OLS's definition: **minimize the sum of
squared vertical deviations** — penalize being wrong, symmetrically,
quadratically:

$$\min_{a,b}\; S(a,b) = \sum_{t=1}^n (y_t - a - b\,x_t)^2$$

Why squares? (a) Big errors hurt more than proportionally — variance
thinking from module 02; (b) the math is linear-algebra-shaped, which you'll
feel in one paragraph; (c) squares are a *choice with costs* (day 11:
outliers exploit exactly this).

## 3. The mathematics (you already own it)

Setting the two partial derivatives of $S$ to zero gives the **normal
equations** — module 01.11 with $X = [\mathbf{1}\;\; x]$:

$$X'X\,\hat\beta = X'y \quad\Longrightarrow\quad \hat\beta = (X'X)^{-1}X'y$$

For one regressor, work the algebra once and it simplifies to the closed
form you should be able to recite:

$$\hat\beta = \frac{\widehat{\mathrm{cov}}(x,y)}{\widehat{\mathrm{var}}(x)},
\qquad \hat\alpha = \bar y - \hat\beta\,\bar x$$

Read $\hat\beta$ like a researcher: *scaled covariance* — how much of the
co-movement survives per unit of $x$-movement. If the market moves 1% and
your stock co-moves with it at 60% correlation with equal vols, $\hat\beta
\approx 0.6$: **correlation, scaled by relative vol** — not a magic object.

## 4. Python implementation — solve, don't invert

```python
def ols(x, y):
    \"\"\"OLS with intercept, by hand. Returns (alpha, beta) for one regressor.\"\"\"
    x = np.asarray(x, float); y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(x)), x])      # intercept column FIRST
    b = np.linalg.solve(X.T @ X, X.T @ y)          # solve the normal equations
    return b                                        # [alpha, beta]
```

Two numerical disciplines, learned once: **never** compute `(X.T @ X)`
explicitly inverted with `np.linalg.inv` when `solve` exists — inversion is
slower *and* numerically worse; and the intercept is a *column of ones you
add yourself* — forget it and your regression is forced through the origin,
which silently asserts $\alpha = 0$.

## 5. On real (and planted) data

```python
from qrc.data import get_prices
from qrc.synth import synthetic_prices

if DATA_SOURCE == "real":
    px = get_prices(["QQQ", "SPY"], start="2010-01-01")
else:
    px = synthetic_prices(n_days=3800, n_assets=2, seed=11, corr=0.64,
                          drift_spread=0.0001)
    px.columns = ["QQQ", "SPY"]

r = np.log(px).diff().dropna()          # log returns (module 01.3 discipline)
a, b = ols(r["SPY"], r["QQQ"])          # QQQ on the market
print(f"alpha {a*252*100:+.2f}%/yr   beta {b:.3f}")
```

Expected shape of the answer: QQQ-on-SPY β ≈ 1.1–1.3 (Nasdaq is a levered
market bet), α near zero with a large error bar (module 04 warned you). In
synthetic mode the truth is planted — verify your code *recovers* what was
planted before trusting it on data where the truth is unknown. That habit —
estimator validated on a known world first — is the module's spine.

## 6. Common mistakes

1. **Regressing prices, not returns.** Two non-stationary price series give
   spectacular R² and a meaningless β (module 08's spurious regression, in
   person). Returns are the unit; prices are the price.
2. **Forgetting the intercept** because "alpha is zero anyway" — you then
   *force* it to be, and β̂ absorbs the difference. Always add the ones
   column; let the data say alpha is zero.
3. **`np.linalg.inv(X.T @ X) @ X.T @ y`** in production code — slower,
   less stable, and it fails loudly at the worst time (near-collinearity,
   day 9). `solve` degrades gracefully.

## Self-check

1. From memory: write the two-variable closed form for $\hat\beta$ and
   $\hat\alpha$. What does "scaled covariance" mean, in one sentence?
2. `X = np.column_stack([np.ones(n), x])` — what goes wrong statistically
   if you drop the ones column, and why does β̂ move?
3. You fit QQQ ~ SPY on **price levels** and get R² = 0.97. Is the
   relationship strong? What test tells you the fit was garbage?

---

**Answers:** (1) $\hat\beta = \widehat{\mathrm{cov}}/\widehat{\mathrm{var}}$,
$\hat\alpha = \bar y - \hat\beta\bar x$; the slope re-expresses co-movement
in units of x-variance — corr·(σ_y/σ_x). (2) Without the ones column the
line is forced through the origin: you have asserted α = 0, so any nonzero
mean in y is pushed into β̂ — a *biased* slope. (3) No — non-stationary
levels are mechanically correlated (two wandering lines correlate); the
spurious-regression signature is R² ≈ 1 with Durbin–Watson ≈ 0 (residuals
autocorrelated). Returns first, always.

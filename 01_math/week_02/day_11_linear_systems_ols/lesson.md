# Day 11 — Linear Systems and the Geometry of Regression

## Warm-up retrieval (no notes)

1. Write $\mathbf{w}^\top\Sigma\mathbf{w}$ as a double sum and explain the
   pieces.
2. What does the equal-weight variance formula converge to as N → ∞?
3. Why is matrix multiplication order-sensitive?

## 1. Why a quant needs this

On day 5 you *minimized* SSE numerically — a line fit through valley-walking.
Today you learn that for least squares the valley has a **closed-form floor**,
found by solving a linear system. This is OLS — the engine of modules 06, 07,
08, and 09 — and you will build it yourself before statsmodels hides it.

## 2. Regression as a system that can't be solved (exactly)

You want $\hat{y} = X\beta$ with data $X$ (T×k) and $y$ (T). With more
equations than unknowns ($T > k$), no exact solution exists — the data don't
lie on a line. **OLS picks the closest achievable point**: the *projection*
of $y$ onto the space spanned by $X$'s columns. Residuals
$\mathbf{e} = y - X\hat{\beta}$ are then *perpendicular* to that space —
"what's left over is unrelated to the regressors". That perpendicularity is
not aesthetics; it's the equation that defines the solution.

## 3. The normal equations

Setting "residuals ⊥ columns of X" in math gives

$$\boxed{\ X^\top X \hat{\beta} = X^\top y\ }\qquad\Longrightarrow\qquad \hat{\beta} = (X^\top X)^{-1} X^\top y$$

Read the boxed system: a $k{\times}k$ linear system (left) built from your
data, and its solution (right). $X^\top X$ (the "Gram matrix") is k×k no
matter how many observations — that's why regression scales.

```python
import numpy as np

def ols_by_hand(X, y):
    """X: (T, k) including a intercept column if you want one. y: (T,)."""
    XtX = X.T @ X
    Xty = X.T @ y
    return np.linalg.solve(XtX, Xty)      # solve, don't invert

# design matrix with intercept: a column of ones, then the predictor
X = np.column_stack([np.ones(len(y)), x])   # shape (T, 2)
beta_hat = ols_by_hand(X, y)                # [intercept, slope]
```

Two craft rules: use `np.linalg.solve`, not `inv` (faster, stabler — same
answer); and *always* add the ones-column explicitly (statsmodels' `add_constant`
does exactly this).

## 4. What you get out

- $\hat{\beta}$: slopes (and intercept) — the sensitivities of day 2,
  measured.
- Fitted values $\hat{y} = X\hat{\beta}$ and residuals
  $e = y - \hat{y}$.
- $R^2 = 1 - \frac{\sum e_t^2}{\sum (y_t - \bar{y})^2}$: share of y's
  variance explained (module 06 interrogates it).

## 5. On real data: your first market-model regression

```python
from qrc.data import get_prices
px = get_prices(["SPY", "XLE"], start="2015-01-01")
r = px.pct_change().dropna()
y = r["XLE"].values
X = np.column_stack([np.ones(len(r)), r["SPY"].values])

beta_hat = ols_by_hand(X, y)
print(f"alpha(daily) = {beta_hat[0]:.5f}, beta = {beta_hat[1]:.3f}")

import statsmodels.api as sm
print(sm.OLS(y, X).fit().params)       # must match — you just built their engine
```

XLE's beta vs SPY lands around 1.1–1.4 (energy is a high-beta sector). The
*meaning* of that slope — exposure, hedging, "is my strategy just levered
market?" — is module 06/07's business. Today's achievement is mechanical:
**you derived the same numbers statsmodels does, from three lines of linear
algebra.** When module 06 hands you p-values and standard errors, you'll
know exactly what they attach to.

## 6. Research connection

The Fama–French time-series regression you read on day 2.7 is
$X\hat{\beta} = X^\top y$ solved with $X$ = [1, Mkt−RF, SMB, HML]: four
columns, one intercept, three slopes ("loadings"). Their published alphas
are the intercepts of exactly this system, evaluated per portfolio. When you
reproduce FF93 in module 07, `ols_by_hand` is all you need — and knowing
that, the mystique of "running a factor regression" is gone before you get
there.

## 7. Common mistakes

- Forgetting the intercept column (forces the line through the origin;
  silently biases slope and intercept alike).
- Singular $X^\top X$ (perfectly collinear columns — module 06's
  "multicollinearity", met here as a crash) — `solve` will throw; that crash
  is *informative*.
- Inverting matrices explicitly. `solve` is the professional move.

## 8. Reflection

1. Why is it meaningful that OLS residuals are perpendicular to the
   regressors? What would correlated residuals with the regressors imply
   about your estimate?
2. Where in the papers you've read does "solve the normal equations" hide
   behind the phrase "we estimate by OLS"?

**Self-check:** write the normal equations from memory, explain the role of
each matrix product, and say what the ones-column is for.

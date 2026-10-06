# OLS — Reference Sheet

The one-page anatomy of the linear regression, as used in module 06.
Notation follows `01_math/concepts/notation.md`: bold-free scalars, hats on
estimates, $i$ indexes assets, $t$ indexes time.

## The model

$$y_t = \alpha + \beta x_t + \varepsilon_t, \qquad t = 1..n$$

Matrix form with intercept: $y = X\beta + \varepsilon$, where the first
column of $X$ is ones and $\beta = (\alpha, \beta)'$. The regression *fits*;
it does not (by itself) *explain* — exogeneity is what buys interpretation.

## The estimator

Minimize $S(b) = \sum_t (y_t - x_t'b)^2$. First-order conditions give the
**normal equations** $X'X\hat\beta = X'y$ (module 01.11), so:

$$\hat\beta = (X'X)^{-1}X'y$$

Two-variable closed form (worth memorizing — it *is* what regression does):

$$\hat\beta = \frac{\widehat{\mathrm{cov}}(x, y)}{\widehat{\mathrm{var}}(x)},
\qquad \hat\alpha = \bar y - \hat\beta \bar x$$

In NumPy: `np.linalg.solve(X.T @ X, X.T @ y)` — solve, never `inv`.
In statsmodels: `sm.OLS(y, sm.add_constant(x)).fit()`.

## Identities that are always true (with an intercept)

- $\sum_t e_t = 0$ and $\sum_t x_t e_t = 0$ — residuals are orthogonal to
  every regressor, numerically: `X.T @ e ≈ 0`.
- $y = \hat y + e$, and $\mathrm{var}(y) = \mathrm{var}(\hat y) +
  \mathrm{var}(e)$ — the variance decomposition behind $R^2$.
- The fitted line passes through $(\bar x, \bar y)$.

## Fit and inference

```
SSE  = e'e                       residual sum of squares
SST  = Σ(y_t − ȳ)²               total sum of squares
R²   = 1 − SSE/SST               fraction of variance explained
σ̂²   = SSE/(n − k)               k = number of coefficients (incl. intercept)
Var̂(β̂) = σ̂² (X'X)⁻¹             classical covariance matrix
SE_j = sqrt(Var̂(β̂)_jj)           standard error of coefficient j
t_j  = β̂_j / SE_j                t-stat, df = n − k, if assumptions hold
CI   = β̂_j ± t_{0.975, n−k} · SE_j
```

Single regressor with intercept: $R^2 = \widehat{\mathrm{corr}}(x, y)^2$.
More regressors: $R^2$ never falls when you add one — adjusted
$R^2 = 1 - \frac{SSE/(n-k)}{SST/(n-1)}$ penalizes.

## What the classical formulas need (and what failure costs)

| Assumption | Buys | Breaks in returns data via |
|---|---|---|
| Linearity in parameters | the model form | nonlinear payoffs, regime switches |
| Exogeneity, $E[\varepsilon|X]=0$ | **unbiasedness** of β̂ | omitted factors, simultaneity |
| No perfect collinearity | existence of (X'X)⁻¹ | duplicated factors |
| Homoskedasticity | valid classical SEs | vol clustering, cross-asset vol gaps |
| No autocorrelation in ε | valid classical SEs | overlapping windows, stale prices |

The last two leave β̂ unbiased but make the *default* SEs wrong — the repair
lives in `concepts/standard_errors_reference.md`.

## The two sentences to internalize

1. **β̂ is a random variable.** Re-draw the sample and it moves; the SE is
   the SD of that movement, not an afterthought.
2. **The coefficient table is a claim plus its tolerances.** Reading a paper
   is: which column, which SE, what would break it.

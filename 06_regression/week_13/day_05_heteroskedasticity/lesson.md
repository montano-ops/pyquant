# Day 5 — Heteroskedasticity & White's Repair

## 1. Why a quant needs this

Yesterday's tournament showed the classical SE lying whenever error
variance varies with the data. In finance that is the *default*: volatility
clusters in time, and cross-sections mix 10%-vol utilities with 60%-vol
biotechs. Hal White's 1980 repair — the most-cited paper in econometrics —
gives you SEs that stay honest **without knowing the form** of the variance
problem. Every "robust standard errors in parentheses" footnote you will
ever read is this day's math.

## 2. The problem, stated exactly

Classical: $\widehat{\mathrm{Var}}(\hat\beta) = \hat\sigma^2(X'X)^{-1}$ —
one variance, $\hat\sigma^2$, for every observation: assumption A4 baked
into the arithmetic.

Truth under heteroskedasticity (A2 intact, so still unbiased):

$$\mathrm{Var}(\hat\beta) = (X'X)^{-1}\Big(\sum_t \sigma_t^2\, x_t x_t'\Big)(X'X)^{-1}$$

The classical formula substitutes $\bar\sigma^2$ for every $\sigma_t^2$ —
averaging where it should weight. When big-variance observations coincide
with big-|x| observations (they do: |returns| and vol move together), the
variance of β̂ is driven by the extremes, and the classical SE points the
wrong way (yesterday: too small).

## 3. White's idea: let each observation confess its own variance

We don't know $\sigma_t^2$ — so estimate it from the only witness each
observation offers: its own squared residual, $e_t^2$ (an unbiased-if-noisy
estimate of $\sigma_t^2$):

$$\widehat{\mathrm{Var}}_{\text{White}}(\hat\beta) = (X'X)^{-1}\Big(\sum_t e_t^2\, x_t x_t'\Big)(X'X)^{-1}$$

Bread, meat, bread — the **sandwich estimator**. The meat is what changed:
a diagonal matrix of $e_t^2$ instead of $\hat\sigma^2 I$. Consistent under
heteroskedasticity *of unknown form*, with no model of the vol process —
that is the entire trick, and it is why the paper is cited ~50,000 times.

```python
def se_white(X, e):
    XtX_inv = np.linalg.inv(X.T @ X)
    meat = X.T @ (e[:, None] ** 2 * X)
    return np.sqrt(np.diag(XtX_inv @ meat @ XtX_inv))
```

Flavors: **HC0** = as above; **HC1** = HC0 × n/(n−k) (a degrees-of-freedom
nudge, what statsmodels and Stata report by default); HC2/HC3 further
leverage corrections. At research n the choice is cosmetic.

## 4. What White does — and pointedly does not — fix

- **Fixes (A4):** SEs valid under arbitrary heteroskedasticity; β̂ untouched
  (still the OLS point estimate, still unbiased under A2).
- **Does not fix (A5):** if residuals are autocorrelated, $e_t^2$ says
  nothing about $e_t e_{t-1}$ terms — the meat needs the cross-lag products
  that Newey–West adds (day 8). White's estimator is *not* a blanket
  "robust" stamp.
- **Does not fix (A2):** no SE estimator touches bias.
- **Costs:** White SEs are *noisier* estimates of the SE itself than
  classical ones when A4 actually holds — you trade a little efficiency for
  insurance. The professional default in empirical finance: pay it.

Practical reading rule: when a paper says "robust SEs" with no qualifier,
ask robust-to-what. Then check that the answer matches the data structure
(cross-section → White enough; overlapping windows → insufficient).

## 5. Detecting it before repairing it

You will feel it first in the residual plot: a **fan** — |e| widening with
|x̂| or with calendar vol regimes. Formal check: the **White test** —
regress $e_t^2$ on $x_t$ and $x_t^2$; significance in that *auxiliary*
regression rejects homoskedasticity (n·R² ~ χ²). You will implement the
meat, not the test machinery, today — the regression *is* the test once you
see that $e_t^2$ is a variance proxy. But the fan-plot instinct is what
catches it in the wild, where nobody hands you a formal test.

## 6. Common mistakes

1. **Slapping White on autocorrelated data** and concluding the t-stats
   are safe. White's meat is diagonal; autocorrelation lives off-diagonal.
2. **Comparing White to classical and using whichever is smaller.** The
   estimators measure different things; the smaller is not "better", it is
   *wrong under the failure*. The entire point is insensitivity to the
   failure mode.
3. **Forgetting β̂ doesn't move.** Robust-SE refits change the *error bar*,
   never the point estimate; a shrunken t means your inference was
   overstated, not that the coefficient got worse. Report both SE flavors
   once, and see how much of your story survives — that gap is the day's
   lesson made personal.

## Self-check

1. Write the sandwich form and name bread/meat. What exactly replaces
   $\hat\sigma^2$ in the meat, and why is that legal?
2. White SE fixes which assumption's failure, leaves which two to other
   repairs — and why is each beyond its reach?
3. Your classical SE is 0.020, your White SE is 0.031. One sentence for
   your research log; then one sentence for the case White 0.020 /
   classical 0.031.

---

**Answers:** (1) $(X'X)^{-1}(\sum e_t^2 x_tx_t')(X'X)^{-1}$; each
observation's own squared residual stands in for its unknown $\sigma_t^2$ —
a noisy but unbiased per-observation variance estimate, and consistency
needs only the average meat to be right. (2) Fixes A4; A5 needs the
off-diagonal lag terms (Newey–West, day 8) because diagonal $e_t^2$ cannot
represent $E[e_te_{t-l}] \neq 0$; A2 is bias — outside any SE estimator's
jurisdiction. (3) First case: "classical precision was overstated; the
robust SE is the honest one — the t-stat shrinks and the claim must
requalify." Second: "the data's variance is *smaller* at the extremes than
the classical average — unusual; check for outliers dominating mid-range
x and for a misspecified variance story before quoting either."

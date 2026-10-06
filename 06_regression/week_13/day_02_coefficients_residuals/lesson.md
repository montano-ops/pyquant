# Day 2 — Coefficients & Residuals

## 1. Why a quant needs this

A regression prints two numbers; a researcher's job is to say what each one
*is* with brutal precision, and then to interrogate what the model **left
out** — because the leftovers (the residuals) are where anomalies, risk
factors, and phony alphas live. Event studies cumulate residuals. Idio vol —
the denominator of half the risk metrics you'll build — is the residual's
standard deviation. Learn to treat residuals as *data*, not garbage.

## 2. Reading the coefficients — units first

Fit $r_{\text{AAPL},t} = \alpha + \beta\, r_{\text{SPY},t} + \varepsilon_t$
on daily returns.

- **β = 1.15** means: days when the market is +1% see AAPL +1.15% *on
  average, in this window*. It is a hedge ratio (short 1.15 SPY per 1 AAPL
  to neutralize market exposure), a leverage measure (> 1 = amplifier), and
  a correlation in disguise (day 1). It is **not** a statement about AAPL
  being up when SPY is up on any given day — that's ρ.
- **α = +0.03%/day** means: the average daily return *unexplained by the
  market* — about 7.8%/yr — before you ask whether its standard error is
  0.01%/day (trade it) or 0.05%/day (ignore it; module 04). Always convert
  α to an annual number before judging it; daily alphas *look* tiny and
  compound loudly.

The intercept earns its keep by a second, subtler identity: **with an
intercept included, the regression line passes through $(\bar x, \bar y)$**,
i.e. $\bar y = \hat\alpha + \hat\beta\,\bar x$. So $\hat\alpha$ is exactly
"the stock's mean return minus β × the market's mean return" — the
de-marketed mean. No intercept, no such decomposition.

## 3. Residuals: three identities that are always true

With an intercept, by construction (verify numerically today — *verify*, not
believe):

1. $\sum_t e_t = 0$ — residuals average to zero;
2. $\sum_t x_t e_t = 0$ — residuals are **orthogonal to the regressor**
   ($x'e = 0$): in-sample, no linear information about $x$ remains in $e$;
3. $y = \hat y + e$ with $\hat y \perp e$: the data is exactly "explained +
   unexplained", so $\mathrm{var}(y) = \mathrm{var}(\hat y) +
   \mathrm{var}(e)$ — tomorrow's R² is this identity divided through.

Identity 2 is the one to internalize: **OLS is the projection that uses up
all linear $x$-content**. If you find $x$-predictability in the residuals,
you specified the functional form wrong (nonlinearity — a candidate
finding), not that OLS missed something linear.

## 4. The residual as a research object

```python
e = y - (a + b * x)              # residual returns
idio_vol = e.std() * np.sqrt(252)
print(f"total vol {y.std()*np.sqrt(252):.1%}  idio vol {idio_vol:.1%}")
```

- **Event studies** stack $e_t$ around earnings dates: abnormal return IS a
  residual (module 10).
- **Idio vol** = std(e). For AAPL ~ 60% of variance is idiosyncratic —
  stock-picking P&L lives and dies in $e$ (module 11 sizes positions with
  it).
- **Residual return** de-markets a position: the strategy "long the
  residual" is the market-neutral version of long the stock — module 07's
  factor regressions formalize exactly this.

And the diagnostics preview: plot $e$ against time and against $\hat y$.
White noise with constant spread = the model did its job; structure (vol
clusters, trends, fans) = name the failure — the rest of this week.

## 5. Common mistakes

1. **Causal β.** "β = 1.15" does not mean the market *causes* AAPL's moves;
   both are driven by common information. Regression measures co-movement;
   causality is a model claim (module 09).
2. **Interpreting α without converting units or without its SE.** Daily
   α = +0.03% is 7.8%/yr — and if SE = 0.05%/day it is also zero. The
   number, the annualization, and the error bar are one object.
3. **Treating residuals as scrap.** Deleting $e$ after fitting is deleting
   the informative half of the analysis — the diagnostics (day 10) and half
   of module 07 read only residuals.

## Self-check

1. SPY falls 2% on a day, β_AAPL = 1.15, α̂ ≈ 0. What is the *expected* AAPL
   move, what is the residual if AAPL actually falls 1%, and what does that
   +1% residual mean?
2. Recite the two orthogonality identities. Which one fails if the
   regression has no intercept, and why does that break the "de-marketed
   mean" reading of α̂?
3. A colleague reports: "the model is great, residuals average −0.4%/day."
   Impossible — explain in one sentence.

---

**Answers:** (1) Expected move = β·(−2%) = −2.3%; actual −1% → residual
e = −1% − (−2.3%) = +1.3%: AAPL outperformed its market-implied move by
1.3% — company-specific information (the second identity says nothing about
*sign* on one day; orthogonality holds in sample, on average). (2) Σe = 0
and Σxe = 0. Both fail without an intercept — residuals need not average
zero, so α̂ is not the de-marketed mean and the explained/unexplained
variance split breaks. (3) With an intercept residuals average exactly zero
by construction; −0.4% means the intercept was omitted or the arithmetic is
wrong — either way the regression table cannot be trusted.

# Day 3 — R², Standard Errors, t-Stats

## 1. Why a quant needs this

Yesterday β̂ was a number. Today it becomes a number *with its tolerances* —
the form in which every paper reports it: `0.93 (0.04)`. The SE is not
decoration. It is the answer to "how much would β̂ move if history had
dealt a different hand of the same game?" — and you will answer it today
two ways: by formula, and by simulation, watching β̂ scatter across 500
parallel histories with your own eyes. After today, a beta quoted without
an SE will feel like a price quoted without a currency.

## 2. R²: the variance share, with its ceilings

From yesterday's identity, divide var(y) = var(ŷ) + var(e) by var(y):

$$R^2 = 1 - \frac{SSE}{SST} = \frac{\text{variance explained}}{\text{total variance}}$$

With one regressor and an intercept, $R^2 = \widehat{\mathrm{corr}}(x,y)^2$
— worth remembering: the mysterious "fit" is just squared correlation.

Three calibrations for returns data, so your eye is trained:

- Stock ~ market, daily: R² ≈ 0.2–0.5 (most of a stock's variance is idio).
- ETF ~ its index: R² ≈ 0.95+.
- **Predictive regression of next month's return on a signal: R² = 0.02 with
  a real signal is *large*.** Daily-return R² is noise-dominated by design;
  the economics live in t-stats and out-of-sample behavior (day 14 is built
  on this sentence).

R² measures in-sample fit — never "is the model true", never "is the signal
tradable". A 0.99 R² on overlapping sums of the same returns is an
arithmetical artifact (day 8).

## 3. The sampling distribution of β̂ — formula

Assume (for today) residuals are well-behaved: mean zero given $x$, common
variance $\sigma^2$, uncorrelated. Then

$$\widehat{\mathrm{Var}}(\hat\beta) = \hat\sigma^2 (X'X)^{-1},
\qquad \hat\sigma^2 = \frac{SSE}{n-k}$$

For one regressor the slope's SE has the closed form you can derive in two
lines and should remember forever:

$$SE(\hat\beta) = \frac{\hat\sigma_e}{\hat\sigma_x \sqrt{n}}$$

Read it: coefficient uncertainty falls with √n (module 02's law), rises
with residual noise, and **falls with more spread in x** — which is why
crisis years *improve* your beta estimates, an oddly comforting fact.
Then: $t = \hat\beta/SE(\hat\beta)$, CI = $\hat\beta \pm t_{0.975,\,n-k}\,
SE$ (module 04 machinery, unchanged).

## 4. The same fact, by simulation

```python
rng = np.random.default_rng(0)
betas = [fit_beta(rng) for _ in range(500)]   # 500 parallel 3-year histories
print(f"mean {np.mean(betas):.3f}  sd {np.std(betas):.3f}  formula SE {se_formula:.3f}")
```

The standard deviation of the 500 β̂'s *is* the standard error — the formula
is a shortcut for repeating history, valid when the assumptions hold. Watch
the two depart from each other when they don't (days 4–5 and 8 break them
one at a time and measure the gap). This is module 02's Monte Carlo
discipline, now pointed at estimation itself.

## 5. On the desk: the three reading rules

1. **Every coefficient arrives as (estimate, SE, n).** Drop one and the row
   is unreadable. FF92's tables (day 16) are average slopes *with* SEs from
   the month-to-month scatter — the same idea at panel scale.
2. **t > 2 is a property of (β̂, SE, n) jointly** — the same β̂ is
   significant at 10 years of data and junk at 6 months. Significance is
   about precision, not size: "statistically ≠ economically" (module 04),
   now in regression dress.
3. **The CI is for the *parameter in this window*, not for the future.** A
   CI on beta says where the estimate sits, not where beta will be (day 17
   bills you for the difference).

## 6. Common mistakes

1. **R² worship / R² dismissal.** Both errors: fit is not truth (levels
   regression, day 1), and low R² is not uselessness (predictive
   regressions live at 0.01–0.05). Judge a regression by what question it
   answers.
2. **Adjusted R² amnesia.** Adding regressors never lowers R² — a 40-factor
   in-sample fit is a flexible mirror. Papers with modest R² and honest
   SEs beat baroque R² monuments (module 13 formalizes why).
3. **Reporting t but not n** — t = β̂√n·σ_x/σ_e hides n inside; a t-stat
   without the sample size can't be sanity-checked.

## Self-check

1. Derive $SE(\hat\beta)$'s closed form from $\hat\sigma^2(X'X)^{-1}$ for
   one regressor. Which of its three terms is under your control as a
   researcher, and how?
2. corr(AAPL, SPY) = 0.55 daily. What R² do you expect in the market-model
   regression, and what does the other 70% of variance *mean*?
3. "The signal's monthly regression has R² = 0.015, therefore it is
   economically irrelevant." Refute or accept, precisely.

---

**Answers:** (1) $(X'X)^{-1}_{22} = 1/\sum(x_t-\bar x)^2 = 1/(n\hat\sigma_x^2)$,
so $SE = \hat\sigma_e/(\hat\sigma_x\sqrt n)$; only $n$ (and $x$'s spread, via
design — longer samples, more varied regimes) is yours; σ_e is the world's.
(2) R² ≈ 0.55² ≈ 0.30; the rest is idiosyncratic variance — firm-level news,
the component a market hedge does not touch. (3) Refute: at monthly
frequency R² = 0.015 on a *return* can correspond to a large, tradable edge
(predictability is bounded by noise by construction); the economic test is
net return after costs vs the t-stat, not R² — day 14 puts numbers on it.

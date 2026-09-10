# Day 3 — Exponents, Logarithms, and the Arithmetic of Growth

## Warm-up retrieval (no notes)

1. In a linear model, what do slope and intercept each mean? Give two
   finance aliases for each.
2. Why is the P&L of a short position still a linear function of price, but
   a dangerous one?
3. Write the "growth of $1" formula over T periods.

## 1. Why a quant needs this

Returns compound. Almost every wrong number you will ever see in trading
research — mis-annualized Sharpe, overstated backtest, bogus "average
return" — is an exponent or logarithm used carelessly. Today is the definitive
treatment; the course never re-litigates it.

## 2. The three growth operators

$$\text{growth factor } G = \prod_{t=1}^{T}(1+r_t), \qquad
\text{log growth} = \sum_{t=1}^{T}\ln(1+r_t), \qquad
\text{CAGR} = G^{1/T} - 1$$

Key facts, each one a working tool:

- **Logs turn products into sums**: $\ln G = \sum_t \ln(1+r_t)$. This is why
  log returns add over time (orientation day 4, now proven).
- **Roots answer "what constant rate would have gotten me here?"**: CAGR is
  the *constant* return that compounds to the same end wealth.
- **Exponentials undo logs**: $G = e^{\sum_t \ln(1+r_t)}$.

## 3. Geometric vs arithmetic means (where careers go wrong)

- **Arithmetic mean**: $\bar{r}_{arith} = \frac{1}{T}\sum_t r_t$ — the mean
  of the returns. Answers: "what was the average *one-period* return?"
- **Geometric mean**: $\bar{r}_{geo} = \left(\prod_t (1+r_t)\right)^{1/T} - 1$
  = CAGR. Answers: "at what constant speed did my money actually grow?"

These differ, and the difference is not a technicality:

$$\bar{r}_{arith} - \bar{r}_{geo} \approx \frac{\sigma^2}{2}$$

— the **volatility drag**. A strategy returning +10%, −10% alternately has
arithmetic mean 0% but compounds to (1.1)(0.9) = 0.99 per two days — a
guaranteed slow loss. Higher volatility makes the wedge bigger.

**Which mean when?**

- Predicting the *next period's* expected return (statistical expectation):
  arithmetic.
- Describing *what an investor actually experienced* (growth): geometric.
- Reporting a backtest's return: geometric/CAGR, or you are lying by
  arithmetic.

## 4. Annualization, done right

Daily → annual, two different quantities:

- **Returns**: compound — $(1+\bar{r}_{daily})^{252} - 1$ (or
  $e^{252\cdot\overline{\ln(1+r)}}-1$ for logs). Never ×252 the *simple*
  daily mean and call it an annual return (that's the arithmetic shortcut —
  it overstates by the drag).
- **Volatility**: scale — $\sigma_{ann} = \sigma_{daily}\sqrt{252}$.
  Variance adds over independent periods, so *standard deviations* scale
  with √T, not T.

The pair to memorize: **mean compounds, volatility scales by √time.** (Why
√time: module 02 derives it from variance of sums.)

## 5. Python implementation

```python
import numpy as np

def cagr(returns, periods_per_year=252):
    """Geometric mean annualized. `returns` = simple per-period returns."""
    growth = np.prod(1 + returns)
    years = len(returns) / periods_per_year
    return growth ** (1 / years) - 1

def ann_vol(returns, periods_per_year=252):
    return returns.std(ddof=1) * np.sqrt(periods_per_year)

def ann_return_arithmetic(returns, periods_per_year=252):
    return returns.mean() * periods_per_year   # the OVERSTATED version — know it, label it
```

## 6. On real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2010-01-01")
r = px["SPY"].pct_change().dropna()
print(f"arith ann: {ann_return_arithmetic(r):.2%}")   # almost always bigger
print(f"geometric: {cagr(r):.2%}")                    # what you actually lived
print(f"drag ≈ sigma^2/2 = {r.var(ddof=1) * 252 / 2:.2%} per year")
```

The two annualized numbers differ by roughly half the annual variance —
for an index, a fraction of a percent; for a levered or single-stock
strategy, multiple percent per year. The exercise measures this wedge across
very different assets.

## 7. Research connection

Papers report "mean monthly return" (arithmetic — a statistical object, the
right choice for testing predictability) but investors care about CAGR
(geometric). Both are correct in their own frame; mixing them silently is
how "1% per month" becomes "12.7% per year" (true arithmetic annualization)
or "compounding to 12.68%" (nearly identical here — but NOT identical for
volatile strategies: +1%/month at 0 vol ≠ +1%/month with variance). When
you reproduce a table, know which mean each column reports. JT93's Table 1
reports arithmetic monthly means — that's standard, and now you know what
it does and doesn't claim.

## 8. Common mistakes

- Multiplying the arithmetic mean by 252 and calling it "annual return" —
  overstated by σ²/2 (fine as an *expectation* statement, wrong as a
  *growth* statement).
- $\sqrt{252}$ applied to returns instead of volatilities (or 252 applied to
  volatilities).
- Averaging multi-year CAGRs of sub-periods and calling the average the
  CAGR of the whole period (geometric means don't average arithmetically).

## 9. Reflection

1. A levered fund doubles an index's return *and* its volatility. Using the
   drag formula, explain why leverage hurts compounding even when the
   expected return rises.
2. Where in orientation's day-7 mini-project did you (correctly) use
   geometric reasoning without naming it?

**Self-check:** state the "mean compounds, volatility scales" rule and the
drag formula, and explain the drag to a non-technical friend in two
sentences.

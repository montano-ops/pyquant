# Day 11 — The Normal Distribution

## Warm-up retrieval (no notes)

1. E and Var of Bernoulli(p) and Binomial(n, p)?
2. SE of p̂ over 252 trials at p = 0.55? Is 60% over one year surprising?
3. Why is p = 0.5 the noisiest case?

## 1. Why a quant needs this

The normal distribution is finance's most-used and most-abused model. You
need it three ways: as a *reference scale* (z-scores), as the *sampling
distribution* that makes t-tests possible (day 15), and as an *assumption
about returns* that real data violates enough to matter (today's QQ
preview; module 03's full autopsy).

## 2. The object

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Symmetric, bell-shaped, fully described by (μ, σ). The **empirical rule**:
68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ. Standardization:

$$z = \frac{x - \mu}{\sigma} \quad \text{(any normal → standard normal)}$$

z-scores are the *common currency* of "how unusual": "a −3σ day" is a z of
−3 regardless of the asset. Everything in module 04 (t-statistics,
p-values) is expressed on this scale.

```python
import scipy.stats as st
# how likely is a -3 sigma day under normality?
print(f"Phi(-3) = {st.norm.cdf(-3):.4%}")
# and what actually happened in SPY history? (exercise)
```

## 3. Why it's everywhere: two honest reasons

1. **Averages**: the CLT (day 15) makes *sample means* approximately normal
   under almost any underlying data — so normality of *statistics* is often
   legitimate even when normality of *returns* is not.
2. **Mathematical convenience**: normality is closed under addition
   (independent normals sum to normal) and under portfolio weights — the
   reason Markowitz's world is built on it.

## 4. Where it fails: the fat-tail fact (preview of module 03)

Under normality, SPY's worst days should be bounded: a −20σ day (Oct 19,
1987) has probability so small the universe's age can't buy you one. Real
daily returns:

- have more extreme days than normality allows (excess kurtosis),
- are negatively skewed (crashes bigger than rallies),
- and their *volatility changes* day to day, so "σ" itself is a moving
  target (day 19).

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="1990-01-01")          # long sample if available
r = px["SPY"].pct_change().dropna()
z = (r - r.mean()) / r.std()
print(f"days beyond |3σ|: {(np.abs(z) > 3).mean():.3%} (normal predicts 0.27%)")
print(f"days beyond |4σ|: {(np.abs(z) > 4).mean():.4%} (normal predicts 0.006%)")
```

If real data gives you 1-2% of |z|>3 days, tail risk under a normal model
is understated by an order of magnitude. **The QQ plot** — sorted data
z-scores vs normal quantiles — makes this visual; you build it in the
exercise, and module 03.8 rebuilds it with full care.

## 5. The lognormal connection (closing a loop from module 01)

If *log* returns are normal, prices are lognormal — positive by
construction, right-skewed. "Assume returns are normal" is usually the
sloppy version of "assume *log* returns are normal," which is at least
compatible with prices > 0. This is why module 01's statistics-in-logs
convention exists.

## 6. Research connection

- Every starred t-stat in every table you've read is evaluated against a
  normal-ish sampling distribution — legitimate via CLT (day 15), *not*
  because returns are normal.
- Risk models: parametric VaR assumes (conditional) normality; the 1987 and
  2008 losses were "impossible" under the models of their day. Regulators
  responded by adding fat-tail corrections — an industry built on the gap
  between Φ(−3) and reality.
- GARCH (module 09) rescues the normal by making σ_t *conditional*: today's
  distribution is normal-ish *given today's volatility* — a profound and
  practical fix.

## 7. Common mistakes

- z-scoring with full-sample μ and σ and calling the result "today's
  surprise" — full-sample σ contains the future (look-ahead, mild form;
  module 13's leakage day covers the ML version).
- "Returns aren't normal, so statistics is invalid" — no: *statistics of
  averages* is often fine (CLT); *risk models of tails* are what breaks.
- Confusing "95% of days within 2σ" with "max loss is 2σ" — tails exist,
  and they're fatter than the model says.

## 8. Reflection

1. Your risk system says a −4σ day is "once in 30,000 years". Your data
   shows two in a decade. Give the two candidate explanations and how
   you'd distinguish them.
2. Why does the normal's closure-under-addition property matter for
   portfolio math — and what sneaky assumption does it smuggle in?

**Self-check:** the empirical rule; the standardization formula; one
sentence each on when normality is legitimate (statistics) and when it's
dangerous (tails).

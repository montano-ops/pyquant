# Day 4 — Random Variables and Distributions

## Warm-up retrieval (no notes)

1. Write Bayes' rule; name the three components.
2. A signal with 80% hit rate fires 15% of the time; crashes are 2% likely.
   P(crash | signal)?
3. Why must a signal be shifted before conditioning future returns on it?

## 1. Why a quant needs this

"Tomorrow's return" as a number-in-waiting needs machinery: something that
assigns likelihoods across the whole range of possible values. That
machinery is the random variable and its distribution — the object every
model in this course (and every model in every paper) is *about*.

## 2. Random variables: outcomes become numbers

A **random variable** X is a rule assigning a number to each outcome.
"Tomorrow's simple return" is a random variable; on Wednesday it *takes a
value*. Two layers, never to be conflated:

- the **distribution** (the whole likelihood pattern — the truth-in-waiting)
- the **realization** (the number that actually showed up — your data)

Notation you can now read: $r_t \sim F$ — "returns at time t are drawn
from distribution F". The papers you've dissected *assume* an F (often
normal-ish) and everything downstream inherits that assumption.

## 3. Discrete vs continuous

**Discrete**: countable values. PMF $p(x) = P(X = x)$. Trading: win/lose
(Bernoulli), wins-in-a-year (binomial), number of signals fired (day 10).

**Continuous**: values on a continuum — returns, precisely. For continuous
X, $P(X = x) = 0$ exactly (a point has no width); likelihood lives in
*densities* and *intervals*:

- **PDF** $f(x)$: likelihood *density* — height matters only relatively;
  $P(a < X < b) = \int_a^b f(x)dx$ (the area).
- **CDF** $F(x) = P(X \le x)$: the *accumulated* probability up to x —
  always between 0 and 1, always increasing. The natural language of risk:
  "5th-percentile loss" is $F^{-1}(0.05)$.

```python
import numpy as np
import scipy.stats as st

x = np.linspace(-0.05, 0.05, 400)
f = st.norm.pdf(x, loc=0.0004, scale=0.011)     # a toy model of daily returns
F = st.norm.cdf(x, loc=0.0004, scale=0.011)
# P(-1% < r < +1%):
print(st.norm.cdf(0.01, 0.0004, 0.011) - st.norm.cdf(-0.01, 0.0004, 0.011))
```

## 4. Distributions as *models* — the point of view that makes you a researcher

A distribution is a **claim about the data-generating process**, not a fact
about data. The normal model of daily returns is: symmetric, thin-tailed,
volatility-constant. Real daily returns violate all three (module 03
measures the violations). So why do papers keep assuming it? Because
*averages* behave better than raw data (day 15's CLT) and because the
alternatives cost complexity. Your job when reading: notice which F is
assumed, and ask what breaks if it's wrong. That question is roughly the
research-robustness industry in miniature.

## 5. On real data: the empirical CDF (no model, just data)

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")
r = np.sort(px["SPY"].pct_change().dropna().values)
ecdf = np.arange(1, len(r) + 1) / len(r)

import matplotlib.pyplot as plt
plt.plot(r, ecdf); plt.xlabel("daily return"); plt.ylabel("F(r)")
plt.title("Empirical CDF of SPY daily returns")
plt.show()
print(f"5th percentile: {np.percentile(r, 5):.3%}")
```

The ECDF answers percentile questions *from data alone* — the ancestor of
historical VaR (module 12). Compare with the normal model's 5th percentile:
they differ, and the direction of that difference is the fat-tail story.

## 6. Research connection

- VaR is a CDF level. Expected shortfall is a tail expectation (module 12).
- Every parametric test in module 04 assumes a distribution (normal-ish
  sampling distributions — justified by CLT, not by raw returns being normal).
- GARCH (module 09) is a model of the *distribution of tomorrow's return
  conditional on today* — a conditional distribution, exactly the object
  you learned to think about on day 3.

## 7. Common mistakes

- Reading PDF height as probability (it can exceed 1!); only *areas* are
  probabilities.
- Using the normal's 5th percentile when the data's is much lower — the
  standard error of risk models (module 03 quantifies with kurtosis).
- Forgetting the ECDF is itself a *sample statistic* — it wobbles with the
  sample (day 1's lesson, now in CDF form).

## 8. Reflection

1. Why is P(return = +0.01 exactly) = 0, yet the PDF at 0.01 meaningful?
2. Your risk model uses the empirical 5th percentile from 3 years of data.
   Name two distinct ways that number misleads (sample noise; regime change).

**Self-check:** PMF vs PDF vs CDF; then explain what assuming "returns are
normal" claims about the world.

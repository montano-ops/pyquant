# Day 5 — Expectation and Variance

## Warm-up retrieval (no notes)

1. PDF vs CDF — which one answers "what's the 5th-percentile loss"?
2. What does it mean to call a distribution a *model*?
3. P(X = x) for continuous X?

## 1. Why a quant needs this

Expectation and variance are the two numbers that run finance: expected
return is why you trade; variance is what it costs you. Module 01 gave you
their sample versions ($\bar r$, $s^2$); today the *population* versions —
and the exact relationship between the two that module 04 will exploit.

## 2. Expectation: the long-run average of the process

$$\mathbb{E}[X] = \sum_x x\, p(x) \quad \text{(discrete)} \qquad
\mathbb{E}[X] = \int x f(x)\, dx \quad \text{(continuous)}$$

Read: *average of values, weighted by likelihood*. Properties you will use
weekly (linearity):

$$\mathbb{E}[aX + bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y]$$

— portfolio expected returns are weighted averages *because expectation is
linear* (module 01's dot product, now justified).

**Expectation is not a promise.** $\mathbb{E}[X] = 0.04\%$ per day does not
mean you make 0.04% on any given day; it means the *average over infinitely
many parallel days* centers there. Your single realized path (day 1) will
wander around it for a long, long time (day 12).

## 3. Variance: the price of the average

$$\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - \mathbb{E}[X]^2$$

Squaring does two jobs: makes deviations positive and makes *big* deviations
disproportionately expensive. $\sigma = \sqrt{\text{Var}}$ returns to the
original units — "volatility".

**Traders' reading of σ:** the typical distance from the mean. If
$\mu = 0.04\%$ and $\sigma = 1.1\%$ daily, then a *zero*-return day is a
1σ event and the "edge" is 0.04σ. The ratio $\mu/\sigma$ is the daily
Sharpe ratio in embryo — the single most important number in strategy
evaluation (module 12 annualizes it; module 13 deflates it).

## 4. The two-layer identity that powers statistics

Sample versions estimate population versions:

$$\bar r \approx \mu \quad s^2 \approx \sigma^2$$

with **how wrong the approximation is** being itself a measurable quantity
(the standard error — day 15's CLT makes it precise, module 04 weaponizes
it). Internalize the three-layer stack:

```
population truth (μ, σ²)  ← never observed
        ↑ estimated by
sample statistics (r̄, s²) ← noisy: they wobble per sample
        ↑ computed from
one realized path (your data) ← survivorship-, regime-, and bias-prone
```

Every number in every paper lives on layer 2 and makes claims about layer 1.
Layer 3 is where all the biases live.

## 5. On real data: the expectancy of a rule, computed honestly

Trading expectancy (discrete RV form): you win $W$ with probability $p$,
lose $L$ with probability $1-p$:

$$\mathbb{E}[\text{P&L}] = pW - (1-p)L$$

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")
r = px["SPY"].pct_change().dropna()

p, W, L = (r > 0).mean(), r[r > 0].mean(), -r[r < 0].mean()
print(f"p={p:.3f}  avg win={W:.4%}  avg loss={L:.4%}")
print(f"daily expectancy: {p * W - (1 - p) * L:.5%}")
print(f"daily mu (check): {r.mean():.5%}")
```

The identity: slicing one distribution into win/loss pieces and re-averaging
reproduces $\bar r$ exactly — expectation is expectation, however you
partition it. But note what the decomposition *buys* you: a strategy's
character (high-p/low-W vs low-p/high-W) has wildly different drawdown and
psychological profiles at the same expectancy — and wildly different
*sampling noise* on p (day 10).

## 6. Research connection

- Every paper's "mean monthly return" is an estimate of a layer-1 μ for
  some portfolio; its t-statistic is a statement about layer-2 noise.
- The Sharpe ratio is $\mu/\sigma$ annualized; "alpha" is an intercept
  expectation after conditioning on factors (module 07).
- Variance's squaring is why outliers dominate risk statistics — the
  1987 −20% day sits 20σ from a normal model's mean (module 03's kurtosis
  discussion; the reason risk models failed that day).

## 7. Common mistakes

- Treating E[X] as "the likely outcome" — for symmetric thin-tailed X it's
  the center; for skewed X the *typical* outcome can be far from E[X].
- Variance of a sum = sum of variances *only under independence* —
  day 9 adds the covariance term; forgetting it is the classic portfolio
  error.
- Reporting μ/σ from a sample without asking about the sample (layer 3!).

## 8. Reflection

1. Two strategies, same expectancy: 55%/±1% vs 35%/+2.4%−2.0%. Which has
   noisier estimation of its own win rate? Which survives a bad month
   psychologically? (Quantify the first with day 10's binomial variance.)
2. Where in the three-layer stack does survivorship bias operate? Look-ahead?

**Self-check:** write E and Var; state linearity; say what μ/σ is and why
its *sample* version wobbles.

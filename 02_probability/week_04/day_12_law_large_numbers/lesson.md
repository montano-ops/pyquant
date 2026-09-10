# Day 12 — The Law of Large Numbers

## Warm-up retrieval (no notes)

1. The empirical rule; standardize x = μ − 2.3σ to a z-score.
2. Two reasons normality is everywhere?
3. What fraction of |z|>3 days do real returns show vs the normal's 0.27%?

## 1. Why a quant needs this

The LLN is why averaging works at all — why your backtest's mean return
tells you *something*. Its fine print — the *rate* of convergence — is why
backtests are so easily fooled. Today you watch convergence happen and
measure its speed. This is the single most practically important
probability lesson in the course.

## 2. The theorem

**Weak LLN (informal):** as n grows, the sample mean $\bar X_n$ converges
in probability to the true mean μ:

$$\bar X_n \xrightarrow{P} \mu$$

Guarantee: keep collecting data and your estimate settles on the truth.
The fine print — *how fast* — comes from the sampling variance:

$$\text{Var}(\bar X_n) = \frac{\sigma^2}{n}, \qquad SD(\bar X_n) = \frac{\sigma}{\sqrt{n}}$$

The SE of the mean *shrinks like* $1/\sqrt{n}$: **quadruple the data,
halve the noise.** Ten times the data buys ~3× precision. Never more.

## 3. Watch it converge (and feel the slowness)

```python
import numpy as np
rng = np.random.default_rng(11)

mu, sigma = 0.0005, 0.011                      # daily edge & vol (generous!)
n = 10_000
means = np.cumsum(rng.normal(mu, sigma, n)) / np.arange(1, n + 1)
se = sigma / np.sqrt(np.arange(1, n + 1))     # the shrinking uncertainty

import matplotlib.pyplot as plt
plt.plot(means, label="running mean")
plt.plot(se, "r--", label="+1 SE"); plt.plot(-se, "r--")
plt.axhline(mu, color="k", lw=1, label="true mu")
plt.xscale("log"); plt.legend(); plt.xlabel("n days (log)")
plt.title("The mean of a noisy edge converges — slowly")
plt.show()
```

Run it and sit with the shape: after **2,500 days (10 years!)** the SE is
still σ/50 = 0.00022 — the *edge itself* (0.0005) is barely two SEs from
zero. This is the LLN's cruel arithmetic: **for financial signal-to-noise
ratios, "large numbers" means decades.** (Module 04.7 computes exactly how
many years a Sharpe-0.5 strategy needs to reach t=2. Spoiler: ~13.)

## 4. The fine print that makes real life worse

The $1/\sqrt n$ rate assumes i.i.d. data with finite variance. Two
real-world degradations:

1. **Fat tails**: with heavy-tailed data, extreme observations dominate
   early samples; convergence still holds (if variance is finite) but is
   *erratic* — long flat stretches punctuated by jumps. With infinite
   variance (some candidate models), the sample mean may never settle —
   the mean itself is a poor summary.
2. **Dependence & regimes**: positively autocorrelated data has *effective*
   sample size n_eff < n — a 252-day year of clustered-vol returns carries
   less information than 252 independent draws (day 19 quantifies).

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="1990-01-01")
r = px["SPY"].pct_change().dropna()
means = r.expanding().mean()
print(f"SE of SPY's mean daily return after {len(r)} days: "
      f"{r.std() / np.sqrt(len(r)):.5f} vs mean {r.mean():.5f}")
```

Compute how many days until SE < mean (i.e., t ≥ 1): for SPY you'll find
it's a *substantial fraction of the sample* — the entire history barely
resolves the mean. Now you know why "stocks go up" is a statement made
with less confidence than most people feel.

## 6. Research connection

- Every paper's "average portfolio return" is $\bar X_n$; its t-statistic is
  $\bar X_n / (\sigma/\sqrt n)$ — today's SE, promoted to a test statistic
  (module 04).
- The LLN is why **more data** is the only free lunch in research; its rate
  is why **strong signals** matter more than clever statistics.
- Track-record length mathematics (MinTRL, module 13) is the LLN inverted:
  given a claimed Sharpe, how much history must you demand?

## 7. Common mistakes

- "Ten years is a lot of data." For mean returns it is ~2,500 observations
  of a signal-to-noise ratio near 0.05 — it is *not* a lot. (For
  *volatility* it's plenty: vol is estimated ~50× more precisely than the
  mean at the same n, because σ is a much larger number relative to its own
  noise. Estimate-precision depends on what you're estimating!)
- Believing LLN protects you from regime change: it averages over the
  *distribution you sampled* — if the distribution shifts, you're averaging
  over a mixture that no longer exists.
- Gambler's fallacy as "LLN in action": "the mean must revert to
  compensate my losses." The theorem is about the *average*, not about
  compensation — losses are not followed by wins; they're *diluted*.

## 8. Reflection

1. Your strategy's daily edge is 0.1% with 1% vol. Roughly how many days
   for the mean to clear 2 SEs? What fraction of careers is that?
2. Explain dilution-vs-compensation to a gambler friend in two sentences.

**Self-check:** state the LLN and the SE formula; give the
quadruple-the-data rule; explain dilution vs compensation.

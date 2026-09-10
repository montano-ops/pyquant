# Day 15 — The Central Limit Theorem

## Warm-up retrieval (no notes)

1. The LLN and the SE-of-the-mean formula; the quadruple-data rule.
2. Dilution vs compensation — explain the difference.
3. How many days for a 0.1%-edge, 1%-vol strategy to clear 2 SEs?

## 1. Why a quant needs this

The CLT is the license for the entire statistical toolkit of module 04:
t-tests, confidence intervals, p-values. It says: **the distribution of the
sample *mean* is approximately normal, whatever the underlying data.** You
will verify it by simulation today — including on fat-tailed data where it
works *but slower* — so that when module 04 hands you a t-statistic, you
know exactly what machinery you're trusting and when it strains.

## 2. The theorem (practical form)

If $X_1, …, X_n$ are independent with mean μ and variance σ² (finite), then

$$\frac{\bar X_n - \mu}{\sigma/\sqrt n} \ \xrightarrow{approx}\ \mathcal{N}(0, 1)$$

Read: standardize the sample mean by its own SE, and you get a standard
normal — regardless of the parent distribution. Two claims in one:

1. $\bar X_n$ is *centered* on μ (that's the LLN);
2. its *deviations* from μ are approximately normal with scale $\sigma/\sqrt n$.

So there are two distributions you must never confuse again:

- the **parent** distribution of returns (fat-tailed, skewed — module 03);
- the **sampling** distribution of the mean (≈ normal, narrow).

Statistics lives in the second. Risk management lives in the first.
Confusing the two is the root of most quant disasters.

## 3. Verify it by simulation

```python
import numpy as np
rng = np.random.default_rng(5)

def sample_means(dist, n, reps=20_000):
    return np.array([dist(rng, n).mean() for _ in range(reps)])

# parent 1: uniform (nothing like normal)
unif = sample_means(lambda r, n: r.uniform(-1, 1, n), 30)
# parent 2: fat-tailed t(3)
t3 = sample_means(lambda r, n: r.standard_t(3, n), 30)

for name, sm in [("uniform", unif), ("t(3)", t3)]:
    z = (sm - sm.mean()) / sm.std()
    print(f"{name}: share beyond |2| = {(np.abs(z) > 2).mean():.3%} (normal: 4.55%)")
```

Even from a t(3) parent, 30-observation means are *close* to normal in the
center — the CLT is robust. Now shrink n to 5 and watch the t(3) case's
tails stay fat: **the approximation degrades from the tails inward, and
faster for fatter parents.** For daily-return-type parents (kurtosis 5–15),
the practical rule: n ≥ 30 decent in the center; tails are untrustworthy
until much larger n.

## 4. The standard error, promoted

Everything in module 04 is built from today's box:

$$\bar X_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)
\quad\Longrightarrow\quad
z = \frac{\bar X_n - \mu_0}{s/\sqrt n} \text{ tests } \mu = \mu_0$$

(with s estimated — the "t-statistic", module 04.4). You already know each
ingredient: μ from day 5, σ from day 5, the SE from day 12, the normal from
day 11, the z-scale from day 11. **The CLT is the assembly step.**

## 5. When it strains (the honest caveats)

1. **Fat tails**: slow convergence; tail behavior of the mean's sampling
   distribution inherits parent extremeness for small n.
2. **Dependence**: i.i.d. is required. Autocorrelated data has effective
   sample size $n_{eff} = n / (1 + 2\sum_k\rho_k)$ — smaller n, wider real
   SEs (day 19 measures this for vol-clustered returns).
3. **Nonstationarity**: sampling from a mixture of regimes is not sampling
   from a distribution with one μ.

All three are *properties of financial data*. The CLT still does heavy
lifting (means over moderate windows are usually fine) — but the caveats
are why module 04 teaches the bootstrap as the robust alternative.

## 6. Research connection

- A paper's t-stat of 3.1 on mean monthly returns is
  $\bar X / (s/\sqrt T)$ — the CLT's normal approximation *is* the
  p-value's source. When you read "Newey-West standard errors", you're
  reading a patch for caveat 2 (autocorrelation, from overlapping
  portfolios).
- The binomial→normal approximation (day 10.5) is the CLT applied to
  counts.
- The entire field of robust inference (bootstrap, permutation) exists as
  insurance for days when the caveats bind.

## 7. Common mistakes

- "Returns aren't normal, so t-tests are invalid" — wrong direction:
  t-tests need the *mean* to be approx-normal, which CLT provides; the
  right worry is *how big n is* and *how dependent* the data.
- Using the CLT on n = 5 fat-tailed observations' *tails* — that's where it
  fails first.
- Forgetting s is estimated (not σ) — that's why it's a *t*, not a *z*
  (module 04's first refinement).

## 8. Reflection

1. Parent vs sampling distribution — explain the difference to a colleague
   using "SPY's daily returns" vs "the mean of 100 days".
2. Your backtest's monthly mean has a t-stat of 1.8. List which caveats
   (fat tails, dependence, nonstationarity) would make the *true* evidence
   even weaker than 1.8 suggests.

**Self-check:** state the CLT in one sentence; the two-distributions
distinction; the three strain-cases.

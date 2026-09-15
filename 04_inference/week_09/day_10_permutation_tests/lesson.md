# Day 10 — Permutation Tests

## 1. Warm-up retrieval (no notes)

1. What is the p-value, in the correct definition (not the two wrong
   readings)?
2. Welch's t-test assumes what about the two groups' errors?
3. What did module 02 say happens to *anything* you compute after you
   shuffle a time series?

## 2. Why a quant needs this

The t-test's p-value assumes a sampling distribution (normality,
independence). The permutation test assumes *almost nothing*: under the
null hypothesis, **it doesn't matter which observations belong to which
group** — so it doesn't matter which labels you assign. Fix the data
values, reshuffle the labels, recompute the statistic. The spread of
that statistic across shuffles *is* its distribution under the null.

In research this is the logic behind: "is this characteristic's
premium different from zero?" (permute which stocks are 'high
momentum'), event studies ("are these event days special?" → compare
against placebo event days), and module 13's placebos. It is also the
cleanest way to *see* what a null looks like.

## 3. Intuition — labels, not data

Two samples: winners (W, n₁) and losers (L, n₂). The sharp null: the
*labels* are arbitrary — the n₁+n₂ values were drawn from one
population, and which ones got called "winner" was chance. Then every
split of the pooled values into (n₁, n₂) is equally likely under H₀.
The observed difference in means is one draw from that set. If it is
unusually large among all splits, the labels are *not* arbitrary —
something real sorts the data.

```
observed  x̄W − x̄L  =  +1.9%
null world (shuffles):  +0.3, −0.1, +0.8, +2.4, −0.4, ...
p = fraction of shuffles as extreme as +1.9
```

Note the contrast with the bootstrap: the **bootstrap resamples values**
(sample ≈ population) to estimate a sampling distribution; the
**permutation resamples labels** (labels ≈ arbitrary) to estimate the
null distribution. Same Monte Carlo skeleton, opposite assumption.

## 4. The mathematics

**Two-sample permutation test** (two-sided):
1. Pool the values; the groups are defined by a label vector of length
   n with n₁ ones.
2. Observed statistic t_obs = x̄₁ − x̄₂ (or its t-version).
3. For b = 1…B: shuffle the *labels* (equivalently, the pooled values
   with fixed labels), compute t*_b.
4. p = #{|t*_b| ≥ |t_obs|} / B (use (1 + count)/(B+1) to avoid
   p = 0).

**Assumptions.** The sharp null + *exchangeability*: under H₀ any
assignment of labels is equally likely. For cross-sectional data with
independent units: yes. For time series: **no** — shuffling values
destroys the temporal dependence the statistic depends on. The two
repairs:

- **Block permutation**: shuffle *blocks* of length b (keeps within-
  block structure, breaks between-block structure) — the same b logic
  as the block bootstrap.
- **Rank / sign alternatives**: where only the *sign* of the
  dependence matters, permute signs or ranks instead of values.

There is no single correct repair; the honest move is to run more than
one and show the conclusion survives.

## 5. Python implementation

```python
import numpy as np
rng = np.random.default_rng(5)

def perm_test_two_sample(x, y, B=2000, rng=rng):
    x, y = np.asarray(x), np.asarray(y)
    pooled = np.concatenate([x, y])
    obs = x.mean() - y.mean()
    n1 = len(x)
    count = 0
    for _ in range(B):
        perm = rng.permutation(pooled)
        if abs(perm[:n1].mean() - perm[n1:].mean()) >= abs(obs):
            count += 1
    return (count + 1) / (B + 1)

a = rng.normal(0.0002, 0.01, 300)
b = rng.normal(0.0002, 0.01, 300)
print("null data, p should be ~uniform:", perm_test_two_sample(a, b))
```

## 6. On real data

A clean first application: **is one day of the week different from the
others?** Take SPY daily returns, label Mondays vs non-Mondays, permute
the labels, and read the p. (Day 04.12 does the full weekend-effect
study with the multiplicity audit this one-number version hides.)

```python
from qrc.data import get_prices
import pandas as pd
r = get_prices("SPY", start="1990-01-01").iloc[:, 0].pct_change().dropna()
mon = (r.index.dayofweek == 0).astype(int)
print("Monday excess:", r[mon==1].mean() - r[mon==0].mean())
```

## 7. Research connection

Event studies are permutation tests in disguise: the event day's return
is tested against the distribution of *non-event* (placebo) days'
returns. MacKinlay (1997, event-study review) formalizes exactly this
comparison. Module 13's "design a placebo for your strategy" is the
same engine: if a signal's power comes from real information, a
*shuffled-labeled* version of the signal should not reproduce the
edge.

## 8. Common mistakes

1. **Shuffling time series values to test dependence.** Testing
   "does |r| have positive autocorrelation" by shuffling |r| builds a
   null world with *zero* autocorrelation but also zero clustering —
   the observed statistic looks more extreme than it deserves; p is
   too small. Use blocks. (This is the single most common
   permutation mistake in quant work.)
2. **Permutation ≈ bootstrap.** Different assumptions (labels vs
   values); different uses (null distribution vs sampling
   distribution). Using the bootstrap to answer "is this different
   from zero" answers the wrong question — the CI includes 0 or not,
   but it is not a test under the sharp null.
3. **Ignoring multiple comparisons inside the permutation.** Testing
   5 days of the week = 5 permutation tests = the module 04.11
   problem waiting to happen.

## 9. Reflection

- The permutation test is *exact* for the label-shuffle null when B →
  ∞ (all splits). Why is it still an *approximation* when you run
  B = 2000, and how does that approximation behave when p is large vs
  small? (Monte Carlo noise: p = 0.45 ± 0.015 is fine; p = 0.001 is
  0 or 1 coin flips — you can only *claim* p < 1/B.)
- If the data are time series *and* the groups are "before event" vs
  "after event" (not arbitrary labels at all), what null can a
  permutation test honestly claim?

## Self-check

1. In one sentence each: what does the permutation test shuffle, what
   does the bootstrap resample, and what does each estimate?
2. You suspect |r| is autocorrelated. Why is the naive-shuffle p an
   *upper bound* on your honesty — i.e., why does it err toward
   rejecting?

---

**Answers:** (1) Permutation shuffles *labels* (group assignment) and
estimates the statistic's distribution *under the sharp null*; the
bootstrap resamples *values* (sample ≈ population) and estimates the
statistic's *sampling distribution* under the fitted model. (2) Naive
shuffling destroys the clustering, so the shuffled |r| series is more
like iid white noise than the real one; the real series' positive
autocorrelation then looks more extreme against that too-quiet null
world → p too small → false confidence. The block version keeps
clustering inside blocks, so the null world has the right dependence
texture and the p is honest.

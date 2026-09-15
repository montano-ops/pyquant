# Day 11 — Multiple Testing

## 1. Warm-up retrieval (no notes)

1. Define the p-value correctly (the sampling-statement version).
2. If you run one test at α = 0.05 on a true null, what is the chance
   of a false positive? If you run 100 such tests, what is the chance
   of *at least one* false positive?
3. What did the binomial give you for "10 or more wins in 100 trials
   at 5% per trial"?

## 2. Why a quant needs this

One test at 5%: a 1-in-20 chance of a false alarm. But research is not
one test. A factor paper tests 25 portfolios × several horizons; a
momentum study tries 12 formation months × 6 holding months; *you* try
five window lengths before showing anyone the heatmap. Each test that
"could have been run" is a lottery ticket. The 5% lottery, played m
times, hands out winners with probability 1 − 0.95^m:

```
m = 10    -> 40% chance of ≥1 false "discovery"
m = 40    -> 87%
m = 100   -> 99.4%
m = 1000  -> 1 − 2.6e-23 (certain, for all practical purposes)
```

Every unadjusted t = 2.0 in a paper that quietly ran 50 variations is a
lottery winner. Module 13 turns this into the deflated Sharpe; today
you get the arithmetic.

## 3. Intuition — two different goals

- **FWER** (family-wise error rate): P(≥ 1 false positive among all
  rejections). Goal: "no false discoveries, ever." Cost: brutal.
- **FDR** (false discovery rate): among the things you *declare*, the
  expected fraction that are false. Goal: "keep my declared list
  mostly true." Cost: mild; this is what mining settings want.

Research papers mostly want FDR control (they'd rather include a
couple of junk factors than miss the real ones); regulators and
practitioners reading "is this ONE strategy real" want FWER. Say which
game you are playing.

## 4. The mathematics

**Bonferroni (FWER).** m tests, each at α/m. Then P(≥ 1 false
rejection) ≤ m·(α/m) = α (union bound — exact if independent,
conservative if positively correlated, and *very* conservative when the
tests are near-duplicates).

**Benjamini–Hochberg (FDR).** Sort p-values p(1) ≤ … ≤ p(m). Find the
largest k with p(k) ≤ k·q/m. Reject hypotheses 1…k. Controls E[FDR] ≤ q
under independence (and most positive-dependence structures).

**The zoo calculation (Harvey, Liu & Zhu 2016).** Suppose a factor
library has m ≈ 100+ candidates, only a fraction truly priced, and each
candidate's t is drawn from a mixture of null (t ~ 0) and signal (t >
0). The share of "discovered" factors that are junk rises fast with m.
Their arithmetic: at m = 100 with realistic signal strength, the
single-test threshold t ≈ 2.0 admits roughly 50–80% junk among
discoveries; **t > 3.0 cuts the junk rate to ~20–30%** — hence the
"t > 3 for new factors" rule. You will reproduce this mixture
calculation in the exercise; it is the most-used number in factor
research and it is three lines of arithmetic.

## 5. Python implementation

```python
import numpy as np
from scipy.stats import norm
rng = np.random.default_rng(13)

m, n_true = 100, 10
p_null = rng.uniform(0, 1, m - n_true)
t_sig = 2.5                                   # signal strength (large n)
p_true = np.array([2*(1 - norm.cdf(t_sig)) for _ in range(n_true)])
p = np.sort(np.concatenate([p_null, p_true]))
# Benjamini–Hochberg at q = 0.05
ks = np.arange(1, m + 1)
k = np.max(ks[p <= ks*0.05/m]) if (p <= ks*0.05/m).any() else 0
print(f"rejected {k} of {m}; at most {n_true} of the rejections are true signals")
```

## 6. On real data (preview)

Five days of the week, five tests of "day d's mean return ≠ 0", on
SPY. Tomorrow (04.12) runs the full study; today just see the raw p's,
then the Bonferroni verdict. The classic "Monday effect" paper (French
1980) reported exactly this kind of result — and the multiplicity
audit is the reason the effect has mostly not replicated.

```python
from qrc.data import get_prices
import pandas as pd
r = get_prices("SPY", start="1953-01-01").iloc[:, 0].pct_change().dropna()
by_dow = r.groupby(r.index.dayofweek).mean()
```

## 7. Research connection

- **Harvey, Liu & Zhu (2016), "…and the Cross-Section of Expected
  Returns":** the t > 3 rule, derived from exactly the mixture
  arithmetic above, updated for the zoo's growth over 1963–2013.
- **Fama & French (1992/1993):** 2×3 and 3×3 portfolios are 5–9
  *comparisons* per table, before the cross-sectionals — the "25
  portfolio sorts" in their later work multiply the family.
- **McLean & Pontiff (2016)** (module 13): post-publication decay is
  partly the zoo arithmetic working as designed — published
  discoveries include the lottery winners, who decay to zero.

## 8. Common mistakes

1. **"We tried 20 specs, here is the best."** Reporting the minimum
   p over a search without telling the family size is the core sin;
   the honest p is a *mixture* (best of m null p's) and is much larger.
   (Module 13's deflated Sharpe prices this exactly.)
2. **Bonferroni on near-duplicate tests.** Testing the same edge at
   11, 12, 13 formation months are *not* 3 independent tests;
   Bonferroni (α/3) is fine as a conservative floor, but the *effective*
   family is ~1. Know which game you're playing: effective family size
   is the honest input, and it must be argued, not asserted.
3. **FDR as a pass/fail stamp.** BH controls the *expected* fraction
   false across the declared set — one declared factor is not "80%
   likely real" by the procedure. It manages a portfolio of claims,
   not a single bet.

## 9. Reflection

- The zoo calculation assumes you can count m — the number of
  hypotheses *actually tried*, including the ones that died in
  notebooks. Your honest m is bigger than your paper's m. What does
  that do to your t threshold, and where does the course's research
  log come in?
- BH controls FDR, not FWER. If your boss only wants to fund ONE
  strategy from your 100 candidates, which procedure should you run,
  and what is its cost?

## Self-check

1. 100 independent null tests at 5%: expected false positives; chance
   of at least one. (Show the arithmetic.)
2. Your study ran 40 correlated variations of one idea. Bonferroni's
   α per test? Is that the *right* number, or just the safe one —
   and what do you need to argue to claim a smaller effective family?

---

**Answers:** (1) E[V] = 100 × 0.05 = 5. P(V ≥ 1) = 1 − 0.95^100 ≈
0.994. So a "clean" 100-null study with one significant result is the
*expected* outcome of pure noise. (2) α/40 = 0.00125 per test. It is
the safe number, not necessarily the right one: if the 40 variations
are near-duplicates (same signal, different windows), the effective
family is far smaller and Bonferroni throws away real power. To claim
a smaller effective family you must show the dependence (correlation
of the test statistics) — e.g., the 11/12/13-month formations share
10/12 of their observation window, so their p's are nearly identical;
the family is 1 signal, 40 measurements.

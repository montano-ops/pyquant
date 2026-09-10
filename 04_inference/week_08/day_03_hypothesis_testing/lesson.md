# Day 3 — Hypothesis Testing

## 1. The courtroom

- **H₀ (null)**: the kill — "no edge," "μ = 0," "the factor price is
  zero." Boring, precise, assumed true until the data disagree loudly.
- **H₁ (alternative)**: μ ≠ 0 (two-sided) or μ > 0 (one-sided — you had
  a direction BEFORE seeing the data, or you don't get the one-sided
  discount).
- **Test statistic**: t = x̄/(s/√n) — how many SEs from the null's
  world.
- **Rejection region / p-value**: how surprising is this t under H₀?

The logic is asymmetric by design: we reject H₀ when the data would be
rare under it — we NEVER "accept" H₀. **"Fail to reject" ≠ "H₀ is
true"** — absence of evidence is not evidence of absence (you felt this
in 02.21's power computation).

## 2. The p-value, defined so you can't misuse it

> p-value = P(data at least this extreme | H₀ true).

The probability of the DATA given the null — NOT the probability of
the null given the data. The two wrong readings, both career-enders:

1. "p = 0.03 means 3% chance the result is luck" — no: under pure luck,
   results this extreme happen 3% of the time. The luck-probability
   statement needs a prior (Bayes, module 02.3 — the posterior of "real
   edge" depends on how many strategies exist).
2. "p = 0.20 means no effect" — no: it means underpowered or absent;
   only a power analysis (day 5) distinguishes.

```python
from scipy import stats
import numpy as np
# the shape of p: uniform under the null
rng = np.random.default_rng(1)
pvals = [stats.ttest_1samp(rng.normal(0, 0.01, 100), 0).pvalue for _ in range(5000)]
print(f"under H0: P(p<0.05) = {np.mean(np.array(pvals)<0.05):.3f}  (uniform by design)")
```

**p is UNIFORM under H₀** — that fact IS the multiple-testing crisis
(day 04.11 in week 9): run 100 null tests, ~5 "discoveries" guaranteed.

## 3. The dance of the p-value

```python
rng = np.random.default_rng(2)
mu = 0.0002; sigma = 0.01; n = 100
sigs = 0
for _ in range(1000):
    x = rng.normal(mu, sigma, n)
    t = x.mean()/(x.std(ddof=1)/np.sqrt(n))
    sigs += abs(t) > 1.98
print(f"true effect, n=100: P(reject at 5%) = {sigs/10:.0%}   <- power, day 5's topic")
```

With a REAL edge (0.02%/day on 1% vol) and n=100, rejection happens
~16% of the time — **the p-value bounces across the significance line
from sample to sample like a coin that's slightly loaded.** Anyone who
has watched a backtest's p-value evolve month to month has seen the
dance; knowing it's a dance is the defense.

## 4. One-sided vs two-sided (the honesty tax)

One-sided p = two-sided p ÷ 2 — but ONLY if the direction was
pre-specified. Choosing one-sided AFTER seeing the effect's sign is p-
hacking in its purest form: it converts every 10% result into a 5%
result. **Course rule: papers you read get two-sided by default; your
one-sided claims require the pre-registered direction (capstone 6's
log).**

## 5. The 5% lottery, first pass

```python
rng = np.random.default_rng(3)
null_pvals = rng.random((100, 1000))          # 100 null "strategies", 1000 sims
discoveries = (null_pvals < 0.05).sum(axis=0)
print(f"100 null tests: mean discoveries {discoveries.mean():.1f}; "
      f"P(at least one) = {(discoveries>0).mean():.0%}")
```

≈5 expected "significant" results among 100 pure-noise strategies; at
least one "discovery" in ~99.4% of runs. **A shop that tests 100 ideas
and funds the significant ones is a random-number generator wearing a
tie.** Week 9's day 04.11 builds the corrections (Bonferroni,
Benjamini–Hochberg); today, hold the picture.

## 6. Reading a test in a paper (the five questions)

1. What exactly is H₀? (Coefficient = 0? Alpha = 0 vs WHICH model?)
2. What statistic, computed HOW? (t with which SE? Robust? HAC?)
3. One- or two-sided, and was the direction pre-committed?
4. What power would this design have against a *plausible* effect?
5. How many tests does this table represent (including the ones not
   shown)?

## Self-check

1. p = 0.048, two-sided, 20 coefficients in the table. Your reaction?
2. Why can't a test "prove" H₀? Give the power-flavored answer.
3. The significance dance: a strategy's p crosses 0.05 four times in
   two years of rolling evaluation. What is actually happening?

---

**Answers:** (1) One of ~20 coefficients at 5% is expected by luck —
multiplicity; the honest p for "best of 20" needs correction (week 9);
also ask power and effect size before celebrating. (2) Because failure
to reject occurs both when H₀ is true AND when the test is too small/
noisy to see the effect — distinguishing requires power you didn't
compute. (3) A true effect near the detection boundary: the t-stat is
wandering around 2, and 2 ± sampling noise crosses the line repeatedly.
The p-value is a noisy statistic too — it has a sampling distribution
(you could compute ITS SE).

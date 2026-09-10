# Day 11 — Non-Normality, Quantified

## 1. The formal tests

You've *seen* non-normality (QQ, kurtosis). Formal tests put a p-value on
it. The two you must know:

**Jarque–Bera** — a market for the moments you already own:

JB = n·(ν̂²/6 + k̂²/24) ~ χ²(2) under normality.

It asks: "are skew and excess kurtosis jointly zero?" — combining day 4's
two statistics, weighted by their SEs (√(6/n), √(24/n)).

**Lilliefors (Kolmogorov–Smirnov with estimated parameters)** — the
supremum distance between the empirical CDF and the fitted normal:

D = max|ECDF(x) − Φ((x−x̄)/s)|.

Distance-based, less tail-obsessed than JB, more "whole shape".

```python
from qrc.data import get_prices
import numpy as np
from scipy import stats
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
z = (r - r.mean())/r.std()
jb = len(r)*(z.skew()**2/6 + (((z**4).mean()-3)**2)/24)
print(f"JB = {jb:,.0f} vs χ²(2) 99% critical value {stats.chi2.ppf(0.99, 2):.1f}")
print(f"p-value ≈ 0 to {max(0, 308-int(np.log10(jb)))} digits, effectively")
```

Real SPY: JB in the *thousands* against a critical value of 9.2. The
p-value is not small; it is comic.

## 2. The big-sample pathology

With n = 252, JB has real work: SPY's daily kurtosis ~10 gives JB ≈ 252·
(0.1/6 + 100/24) ≈ 1050 — still absurd. Even a strategy with κ = 0.4
(imaginally modest) at n = 5,000 gives JB ≈ 5000·0.4²/24 ≈ 33 >> 9.2.
**At market n's, JB rejects essentially everything** — with n in the
thousands, it detects departures from normality that are *real but
irrelevant* (κ = 0.3 matters for nothing).

This is the general curse of consistent tests: **n → ∞ means power → 1
against ANY fixed alternative.** The test answers "is it exactly
normal?" — and the answer is always eventually no, for any data. The
interesting question is not *whether* but *how much* and *where*:

- effect size over p-value: report κ = 12 ± 0.4, not "JB p < 0.001";
- the QQ plot's bend location (which tail, at what z);
- the tail multiple (module 02.11: observed |z|>3 vs 0.27%).

**Rule: p-values test existence; effect sizes test importance.** A
significant test with a trivial effect is a fact about your n, not about
the market.

## 3. When the tests fail the OTHER way

Small samples (n < 100, the reality of monthly strategy data): kurtosis
SE ≈ 0.5, skew SE ≈ 0.25 — genuinely fat-tailed data can look normal for
years. **JB has low power at exactly the n's where most strategy
evaluations live.** The asymmetry to remember:

- Daily data, thousands of obs: tests scream at trivial departures.
- Monthly data, dozens of obs: tests sleep through real ones.

The pathology is symmetric and always against you: the test's
sensitivity is a function of n, not of what matters.

## 4. The reporting standard for normality

The professional package for "is X normal?":

1. κ̂ ± SE, ν̂ ± SE (the effect sizes);
2. JB or Lilliefors p-value (the formality);
3. QQ plot (the location);
4. **the consequence sentence**: "...therefore normal-based [VaR /
   option pricing / position sizing] understates [left-tail risk] by
   approximately [the tail multiple]." — a test without a consequence is
  stamp collecting.

## 5. Preview: why this matters beyond risk

Module 04's t-tests and regressions *assume* (roughly) normal errors.
With fat tails, t-statistics computed at n = 60 are themselves
fat-tailed — your "t = 2.1, significant!" is less significant than it
looks (the CLT needs n; module 02.15's E1 showed t(3) parents still
misbehaving at n = 30). The fixes — robust SEs, longer samples — are
module 04/06 business. Today: know that the assumption is false, know
how false, and know what it does to everything built on it.

## Self-check

1. JB = n·(ν̂²/6 + κ̂²/24). For n = 504, what's the smallest excess
   kurtosis that rejects at χ²(2) 95% (5.99)?
2. Why does Lilliefors replace the KS test's known-parameters version?
3. A paper reports "returns are non-normal (JB p < 0.01, n = 4,000)".
   What follow-up question does the professional ask?

---

**Answers:** (1) Reject when n·κ̂²/24 > 5.99 → κ̂ > √(24·5.99/504) ≈ 0.53
— kurtosis half a unit rejects. Every real daily-return series clears it
by 10–20×; that's the pathology quantified. (2) KS assumes the null's
parameters are known (μ, σ specified in advance); testing a *fitted*
normal with plain KS is invalid — the fit absorbs the data's own
moments, making D too small. Lilliefors uses fitted-parameter critical
values. (3) "How non-normal, and where?" — κ̂ ± SE, the QQ bend, the tail
multiple, and the consequence for the paper's risk/statistical claims.
p < 0.01 at n = 4,000 is a statement about the sample size.

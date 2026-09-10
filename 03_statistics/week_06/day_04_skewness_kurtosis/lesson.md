# Day 4 — Skewness & Kurtosis

## 1. The two shape statistics

Standardize first: z = (x−μ)/σ. Then:

- **Skewness** ν = E[z³] — which tail is long. Negative = crash tail.
- **Kurtosis** E[z⁴] (usually *excess*: κ = E[z⁴] − 3) — tail weight
  *and* shoulder behavior vs the normal.

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
z = (r - r.mean()) / r.std()
skew, kurt = (z ** 3).mean(), (z ** 4).mean() - 3
print(f"skew {skew:+.2f} (SE ≈ {np.sqrt(6/len(r)):.2f}) | "
      f"excess kurtosis {kurt:.1f} (SE ≈ {np.sqrt(24/len(r)):.1f})")
```

**Expected on real SPY:** skew −0.2 to −0.5; excess kurtosis 10–15 (daily).
The SEs at n≈7,500: ±0.03 and ±0.06 — both are *hundreds* of SEs from
normality. This is not a subtle finding. It is the headline fact of
empirical finance (Cont fact #1).

## 2. Kurtosis is an outlier detector

One point can dominate kurtosis. If a sample of n has a single
observation at k standard deviations, it contributes ≈ k⁴/n to the
estimate:

```python
import numpy as np
normal = np.random.default_rng(0).normal(size=5000)
with_one = np.append(normal, 20)   # one 20-sigma-ish outlier
print(f"kurtosis clean {((normal**4).mean()-3):.2f} "
      f"vs with one outlier {((with_one-np.mean(with_one))**4).mean()/with_one.std()**4-3:.1f}")
```

One 20σ point adds ≈ 20⁴/5001 ≈ 32 to kurtosis. **This sensitivity is a
feature and a bug**: kurtosis finds the 1987s like a smoke detector finds
smoke — but it also screams when the "outlier" is a data error (day 5's
job: tell them apart).

## 3. Skew: the crash asymmetry

For equities, negative skew has a mechanism: leverage. Falling prices →
leveraged holders cut positions → more selling (Black 1976; Cont fact
#5's cousin). Consequences you can price:

- **Strategies short vol** (selling puts, carry trades) harvest positive
  mean returns with *negative* skew — the classic "picking up pennies
  in front of a steamroller" profile. Your P&L histogram tells you if
  you are running it.
- **Win rate and skew are connected**: high win rate + negative skew =
  the most seductive and most dangerous strategy shape there is (module
  02.5's p, W, L triangle — now with shape language).

## 4. The QQ plot: shape, seen

Module 02.11 built it; now read it through the moment lens:

- **Left tail below, right tail above the line, symmetric** → fat tails,
  κ > 0, ν ≈ 0.
- **Left tail way below, right tail roughly on the line** → negative
  skew — the equity signature.
- **S-shape through the middle** → shoulders too fat/thin — kurtosis
  without tail action (rare in returns; check for data problems).

One plot, both statistics, every assumption visible. Day 8 makes it a
required exhibit.

## 5. Robust alternatives (when moments scream)

- **Skew via mean−median**: (x̄ − median)/s — bounded, robust, crude.
- **Bowley skew**: (Q3−2·median+Q1)/(Q3−Q1) — quartile-based.
- **Tail index** (Hill): fits P(|z|>x) ~ x^(−α) — module 09's GARCH era.

Rule: **when the moment statistic and its robust cousin disagree, the
outliers are doing the talking** — go find them (tomorrow).

## Self-check

1. Excess kurtosis of a t-distribution with 5 df? (Compute it; the
   answer explains why t(5) is the workhorse fat-tail model.)
2. A strategy shows skew +1.2, kurtosis 2.1. Sketch its P&L histogram;
   guess its win rate; what is it probably selling?
3. Why can't kurtosis distinguish "one catastrophic day" from "many
  moderately bad days"?

---

**Answers:** (1) 6/(ν−4) = 6 at df=5 → excess kurtosis 6 (t(5): κ = 6).
That's inside the SPY range — the standard toy. (2) Long right tail,
short left: occasional big wins, many small losses → *low* win rate,
positive skew — it's probably *buying* volatility/convexity (long
options, trend following). (3) Both put mass in z⁴ — the fourth moment
counts intensity, not frequency. Distinguishing them needs the QQ plot
or the tail index (where in the distribution the mass sits).

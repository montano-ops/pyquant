# Day 8 — Full EDA of Daily Returns

## 1. The liturgy, formalized

Exploratory Data Analysis is not ad hoc — it is a fixed sequence that a
professional can audit. The order matters: **structure before shape,
shape before tails, tails before dynamics.**

| Step | Exhibit | Question it answers |
|---|---|---|
| 0 | n, date range, NaNs, data quality | is the data even real? |
| 1 | headline stats: mean, SD, quartiles, min/max, mean vs median | where's the center, how wide, any instant alarms? |
| 2 | histogram + KDE (log-scale option) | what family does this look like? |
| 3 | skew & kurtosis **with SEs** | shape, quantified (day 4) |
| 4 | QQ plot vs normal | where exactly does normality die? (module 02.11) |
| 5 | rolling 63d mean & vol | is any of this stable? (day 9 previews) |
| 6 | ACF of r and \|r\| | dependence in level, dependence in risk |
| 7 | the verdict paragraph | "distribution X, except…" |

## 2. The workflow, executed

```python
from qrc.data import get_prices
import numpy as np, matplotlib.pyplot as plt
import scipy.stats as st

px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()

# Step 0-1: structure + headline
print(f"n={len(r)}, {r.index[0].date()} → {r.index[-1].date()}, NaNs in raw: {px['SPY'].isna().sum()}")
print(r.describe().round(4))

# Step 3: shape with SEs
z = (r - r.mean()) / r.std()
n = len(r)
print(f"skew {(z**3).mean():+.2f} ± {np.sqrt(6/n):.2f} | "
      f"kurt {(z**4).mean()-3:.1f} ± {np.sqrt(24/n):.1f}")

# Step 4: QQ
q = st.norm.ppf((np.arange(n) + 0.5) / n)
plt.scatter(q, np.sort(z), s=4); plt.plot([-4,4],[-4,4],'r--')
plt.title("QQ: SPY daily vs normal"); plt.show()
```

Run the rest yourself: histogram (try `bins=np.linspace(-0.05, 0.05, 60)`
and see the shoulders), rolling stats, both ACFs. Each exhibit earns its
place by answering its question — no decorative plots.

## 3. Reading like a referee

For each exhibit, the referee's questions:

- **Histogram**: symmetric? where's the mass? does the KDE hide the bins?
  (KDE bandwidth can smooth away real spikes — look at both.)
- **QQ**: WHERE does it bend? Left tail only (crash asymmetry)? Both
  (symmetric fat tails)? In the middle (data problems)?
- **Rolling mean**: does it cross zero? How many "regimes" do you see —
  and would you have traded any of them?
- **ACF|r|**: how far out does dependence run (weeks? months?) — that's
  your block-bootstrap block length (module 02.19) staring back at you.

## 4. The verdict paragraph — the actual deliverable

Every EDA ends in prose. The template:

> "Asset X's daily returns (n = ..., YYYY–YYYY) have mean ... ± ...%,
> SD ...%, skew ... (±...), excess kurtosis ... (±...). The QQ plot
> shows [left-tail departure beginning at z ≈ ...]. Volatility clusters
> (|r| ACF lag-1 = ... vs band ±...). The distribution resembles
> [a t with ~5 df / nothing standard] except [leverage asymmetry /
> the 20XX cluster]. Models assuming [normality / iid] are disqualified
> for [risk / simulation] purposes."

Write it for SPY today. The day-14 checkpoint asks you to write it for an
asset *you* choose — the paragraph is the grade.

## 5. What EDA is for (and against)

EDA's output is *hypotheses*, not conclusions. The honest sequence:
explore on window A → *write down* the hypothesis → *test* it on window B
(module 04's inferential machinery). Exploring and confirming on the same
data is how "I noticed the pattern" becomes "the pattern works" becomes
"the fund is down 40%" — the data-snooping loop, seen from the inside.

## Self-check

1. Why does the liturgy run structure → shape → tails → dynamics, and
   not the reverse?
2. Your QQ plot bends at exactly z = ±3. What does that location say
   about the generating process?
3. You run EDA and "discover" that months starting on Fridays have
   higher means. What is the correct next step, and what is the
   sophomore's next step?

---

**Answers:** (1) Structure questions (n, missingness, range) qualify every
later exhibit — a kurtosis of 30 computed over a window with a data gap
is garbage; shape before tails because moments 1–2 must be trusted before
moments 3–4 can be read; dynamics last because time structure doesn't
affect the marginal shape but DOES affect every SE (n_eff). (2) The body
(central 99.7%) is roughly normal and the extremes are not — a mixture
regime: ordinary days from one process, crash/panic days from another.
That's precisely the GARCH-with-fat-tails motivation (module 09).
(3) Correct: register the hypothesis, test out-of-sample with
multiplicity control (many calendar slices were implicitly tried —
module 04's multiple testing). Sophomore: trade it.

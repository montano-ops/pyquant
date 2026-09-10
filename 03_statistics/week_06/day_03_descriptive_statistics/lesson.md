# Day 3 — Descriptive Statistics on Returns

## 1. The five-number summary, on real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
print(r.describe().apply(lambda x: f"{x:.4%}"))
```

Read it like a trader, not a student: min (the worst day in 30 years —
feel it), Q1/median/Q3 (the central mass — the "ordinary day"), max (the
best day), mean vs median (asymmetry — mean above median = right tail
dragging).

## 2. Robust vs non-robust: an experiment

A statistic is **robust** if one rogue observation can't move it much.
Watch the mean and median disagree under attack:

```python
import numpy as np
core = np.random.default_rng(0).normal(0.0004, 0.01, 500)
data = np.append(core, -0.20)          # one 1987
print(f"with crash:    mean {data.mean():.5%}  median {np.median(data):.5%}")
print(f"without crash: mean {core.mean():.5%}  median {np.median(core):.5%}")
```

The mean moves massively; the median barely notices. Now the same for
spread:

```python
print(f"SD with crash {data.std():.4%} vs without {core.std():.4%}")
mad = np.median(np.abs(data - np.median(data))) * 1.4826
print(f"MAD-scaled with crash {mad:.4%}")
```

**SD nearly doubles; the scaled MAD barely moves.** The 1.4826 factor
calibrates MAD to equal SD *if* the data were normal — so MAD is a
drop-in robust σ̂. When SD and MAD disagree by a lot, the gap itself is a
fat-tail diagnostic (day 4 makes it official).

## 3. Percentiles as risk objects

The p-th percentile is the value below which p% of days fall. Risk
management *is* percentile management:

- **median** (p50): the typical day.
- **p5**: the "bad but monthly" day — a rough 95% VaR.
- **p1**: the daily VaR that regulators and margin desks argue about.

But remember day 2: **tail percentiles have huge SEs.** The empirical p1
of a 252-day sample is the 2nd–3rd worst day of *that year* — next year
redraws it completely. Risk numbers from short windows are themselves
risky.

## 4. Trimmed and winsorized means

Two middle paths between the mean (all in) and the median (all out):

```python
from scipy import stats
print(f"mean {r.mean():.5%} | 5% trimmed {stats.trim_mean(r, 0.05):.5%} "
      f"| 5% winsorized {stats.mstats.winsorize(r, limits=[0.05, 0.05]).mean():.5%}")
```

- **Trim** α: drop the top and bottom α, average the rest.
- **Winsorize** α: *cap* at the quantiles (keep every day, shrink the
  extremes), then average.

For SPY the three land close together (the daily drift is robust to its
own crashes); for a single stock or a strategy with one blowup year they
differ materially. The habit: **report mean, trimmed mean, and median
together.** A big spread among them is a finding, not a nuisance.

## 5. The signal-to-noise reality check

The single most important descriptive "statistic" in this course:

```python
print(f"mean {r.mean():.5%} vs SD {r.std():.4%}: ratio {abs(r.mean()/r.std()):.4f}")
```

≈ 1:25 to 1:35. **The drift is one part signal in ~30 parts noise.** No
descriptive statistic fixes this; everything in modules 04–13 is about
not fooling yourself given it. (Compare: a coin with 51% edge has
mean/σ = 0.02/0.5 ≈ 1:25 on a *per-flip* basis too — but you can flip a
coin 100,000 times by lunch. Markets give you 252 flips a year.)

## Self-check

1. Mean > median for SPY daily returns: which tail is heavier? Check the
   actual data — were you right?
2. You winsorize at 1% before computing the Sharpe ratio. Which of bias
   or variance did you change, in which direction?
3. Why report all three centers (mean/trimmed/median) instead of picking
   the "best" one?

---

**Answers:** (1) Right tail heavier *for the mean-median gap* — but check
the sign: SPY's daily skew is usually *negative* (crashes), which would
push the mean *below* the median; the two effects fight and the sign has
flipped across decades. The data decides — that's the lesson. (2) Both:
you added downward bias to the SD (crashes capped → σ̂ too small → Sharpe
too *high*) and reduced its variance. Capping tails before risk metrics
is how banks used to pass risk models. (3) Because they answer the same
question differently, and the spread among them is itself a robustness
summary. Picking one hides the disagreement.

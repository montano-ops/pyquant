# Day 9 — Is the Mean Stable?

## 1. The mean, rolled

```python
from qrc.data import get_prices
import numpy as np, matplotlib.pyplot as plt
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()

m63 = r.rolling(63).mean()          # quarterly mean, daily
plt.plot(m63, label="63d rolling mean")
plt.axhline(r.mean(), color="red", ls="--", label="full-sample")
se63 = r.std()/np.sqrt(63)
plt.axhspan(r.mean()-2*se63, r.mean()+2*se63, alpha=0.2, color="gray")
plt.legend(); plt.show()
print(f"rolling 63d mean: min {m63.min():.4%}, max {m63.max():.4%}; "
      f"negative {np.mean(m63.dropna()<0):.0%} of days")
```

**What you see:** the rolling quarterly mean spends real time below zero
(typically 25–40% of days over a 30-year sample), swings between roughly
−0.1%/day and +0.15%/day — a 25bp band — while the full-sample mean sits
near +0.04%. **If the "market's mean return" were a stable number, the
rolling estimate would converge to it and stay.** It doesn't.

## 2. Three rival explanations (and why they matter)

1. **Pure noise**: even with a CONSTANT μ, a 63-day mean has SE ≈
   1.05%/√63 ≈ 0.13% — the swings are ~±2 SE. Plausible! The rolling
   mean's instability is *mostly* what a constant-mean world looks like.
2. **Regime drift**: μ really differs across eras (1990s vs 2000s vs
   2010s). Some evidence for this — but (1) makes it hard to PROVE at
   these n's (module 04's tests will formalize; power is low).
3. **Time-varying risk premium**: μ_t moves with vol, rates, sentiment —
   the asset-pricing view (modules 07, 10).

**The practitioner's stance:** you cannot distinguish (1) from (2)–(3)
at quarterly resolution — so never *claim* regime in the mean without
statistics that survive module 04, and never *design* a strategy whose
edge lives inside that 25bp band. **Strategies should live in things
that ARE stable (cross-sectional rankings, vol structure) or accept that
their mean is a moving target.**

## 3. Subsample stability — the 5×5 grid

```python
years = 25
chunks = np.array_split(r.values, 10)
means = [f"{c.mean():+.4%}" for c in chunks]
print("decade-chunk means:", means)
print(f"spread of chunk means: {np.std([c.mean() for c in chunks]):.4%} "
      f"vs SE of a {len(r)//10}-day mean {r.std()/np.sqrt(len(r)//10):.4%}")
```

Compare the *observed spread across chunks* with the SE each chunk's mean
should have under stability. If observed ≈ SE: consistent with a constant
mean + noise. If observed >> SE: the mean genuinely wanders. (Real SPY:
observed spread is typically 1.5–2.5× the pure-noise SE — suggestive of
drift, not proof; overlapping information makes even this rough.)

## 4. The equity premium's fragility

The full-sample mean return of equities — the number trillion-dollar
allocations hinge on — is itself one draw. Bootstrapped over 30-year
windows, the annualized US equity premium has historically ranged from
~2%/yr to ~9%/yr depending on the start date. **Retirement plans and
endowment spending rules assume the mean is the full-sample number; the
data says the mean is a distribution.** (See also module 12's MinTRL:
how many years of data a Sharpe ratio needs.)

## 5. What survives

Means wobble; **structure wobbles less**:

```python
v63 = r.rolling(63).std()
print(f"rolling vol: min {v63.min():.2%}, max {v63.max():.2%}")   # moves 3-5x — but PREDICTABLY (tomorrow)
r_rank = r.rolling(252).apply(lambda x: (x > 0).mean())
print(f"rolling win-rate: {r_rank.dropna().min():.2f}–{r_rank.dropna().max():.2f}")
```

The mean is unstable AND unpredictable; vol is unstable BUT predictable
(tomorrow's day). That asymmetry — **drift: unknowable; risk:
forecastable** — is the deep structure that volatility trading, option
pricing, and risk parity (modules 09–11) are built on. Hold it; it
organizes half the course.

## Self-check

1. A constant-μ world: what fraction of 63-day rolling means land below
   zero if μ = 0.04%, σ = 1.05%? (Compute P(z < −0.0004/0.0132).)
2. Why is "the strategy's mean return decayed to zero after 2010" a
   difficult claim to test?
3. Name one thing in returns that is unstable-but-predictable, and one
   that is stable-but-unpredictable.

---

**Answers:** (1) SE ≈ 0.0132; z = −0.03 → ≈ 49% — in a constant-mean
world, quarterly means straddle zero almost half the time! The observed
instability is no evidence of instability. (2) Because under stability,
the post-2010 window's mean is a draw with SE ≈ σ/√3500 ≈ 0.018% daily;
"decayed to zero" needs a before/after difference that clears the
combined SE — with means this small, power is terrible, and the
backtest's own selection (it was *chosen* because pre-2010 was good)
biases the comparison (regression to the mean, module 02.17). (3) Vol:
unstable level, strongly predictable (ACF of |r| ~0.2+ at lag 1). A
stable-but-unpredictable object: the direction of the *next* day's return
— its distribution is nearly stationary, and knowing it doesn't help you
time tomorrow.

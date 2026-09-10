# Day 10 — Volatility

## 1. Rolling volatility, the market's EKG

```python
from qrc.data import get_prices
import numpy as np, matplotlib.pyplot as plt
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()

v21 = r.rolling(21).std() * np.sqrt(252)     # annualized
v63 = r.rolling(63).std() * np.sqrt(252)
plt.plot(v21, lw=0.8, label="21d"); plt.plot(v63, lw=1.2, label="63d")
plt.axhline(r.std()*np.sqrt(252), color="red", ls="--", label="full-sample")
plt.legend(); plt.title("SPY annualized vol"); plt.show()
print(f"vol range: {v21.min():.0%} to {v21.max():.0%} — a {v21.max()/v21.min():.0f}x swing")
```

Vol ranges from ~7% (sleepy 2017) to 80%+ (2008, 2020) annualized — a
10× swing. **"The volatility of SPY" is not a number.** It is a process:
low-frequency regimes with bursts.

## 2. Annualization — and its one assumption

σ_annual = σ_daily × √252. Where does √252 come from? Variance of a sum
of *independent* returns: Var(r₁+…+r₂₅₂) = 252·Var(daily). Independence.
Return autocorrelation ≈ 0 makes it approximately fine for variance; but
**vol clustering changes the interpretation** — the annualization of a
*current* 21-day vol assumes the current regime persists for a year,
which it won't. Annualized vol is a *convention*, a translation into
comparable units — not a forecast. When someone reports "vol is 80%,"
they mean "if this month's weather lasted a year."

```python
# check it: non-overlapping 252-day realized vol vs daily*sqrt(252) per year
yr = r.groupby(r.index.year).std() * np.sqrt(252)
print(yr.round(3))
```

## 3. Estimators of vol — the zoo

| Estimator | Formula | Notes |
|---|---|---|
| Close-to-close | SD of daily returns | the default; wastes intraday info |
| Parkinson | √(mean of (ln(H/L))²/4ln2) | uses high-low; ~5× more efficient IF H/L are real |
| EWMA | σ²ₜ = λσ²ₜ₋₁ + (1−λ)r²ₜ, λ≈0.94 | RiskMetrics; reacts fast, forgets exponentially |
| Realized vol | Σ intraday squared returns | the gold standard when you have the data (module 09) |

```python
lam = 0.94
ewma = r.pow(2).ewm(alpha=1-lam).mean() ** 0.5 * np.sqrt(252)
plt.plot(v21, label="21d rolling"); plt.plot(ewma, label="EWMA λ=0.94", alpha=0.8)
plt.legend(); plt.show()
print(f"corr(21d, EWMA): {v21.corr(ewma):.2f}; EWMA spike speed — compare 2008/2020 peaks")
```

EWMA tracks the rolling window but turns on a dime (one 3σ day
immediately lifts it ~6%, vs ~5% for a 21-day window that also *forgets
slowly*). The estimator choice is a bias-variance dial (day 2's lesson,
now with prices).

## 4. What vol does NOT tell you

Vol is symmetric — it contains the size of surprises, not their
direction. Three blind spots:

1. **Direction**: σ = 20% says nothing about drift. (Though leverage
   effect: *past* negative returns predict *future* vol — fact 5.)
2. **Tails beyond the second moment**: two assets at σ = 20% — one
   normal, one with κ = 10 — have utterly different 1% VaRs. Vol is the
   *scale*, not the *shape*.
3. **Jumps vs diffusion**: GARCH-vol is smooth; real markets gap.
   Overnight risk (close→open) is a separate bucket that close-to-close
   vol hides inside a single number (module 09's close-open-open-close
   decomposition).

**The professional sentence: "vol tells you the typical size of a move,
conditional on the shape, the direction being unknown, and no jumps."**
It is one coordinate, not the map.

## 5. Vol regimes, quantified

```python
# regime split: vol above/below its rolling median
hi = v21 > v21.rolling(500).median()
print(f"high-vol days: {hi.mean():.0%} of sample")
print(f"mean |r| in high-vol regime {r[hi.fillna(False)].abs().mean():.3%} "
      f"vs low {r[~hi.fillna(False)].abs().mean():.3%}")
```

Vol is bimodal-ish (calm/panic), persistent (months), and the regime
membership of a day predicts its |r| several times better than the
unconditional SD does. **This is THE predictability in markets** (module
02.16's sentence — direction unpredictable, risk predictable — now with
the estimator toolkit). Vol targeting (module 10) and GARCH (module 09)
are industries built on this one fact.

## Self-check

1. Why is √252 annualization a *convention* rather than a forecast?
2. EWMA with λ = 0.94: what's the effective memory (0.94ᵏ = 0.5)?
3. Your Sharpe uses annualized vol from a 21-day window in March 2020.
   Name everything wrong with that number as a denominator.

---

**Answers:** (1) It translates today's regime into yearly units assuming
the regime persists — but regimes die in weeks; the true year's realized
vol depends on the regime *path*, unknowable today. (2) k = ln0.5/ln0.94
≈ 11 days — half the weight comes from the last ~2 weeks; that's the
"fast but jumpy" dial setting. (3) (a) It's a draw from the most extreme
vol regime in 20 years — not representative of any forward year;
(b) window of 21 days means SE ~ σ/√42, a ±11% relative band even before
regime issues; (c) vol clustering means next month's vol is likely
different; (d) the numerator (mean) and denominator (vol) come from
different distributions' moments — Sharpe in a crisis is a ratio of
regime artifacts (module 12 treats this properly).

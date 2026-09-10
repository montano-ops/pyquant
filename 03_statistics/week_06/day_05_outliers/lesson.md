# Day 5 — Outliers

## 1. Information, not dirt

The instinct from statistics class — "remove outliers, then analyze" — is
backwards for returns. The outliers ARE the phenomenon: 1987 (−20%),
2008 (a *cluster* of ±8–10% days), 2020 March (16 records in 3 weeks), 
2010's Flash Crash, 2015's CHF de-peg. A risk model fitted on
outlier-free data is a helmet for a world without pavement.

So today's question is never "delete?" It is: **"is this point the
market, or is it a data error?"** — and then, either way, "what does it
do to my statistics?"

## 2. Identification — and why 3σ fails

```python
from qrc.data import get_prices
import numpy as np
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
z = (r - r.mean()) / r.std()
print(f"|z|>3: {(abs(z)>3).sum()} days ({(abs(z)>3).mean():.2%}); normal predicts {2*(1-0.99865):.2%}")
print(f"|z|>5: {(abs(z)>5).sum()} days")
```

Real SPY: dozens of |z|>3 days, several |z|>5. Under normality, a |z|>5
happens once per ~3.5 million days (14,000 years). **The 3σ rule flags
real market days as "errors" — and worse, it barely flags them, because
σ̂ is itself inflated by the outliers (masking).** Robust z instead:

```python
med = r.median(); mad = np.median(np.abs(r - med)) * 1.4826
zr = (r - med) / mad
print(f"robust |z|>5: {(abs(zr)>5).sum()} days; worst {zr.min():.1f}")
```

The robust score finds MORE extreme points than the classical z —
masking gone. Also check the calendar: a "−38% day" in a stock with a
split you didn't adjust is not a crash, it's a data error. **Volume,
news, and the price series around the point are the final judges.**

## 3. Winsorizing and trimming, honestly

Once identified (and confirmed real), you may still want statistics that
don't dance to one day's tune:

```python
from scipy import stats
lo, hi = r.quantile([0.01, 0.99])
w = r.clip(lo, hi)                       # winsorize at 1%
t = r[(r >= r.quantile(0.01)) & (r <= r.quantile(0.99))]  # trim 1%
print(f"mean raw {r.mean():.5%} | winsor {w.mean():.5%} | trim {t.mean():.5%}")
print(f"SD  raw {r.std():.4%} | winsor {w.std():.4%} | trim {t.std():.4%}")
```

Watch: the mean barely moves (SPY's drift survives its crashes), the SD
drops ~15–20%, kurtosis collapses. **Winsorizing before risk statistics
makes the risk look smaller.** That is sometimes right (stabilize an
estimate) and sometimes fraud (report the capped VaR as the real one).
The difference is disclosure.

## 4. The 1987 experiment

```python
# what one day does to your favorite statistics
oct87 = r.idxmin()
print(f"worst day: {oct87.date()} {r.min():.2%}")
with_exc = r.drop(oct87)
print(f"kurtosis with {(( (r-r.mean())/r.std())**4).mean()-3:.1f} "
      f"without {(((with_exc-with_exc.mean())/with_exc.std())**4).mean()-3:.1f}")
print(f"max drawdown with {((1+r).cumprod()/(1+r).cumprod().cummax()-1).min():.1%}")
```

One day rewrites kurtosis and owns the max drawdown. Any statistic whose
value is "one observation deep" is not a summary of the distribution —
it is a report about a single date. Report those with the date attached.

## 5. Protocol (the professional standard)

1. **Detect** with robust scores, not classical z.
2. **Verify** against the calendar, volume, and external records — data
   error vs market event. Log every decision.
3. **Report twice**: with and without. If conclusions differ, the
   conclusion IS "the result is outlier-driven."
4. **Never** silently delete. A cleaned dataset without a cleaning log
   is not reproducible — it's a rumor.

## Self-check

1. Why does winsorizing reduce kurtosis more than the mean?
2. Your robust z-scores flag a day that the classical z did not. Explain
   "masking" in one sentence.
3. A fund's factsheet reports vol and VaR after 1% winsorization, with
   no mention. Which number is more misleading, and why?

---

**Answers:** (1) Mean depends on z¹ (the crash contributes its −20% once,
diluted by n); kurtosis on z⁴ — a 20σ day's contribution is 20⁴, utterly
dominating. Capping it removes that z⁴ term. (2) The outlier inflates σ̂
(and shifts x̄), shrinking the very z-score that should have caught it —
the alarm silences itself. (3) The VaR: vol is a central-ish statistic
(winsorizing changes it moderately), but VaR *is* a tail quantile —
capping the tail then reporting the tail quantile reports a number about
the cap, not the market. It's like reporting the high score of a game
with a score limiter installed.

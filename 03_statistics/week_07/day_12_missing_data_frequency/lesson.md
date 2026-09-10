# Day 12 — Missing Data & Frequency Choices

## 1. NaNs: the silent bias

Data arrives with holes: holidays differ across exchanges (a Tokyo
stock's calendar vs yours), halted trading (2020's circuit breakers —
real data, missing *volume*, not price), vendors drop days, and merges
of multi-asset panels riddle the frame with NaNs (SPY traded Monday; the
London listing didn't).

**The iron rule: NaNs are not zero.** `.fillna(0)` turns a missing day
into a "price didn't move" day — flat returns that *shrink* your vol
estimate, *bias* correlations toward zero, and *fabricate* calm.
Similarly dangerous defaults:

```python
import pandas as pd, numpy as np
idx = pd.date_range("2024-01-01", "2024-01-10", freq="B")
px = pd.Series([100, 101, np.nan, 99, 98, np.nan, 97], index=idx[:7])
r_bad = px.pct_change().fillna(0)          # missing -> "calm day" LIE
r_ok  = px.pct_change()                    # NaN stays NaN
r_ff  = px.ffill().pct_change()            # forward-fill: price frozen = 0% return
print(pd.DataFrame({"fill0": r_bad, "keep": r_ok, "ffill": r_ff}).round(4))
```

`ffill` for *prices* is correct for level series (you hold at last
marked price) but *transforms* the return series: every gap becomes a 0%
day followed by a jump-when-it-returns. Vol computed on ffilled returns
is biased down by the fake zeros. **ffill levels → compute returns →
remember the zeros are artifacts** (drop them, or model the gap).

## 2. The multi-asset NaN lattice

```python
from qrc.data import get_prices
px = get_prices(["SPY", "TLT", "GLD", "EWJ", "EEM"], start="2005-01-01")
r = px.pct_change()
print(r.isna().mean().round(3))            # per-column missingness
print(f"rows complete after dropna: {len(r.dropna())} of {len(r)}")
```

`dropna()` on the panel keeps only days where *everything* traded — fine
for a portfolio traded at the intersection calendar, silently
destructive for anything else (EEM's holidays delete SPY's data). The
professional choices, in order of honesty:

1. **Trade-calendar intersection** for portfolio simulation (you can only
   trade when everything trades);
2. **Per-asset series** for statistics (each asset's own calendar);
3. **Never** impute returns (imputing *levels* for display: fine).

**Missingness is data**: a stock that halts during crashes is not
missing at random (MNAR — missing not at random). Its surviving
returns are a *biased sample of its own distribution* — the calm ones.
This is survivorship's twin sister and it eats illiquid strategies
(module 05 does the autopsy).

## 3. Frequency: the same market, four distributions

```python
from qrc.data import get_prices
px = get_prices("SPY", start="1993-01-01")
r = px["SPY"].pct_change().dropna()
freqs = {"daily": r, "weekly": r.resample("W").sum(),
         "monthly": r.resample("ME").sum(), "quarterly": r.resample("QE").sum()}
for name, s in freqs.items():
    z = (s - s.mean())/s.std()
    print(f"{name:9s}: n={len(s):5d} skew {z.skew():+.2f} kurt {(z**4).mean()-3:6.1f}")
```

**Aggregational Gaussianity** (Cont fact #4, day 7's project): kurtosis
collapses from ~15 (daily) to ~2 (weekly) to ~0.5 (monthly). The CLT is
summing away the fat tails as you aggregate... but *slower* than
independence would predict (dependence — module 02.19's n_eff again).

Consequences, each a rule:

- **Risk models calibrated on daily data overstate monthly-tail risk if
  naively scaled** (or understate daily tail risk if built monthly and
  scaled down — the killer direction).
- **Statistical tests on monthly n=12/year need decades**; on daily
  n=252/year they scream at trivia (day 11's pathology). Choose
  frequency by the decision, not the habit.
- **Strategies' horizon should match their data's frequency**: a signal
  visible in monthly returns cannot be traded on daily data's noise,
  and a daily-mean-reversion edge washes out monthly.

## 4. The decision table

| You want to... | Use | Because |
|---|---|---|
| Forecast tomorrow's risk | daily (+ intraday if available) | vol clustering lives at days |
| Test a mean/edge honestly | longest available, lower frequency | mean SE shrinks with total info, not n per year |
| Estimate a tail quantile | daily + extreme-value theory | tails live at daily frequency; monthly hides them |
| Backtest a monthly-rebalance strategy | daily *data*, monthly *decision points* | execution reality + no peeking at intra-month |

## 5. The data-quality checklist (tape it to the monitor)

Before ANY analysis: n and date range sanity; duplicate dates; gaps vs
the trading calendar; splits/dividends (a −50% "crash" that's a split);
stale prices (ffill'd vendor rows — detect via zero-return runs); the
2020 halts; currency and timezone alignment for multi-asset panels; and
**where did this data come from and who survived to be in it** (module
05's question, asked early).

## Self-check

1. A panel of 30 stocks, `dropna()`: 40% of rows vanish. What happened,
   and what did you just do to your sample?
2. Why does ffill-ing *prices* then computing returns bias vol down in
   illiquid names?
3. Monthly kurtosis ≈ 0.5: does that mean monthly returns are safe to
   model as normal for risk purposes? (Careful — this is a trap.)

---

**Answers:** (1) Different listings/calendars/holidays → the intersection
is much smaller than each series; you redefined the sample as "days all
30 traded" — a liquid-moment sample, over-representing calm regimes and
dropping exactly the chaotic days illiquid names go missing (MNAR).
(2) Frozen prices → literal 0% returns sprinkled through the series; σ²
is an average of squared returns, and fake zeros dilute it — the
illiquid name looks *safer* than it is. (3) The shape is near-normal,
yes — but (a) n is tiny (12/yr), so the kurtosis *estimate* has SE
√(24/300) ≈ 0.28 at 25 years — the "0.5" is 2 SE from nothing; (b)
aggregation doesn't remove serial dependence — monthly VaR still
underestimates crash clustering (2008 Q4 was three bad *months* in a
row); (c) the left tail you care about (annual worst cases) is a
tail-of-tails. "Approximately normal monthly" ≠ "normal risk".

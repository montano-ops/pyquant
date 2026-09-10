# Day 2 — Corporate Actions by Hand

## 1. The algorithm (the whole day is these five lines, done carefully)

**Splits first, then dividends, backward through time:**

```text
factor = 1
for event in reversed(dates):            # newest to oldest
    if split at t:  factor *= split_ratio        # e.g. 2.0 for 2:1
    if dividend at t: factor *= (1 - D_t / P_t_ex)
    adj_factor[t] = factor               # applies to prices BEFORE t
adjusted = raw × adj_factor
```

Equivalently (CRSP return convention), build returns directly:

> r_t = (P_t · S_t + D_t) / P_{t−1} − 1

where S_t = cumulative split ratio between t−1 and t. The two
constructions must produce identical returns — that identity is your
unit test.

## 2. Build it

```python
import numpy as np, pandas as pd
from qrc.data import get_actions, get_prices

ticker = "AAPL"
raw = get_prices(ticker, field="raw_close")[ticker]
acts = get_actions(ticker)                      # Dividends, Stock Splits
print(acts.tail(8))

# --- split-only factor (cumulative, backward) ---
splits = acts["Stock Splits"]
splits = splits[splits != 0]
f_split = pd.Series(1.0, index=raw.index)
for dt, ratio in splits.sort_index().items():
    f_split.loc[f_split.index < dt] /= ratio     # past prices divided by ratio

# --- dividend factor ---
divs = acts["Dividends"]
divs = divs[divs != 0]
f_div = pd.Series(1.0, index=raw.index)
for dt, d in divs.sort_index().items():
    if dt in raw.index:
        p_ex = raw.loc[dt]
        f_div.loc[f_div.index < dt] *= (1 - d / p_ex)

adj_hand = raw * f_split * f_div
adj_prov = get_prices(ticker, field="adj_close")[ticker]
common = adj_hand.dropna().index.intersection(adj_prov.dropna().index)
ratio = (adj_hand[common] / adj_prov[common]).dropna()
print(f"hand/provider ratio: mean {ratio.mean():.6f}, sd {ratio.std():.6f}")
```

**Expected:** the ratio is a constant to ~6 decimals — your algorithm
reproduces the provider's series up to a scaling (providers anchor the
adjustment to different dates). **Constant ratio ⇒ identical returns**
— check `adj_hand.pct_change().corr(adj_prov.pct_change()) ≈ 1.000`.

## 3. Where the hand-build diverges (and what each divergence teaches)

- **Timing conventions**: using the announcement date instead of
  ex-date shifts the factor one day — tiny per event, systematic
  across hundreds.
- **Special dividends** (huge D/P): the multiplicative approximation
  (1 − D/P) vs exact ratio differs in the 4th decimal — matters only
  for special-distribution studies.
- **Provider quirks**: some providers adjust for dividends only down
  to a floor, or round factors — the drift shows up as returns of
  ±0.01% on ex-dates with no action. Scan your panel for it (day 7).

## 4. Why every quant should do this once

(1) **You learn what "adjusted" is** — a construct, not a price; it
changes retroactively and differs by provider. (2) **You gain an
audit**: when a downloaded series looks wrong (the −35% single day
from module 03.5), you can rebuild returns from raw + actions and see
which pipeline lied. (3) **Delisting returns (week 12)** are just one
more corporate action — the algorithm generalizes to the event that
kills companies.

## 5. The synthetic self-test (offline-safe, works both modes)

Construct a stock you fully control: $100, 2%/quarter dividend,
3:1 split at day 300, some noise. Recover the TRUE total return from
raw + actions using your algorithm. If your algorithm is right, the
recovered series matches the constructed truth to machine precision —
**you are testing the estimator against a world where you know the
answer** (the course's recurring method, now for data pipelines).

## Self-check

1. Why do splits divide PAST prices while dividends multiply past
   prices by (1 − D/P)? (One is a change of units; the other is
   cash that left.)
2. Your hand-built and provider series have a ratio that DRIFTS by
   0.1% over ten years. What is the most likely cause?
3. Total-return index vs adjusted price: why do researchers often
   prefer building the return series directly (r_t = (P·S + D)/P − 1)
   over using adjusted levels?

---

**Answers:** (1) A split changes the unit (one new share = 3 old) —
prices before it must be restated in new units; a dividend is cash
leaving the firm — the holder keeps it, so past prices are discounted
by the fraction paid out. (2) A missed or mistimed event (one
dividend assigned to the wrong ex-date, or a split ratio of 2.0 vs
2.5): each event's error compounds multiplicatively. (3) Levels are
provider-anchored constructs that change retroactively; the return
series is the invariant object — it survives re-downloads, provider
switches, and cache staleness.

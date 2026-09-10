# Day 4 — Prices, Returns, and Your First Charts

## Warm-up retrieval (no notes)

1. What are the first four steps of the paper workflow?
2. What universe and period did JT93 use?
3. In what order do you read a paper's sections?

## 1. What a "price" in your dataset actually is

You download data and get columns like `Open, High, Low, Close, Adj Close,
Volume`. Two of these are not like the others:

- **`Close`** is the as-traded price on that day.
- **`Adj Close`** is a *constructed* series: the historical as-traded prices
  scaled for splits and dividends so that its percentage changes approximate
  the **total return** — what you'd have earned holding the stock and
  reinvesting dividends.

Why this matters immediately: a mature company might pay a 3–4% dividend per
year. Over ten years, an analysis using `Close` understates the investor's
return by a third or more. A growth stock that splits 4-for-1 shows a "75%
crash" in `Close` that never happened to any shareholder. Papers invariably
use total-return-consistent series; reproduction failures are routinely
traced to this choice.

You will build the adjustment *yourself* from raw prices and corporate
actions in module 05. Today: use the provider's adjusted series, know what it
means, and measure how much it matters.

## 2. Simple and log returns (the definitions you'll use for 46 weeks)

With price P on consecutive days t−1, t:

- **simple return:** r_t = P_t / P_{t−1} − 1 — "I made 2% today."
- **log return:** r_t = ln(P_t / P_{t−1}) = ln(1 + r_t) — "my log wealth grew by 0.0198."

Why two? Because they aggregate differently:

- Log returns **add over time**: the 2-day log return is r₁ + r₂. Clean for
  statistics.
- Simple returns **combine across assets**: a portfolio with weights w has
  return Σ wᵢ rᵢ using *simple* returns. Log of a sum ≠ sum of logs, so this
  fails for log returns. Clean for portfolios.

When |r| is small (say < 1%), ln(1+r) ≈ r and the distinction is cosmetic.
In crashes it is not: −50% simple is ln(0.5) = −69.3% log. And simple returns
floor at −100%; log returns don't (but prices stay positive — that's the
point of doing math in log space).

**Course convention** (full table in [conventions](../../concepts/course_conventions.md)):
statistics on single series → log returns are elegant; anything involving
weights, positions, money → simple returns.

## 3. First charts that earn their place

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(px.index, px["SPY"]);           ax[0].set_title("price level")
ax[1].plot(rets.index, rets["SPY"]);       ax[1].set_title("daily returns")
```

The two-panel "level vs return" plot is the first thing a researcher looks
at: the level shows compounding (and data errors: gaps, spikes, a split), the
returns show the actual noise you'll be modeling. A price series that looks
smooth hides returns that look like static. That contrast — trend you can see
vs. signal you can barely measure — is the central empirical fact of this
course, and module 03 quantifies it.

## 4. Common mistakes

- Using `Close` because it's alphabetically first / matches "price" intuition.
- Mixing two assets where one series is adjusted and the other isn't.
- `np.log(rets)` — log of a *return* instead of log of the price ratio; wrong
  and crashes on negative returns (a useful crash — it catches you).
- Reading a "gap" between adjusted and unadjusted total returns as free
  money; it's dividends, already in the adjusted series.

## 5. Research connection

When a paper says "we compute monthly returns from daily closing prices",
every word is load-bearing: *monthly* (aggregation compounds — resample
prices, then returns, or sum logs), *closing* (timing → the shift discipline),
and the silent assumption of *total return* (dividends reinvested). In
today's exercise you quantify the dividend gap for a real payer vs a non-payer
— a number many "reproductions" silently get wrong.

## 6. Reflection

1. Why can log returns be below −100% while simple returns can't? Is that a
   problem? (Hint: what can the *price* do?)
2. You see a backtest of a dividend-stock strategy using unadjusted prices.
   Which direction is the error — overstated or understated — and roughly how
   big for a 3%-yield stock over 10 years?

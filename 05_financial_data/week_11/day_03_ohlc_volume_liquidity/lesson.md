# Day 3 — OHLC, Volume, Liquidity

## 1. The columns beyond close

- **OHLC**: open/high/low/close — the intraday envelope. High-low
  range carries vol information (Parkinson, module 03.10); open vs
  close separates overnight from intraday returns (module 09's
  decomposition).
- **Volume**: shares traded. **Dollar volume** = price × volume — the
  comparable-across-time-and-tickers liquidity measure.
- **Market cap** = price × shares outstanding (the size factor's raw
  material — capstone 3).
- **Turnover** = volume / shares outstanding — activity vs size.

```python
from qrc.data import get_prices
px = get_prices("SPY", field="close")["SPY"]
vol = get_prices("SPY", field="volume")["SPY"]
dv = px * vol                      # dollar volume
print(f"dollar volume: median ${dv.median()/1e6:,.0f}M/day")
```

## 2. Amihud illiquidity — the one-line measure worth knowing

> ILLIQ = mean( |r_t| / dollar_volume_t )

"How many percent does the price move per million dollars traded?"
Illiquid names: 5–50 bp per $1M; SPY: ~0.01bp per $1M. It predicts
price impact — your own trading's cost — and is the standard control
in microstructure-aware factor studies (Amihud 2002; module 10
returns to it).

## 3. The screens papers apply (and what each one costs)

| Screen | Rule of thumb | Why it exists | What it selects away |
|---|---|---|---|
| Price | P > $5 | penny stocks: microstructure noise, data errors, untradable | distressed/recovering names — where some anomalies live |
| Liquidity | ADV > $1M | you cannot trade the backtest | small caps — the size premium's home |
| History | listed ≥ 12m | needs formation data | IPOs (first-year returns are extreme both ways) |
| Exchange | NYSE/NASDAQ/AMEX | data quality + convention | OTC/foreign — and the cross-listed |

**Every screen is a universe definition, and every universe is a
research decision** (day 5's thesis). The standard line — "we exclude
stocks under $5" — quietly removes the exact stocks where the
momentum/reversal anomalies are strongest. The honest paper states
its screens AND runs the boundary as a robustness check (results with
$1 vs $5 vs $10 cutoffs).

## 4. Volume and volatility: the sixth stylized fact, measured

```python
r = px.pct_change().dropna()
common = r.index.intersection(dv.dropna().index)
print(f"corr(|r|, log dollar volume): {r.abs().loc[common].corr(np.log(dv.loc[common])):+.2f}")
```

Cont fact #6: activity tracks risk — correlation of |r| with log
dollar volume typically +0.3 to +0.5. **Volume is a coincident
volatility indicator** (and a slow leading one) — the basis of
volume-adjusted vol models and the practical reason "no one was
trading" is a data-quality alarm, not just color.

## 5. Liquidity in the wild: the 2020 lesson

Liquidity is regime-dependent: ADVs that justified a position size in
February evaporated in March 2020. **A backtest sized on average
liquidity assumes average liquidity at the moment of trading —
exactly when liquidity is worst.** Professional practice sizes on
*percentile* participation (e.g., ≤1% of the worst-decile rolling
ADV), not the mean. When you read a paper's capacity claim ("runs
$2B"), check which ADV percentile it assumed.

## Self-check

1. Stock A: $200, 500k shares/day. Stock B: $4, 8M shares/day. Which
   is more liquid by dollar volume? Which passes the standard
   screens? What anomaly literature does B's exclusion distort?
2. Your strategy trades 5% of a stock's ADV. In a stress week ADV
   falls 80%. What is your new market impact, roughly, if impact ~
   (participation)²?
3. Why is dollar volume preferred to share volume for cross-sectional
   comparisons?

---

**Answers:** (1) A: $100M/day vs B: $32M/day — A is more liquid, but
B is the "liquid" one by share count and STILL fails the $5 screen;
together the screens delete the small-cap/lower-price universe where
size and reversal effects are strongest — measured effects become
"effects that survive in liquid large caps," a different (weaker)
claim. (2) Participation goes 5% → 25% (same shares against 1/5 the
volume); impact ~ participation² → ~25× worse. Liquidity flight
squares into your costs. (3) Share counts are not comparable across
price levels or split histories (a 10:1 split multiplies share volume
by 10 with nothing real changed); dollar volume measures actual
trading capacity.

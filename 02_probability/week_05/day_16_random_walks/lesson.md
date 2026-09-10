# Day 16 — Random Walks and (Near-)Efficient Markets

## Warm-up retrieval (no notes)

1. State the CLT; parent vs sampling distribution.
2. The three strain-cases for the CLT in finance?
3. Why does dependence shrink effective sample size?

## 1. Why a quant needs this

Yesterday's machinery was about *statistics of* returns. Today is about the
*structure of* returns — the random walk model, which is both the
historical null hypothesis of finance and the reason edges are so hard.
Every anomaly paper (momentum included) is a claim to *reject* what you
meet today.

## 2. The random walk model

Prices follow a random walk when *log* prices are a cumulative sum of
i.i.d. shocks:

$$\log P_t = \log P_{t-1} + \varepsilon_t, \qquad \varepsilon_t \sim \text{i.i.d.}(0, \sigma^2)$$

so log *returns* are i.i.d. — tomorrow's return is independent of
everything you know. Consequences (all verifiable in data):

- **No memory in direction**: autocorrelations of returns ≈ 0.
- **Variance scales with time**: Var over k days = kσ² — the √time law,
  now as a *property of prices*, and the basis of the variance-ratio test
  (module 08.21).
- **Cross-sectional near-independence**: past patterns carry no
  exploitable information *in expectation*.

```python
import numpy as np
rng = np.random.default_rng(8)
eps = rng.normal(0.0004, 0.011, 2500)
log_p = np.log(100) + np.cumsum(eps)
```

## 3. The economic story: why would markets be like this?

Not physics — *arbitrage*. If returns had exploitable autocorrelation,
traders would trade on it; their trading *removes* it (buying the
predictable winner pushes its price up today). The random walk is not a
claim that markets are magic; it's the *equilibrium consequence of people
hunting edges*. This is the Efficient-Market Hypothesis (EMH) in one
sentence:

> Prices fully reflect available information, so you can't systematically
> beat them without an informational, structural, or risk-bearing advantage.

**What EMH does NOT say:** prices are always right (they can be wildly
wrong with no way to profit from the wrongness), or that returns are
normal (only that direction is unpredictable), or that edges are impossible
— only that edges are *hard, capacity-limited, and competed*.

## 4. What the data says (and what you'll test in module 08)

Real returns are **close to** a random walk in *direction* but not exactly:

- return autocorrelations: tiny but measurably nonzero at short horizons
  (reversal) and positive at intermediate horizons cross-sectionally
  (momentum — JT93's whole claim);
- *squared/absolute* returns: strongly autocorrelated (vol clustering —
  the random walk is badly wrong about *risk*, even where it's right about
  *direction*);
- variance ratios deviate from k in ways that made Lo & MacKinlay (1988)
  a landmark.

So the honest modern picture: **direction ≈ nearly efficient; risk =
highly predictable.** That sentence organizes the entire strategy landscape
of module 10: the strategies that work at scale are either (a) harvesting
*risk premia* (being paid to bear risk others won't), (b) exploiting small,
costly-to-arbitrage inefficiencies (momentum, reversal — after costs,
thin), or (c) predicting *volatility*, not direction.

## 5. On real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")
r = np.log1p(px["SPY"].pct_change().dropna())
print(f"return autocorr lags 1-5: {[round(r.autocorr(k), 3) for k in range(1, 6)]}")
print(f"|return| autocorr lags 1-5: {[round(r.abs().autocorr(k), 3) for k in range(1, 6)]}")
```

The pattern you'll see — near-zero return autocorrelations, large absolute-
return autocorrelations — is the empirical signature of "efficient-ish
direction, predictable volatility" (module 08 formalizes with confidence
bands; module 09 builds the models).

## 6. Research connection

- JT93 is a *rejection* of the random walk in the cross-section — that's
  why it was controversial and why it matters.
- Lo & MacKinlay (1988) test the random walk with variance ratios — you
  reproduce the test in module 08.
- The EMH's joint-hypothesis problem (Fama 1970, one line): any "beat the
  market" test is secretly a test of *market efficiency + your risk model*
  simultaneously. "Alpha" against a wrong risk model is not alpha — the
  deep reason module 07 exists before any strategy claims get believed.

## 7. Common mistakes

- Reading EMH as "technical analysis is illegal" — it reads "it's *hard*,
  and the easy versions are already traded away".
- Testing the random walk on *prices* instead of returns (prices
  autocorrelate mechanically — the cumulative sum — proving nothing).
- Concluding from ≈0 autocorrelation that *nothing* is predictable:
  volatility is (check the second print) — and cross-sectional
  predictability can hide in near-zero time-series autocorrelation.

## 8. Reflection

1. If tomorrow's *direction* is ~unpredictable but tomorrow's *volatility*
   is ~40% predictable, which businesses make money and how? (Hint:
   options dealers vs. directional funds.)
2. The joint-hypothesis problem: your backtest "beats the market" during a
   period when small stocks crushed large ones. What are the two readings,
   and what would you need to distinguish them?

**Self-check:** write the random walk; state the EMH and its two honest
caveats; give the direction-vs-volatility asymmetry with its evidence.

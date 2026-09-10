# Day 3 — Conditional Probability and Bayes' Rule

## Warm-up retrieval (no notes)

1. The pandas idiom for P(A|B)?
2. What does independence assert about conditionals?
3. Why can P(A|B) ≠ P(B|A) — one sentence?

## 1. Why a quant needs this

The most expensive reasoning error in trading is conditional-probability
confusion, and it comes wearing a suit:

> "80% of major crashes were preceded by our warning signal."

Sounds impressive. But you don't trade P(signal | crash) — you trade
**P(crash | signal)**, and base rates decide which one you're getting.
This day is a vaccine.

## 2. Bayes' rule: flipping the conditioning

$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

Read: *posterior = (likelihood × prior) / evidence*. The three names matter
because they are the three levers of honest belief-updating:

- **Prior** P(A): how rare is the thing itself (base rate)?
- **Likelihood** P(B|A): how reliable is the signal *when the thing happens*?
- **Evidence** P(B): how often does the signal fire overall?

## 3. The signal confusion matrix (the trading-native form of Bayes)

For a binary signal (fires / doesn't) and binary reality (crash / no crash):

|  | crash | no crash |
|---|---|---|
| **signal fired** | hit | false alarm |
| **no signal** | miss | correct calm |

The four cells are all conditional frequencies you can *measure in a
backtest*. From them:

- P(signal | crash) = hit rate — "80% of crashes had the signal" ✓ plausible
- **P(crash | signal) = hit / (hit + false alarm)** — what you actually earn
  from when you act on the signal.

## 4. Worked example (by hand, then code)

Crashes are rare: P(crash) = 2%. Signal fires in 80% of crashes (hit rate)
— but also fires on 15% of calm periods (false alarms).

$$P(\text{crash} \mid \text{signal}) = \frac{0.8 \times 0.02}{0.8 \times 0.02 + 0.15 \times 0.98} = \frac{0.016}{0.163} \approx 9.8\%$$

The "80% accurate" signal is right **less than one time in ten** when it
fires. If hedging costs you the 15% of calm periods' drag, you lose money
with high probability while being "right about crashes" most of the time.

```python
def bayes(prior, likelihood, false_alarm):
    evidence = likelihood * prior + false_alarm * (1 - prior)
    return likelihood * prior / evidence

for prior in [0.02, 0.10, 0.30]:
    print(f"prior {prior:.0%}: P(crash|signal) = {bayes(prior, 0.8, 0.15):.1%}")
```

Run it: the same "80% signal" is worth 9.8%, 37%, or 65% depending purely on
the base rate. **Base rates dominate** — which is why rare-event strategies
(IX-hedging, tail funds) can be "usually right" and still lose money.

## 5. On real data: a volatility signal, honestly evaluated

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")
r = px["SPY"].pct_change().dropna()
vol = r.rolling(21).std()
high_vol = vol > vol.quantile(0.8)          # signal: past-month vol in top quintile

big_loss = r < -2 * r.std()
print(f"P(big loss)        = {big_loss.mean():.3%}")
print(f"P(big loss | high vol) = {big_loss[high_vol.shift(1).fillna(False)].mean():.3%}")
```

(Why `shift(1)`? The signal must be *known before* the day it predicts —
you know this from orientation day 2; it will become reflex.) High past vol
roughly doubles-to-triples crash-day probability — a real, useful,
*conditional* fact. And still nowhere near "vol predicts crashes".

## 6. Research connection

Every event study conditions on an event; every anomaly paper conditions on
a characteristic. The evaluation question — the one this course hammers —
is always: *conditioned on the signal, what actually happens, at what base
rate, net of costs?* Papers report likelihoods (hit rates); you must convert
to posteriors (act-and-earn rates) before believing tradability.

## 7. Common mistakes

- Quoting P(signal | event) as if it were P(event | signal) — the
  prosecutor's fallacy, daily on trading Twitter.
- Ignoring the prior because it's boring. Base rates are the biggest term
  in the multiplication.
- Confusing "the signal improves the odds" (P(A|B) > P(A)) with "the signal
  justifies the trade" (odds must clear *costs*, not just rise).

## 8. Reflection

1. Your signal doubles crash probability (2% → 4%). Hedging costs 0.1% per
   fired signal. When does acting become +EV? What extra number do you need?
2. Explain to a colleague why "7 of the last 8 recessions were preceded by
  an inverted yield curve" cannot be read as "an inverted curve means
  recession is likely" without one more table of numbers.

**Self-check:** write Bayes' rule, name the three components, and compute
the 80%-signal example from memory.

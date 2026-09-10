# Day 10 — Bernoulli and Binomial: The Mathematics of Win Rates

## Warm-up retrieval (no notes)

1. Write the two-asset portfolio variance; where's the covariance term?
2. What does ρ = −1 with equal σs make possible?
3. Why does the minimum-variance weight differ from 100%-in-the-safe-asset?

## 1. Why a quant needs this

"Win rate" is the most-quoted, least-understood number in trading. Today it
gets exact mathematics: how often *should* a 55% strategy win, how much
does a measured win rate wobble, and how big a sample you need before a
win rate means anything at all. This day is the direct engine of the
module checkpoint (day 21).

## 2. Bernoulli(p): one trial

X = 1 (win) with probability p, 0 with probability 1−p.

$$\mathbb{E}[X] = p, \qquad \text{Var}(X) = p(1-p)$$

Note the variance's shape: *maximal at p = 0.5* — a coin-flip strategy is
the noisiest possible; a 90%-win-rate strategy has small per-trial noise
(p(1−p) = 0.09). Everything about strategy evaluation difficulty follows
from this innocent-looking parabola.

## 3. Binomial(n, p): counting wins

$P(K = k) = \binom{n}{k} p^k (1-p)^{n-k}$, with $\mathbb{E}[K] = np$,
$\text{Var}(K) = np(1-p)$.

*Trading question it answers:* "My strategy wins 55% of days. Over a year
(252 days), what's the probability of a *losing quarter* (≤ 60 wins in
126 days)?" — computable exactly:

```python
from scipy import stats
import numpy as np

p = 0.55
# losing quarter: fewer wins than losses -> at most 62 of 126
q = stats.binom.cdf(62, 126, p)
print(f"P(losing quarter) = {q:.1%}")
```

≈ 11%. A genuinely-good daily strategy loses about one quarter in nine on
win-count alone — before costs, before bad luck in win *sizes*. (Now you
know why quarterly evaluation of daily strategies is noise-worship.)

## 4. The win-rate estimator and its noise (the heart of the day)

Measure $\hat p = K/n$. Its variance:

$$\text{Var}(\hat p) = \frac{p(1-p)}{n}, \qquad SE(\hat p) = \sqrt{\frac{p(1-p)}{n}}$$

Evaluate it — this table is worth memorizing:

| n (days) | SE(p̂) at p=0.5 | 95% band |
|---|---|---|
| 63 (quarter) | 0.063 | ±12pp |
| 252 (year) | 0.031 | ±6pp |
| 1260 (5 years) | 0.014 | ±3pp |

A one-quarter observed 60% win rate is *fully consistent* with a true 50%.
A one-year 60% is nearly so. **A win rate needs years to mean anything.**
And this is the *best case* (independent trials); autocorrelation and
regime-dependence (day 19) make real-world noise worse.

```python
import numpy as np
rng = np.random.default_rng(3)
for n in [63, 252, 1260]:
    phat = (rng.random((2000, n)) < 0.55).mean(axis=1)
    print(f"n={n:5d}: sd of measured win rate = {phat.std():.3f}")
```

## 5. Normal approximation (the bridge to day 15)

For large n, $\hat p \approx \mathcal{N}\left(p,\ \frac{p(1-p)}{n}\right)$ —
the binomial (discrete, skewed) is well-approximated by the normal
(smooth, symmetric). This is the CLT in its first practical costume, and
the reason pollsters and quant researchers share machinery. When is n
"large"? Rule of thumb: np ≥ 5 and n(1−p) ≥ 5 — always true at trading
scales.

## 6. On real data

```python
from qrc.data import get_prices
px = get_prices("SPY", start="2005-01-01")
r = px["SPY"].pct_change().dropna()
win_rate, n = (r > 0).mean(), (r > 0).count()
se = np.sqrt(win_rate * (1 - win_rate) / n)
print(f"SPY up-day rate: {win_rate:.1%} ± {1.96 * se:.1%} (95%) over {n} days")
```

SPY's up-day rate is ~53–54% with a 95% band of about ±2pp over two
decades. Is 53% "an edge"? It's *paid for* by crash asymmetry (average down
day bigger than average up day) — win rate alone never settles anything
expectancy does. (Day 5's decomposition, now with uncertainty attached.)

## 7. Research connection

- Sign tests and "fraction of positive months" in papers are binomial
  statements; checking whether a paper's positive-months fraction is
  surprising under p=0.5 is a two-line binomial calculation you can now do.
- The multiple-testing logic of module 04 (and Harvey-Liu-Zhu's factor zoo)
  is binomial at heart: at a 5% significance level, 100 independent null
  tests produce ~5 "discoveries" — Binomial(100, 0.05), exactly today's
  machinery.
- Minimum track record length (module 13) = "how large must n be before a
  Sharpe estimate clears noise" — the same table above, in expectation
  units.

## 8. Common mistakes

- Reporting a win rate with no n and no SE. Always: p̂ ± 1.96·SE.
- Comparing win rates across strategies with different trade frequencies —
  n differs, so noise differs (a 60% rate on 40 trades is worse evidence
  than 53% on 2,500).
- Assuming independent trials: consecutive-day outcomes of *the same
  strategy* share regimes (day 19) — real SEs are wider.

## 9. Reflection

1. A Twitter account shows 8 winning months out of 10. Compute P(≥8 wins in
   10 | p=0.5). What is the account's win rate consistent with?
2. Why is p = 0.5 the *hardest* win rate to evaluate? (The parabola.)

**Self-check:** Bernoulli and binomial means/variances; the SE of p̂; the
n=63 vs n=1260 comparison from memory.

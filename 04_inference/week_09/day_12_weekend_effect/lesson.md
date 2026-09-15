# Day 12 — The Weekend Effect

## 1. Warm-up retrieval (no notes)

1. What are the two correct p-values in a study that tests 5 days of
   the week? (Raw, and after the family is counted.)
2. What is the t-stat of a mean, and what does ×252 do to it?
3. Why is "Monday's mean is −0.04%, t = 2.1" not yet a strategy?

## 2. Why this paper, why now

French (1980) reported that **Monday returns are systematically lower
than the other days** for NYSE stocks, 1953–1978. It is the perfect
target for week 9's toolkit because it exercises *all* of it at once:

- grouped means and t-tests (04.1–04.4),
- the right contrast (paired/Welch, 04.8),
- the family of 5 days — and of 5 days × several sub-periods
  (04.11),
- stability over time (03.9),
- and the tradability gate (04.17, previewed today).

It is also the perfect *story*: a real published effect that has
largely not survived later samples. Module 13 will explain the
mechanism (publication selection + decay); today you just reproduce
the audit honestly, on both worlds: real data, and synthetic data
where the effect is guaranteed to be zero.

## 3. The hypotheses, precisely

There are three different claims that get conflated:

1. **H1 (level):** Monday's *mean* return differs from 0.
2. **H2 (contrast):** Monday differs from the *other four days*
   (the tradable claim — you only trade the Monday spread).
3. **H3 (some day differs):** at least one day of the week is special
   (the family the multiplicity audit targets).

A paper can satisfy H1 or H3 and fail H2 — "Monday is negative" is
not the same as "Monday is *less than Tuesday–Friday*." The tradable
claim is H2, so that is the one we test hardest.

## 4. Intuition — what could produce it, what could fake it

**Real mechanisms:** news accrues over the weekend while the market is
closed → Monday digests a larger information batch; weekend sentiment
(overnight bad news, short-covering flows) has been proposed; tax
and dividend calendar effects. **Fake mechanisms:** 5 days × many
sub-periods × many stocks is a big family — some "Mondays" will be
significant by the 5% lottery; a strong pre-1980 sample that never
repeated is a regime artifact, not a law; and even a *true* −3bp
Monday dies against a 5–10bp round-trip cost (04.17).

## 5. The pipeline (this is the template for every anomaly audit)

```
1. Data + universe          SPY (or your index), long history, adjusted
2. The table                mean, SD, n, t per day-of-week (vs 0)
3. The contrast             Monday vs other 4 days (Welch)
4. The family               5 day-tests → Bonferroni (or BH) verdict
5. Stability                sub-periods: does the t hold, flip, or die?
6. The cost                 round-trip cost vs per-event magnitude
7. The verdict              one paragraph, all caveats in
```

```python
import numpy as np, pandas as pd
from qrc.data import get_prices
r = get_prices("SPY", start="1953-01-01").iloc[:, 0].pct_change().dropna()
g = r.groupby(r.index.dayofweek)
tab = pd.DataFrame({"mean": g.mean(), "sd": g.std(), "n": g.size()})
tab["t"] = tab["mean"] / (tab["sd"] / np.sqrt(tab["n"]))
print(tab.round(5))
mon = r[r.index.dayofweek == 0]; oth = r[r.index.dayofweek != 0]
t_welch = (mon.mean() - oth.mean()) / np.sqrt(mon.var()/len(mon) + oth.var()/len(oth))
print(f"Monday vs other 4 days: Welch t = {t_welch:.2f}")
```

## 6. On real data vs the null world

Run the same pipeline on synthetic returns (business days, no
day-of-week structure by construction). The synthetic run is your
**placebo**: it tells you what the pipeline *does* to pure noise at
this sample size. If real-data results sit inside what the null world
produces, the honest verdict is "indistinguishable from the noise we
simulated." (This is the same trick as 03.7's stylized-facts audit.)

## 7. Research connection

- **French (1980):** the original calendar-effect study; Monday
  significantly below the other days for 1953–1978 NYSE stocks.
- **The non-replication arc:** subsequent samples (1980s–2000s,
  different markets) mostly shrink the effect to zero or noise — a
  live textbook example of what McLean & Pontiff (2016) will
  quantify: anomalies decay after publication. The weekend effect is
  the course's running case study for "a real paper, audited honestly."
- **Harvey et al.'s zoo** lists calendar anomalies among the crowded
  family where t > 2 was never enough.

## 8. Common mistakes

1. **Reporting the 5 raw t's as 5 results.** The family is 5 (and 5 ×
   sub-periods if you look at stability *before* deciding). One
   significant day out of 5 is expected ~23% of the time under pure
   noise (1 − 0.95^5).
2. **Stability as a free look.** "It was strong 1953–1980, weak
   after" is a second test that was never declared; the honest
   statement is "the effect is time-varying, and the tradable version
   is the *whole sample*, which is weak."
3. **Confusing the statistical effect with the trade.** The effect is
   a daily *return difference*; the trade is short-Friday /
   cover-Monday with a round-trip cost, overnight gap risk, and
   borrow availability. A −3bp Monday at t = 2.3 is statistically
   real and economically dead.

## 9. Reflection

- If you *did* find a robust, cost-surviving Monday effect in a
  sample French never saw, what is the strongest remaining explanation
  besides "a real weekend mechanism"? (Data artifact: how is a Monday
  open defined? split/dividend adjustments? timezone of the
  "close"? — module 05's domain, revisited here as a hypothesis.)
- The synthetic placebo had *zero* effect by construction. What did
  its t-table look like — and what does that tell you about the
  *power* of this audit at 70 years of daily data? (A test that
  cannot reject a true −3bp Monday is weak even when it "works.")

## Self-check

1. Monday mean −0.03% (SD 1.1%, n = 3,700), other days mean +0.01%
   (SD 1.1%, n = 14,800). Welch t for the contrast? Bonferroni verdict
   over the 5-day family at 5%?
2. A −3bp Monday, tradable 52×/year at 10bp round-trip: annualized
   gross and net edge? One-sentence verdict.

---

**Answers:** (1) SE = 1.1%·√(1/3700 + 1/14800) = 1.1% × 0.0184 ≈
0.020%; t = (−0.04%)/0.020% ≈ **−2.0** on the contrast — marginally
significant at raw 5%, and **below** the Bonferroni threshold for the
5-day family (α/5 = 0.01 → t ≈ 2.58). The lesson of the numbers: a
"significant Monday" at this sample size is still within the noise the
multiplicity audit allows. (The full table — all five days, not just
the Monday contrast — is what a reviewer will ask for.) (2) Gross
52 × 3bp = 156bp/year; cost 52 × 10bp = 520bp/year; **net −364bp** —
a guaranteed loser. Break-even needs an edge > 10bp *per event* (≈
520bp annualized gross) — the 04.17 gate in miniature.

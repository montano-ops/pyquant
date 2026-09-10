# Day 5 — Errors, Power, Effect Size

## 1. The 2×2 (the most important table in empirical finance)

| | H₀ true (no edge) | H₁ true (real edge) |
|---|---|---|
| **Reject** (trade it) | Type I — false discovery | ✓ power |
| **Fail to reject** (pass) | ✓ | Type II — missed edge |

- **α = P(Type I)**: the significance level (5%, say) — you choose it.
- **Power = 1 − P(Type II)**: probability of catching a real effect —
  you must COMPUTE it, and almost nobody does.

**Finance's asymmetry:** the cost of Type I (fund a null strategy) and
Type II (pass on a real one) are both money, but the *literature* is
asymmetric: unpublished Type IIs are invisible, while published Type Is
are the canon — publication itself is a selection on p-values (the file
drawer; Harvey–Liu–Zhu, week 9).

## 2. Power curves, computed

Power depends on (effect size, noise, n, α, one/two-sided). For the
mean-return test, effect size = SR (annualized), and the curve is one
line of code per SR:

```python
import numpy as np
rng = np.random.default_rng(5)
def power(sr_annual, years, n_per_year=252, alpha=0.05, one_sided=False, reps=2000):
    n = int(years * n_per_year)
    z_crit = 1.645 if one_sided else 1.96
    sr_d = sr_annual / np.sqrt(n_per_year)
    hits = 0
    for _ in range(reps):
        x = rng.normal(sr_d, 1/np.sqrt(n_per_year), n)   # daily SR units, sigma=1
        t = x.mean() * np.sqrt(n)
        hits += (t > z_crit) if one_sided else (abs(t) > z_crit)
    return hits / reps

for years in [1, 5, 10, 25]:
    print(f"SR=0.5, {years:2d}y: power = {power(0.5, years, one_sided=True):.0%}")
```

**The brutal row:** a true Sharpe-0.5 strategy reaches 80% power at
~25 years (one-sided 5%: Φ(SR√Y − 1.645)). At 5 years: ~30%. At 1
year: ~13%. **"We'll run it for a quarter and see" is a sentence
about coin flips, not evidence.** (Day 7's lab builds the full grid by
simulation; two-sided 5% power is lower still — Φ(SR√Y − 1.96) plus
the far tail.)

## 3. Effect size: the third leg everyone forgets

Statistical significance ≠ magnitude. The trio you report for every
claim:

1. **Estimate ± SE** (day 1–2): 6.2bp/day ± 2.9bp.
2. **Significance** (day 3–4): t = 2.1.
3. **Effect size in economic units**: annualized edge 15.7bp — vs
   costs?

**The three-way verdict (course law, now formalized):**

- **Statistical**: is it distinguishable from zero? (t, power, audit.)
- **Economic**: does the magnitude exceed costs, borrows, and the
  opportunity cost of risk? (bp arithmetic.)
- **Tradable**: does it survive YOUR constraints — capacity, drawdown
  tolerance, mandate, crowding?

A strategy can pass all three, exactly one, or none. **Statistically
significant and economically dead** (t=3 on 1bp/day net of 4bp costs)
is the most common published crime; **economic and untradable**
(5bp/day at $50M capacity) is the most common fund graveyard.

## 4. The p-value vs the posterior (Bayes creep)

p = 0.05 feels like "95% real." It is not. With a base rate — what
fraction of tested strategies actually have an edge — Bayes gives:

```python
# P(real | significant): base = P(edge exists), power = P(catch it)
def posterior(base, power_, alpha=0.05):
    return base*power_ / (base*power_ + (1-base)*alpha)

print(f"base 1-in-5, power 80%: P(real|sig) = {posterior(0.2, 0.8):.0%}")
print(f"base 1-in-20, power 80%: P(real|sig) = {posterior(0.05, 0.8):.0%}")
print(f"base 1-in-100, power 80%: P(real|sig) = {posterior(0.01, 0.8):.0%}")
```

**80% → 50% → 14%.** With a 1-in-20 base rate of real edges, a
significant result is a *coin flip* on being real — because the 5%
false-alarm rate applied to the 19-in-20 nulls manufactures almost as
many "discoveries" as the real edges deliver. The significance you
celebrate is discounted by the base rate of real edges among everything
you tried (module 02.3's Bayes, now aimed at publication). Week 9
sharpens this into multiple-testing corrections; module 13 into
deflated Sharpe.

## 5. Designing tests (the proactive use)

Power is not just post-hoc honesty — it *designs* studies:

- Choose the minimum effect you care about (economic floor: costs + 2×
  tracking error, say 4bp/day).
- Choose power (80% standard).
- Solve for n: n = ((z_α + z_β)·σ/δ)² — for δ=4bp, σ=1.1%: n ≈
  ((1.96+0.84)·0.011/0.0004)² ≈ 5,900 days ≈ 23 years.
- **If the required n is unobtainable, the design is dead** — no
  amount of cleverness measures a 4bp edge on 1.1% noise in a decade.
  Either find a bigger effect, cheaper noise (cross-sectional pairing,
  hedging), or don't ask.

## Self-check

1. Power 30% at 5 years (SR 0.5). Your backtest cleared significance at
   year 3. What is the honest update?
2. Effect 4bp/day, t = 4.5 (huge sample), costs 5bp round trip per day.
   Verdict on the three-way test?
3. Why does the file-drawer problem make published significance
   *overstate* real-world significance?

---

**Answers:** (1) Weak evidence: power at 3 years is ≈14% (t-center
0.5·√3 ≈ 0.87, two-sided), so significant early results are dominated
by luck — the likelihood ratio is only 0.14/0.05 ≈ 3:1; combine with a
modest prior of real edges and the posterior barely moves).
The honest update is "promising, underpowered — keep collecting," not
"proven." (2) Statistical: yes. Economic: dead — 4bp gross vs 5bp
costs = −1bp net. Tradable: N/A; the three-way verdict is (✓, ✗, ✗).
Significance without the cost line is the marketing version.
(3) Journals publish significant results; null results sit in drawers.
So the published p-values are a selected sample of the p-value
distribution (module 02.17's 500 gurus, in academic dress) — the
"discovery" is partly the selection, and post-publication replication
failures are the base rate reasserting itself.

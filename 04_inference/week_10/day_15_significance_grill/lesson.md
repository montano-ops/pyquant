# Day 15 — The Significance Grill

## 1. Warm-up retrieval (no notes)

1. Power, effect size, SE: the relation, in symbols.
2. The zoo arithmetic: what is the junk fraction at t = 2 with
   m = 100 candidates?
3. The Bartlett factor for H-day overlapping data.

## 2. The exercise

Three published claims, each reported with a t-statistic. Your job:
**grill each one until it is either smaller, bigger, or more
conditional than the paper's headline says.** The grill has four
questions, in order:

1. **Effect size.** What is the premium in *money units* (bp/year),
   not just t? (t = effect/SE, so SE = effect/t — you can back it out.)
2. **Power.** At this sample size and volatility, what effect could
   the study have *detected* (t ≥ 2 at 80% power)? Is the reported
   effect close to the detection limit — i.e., could a half-size
   effect have been missed?
3. **Multiplicity.** How many sibling hypotheses did the paper (or
   the literature, at publication time) effectively test at the same
   time? What does the family do to the threshold?
4. **Design honesty.** Is the t computed on the right SE (overlap?
   pairing? clustering?)?

**The three claims** (numbers as reported / commonly re-estimated;
use these, not your memory of the papers):

| # | Claim | Design | Reported t | Period | n (obs) |
|---|---|---|---|---|---|
| 1 | Momentum: 12-2 winner–loser spread ≈ +9%/yr | monthly, 5-day holding, overlapping | 3.2 | 1964–1989 | ≈ 300 months |
| 2 | Monday underperforms the other 4 days | daily, contrast test | 2.4 | 1953–1978 | ≈ 1,300 Mondays |
| 3 | Low-beta stocks beat CAPM prediction by ≈ 2%/yr | annual portfolio returns | 2.1 | 1927–1984 | 58 years |

**Deliverable:** the grill table (one row per question per claim) and
a three-paragraph mini-report: which claim survives the grill, which
survives conditionally, which doesn't — and what each would need to
change its status.

## 3. The machinery (all from earlier days)

- SE back-out: SE = effect/t. CI: effect ± 1.96·SE.
- Detectable effect at power 0.8: effect_min = (z_{1−α/2} + z_{0.8})·
  SE ≈ (1.96 + 0.84)·SE = 2.8·SE. (Two-sided, large-n.)
- Multiplicity: expected false positives at threshold c among m
  siblings = m·P(|t| > c); BH/Bonferroni verdicts per 04.11.
- Overlap: claim 1's 5-day monthly-overlapping design carries the
  √H ≈ √5 factor (04.13) — the reported 3.2 already uses the
  overlapping t; the grill asks whether it was *corrected*.

## 4. Python implementation

```python
import numpy as np
from scipy import stats

def grill(effect_bp_yr, t, n, m_siblings, overlap_factor=1.0, periods_yr=None):
    se_monthly = None
    # work in annual: effect is bp/yr; convert to per-obs via n
    se = abs(effect_bp_yr) / t
    ci = (effect_bp_yr - 1.96*se, effect_bp_yr + 1.96*se)
    detectable = 2.8 * se
    eff_t = t / overlap_factor
    p = 2*stats.norm.sf(abs(eff_t))
    exp_fp = m_siblings * p
    return dict(effect=effect_bp_yr, se=se, ci=ci, detectable=detectable,
                eff_t=eff_t, p=p, exp_fp=exp_fp)

g = grill(900, 3.2, 300, m_siblings=100)
print({k: (round(v, 2) if isinstance(v, float) else
           tuple(round(x, 1) for x in v)) for k, v in g.items()})
```

## 5. Reading the grill (what the numbers say)

**Claim 1 (momentum).** SE = 900/3.2 ≈ 281bp/yr → CI ≈ [343, 1457]bp —
wide, but entirely positive. Detectable effect ≈ 787bp: a momentum
edge of ~8%/yr is the floor the study could have seen; half of that
would have been invisible. Overlap: if the 3.2 is uncorrected, the
honest t ≈ 3.2/√5 ≈ 1.4 — the single biggest number in the grill;
JT93's design is exactly what 04.13 quantifies. Multiplicity: at
publication, ~10–20 cross-sectional anomalies were live → expected
false t's ≥ 3.2: 20 × 0.0014 ≈ 0.03 — low. *But* the zoo's growth is
the point: by the time Harvey–Liu–Zhu count it, the family is in the
hundreds, and 300 × 0.0014 ≈ 0.4 — the same t that was fine in 1993
is inside the noise band by 2013. What keeps momentum above the
lottery line: the economic mechanism (slow information diffusion),
the decile's *monotonicity* (evidence beyond one spread), and
replication in later, disjoint samples.

**Claim 2 (Monday).** SE = (Monday mean gap)/2.4 — a ~2bp gap at
t = 2.4 is SE ≈ 0.8bp. Detectable ≈ 2.3bp — the study could see
anything above ~2.3bp/Monday. Multiplicity: 5 days × several
sub-periods is a family ≥ 15 → Bonferroni α ≈ 0.003, t threshold ≈
2.9: **2.4 fails the family test.** And the tradability gate (04.12):
2bp/Monday against a 10bp round trip is dead anyway.

**Claim 3 (low beta).** n = 58 *years* of annual returns: SE =
200/2.1 ≈ 95bp/yr, but annual observations are few and vol is high —
detectable effect ≈ 2.8 × 95 ≈ 266bp/yr: the study could NOT have
reliably detected a 100bp/yr CAPM failure. Power, not effect size,
is the problem: **a non-detect, dressed as a small effect.**
Multiplicity: at publication, the CAPM-tests family was ~5–10
different specifications → m × P(|t|>2.1) ≈ 5–10 × 0.037 ≈
0.2–0.4 false expectations: the result is *inside the family's noise
band.*

## 6. What the grill buys you

The t-stat is one number; the grill returns a **conditional verdict**:
"real, if the SE was overlap-corrected and the family is ≤ 20"
(momentum); "statistically real but economically dead and
family-failed" (Monday); "under-powered to detect — the result
constrains the effect to *above* ~2.7%/yr, it does not establish
~2%" (low beta). Every paper you read from here on gets the grill
applied within a page.

## 7. Research connection

**Harvey, Liu & Zhu (2016)** make the grill systematic: they count the
zoo's growth over time and derive that, by 2013, the t needed to
"survive the grill" for a *new* factor is ≈ 3.0–3.5 (their exact
number depends on the assumed zoo size and correlation of factors).
Their excerpt for today: the t > 3 rule is *the grill compressed into
one number* — effect size is assumed, power is ignored, multiplicity
is absorbed into the threshold. You now know what the compression
throws away.

## 8. Common mistakes

1. **Grilling t while ignoring effect size.** t = 2.1 on a 2%/yr
   effect with 58 years is a different animal than t = 2.1 on a
   0.2%/yr effect with 3,000 days. The grill's first row is always
   money units.
2. **Assuming the paper's SE is the honest SE.** The overlap,
   pairing, and clustering questions (04.8, 04.9, 04.13) come before
   the multiplicity question — a corrected t can move the verdict by
   more than the family can.
3. **Verdict without condition.** "Momentum is real" is the wrong
   sentence; "momentum survives the grill *if* its t is overlap-
   corrected and the decile monotonicity is taken as part of the
   evidence" is the sentence.

## 9. Reflection

- The grill is adversarial by design. What is the *constructive*
  version — the set of results that would make you believe a claim
  you grilled to death? (Replication in a disjoint sample;
  monotonicity across quantiles; a mechanism with a testable
  prediction; cost-survival; pre-registration.)
- HLZ's t > 3 is a single threshold. Your grill is four questions.
  Which is more defensible, and why does the literature converge on
  the simpler one? (Communicability. And: the four questions
  *collapse* to a threshold when you must state them ex ante —
  that is the deflated-Sharpe logic of module 13 arriving early.)

## Self-check

1. A claim: "characteristic X premium 150bp/yr, t = 2.6, n = 1,200
   monthly, family of 30." Grill it in four lines (SE/CI, detectable,
   family, design question).
2. Why does claim 3's verdict ("non-detect") not mean "the effect
   doesn't exist"? State what it *does* establish.

---

**Answers:** (1) SE = 150/2.6 ≈ 58bp/yr → CI [35, 265]bp; detectable
≈ 2.8 × 58 ≈ 162bp — the reported 150bp is *below* the 80%-power
line: a real 150bp effect was detectable only ~65–70% of the time.
Family: 30 siblings → Bonferroni threshold t ≈ 3.08: **fails**
(2.6 < 3.08); expected false t's ≥ 2.6 among 30 pure-noise claims ≈
30 × 0.0093 ≈ 0.28. Design: ask the overlap/clustering question
before believing the 2.6. (2) Power says "if the true effect
were 150bp, this study would have missed it more often than caught
it" — a test that is too weak to see the effect cannot rule the
effect out; it bounds the effect *from below only* in the sense that
effects larger than the detectable threshold *would* have shown. The
honest statement: "consistent with effects from ~0 up to ~400bp/yr."

# Day 13 Review — Week-7 Consolidation

## Cold retrieval (reference answers)

1. Liturgy: structure → headline → shape → moments±SE → QQ → rolling +
   ACF → verdict. (Questions: real? center/width? family? how much
   shape? where does normal die? stable? dependent? what's it like?)
2. Verdict template: "X's daily returns (n, range): mean±SE, SD, skew±,
   kurt±; QQ bends at [location]; vol clusters (stat vs band);
   resembles [family] except [particulars]; [models] disqualified for
   [purpose]."
3. Rolling 63d mean: −0.10%..+0.15%, below zero 25–40% of days —
   consistent with constant-μ noise (SE 0.13%).
4. Explanations: noise / regime drift / time-varying premium —
   indistinguishable at quarterly resolution; don't design edges that
   live inside the band.
5. Annualization: σ√252, from independence; convention not forecast.
6. EWMA(0.94): half-memory ≈ 11 days; +3σ day lifts it ~6%.
7. Vol blind spots: direction, shape (scale≠shape), jumps/overnight.
8. JB = n(ν̂²/6 + κ̂²/24): big-n rejects trivia (κ>0.53 at n=504),
   small-n sleeps through monsters (SE(kurt)=0.63 at n=60).
9. fillna(0) lies "calm"; ffill-levels lie "0% then jump"; dropna on
   panels = intersection calendar (MNAR bias in chaos).
10. Aggregational Gaussianity: κ daily→monthly collapses ~10×; scaling
    risk by √t breaks under fat tails + clustering.

## Interleaved problems (reference answers)

**P1.** SE(ν̂)=√(6/260)=0.152 → −0.3 ± 0.30 (2 SE: no verdict);
SE(κ̂)=√(24/260)=0.304 → 2.1 ± 0.61 (3.5 SE: real). JB = 260(0.09/6 +
4.41/24) = 260(0.015+0.184) = 51.8 >> 5.99 — reject, driven almost
entirely by the kurtosis leg. Next: QQ (where?), tail multiple,
consequence sentence.

**P2.** B's VaR is bigger (fatter left tail at equal σ). Bounds only:
VaR depends on the quantile, which depends on the full shape — two
numbers (σ, κ) don't pin it. You can bound the ratio and simulate
families (t with matched κ), but "by how much" needs the distribution
— the reason QQ plots accompany every kurtosis report.

**P3.** (1) 80% annualized = "if this month lasted a year" — a unit
translation of a 21-day window, not a forecast; (2) the window is one
regime draw, SE ≈ 25%/√42 ≈ 4pp even before the regime moves; (3) the
*loss* depends on the mean and the tail *shape*, not vol alone — and
vol clustering means next month's vol is likely different from this
month's (that way can be *up* — a vol spike predicts elevated vol, not
a return to calm).

**P4.** dropna on 30 stocks: intersection calendar (drops each one's
holidays/halts), MNAR in crises, stale zeros from illiquid names kept
(survivorship's twin), and the 2010–2020 window excludes 2008 — the
sample is "liquid, calm-adjacent, surviving" — every bias pointing the
backtest toward beauty.

**P5.** SE(mean) = σ/√n vs SE(σ) = σ/√(2n): vol estimated √2× more
efficiently — plus vol is *predictable* while the mean wanders.
Factor ≈ √2 in raw efficiency, unboundedly more once predictability
counts. One line: risk is measurable, drift is barely measurable.

## Dress rehearsal check

The 20-minute cold EDA: done? Honest score? Tomorrow is closed-book —
the drill IS the checkpoint.

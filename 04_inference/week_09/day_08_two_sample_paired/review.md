# Day 8 Review — Two-Sample & Paired Tests

## Retrieval (answers)

1. Welch t: (x̄₁−x̄₂)/√(s₁²/n₁ + s₂²/n₂) with W–S df; paired t:
   one-sample t on the matched differences, df = n−1. Matched dates
   (or matched units) → paired; separate samples → Welch.
2. Dividend: sd(d)² = sA²+sB²−2ρsA sB. ρ=0.9, equal SDs → SE 2.2×
   smaller. ρ→1 → dividend →∞ (the difference is almost constant).
   ρ<0 → pairing *costs* (SE grows); no dividend, but the design is
   still correct.
3. Annualizing ×252 scales mean, SE, CI identically — the t-stat is
   unchanged. Unit conversion never manufactures significance.
4. Welch on paired data: conservative (overstates SE) — kills real
   edges. Paired on overlapping series: dangerous (inflates t) — the
   day-04.13 problem.

## Elaboration prompts

- Explain to a junior researcher, without formulas, why "same dates"
  makes the paired SE smaller. (Shared market cancels in the
  subtraction; only the private noise remains.)
- Give an example where pairing is the right design but there is no
  dividend. (Equity strategy vs bond benchmark: same dates, ρ≈0 or
  negative.)
- A paper reports "strategy outperforms benchmark, t = 2.1" with no
  statement of which design. Write the three questions you would email
  the author. (Paired or Welch? Holding period vs sampling frequency?
  Which benchmark, and what's the correlation of the legs?)

## Interleaved problem

Two long-only sector strategies, 750 days, same dates. Each SD 1.1%.
Correlation between them 0.6. Mean A 5.2bp, mean B 4.1bp.
(a) Paired t? (b) Welch t? (c) Which do you believe, and what is the
residual caveat on the one you believe?

<details><summary>Reference answer</summary>

(a) sd(d) = 1.1%·√(2(1−0.6)) = 0.757%; SE = 0.757%/√750 = 2.77bp;
t = 1.1/2.77 = **0.40**. (b) SE = √2·1.1%/√750 = 3.87bp → t = 0.28.
(c) Paired is the correct design (same dates, shared market). Both
say: no detectable difference — a real finding needs the means to be
~5.5bp apart for t=2 at this correlation. Residual caveat: 750 days
of correlated sector returns → clustering; the honest SE is a bit
larger, making the null conclusion *more* secure. Here the direction
matters: when the answer is "nothing", the caveats protect you.
</details>

## Self-grade

- Can you write the Welch–Satterthwaite df formula from memory?
- Did you compute both t's on a real pair and explain the ratio?
- Can you state, in one sentence, why JT93 reports t's on the spread?

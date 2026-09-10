# Day 6 — Review: Days 1–5

Cold retrieval first; then the interleaved set. Commit before checking.

## Cold retrieval

1. Estimator properties: consistency, unbiasedness, efficiency — and
   the MSE ledger that licenses deliberate bias.
2. The difference-of-means SE: independent vs paired — why pairing is
   a gift.
3. The three violations that make finance SEs floors, not ceilings.
4. The CI read correctly (procedure, not probability) — and its dual,
   the significance statement.
5. The p-value defined; the two wrong readings; why p is uniform under
   H₀ (and what that seeds).
6. t = SR_annual·√Y; the years-to-t=2 table; the implied-Sharpe way to
   read any paper's t-stat.
7. The three ways t-tests break on returns (fat tails / clustering /
   autocorrelation) with directions.
8. The 2×2; power as a computed quantity; the design equation
   n = ((z_α+z_β)σ/δ)².
9. The three-way verdict: statistical / economic / tradable.
10. Bayes on significance: P(real | significant) with base rates.

## Interleaved problems

**P1.** Strategy A: 3 years, Sharpe 0.8. Strategy B: 12 years, Sharpe
0.4. Which t-stat is larger? Which evidence do you trust more, and
what's the difference between those two questions?

**P2.** A 95% CI for monthly alpha: [2bp, 38bp]. (a) Significance
statement? (b) The strategy costs 25bp/month. Verdict? (c) What sample
would settle the economic question?

**P3.** Your shop tested 200 signals this year; 14 were significant at
5%; 8 got funded. Under the all-null hypothesis, how many significant
results were expected? What is the minimal honest correction to the
"discovery" rate?

**P4.** Monthly strategy, n=48, fat tails (κ=6). The t-test says
p=0.049. Give the three corrections and their rough sizes.

**P5.** One sentence each: why "fail to reject" ≠ "accept"; why power
belongs in every significance claim; why effect size and significance
are orthogonal.

## Build (15 min)

Blank cell → for a returns series: mean, SE, 95% CI, t-stat, p-value,
and the implied Sharpe with years-to-t=2 — the standard inference
report, cold. This is day 7's lab instrument; bring it sharp.

## Error log

Days 1–5: which idea actually changed how you'll read the next paper
touting significance? Log it with the sentence you'll now always ask.

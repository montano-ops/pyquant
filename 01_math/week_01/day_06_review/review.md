# Review — Week 1 of Module 01

## Cold retrieval (write first, check after)

1. Sample mean and sample variance in Σ notation, with the T−1.
2. The three growth operators (product, log-sum, root) and what each answers.
3. Volatility drag formula + a numeric example at σ = 20% annual.
4. "Mean compounds, volatility scales by √time" — state both annualizations.
5. The derivative as nudge-ratio + two finance aliases.
6. SSE in Σ notation; why squares; why check multiple starting points.

<details><summary>Self-grade</summary>

6/6 → excellent. 4–5 → re-derive the misses today. ≤3 → redo days 1–3
exercises before the mini-project; the toolkit project will expose exactly
these gaps in your code otherwise.

</details>

## Interleaved problems (mixed, on purpose)

1. A fund reports +8% arithmetic annual mean, vol 25%. Estimate its CAGR.
2. $w = (0.6, 0.4)$, daily vols (1.2%, 0.8%), correlation 0.3. Portfolio
   daily vol? (You have the tools; day 10 has the formula — attempt with
   Cov = ρσ₁σ₂ and $\sqrt{w^\top\Sigma w}$ intuition.)
3. Your SSE minimizer returns (a, b) = (0.001, 1.2). Interpret both numbers
   if y = XLE's daily return and x = SPY's.

<details><summary>Answers</summary>

1. ≈ 8% − 0.25²/2 = 8% − 3.1% ≈ 4.9% CAGR.
2. Cov = 0.3·0.012·0.008; var_p = 0.6²·0.012² + 0.4²·0.008² +
   2·0.6·0.4·cov → vol ≈ 0.93%.
3. XLE on an average day earns +0.1% independent of the market (intercept);
   each 1% SPY day maps to +1.2% XLE (slope, beta-shaped).

</details>

## Systems check

- [ ] Error log triaged; anything unexplained → question list for tomorrow.
- [ ] Notation cheat-sheet compared to concepts/notation.md; misses scheduled.

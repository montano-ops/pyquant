# The 12-Step Paper Workflow

Every paper in this course is worked through the same 12 steps. The steps are
deliberately ordered so that **understanding precedes reproduction** and
**reproduction precedes criticism**. Print the worksheet
([templates/paper_worksheet.md](templates/paper_worksheet.md)) and fill it in
as you go — by module 07 you do this from habit, and by capstone 6 you do it
to your own research.

| Step | Question you must answer | Output |
|---|---|---|
| **1. Research question** | What are the authors trying to discover? | One sentence |
| **2. Economic intuition** | *Why* might the effect exist? Who is on the other side of the trade, and why are they willing to lose? | A paragraph; if you cannot tell the story, flag it |
| **3. Hypothesis** | What *exactly* is tested? What is the null? | H₀ and H₁ in writing |
| **4. Data** | Universe, frequency, period, variables, filters, sources | A data spec table |
| **5. Methodology** | Translate every equation into plain English, then pseudocode | Annotated equations |
| **6. Reproduction** | Implement the methodology in Python | Code + intermediate checks |
| **7. Results** | Reproduce the key tables/figures where feasible | Your table vs theirs, side by side |
| **8. Strategy** | Convert the result into a trading strategy (universe, signal, weights, rebalancing) | A strategy card |
| **9. Backtest** | Test with appropriate methodology: costs, turnover, realistic execution | Net performance |
| **10. Robustness** | Challenge the result: subsamples, parameters, placebo, OOS | A robustness table |
| **11. Critique** | What could explain this result *other than* the hypothesis? | Alternative explanations list |
| **12. Extension** | Change one thing; does the conclusion survive? | One honest experiment |

## Reading order for a paper (first pass, ~45 minutes)

1. Abstract — what's claimed?
2. Introduction, last paragraph — what did they actually find?
3. Tables — where the evidence lives. Read the *variable definitions* first.
4. Conclusion.
5. Only now: the methodology section, equation by equation.

You are reading to fill steps 1–5, not to be impressed. Two questions
constantly: *what would have to be true for this table to be wrong?* and
*how much money could this actually make after costs?*

## Reproduction honesty rules

- **You will not match published numbers exactly.** Free data ≠ CRSP; periods
  differ; universes differ. What you should reproduce is the *shape*: sign,
  rough magnitude, monotonicity across sorts, and statistical pattern.
- **Document every deviation** (universe, period, weights, filters) in the
  worksheet — deviations are findings, not failures.
- **Bias audit is part of reproduction.** State explicitly how survivorship,
  look-ahead, or point-in-time issues push your numbers relative to the
  paper's.

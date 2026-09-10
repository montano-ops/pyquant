# Review — Functions & Linearity

## Retrieval

1. In $y = a + bx$: give two finance names for b, two for a.
2. Write the P&L function of shorting 200 shares at $40. What is its slope — and its risk asymmetry?
3. Why is a portfolio of linear payoffs still linear? What breaks linearity (two examples)?

<details><summary>Answers</summary>

1. b: beta, exposure, loading, delta, hedge ratio. a: alpha, intercept, baseline, abnormal return.
2. P&L(x) = 200(40 − x) = −200x + 8000; slope −200; losses unbounded because x has no ceiling.
3. Sums of linear functions are linear. Broken by: compounding, fees with
   hurdles (max(·,0)), option payoffs, borrowing constraints.

</details>

## Elaboration

- "Controlling for market exposure means removing $b\cdot x$ from $y$."
  Restate this in your own words and say what the leftover ($a$, roughly) is
  called in research.

## Spaced repetition

- The slope/intercept → beta/alpha mapping returns in module 06.7 and 07.2;
  re-derive the market-model equation from memory then.

# Review — Mini-Project: Return Arithmetic

## Retrieval (about your own toolkit)

1. Which of your functions would break on a Series containing a −101% return, and how?
2. Why must `cagr` use the geometric mean? What does `mean * 252` actually estimate?
3. Your Q2 "frequency illusion": which number was honest growth, and what
   was the other one a *statement about*?

<details><summary>Notes</summary>

1. `to_log`/`to_simple` on simple returns ≤ −100%: log undefined — your
   function should fail loudly, not silently (an impossible return in data
   is a data error: module 05).
2. `mean*252` = the arithmetic expectation of annual return under
   i.i.d.-ish sampling — a *statistical* object; CAGR is the *growth*
   object. Both valid, different questions.
3. Compounding monthly returns = growth; annualizing the daily mean =
   expectation. Investors receive growth.

</details>

## Elaboration

- Where in a *published backtest* would each of your three traps appear?
  Write one sentence per trap naming the table it corrupts.

## Spaced repetition

- Your toolkit functions are permanent course assets: module 02's Sharpe
  exercises will import them. Re-test them cold at +1 week.

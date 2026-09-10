# Day 3 — Anatomy of a Research Paper

## Warm-up retrieval (no notes)

1. What is the difference between an inner and outer join, and which is
   dangerous for pairwise statistics?
2. Resample-then-return vs return-then-resample: which compounds?
3. What is look-ahead bias, in one sentence?

## 1. Why you're reading a paper on day 3

Because papers are what you're training for, and dissecting them is a
separate skill from statistics — one you can start today. You will not
understand JT93's methodology yet. That's expected and fine. Today you learn
to *map* a paper: what it wants, what it did, what it measured. The 12-step
workflow below is the map you'll use on every paper in this course.

## 2. The 12-step workflow (memorize the shape, not the words)

1. **Research question** — what are the authors trying to discover?
2. **Economic intuition** — why might the effect exist? who's on the other side?
3. **Hypothesis** — what exactly is tested; the null and alternative.
4. **Data** — universe, frequency, period, variables, filters, sources.
5. **Methodology** — equations translated to plain English, then pseudocode.
6. **Reproduction** — implement it.
7. **Results** — reproduce the key tables/figures.
8. **Strategy** — convert the finding into a trading strategy.
9. **Backtest** — with costs and realistic execution.
10. **Robustness** — challenge the result.
11. **Critique** — what else could explain it?
12. **Extension** — change one thing; does it survive?

Today you do steps 1–4 only. Steps 5–7 arrive module by module (regression in
06, portfolio construction in 07), and by module 07 you complete all 12 on
this very paper.

## 3. The sections of an empirical paper, and how to read them

Read in this order — **not** front to back:

1. **Abstract** — the claim. (2 minutes)
2. **Introduction, final paragraphs** — what was actually found. (5 minutes)
3. **Tables** — where the evidence lives. Read variable definitions before
   numbers; find the t-statistics; find the star of the show (usually one
   table the abstract refers to).
4. **Data section** — universe, period, filters. This is where reproduction
   succeeds or dies.
5. **Methodology** — only now, equation by equation.

Two questions running constantly: *what would have to be true for this table
to be wrong?* and *how much money is this after costs?*

## 4. The specimen: Jegadeesh & Titman (1993)

> Jegadeesh, N., and S. Titman (1993), "Returns to Buying Winners and Selling
> Losers: Implications for Stock Market Efficiency", *Journal of Finance* 48(1).
> Find it via DOI 10.1111/j.1540-6261.1993.tb04702.x, SSRN, or a library.

The abstract, in compressed form (paraphrased): *this paper examines a
relative-strength strategy — buy stocks with high returns over the past 3–12
months and sell stocks with low returns over the same period — and finds it
produces profits of about 1% per month over 1965–1989.*

**Step 1 — Research question.** Do past returns predict future returns
in the medium term (months), contradicting market efficiency?

**Step 2 — Economic intuition.** Why might winners keep winning for months?
Candidate stories (the paper can't fully distinguish them — note that for
later): investor under-reaction to news; slow diffusion of information;
institutional herding. And the other side of the trade: who loses? Investors
selling winners too early and holding losers too long (disposition effect),
or funds constrained from chasing. Notice: intuition is *a story about human
or institutional behavior*, not an equation. If no story exists, be suspicious.

**Step 3 — Hypothesis.** H₀: past 6–12 month returns carry no information
about future 3–12 month returns (no predictability). H₁: they do. Note what
is NOT tested: whether the effect is tradable after costs (that's our step
9), or why it exists (step 11).

**Step 4 — Data.** From the paper (read this section yourself):

| Item | JT93 |
|---|---|
| Universe | NYSE and AMEX common stocks (US) |
| Period | January 1965 – December 1989 |
| Frequency | monthly returns |
| Source | CRSP (the standard academic US database) |
| Filters | minimum price and data-history requirements to ensure tradability |
| Key variable | cumulative return over months t−12 to t−2 ("6/12-month formation") |

**The construction, in plain English:** each month, rank all stocks by their
past return measured from 12 months ago to 2 months ago (skipping the most
recent month — you'll learn exactly why in module 07). Buy the top decile,
sell the bottom decile, hold for 3–12 months with overlapping portfolios.
The headline: the winner-minus-loser spread earns roughly 1% per month, with
t-statistics well above 2.

**What you are NOT doing today:** implementing any of this. You are learning
to extract the skeleton.

## 5. Reading tables like a researcher

A typical results table in this literature has: portfolios sorted by some
characteristic (rows: decile 1…10), average returns per portfolio, maybe
"high minus low" spreads, and t-statistics in parentheses. Stars (\*, \*\*,
\*\*\*) usually mean p < 0.1, 0.05, 0.01 (check the table notes — conventions
vary). Two habits:

- Find the *monotonicity*: do returns rise smoothly across the sort? A spread
  driven by one extreme portfolio is more fragile than a smooth gradient.
- Find the t-stat of the spread, not just its size. A 1%/month spread with
  t = 4 is a fact; with t = 1.2 it's a coin flip wearing a suit. (What a
  t-statistic *is*: module 04. You only need its role today: evidence
  strength.)

## 6. Common mistakes

- Reading papers front-to-back and drowning in the methodology before knowing
  the claim.
- Confusing "the paper shows past returns predict future returns" with "you
  can trade this" — steps 8–9 are where trading begins, and costs are where
  naive implementations die.
- Skipping the data section. The most common reproduction failure is a
  different universe or period, not a wrong equation.

## 7. Reflection

1. Write the JT93 skeleton from memory: question, intuition, H₀, data
   (universe/period/frequency), construction.
2. What in the paper could you already reproduce with what you know? What
   would you need to learn? (This gap list is literally the course syllabus —
   look at the ROADMAP and compare.)

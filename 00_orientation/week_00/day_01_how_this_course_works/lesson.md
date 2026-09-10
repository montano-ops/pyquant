# Day 1 — How This Course Works

## 1. What this course is

An apprenticeship in quantitative research. You will spend most of your time
solving problems, writing Python, analyzing financial data, reproducing
papers, debugging research, and challenging hypotheses — not reading
explanations. Explanations exist here only when a research problem demands
them.

The course is built around one pipeline, and every concept you meet travels
it fully:

```
Concept → Intuition → small exercise → Python → financial data
        → research paper → strategy → backtest → statistical evaluation
        → reflection
```

Papers appear from day 3 and never stop. You will read Jegadeesh & Titman
(1993) *before* you know what a variance is — because learning to dissect
papers is a skill, separate from statistics, and it starts now. Statistics
then arrives on a need-to-know basis: you learn standard errors because the
paper's t-statistics demand them, GARCH because a volatility paper demands
it, cointegration because pairs trading demands it.

## 2. The rules of engagement

These five rules are the pedagogy. Breaking them converts the course into
reading, and reading doesn't build skill.

1. **Attempt before solution.** Every day: `exercise.ipynb` (no answers) then
   `solution.ipynb`. You open the solution only after a genuine attempt — or
   after writing down precisely where you got stuck. Struggle is the point:
   it is what makes the solution stick.
2. **Retrieval without notes.** Lessons open with warm-up questions from
   previous days. Answer from memory. If you fail, that's information:
   re-derive, don't reread.
3. **Spaced repetition.** `review.md` schedules when to revisit concepts.
   Concepts deliberately recur across modules — variance returns as portfolio
   risk, then Sharpe, then factor variance, then volatility forecasting.
   Each return deepens it.
4. **Research log.** From your first mini-project: every decision made
   *after* seeing a result gets a dated entry. This is the paper trail that
   separates honest research from data snooping, and it starts today.
5. **"How could this be wrong?"** The course's most-repeated question. Every
   analysis ends with it.

## 3. How a day runs

| Step | Time | What |
|---|---|---|
| 1 | 5 min | Open the day's README (objective, self-check) |
| 2 | 10 min | Warm-up retrieval from prior days — no notes |
| 3 | 20–30 min | Read `lesson.md` actively: re-derive, don't just read |
| 4 | 45–75 min | `exercise.ipynb` — attempt everything before hints |
| 5 | 15 min | Compare with `solution.ipynb`; log mistakes in your error log |
| 6 | 10 min | `review.md` — schedule today's concepts for spaced repetition |

Stuck? The 15-minute rule: struggle for 15 minutes, then take the first hint
(hints are ordered, at the bottom of the exercise notebook). Still stuck after
two hints? Read the solution, close it, and re-derive from memory. "I followed
the solution" is not learning — "I reproduced it without looking" is.

## 4. The difficulty ladder (where you're headed)

```
Understand → Calculate → Code → Apply to data → Interpret
   → Reproduce research → Critique research → Modify research
      → Design research → Conduct independent research
```

Nothing in this course jumps more than one rung at a time. Module 00 gets you
to "apply to data". Modules 01–04 build the statistics underneath
"reproduce". By module 13 you critique; by capstone 6 you conduct.

## 5. Set up your environment (do this now, verify in the exercise)

```bash
cd pyquant
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e .           # installs the qrc package
python -m pytest tests -q  # must pass
```

Two things to know about `qrc` (the course's only library):

- It contains **data utilities only** — downloads, caching, synthetic data.
  It deliberately has no statistics and no backtester. You build those.
- `get_prices(["SPY"], start="2015-01-01")` downloads from Yahoo Finance once
  and caches to `data/cache/`. Offline? `synthetic_prices()` generates seeded,
  realistic simulated prices (fat tails, volatility clustering — you'll learn
  what those mean soon, then find them in your data).

## 6. What this course expects from you

- ~90–150 minutes, 6 days a week, for ~46 weeks (accelerate at your peril —
  spacing is part of the method).
- Honest self-assessment. The tracker (`PROGRESS.md`) is private to you; lying
  to it only wastes your own months.
- Comfort with being wrong in writing. Your error log will become the most
  valuable file in this repository.

## 7. Reflection (write answers in your log)

1. Which of the five rules will be hardest for you, and why?
2. What is your honest goal in 12 months — reading papers? trading your own
   strategies? a research role? Write it down; future-you will grade it.

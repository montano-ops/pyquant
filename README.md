# PyQuant — A Paper-Driven Quantitative Trading Research Course

**An apprenticeship in quantitative research, structured as a repository.** You
learn statistics, econometrics, and asset pricing *because the next research
paper demands them* — then you reproduce the paper, build the strategy,
backtest it honestly, and try to break the result.

**End state:** hand this course's graduate a paper claiming *"characteristic X
predicts stock returns"* and they can work through: research question →
economic hypothesis → methodology → data construction → Python implementation →
empirical reproduction → portfolio → backtest → costs → out-of-sample →
robustness → bias investigation → critical evaluation → extension.

---

## Who this is for

You are ready for this course if you can check these boxes:

- [ ] You can write Python and you are **genuinely fluent in pandas** —
      DataFrames, indexing, groupby, merge/join, resample, rolling windows,
      vectorized operations, time-indexed data. (We will *not* teach pandas.
      We will *test* your pandas where it matters for research.)
- [ ] You have minimal formal statistics/probability. That's fine — that's the
      main thing we build.
- [ ] You are interested in quantitative/systematic trading and want to learn
      by implementing and testing ideas from academic research.

You do NOT need: university statistics, econometrics, calculus, linear
algebra, quantitative finance background, or research experience. Each is
taught when a research problem requires it.

## The core method

Every concept travels the full pipeline:

```
Concept → Intuition → small exercise → Python implementation → financial data
        → research paper → strategy implementation → backtest → statistical
        evaluation → reflection
```

and every concept has to answer: **"why would a quantitative researcher need
this?"** If it can't, it isn't in the course.

**Papers do not come at the end.** They appear on day 3 (you *read*
Jegadeesh & Titman 1993 in orientation, before you know any statistics), then
recur in every module — first dissected, then partially reproduced, then fully
reproduced and extended. Statistics is learned *because the next paper needs
it*. The full progression: [docs/PAPERS.md](docs/PAPERS.md).

### The rules of engagement (these are the pedagogy)

1. **Attempt before you look.** Every day has `exercise.ipynb` (no answers) and
   `solution.ipynb`. You open the solution only after a genuine attempt — or
   after writing down exactly where you got stuck.
2. **Retrieval without notes.** Lessons open with warm-up recall questions.
   Review days forbid notes. If you can't retrieve it, you don't know it yet.
3. **Spaced repetition.** Each `review.md` schedules when to revisit concepts.
   Concepts deliberately *return* across modules (mean/variance → portfolio
   risk → Sharpe → factor research → volatility modelling → evaluation).
4. **Keep a research log.** From the first mini-project: every decision you
   make *after* seeing a result gets a dated entry. This is the paper trail
   that separates research from data snooping.
5. **Bias audits, always.** Every project ends with "how could this be wrong?"
   — the course's most-repeated question.
6. **Explain it in your own words.** Key concepts ask you to explain without
   the formula, explain why it matters for trading, and give an example of how
   ignoring it produces a false trading conclusion.

### Exercise levels (used everywhere)

L1 recall → L2 conceptual → L3 calculate by hand → L4 Python → L5 financial
data → L6 research interpretation → L7 critical thinking → L8 independent
research. Early days use L1–L4; by mid-course everything is L5–L8.

## Repository map

```
README.md          you are here
ROADMAP.md         the complete curriculum: every module, week, day, paper
PROGRESS.md        your tracker (mark days, log study time, spaced reviews)
AUTHORING.md       the standard used to author lessons (also: teach-it-back)
docs/              paper index, the 12-step paper workflow
templates/         paper worksheet, research report template
qrc/               data utilities ONLY (no stats, no backtester — those are yours to build)
data/              download scripts + cache (gitignored)
tools/             notebook generator + test runner (+ sources under tools/nbsrc/)
00_orientation/ … 15_derivatives/    the modules
projects/          six capstones (momentum, reversal, factors, pairs, vol, original research)
```

Inside every authored module: `concepts/` (reference sheets), `week_XX/day_XX_topic/`
with `README.md · lesson.md · exercise.ipynb · solution.ipynb · review.md`,
and `review/` for module checkpoints.

## Getting started (15 minutes)

```bash
git clone <this repo> && cd pyquant
python -m venv .venv && source .venv/bin/activate    # or conda
pip install -r requirements.txt
pip install -e .                                     # installs the `qrc` package
python -m pytest tests -q                            # should pass: 8 passed
```

Then start: **[00_orientation/week_00/day_01_how_this_course_works/](00_orientation/week_00/day_01_how_this_course_works/)**

Data: first use of each ticker downloads from Yahoo Finance and caches to
`data/cache/` (parquet). Offline? Every notebook has a
`DATA_SOURCE = "synthetic"` switch — simulated series with realistic fat
tails and volatility clustering, seeded and deterministic. See
[data/README.md](data/README.md) for the honest list of what free data can and
cannot support.

## Time commitment

46 weeks × 6 days × 90–150 min (sustainable) ≈ 11 months; ~6 months at an
intensive pace. Capstones run alongside. The [ROADMAP](ROADMAP.md) is the
source of truth for sequencing.

## The standards you will internalize

- **Paper workflow** — 12 steps from research question to extension:
  [docs/paper_workflow.md](docs/paper_workflow.md)
- **Research notebooks** — the 9-notebook project structure (question → data →
  exploration → methodology → model → backtest → robustness → results →
  conclusion), with exploration strictly separated from confirmation:
  [projects/README.md](projects/README.md)
- **Research reports** — the 15-section write-up every capstone ends with:
  [templates/research_report.md](templates/research_report.md)

## Research quality creed

> A profitable backtest is not automatically evidence of a valid strategy.

Every strategy you build gets evaluated for statistical significance, economic
significance *after costs*, robustness, turnover, liquidity, capacity,
drawdown, regime dependence, out-of-sample performance, data quality, bias,
multiple testing, and reproducibility. You will learn to distrust unexplained
exceptional backtests — including, and especially, your own.

## What this course is not

- Not a generic statistics course (statistics serves the research pipeline).
- Not a pandas tutorial (you already know pandas).
- Not a black-box backtesting framework course (you build the engine yourself).
- Not a deep-learning course (ML arrives in week 40, after you can resist it).
- Not a signal factory (the goal is *judgment*, not a pile of strategies).

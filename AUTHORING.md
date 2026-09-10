# AUTHORING — The Lesson Standard

This document defines the standard every day of the course is authored to. It
serves three audiences:

1. **Maintainers** — day-level content for modules 06–15 is authored
   progressively, to this standard (see status in [ROADMAP.md](ROADMAP.md)).
2. **Learners** — the best-documented way to master a concept is to author a
   lesson for it ("teach it back"). Writing a day to this standard is the
   course's L8 exercise, and a submitted lesson that meets the checklist below
   *is* the checkpoint for that concept.
3. **Reviewers** — use the quality checklist at the bottom.

## File structure per day

```
<module>/week_XX/day_XX_topic/
├── README.md          # the day card (see below)
├── lesson.md          # the teaching content (see template)
├── exercise.ipynb     # problems, no answers; progressive hints at the bottom
├── solution.ipynb     # worked solutions + expected reasoning + common mistakes
└── review.md          # retrieval questions (answers in <details>), elaboration
                        # prompts, spaced-repetition scheduling
```

Notebooks are **generated** from lightweight sources under
`tools/nbsrc/` (mirroring the course tree) with `python tools/nbgen.py`.
Edit the `.mdnb` source, regenerate, commit both. In a `.mdnb` file, text is
markdown; ```python fences become code cells; ```py fences stay markdown.

## Day card (`README.md`) template

```markdown
# Day N — <Title>

**Module:** · **Week:** · **Time:** ~90–150 min
**Objective:** by the end of today you can <observable capability>.
**Prerequisites:** <module.day references>
**Files:** lesson.md → exercise.ipynb (attempt first!) → solution.ipynb → review.md
**Research connection:** <where this appears in real papers>
**Self-check:** <one question you should answer without notes>
```

## `lesson.md` template

Ordered sections — intuition ALWAYS before formulas:

1. **Warm-up retrieval** — 2–4 questions from previous days, answered without
   notes (answers: previous days' `review.md`).
2. **Why a quant needs this** — the research problem that demands the concept.
3. **Intuition** — plain English, analogy, a tiny numeric example by hand.
4. **The mathematics** — the formula, now that it means something; notation
   consistent with `concepts/notation.md`.
5. **Python implementation** — minimal, runnable; faded example style
   (work it fully, then leave gaps in later lessons).
6. **On real data** — a quick application with `qrc.data`.
7. **Research connection** — the specific paper/table/equation where this
   appears, stated precisely.
8. **Common mistakes** — the two or three ways learners actually get this
   wrong, especially any that produce a false trading conclusion.
9. **Reflection** — what assumption does this make? how could it mislead?
   what would you test next?

## `exercise.ipynb` rules

- **Never reveals the answer.** Problems with `# YOUR CODE HERE` markers;
  assertions or printed checks where possible so learners can self-verify.
- **Levels labelled** (L1–L8, see README). A typical day: 2 warm-up retrieval,
  2–3 core problems spanning levels, 1 stretch.
- **Progressive hints** in a final section, ordered, each more specific.
- **Generation before solution**: at least one problem asks the learner to
  *attempt the formula / the code / the interpretation* before any scaffold.
- Setup cell (first code cell, standardized):

```python
import os, sys, pathlib
root = pathlib.Path.cwd()
for _ in range(6):
    if (root / "qrc").is_dir():
        break
    root = root.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 4)

# 'real' downloads from Yahoo (needs internet, cached afterwards);
# 'synthetic' uses seeded simulated data with fat tails + vol clustering.
DATA_SOURCE = os.environ.get("QRC_DATA", "real")
```

## `solution.ipynb` rules

Every solved exercise includes, in this order: **expected reasoning** (how a
researcher thinks about it), **the code**, **the result & interpretation**,
and **common mistakes** (what goes wrong, why it's tempting, what it costs).
Solutions must run top-to-bottom in both `real` and `synthetic` modes
(`QRC_DATA=synthetic python tools/run_notebooks.py <nb>` to verify).

## `review.md` rules

- 5–10 retrieval questions, answers inside `<details><summary>…</summary>`
  blocks so the page doesn't leak answers.
- At least one elaboration prompt per key concept: "explain without the
  formula", "explain why this matters for trading", "give an example of how
  ignoring it produces a false trading conclusion".
- A spaced-repetition line: what to revisit, when, and how (re-derive,
  re-implement from scratch, or self-quiz).

## Mini-project and checkpoint days

Day 07 of each week (and module `review/` checkpoints) follow the research
pattern in miniature: question → data → method → result → interpretation →
*how could this be wrong?* Checkpoints are designed to be completed
**without step-by-step instructions**; the rubric is published up front.

## Quality checklist (a day is done when…)

- [ ] The lesson answers "why would a researcher need this?" concretely.
- [ ] Intuition precedes every formula.
- [ ] The learner writes code; no exercise is copy-paste-only.
- [ ] At least one exercise uses real (or realistically synthetic) data.
- [ ] The exercise notebook contains zero answers.
- [ ] Solutions include expected reasoning and common mistakes.
- [ ] Retrieval questions reference prior days (spacing), and today's concepts
      are added to the spaced schedule.
- [ ] The research connection cites a specific paper/section/table.
- [ ] Both notebooks execute cleanly: `QRC_DATA=synthetic python
      tools/run_notebooks.py <exercise-and-solution>`.
- [ ] A "how could this be wrong?" element is present.

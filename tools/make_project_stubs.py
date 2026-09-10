#!/usr/bin/env python3
"""Generate the standard 9-notebook research scaffold for a capstone project.

Every capstone uses the same notebook sequence (see projects/README.md), so
this script stamps out the skeleton with the project's title, source paper,
and module prerequisites filled in. You then work inside the notebooks.

Usage: python tools/make_project_stubs.py   (regenerates all project stubs)
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.nbgen import build_notebook  # noqa: E402

PROJECTS = {
    "01_momentum": {
        "title": "Capstone 1 — Momentum",
        "paper": "Jegadeesh & Titman (1993), *Returns to Buying Winners and Selling Losers*, Journal of Finance",
        "prereq": "Modules 05 (financial data), 07 (asset pricing), 12 (backtesting), 13 (validation)",
    },
    "02_reversal": {
        "title": "Capstone 2 — Short-Term Reversal",
        "paper": "Jegadeesh (1990), Lehmann (1990) — weekly/monthly reversal studies",
        "prereq": "Modules 05, 10 (strategy research), 12, 13",
    },
    "03_factor_model": {
        "title": "Capstone 3 — Factor Research",
        "paper": "Fama & French (1993); Carhart (1997); Fama & French (2015) as comparison points",
        "prereq": "Modules 05, 06 (regression), 07, 13",
    },
    "04_pairs_trading": {
        "title": "Capstone 4 — Statistical Arbitrage / Pairs Trading",
        "paper": "Gatev, Goetzmann & Rouwenhorst (2006), *Pairs trading: Performance of a relative-value arbitrage rule*, RFS",
        "prereq": "Modules 08 (time series), 09 (econometrics: cointegration), 12, 13",
    },
    "05_volatility": {
        "title": "Capstone 5 — Volatility",
        "paper": "Moreira & Muir (2017), *Volatility-Managed Portfolios*, Journal of Finance (or a GARCH forecasting comparison, your choice)",
        "prereq": "Modules 08, 09 (GARCH), 12, 13",
    },
    "06_original_research": {
        "title": "Capstone 6 — Original Research",
        "paper": "A paper *you* choose (or an original hypothesis of your own)",
        "prereq": "All modules + at least one prior capstone",
    },
}

NOTEBOOKS = [
    ("01_question", "Question & hypothesis",
     "State the research question, the economic hypothesis, and the null you will test. "
     "Write it BEFORE looking at results — this notebook is your pre-registration."),
    ("02_data", "Data",
     "Universe, frequency, period, sources, filters. Document every cleaning decision. "
     "Flag survivorship/selection issues here, before they hide in the code."),
    ("03_exploration", "Exploration",
     "Exploratory analysis. Clearly labelled as EXPLORATION — anything you learn here "
     "must later survive confirmation on untouched data."),
    ("04_methodology", "Methodology",
     "Translate the paper's methodology into plain English, then into pseudocode, then "
     "into Python. Show the mapping: equation -> code line."),
    ("05_model", "Model / signal construction",
     "Build the signal or model. Keep parameters explicit and centralized so "
     "sensitivity tests (07) are possible."),
    ("06_backtest", "Backtest",
     "Positions, portfolio returns, transaction costs, turnover. State every execution "
     "assumption. No peeking at results to tune the strategy — use 07 for that, explicitly."),
    ("07_robustness", "Robustness",
     "Out-of-sample, walk-forward, parameter sensitivity, subsamples, cost sensitivity, "
     "placebo tests, multiple-testing awareness (deflated Sharpe where relevant)."),
    ("08_results", "Results",
     "Final tables and figures: performance metrics, statistical significance, economic "
     "significance after costs. Separate exploration from confirmation."),
    ("09_conclusion", "Conclusion & report",
     "What did you establish? What survives? What could explain the result other than "
     "your hypothesis? Limitations, biases, further research. Then write REPORT.md from this."),
]

SETUP_CELL = """import os, sys, pathlib
# make `qrc` importable no matter where the notebook kernel was started
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
pd.set_option("display.float_format", lambda x: f"{x:,.4f}")

DATA_SOURCE = os.environ.get("QRC_DATA", "real")  # 'real' or 'synthetic' (offline)

print("project scaffold ready")"""


def main() -> int:
    n = 0
    for slug, meta in PROJECTS.items():
        for stem, short, long_desc in NOTEBOOKS:
            text = f"""# {meta['title']} — {short}

**Source paper:** {meta['paper']}

**Prerequisites:** {meta['prereq']}

{long_desc}

> Research standard: keep `RESEARCH_LOG.md` (in this folder) up to date as you go.
> Every decision you make after seeing a result gets a dated entry — that is the
> paper trail that separates honest research from data snooping.
"""
            if stem in ("02_data", "03_exploration", "06_backtest"):
                text += "\n```python\n" + SETUP_CELL + "\n```\n"
            else:
                text += "\n```python\nimport numpy as np\nimport pandas as pd\n```\n"
            out = REPO_ROOT / "projects" / slug / f"{stem}.ipynb"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(__import__("json").dumps(build_notebook(text), indent=1) + "\n")
            n += 1
    print(f"make_project_stubs: wrote {n} notebooks across {len(PROJECTS)} projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

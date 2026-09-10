"""qrc — data utilities for the paper-driven quant research course.

Scope policy (important):
    qrc contains ONLY data plumbing (downloading, caching, synthetic data,
    universe lists). Every statistical, backtesting, or signal computation
    in this course is something YOU implement in the lessons. If qrc ever
    grows a backtester, something has gone wrong.

Typical use:

    from qrc.data import get_prices, get_ff
    from qrc.synth import synthetic_prices
    from qrc.universe import load_universe

    px = get_prices(["SPY", "TLT", "GLD"], start="2010-01-01")   # needs internet once
    px = synthetic_prices(n_days=1500, n_assets=3, seed=7)       # always works
"""

__version__ = "0.1.0"

from . import data, synth, universe  # noqa: F401

__all__ = ["data", "synth", "universe", "__version__"]

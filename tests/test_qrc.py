"""Tests for the qrc package and tooling.

Run with:  pytest tests -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from qrc import synth, universe  # noqa: E402
from qrc.data import _parse_ff_text  # noqa: E402


def test_synthetic_returns_deterministic():
    a = synth.synthetic_returns(n_days=200, n_assets=3, seed=42)
    b = synth.synthetic_returns(n_days=200, n_assets=3, seed=42)
    pd.testing.assert_frame_equal(a, b)


def test_synthetic_returns_shape_and_properties():
    r = synth.synthetic_returns(n_days=1000, n_assets=4, seed=1, drift_spread=0.0005)
    assert r.shape == (1000, 4)
    assert list(r.columns) == ["S0", "S1", "S2", "S3"]
    # drift_spread -> S3 should have higher mean log return than S0
    assert r["S3"].mean() > r["S0"].mean()

    # vol clustering is easiest to see with gaussian innovations (the lag-1 ACF
    # estimator of squared t-noise is itself heavy tailed — a course lesson!)
    from scipy import stats

    g = synth.synthetic_returns(n_days=2000, n_assets=1, seed=11, fat_tails=False)
    assert (g["S0"] ** 2).autocorr(1) > 0.10
    # gaussian + vol clustering already yields excess kurtosis (mixture effect),
    # but t innovations must add clearly MORE tail weight:
    t = synth.synthetic_returns(n_days=2000, n_assets=1, seed=11, fat_tails=True)
    assert stats.kurtosis(t["S0"]) > stats.kurtosis(g["S0"]) + 2.0
    assert stats.kurtosis(t["S0"]) > 6.0  # clearly heavy tailed


def test_synthetic_prices_positive():
    px = synth.synthetic_prices(n_days=500, n_assets=2, seed=3)
    assert (px > 0).all().all()
    assert px.index.is_monotonic_increasing


def test_universes():
    assert len(universe.load_universe("core_etfs")) == 12
    assert len(universe.load_universe("research50")) == 50
    assert len(universe.load_universe("delisted_demo")) >= 5
    with pytest.raises(ValueError):
        universe.load_universe("nope")


def test_parse_ff_text_daily():
    text = (
        "Some header junk\n"
        "annual returns blah\n"
        ",\n"
        "  Mkt-RF   SMB   HML   RF\n"
        "19260701    0.10  -0.20   0.30  0.001\n"
        "19260702   -0.50   0.30  -0.10  0.001\n"
        "\n"
        "  Copyright Kenneth R. French\n"
    )
    df = _parse_ff_text(text, "F-F_Research_Data_Factors_daily")
    assert list(df.columns) == ["Mkt-RF", "SMB", "HML", "RF"]
    assert len(df) == 2
    assert df.index[0] == pd.Timestamp("1926-07-01")
    assert df["Mkt-RF"].iloc[1] == -0.50


def test_parse_ff_text_monthly():
    text = (
        "junk\n"
        "  Mkt-RF   SMB   HML   RF\n"
        "192607    0.10  -0.20   0.30  0.001\n"
        "192608   -0.50   0.30  -0.10  0.001\n"
        "\n"
        "footer\n"
    )
    df = _parse_ff_text(text, "F-F_Research_Data_Factors")
    assert len(df) == 2
    assert df.index[0] == pd.Timestamp("1926-07-01")


def test_nbgen_roundtrip():
    from tools.nbgen import build_notebook, parse_source

    src = "Title text\n\n```python\nx = 1\n```\n\nafter text\n"
    cells = parse_source(src)
    kinds = [k for k, _ in cells]
    assert kinds == ["markdown", "code", "markdown"]
    nb = build_notebook(src)
    assert nb["nbformat"] == 4
    code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
    # canonical nbformat: every line ends with \n except the last
    assert code_cells[0]["source"] == ["x = 1"]
    assert all("id" in c for c in nb["cells"])


def test_nbgen_markdown_py_fence_is_not_code():
    from tools.nbgen import parse_source

    src = "example:\n\n```py\nnot a cell\n```\n"
    cells = parse_source(src)
    assert [k for k, _ in cells] == ["markdown"]

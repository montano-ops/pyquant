"""qrc.synth — synthetic financial data with realistic statistical properties.

Why synthetic data is a genuine research tool (not just an offline fallback):

1. You control the TRUE data-generating process, so you can test whether a
   method recovers a signal you *know* exists (power), and whether it invents
   one that does not (false positives).
2. You can simulate thousands of parallel histories — the "what else could
   have happened" that a single historical path can never show you.

Properties of `synthetic_prices`:
    - log-normal prices (prices can never go below zero),
    - daily returns with small drift and ~1% daily volatility by default,
    - volatility clustering (persistent, slowly decaying volatility, GARCH-like),
    - fat tails (standardized Student-t innovations with df=5 by default),
    - cross-asset correlation through a common market factor (n_assets > 1),
    - deterministic given the seed.

Everything is generated in LOG space, so the returns series is exact.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

__all__ = ["synthetic_returns", "synthetic_prices"]


def synthetic_returns(
    n_days: int = 1500,
    n_assets: int = 1,
    seed: int = 0,
    mu: float = 0.0003,
    sigma: float = 0.01,
    drift_spread: float = 0.0,
    vol_clustering: bool = True,
    fat_tails: bool = True,
    corr: float = 0.4,
    end: str | None = None,
) -> pd.DataFrame:
    """Simulated daily *log* returns, wide (rows=dates, columns=assets).

    Parameters
    ----------
    mu, sigma : average daily log drift and average daily volatility
    drift_spread : if > 0, asset i gets a persistent drift spread linearly
        from -drift_spread to +drift_spread across assets. Use this to create
        a universe where cross-sectional ranking exercises have REAL signal
        to find (e.g. momentum/reversal lessons on synthetic panels).
    vol_clustering : persistent stochastic volatility (log-AR(1), ~monthly decay)
    fat_tails : standardized Student-t(df=5) innovations instead of Gaussian
    corr : average pairwise correlation via a one-factor structure (n_assets>1)
    """
    rng = np.random.default_rng(seed)
    df_t = 5

    def draws(k: int) -> np.ndarray:
        if fat_tails:
            z = rng.standard_t(df_t, size=k)
            return z / np.sqrt(df_t / (df_t - 2))  # standardize to unit variance
        return rng.standard_normal(k)

    def vol_path() -> np.ndarray:
        if not vol_clustering:
            return np.full(n_days, sigma)
        rho, s = 0.97, 0.45
        log_sig = np.empty(n_days)
        log_sig[0] = np.log(sigma)
        eta = rng.standard_normal(n_days)
        for t in range(1, n_days):  # explicit loop is the honest way to read an AR(1)
            log_sig[t] = rho * log_sig[t - 1] + (1 - rho) * np.log(sigma) \
                + s * np.sqrt(1 - rho ** 2) * eta[t]
        return np.exp(log_sig)

    z_m = draws(n_days)
    rets = {}
    for i in range(n_assets):
        z_i = np.sqrt(corr) * z_m + np.sqrt(1 - corr) * draws(n_days) if n_assets > 1 else draws(n_days)
        mu_i = mu + (drift_spread * (2 * i / max(n_assets - 1, 1) - 1) if n_assets > 1 else mu)
        rets[f"S{i}"] = mu_i + vol_path() * z_i

    idx = pd.bdate_range(end=end or pd.Timestamp.today().normalize(), periods=n_days)
    return pd.DataFrame(rets, index=idx)


def synthetic_prices(**kwargs) -> pd.DataFrame:
    """Simulated daily *prices* (the cumulative product of `synthetic_returns`).

    Same parameters as `synthetic_returns`; prices start at 100.0.
    """
    start_level = kwargs.pop("start", 100.0)
    r = synthetic_returns(**kwargs)
    return start_level * np.exp(r.cumsum())

# Stylized Facts — Cont (2001) Field Guide

**Source:** R. Cont (2001), "Empirical properties of asset returns:
stylized facts and statistical issues," *Quantitative Finance* 1(2).

A *stylized fact* is an empirical regularity so robust it survives across
markets, asset classes, and periods. Cont's list (abridged to the ones
this course can test):

| # | Fact | Test in this course | Module |
|---|---|---|---|
| 1 | **Heavy tails**: P(|r| > x) decays like a power law, not exponentially | tail multiples, QQ plots, Hill-ish plots | 02.11, 03.4–5, 03.7 |
| 2 | **Absence of autocorrelation** (of returns) | ACF vs ±2/√T bands | 02.16, 03.7 |
| 3 | **Volatility clustering**: |r| (and r²) autocorrelate for weeks/months | ACF of |r|; rolling vol | 02.16, 03.10 |
| 4 | **Aggregational Gaussianity**: tails thin as frequency drops | kurtosis daily vs weekly vs monthly | 03.7, 03.12 |
| 5 | **Leverage effect** (equities): vol ↑ after price ↓ | corr(r, Δvol) < 0 | 03.7, 09.x |
| 6 | **Volume/vol correlation**: trading activity tracks vol | corr(|r|, volume) | 03.7 (where volume exists) |

**Why "stylized" matters:** a model that violates fact 1 (e.g., normal
daily returns) is wrong about the exact thing risk management cares
about; a model violating fact 3 (e.g., iid returns) is wrong about the
*clustering* of risk — and therefore about drawdowns. Backtest engines
and risk systems live or die on these six lines.

**The honest caveats (audit material):**
- Facts estimated on one asset, one window = one draw (day 1's lesson).
- Power-law vs lognormal tails: distinguishing them needs oceans of data
  — Cont says so himself. "Heavy tails" is a robust statement; the exact
  tail index is not.
- Fact 5 is equity-specific and asymmetric; fact 6 needs volume data
  quality you should check first.

**Day-7 deliverable:** a table — fact, test, statistic, verdict,
n — for three assets, plus the paragraph a risk manager would write.

# Module 03 — Statistics (Weeks 6–7)

Module 02 handed you distributions as *models*. This module points the
machinery at real return data and asks the practitioner's question: **which
summary statistics can you trust, and how exactly does each one lie?**

The mean is fragile, the median is stubborn, skew and kurtosis are
evidence, outliers are information — not noise — and every estimate comes
with an error bar you must know by heart. The module ends where every
quant session begins: a full exploratory data analysis, done by hand,
then written up as your first formal research report.

| Week | Days | Theme |
|---|---|---|
| 6 | 1–7 | Population vs sample → sampling distributions → descriptive statistics → skew & kurtosis → outliers; **mini-project: stylized-facts audit (Cont 2001)** |
| 7 | 8–14 | Full EDA workflow → mean stability → volatility → formal non-normality tests → missing data & frequency; **checkpoint: anatomy of a distribution** |

Reference sheets: [concepts/descriptive_stats_reference.md](concepts/descriptive_stats_reference.md) ·
[concepts/stylized_facts.md](concepts/stylized_facts.md)

**Papers:** Cont (2001), *Empirical properties of asset returns: stylized
facts and statistical issues* — the day-7 mini-project reproduces its core
facts on your own data. Everything else is the toolkit that paper assumes
you already own.

**The through-line:** a statistic is a random variable (day 2 proves it).
Every number in every backtest you ever run is a draw from a sampling
distribution — and the job is to report the draw *with* its distribution.

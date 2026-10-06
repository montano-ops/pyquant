# Module 06 — Regression (Weeks 13–15)

Module 01 made you solve the normal equations in NumPy; modules 03–04 put an
error bar on every estimate. This module welds the two into the most-used
tool in empirical finance: **the linear regression, owned end-to-end** —
fitted by *your* code before statsmodels is allowed to hide anything, and
above all **inference you can defend**: the right standard error for the
violation your data actually commits.

Returns data breaks the classical assumptions on a schedule you can set your
watch by — volatility clusters, overlapping windows autocorrelate, tails are
fat, panels cross-correlate. Each break costs a specific thing (unbiasedness,
efficiency, or the validity of your t-stats), and each has a specific repair
(White, Newey–West, Fama–MacBeth). By day 18 you will own the decision table
that maps violation → consequence → repair, and by day 21 you will run a
cross-sectional study — characteristic vs future returns — the way papers
do, with the caveats audited out loud.

| Week | Days | Theme |
|---|---|---|
| 13 | 1–7 | OLS from scratch → coefficients & residuals → R², SEs, t-stats → the GM assumptions → heteroskedasticity & White SEs → review; **mini-project: beta lab (10 names, rolling betas, stability)** |
| 14 | 8–14 | Autocorrelation & Newey–West → multicollinearity & VIF → diagnostics → outliers & winsorizing → specification (logs, dummies, interactions) → review; **mini-project: predictive regression** |
| 15 | 15–21 | Fama–MacBeth → reading FF92 → rolling & expanding windows → which SE when → FF92 partial reproduction → review; **module checkpoint: cross-section lab** |

Reference sheets: [concepts/ols_reference.md](concepts/ols_reference.md) ·
[concepts/standard_errors_reference.md](concepts/standard_errors_reference.md)

**Papers:** Fama & French (1992), *The Cross-Section of Expected Stock
Returns* — dissected on day 16 and partially reproduced on day 19, on the
characteristics free data can support. The machinery: Fama & MacBeth (1973)
— the two-step every cross-sectional paper still runs; White (1980) and
Newey & West (1987) — the two most-cited repairs in econometrics, both
implemented by you, by hand, before statsmodels confirms them.

**The through-line:** a regression coefficient is a random variable (day 3's
simulation proves it). Every β̂ in every paper is a draw from a sampling
distribution — and the job is to report the draw *with* its standard error,
where "standard error" means the one that survives what your data is doing.

**Entry condition:** modules 00–05 (or demonstrated fluency: normal
equations in NumPy, sampling distributions, confidence intervals, t-tests,
and a clean research panel).

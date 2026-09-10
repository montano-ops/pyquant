# ROADMAP — The Complete Curriculum

This is the canonical map of the course: every module, every week, every day,
every paper, and how they connect. Modules 00–05 are fully authored (day
folders contain lesson / exercise / solution / review). Modules 06–15 are
fully **specified** at the day level below and in each module's README — their
day folders are authored to the same standard progressively (see
[AUTHORING.md](AUTHORING.md) for the exact template; the roadmap marks each
week's status).

**Legend:** ✅ authored (complete day folders) · 🟨 partially authored · 🔲 specced (blueprint below + module README)

## The arc

```
 Module 00        Orientation: how to read a paper, how the course works
    │
 01–04  ─────────  The statistics apprenticeship: math → probability → statistics → inference
    │              (every concept taught BECAUSE a research question needs it)
    │
 05     ─────────  Financial data: prices, adjustments, panels, bias
    │
 06–07  ─────────  Regression & asset pricing: first real paper reproductions
    │              (FF93, JT93 momentum — capstone 1 begins)
    │
 08–09  ─────────  Time series & financial econometrics: stationarity, ARMA,
    │              GARCH, cointegration — pairs trading (capstone 4 seed)
    │
 10     ─────────  Strategy families: momentum, reversal, stat-arb, factors,
    │              events, volatility, microstructure
    │
 11–12  ─────────  Portfolio construction & your own backtesting framework
    │
 13     ─────────  Research validation: biases, snooping, deflated Sharpe,
    │              out-of-sample discipline (the module that changes how you read)
    │
 14–15  ─────────  Machine learning (last, not first) & derivatives
    │
 projects/* ─────  Six capstones, culminating in original research
```

**Pacing.** 46 study weeks × 6 days/week × ~90–150 min/day ≈ 11 months at a
sustainable pace. Accelerated (~3h/day): ~6 months. There is no prize for
speed: the retrieval practice, spacing, and re-derivations ARE the course.

**The weekly rhythm (every module, every week):**

| Day | Role |
|---|---|
| 01–05 | Concept lessons: intuition → math → Python → real data → research connection |
| 06 | Review: retrieval without notes, error log, spaced-repetition scheduler |
| 07 | Mini-project or research checkpoint (cumulative, increasingly independent) |

## Module map and status

| # | Module | Weeks | Status |
|---|---|---|---|
| 00 | [Orientation](00_orientation/) | 0 | ✅ |
| 01 | [Mathematical foundations](01_math/) | 1–2 | ✅ |
| 02 | [Probability](02_probability/) | 3–5 | ✅ |
| 03 | [Statistics](03_statistics/) | 6–7 | ✅ |
| 04 | [Statistical inference](04_inference/) | 8–10 | 🟨 (week 8 authored; 9–10 specced) |
| 05 | [Financial data](05_financial_data/) | 11–12 | 🟨 (week 11 authored; 12 specced) |
| 06 | [Regression](06_regression/) | 13–15 | 🔲 |
| 07 | [Asset pricing & factors](07_asset_pricing/) | 16–19 | 🔲 |
| 08 | [Time-series analysis](08_time_series/) | 20–22 | 🔲 |
| 09 | [Financial econometrics](09_financial_econometrics/) | 23–27 | 🔲 |
| 10 | [Strategy research](10_strategy_research/) | 28–31 | 🔲 |
| 11 | [Portfolio construction](11_portfolio_construction/) | 32–33 | 🔲 |
| 12 | [Backtesting & performance](12_backtesting/) | 34–36 | 🔲 |
| 13 | [Research validation](13_research_validation/) | 37–39 | 🔲 |
| 14 | [Machine learning](14_machine_learning/) | 40–43 | 🔲 |
| 15 | [Derivatives](15_derivatives/) | 44–46 | 🔲 |

Mapping to topic areas: scope areas 9–10 (financial time series,
multivariate/econometrics) live in `09_financial_econometrics`; performance &
risk metrics live in `12_backtesting` (weeks 36); backtest biases (14) and
research methodology (16) are combined in `13_research_validation` because
they are one discipline.

**Papers appear from day 3 of the course and recur in every module** —
reading, then dissecting, then reproducing, then extending. Full index with
reproducibility notes: [docs/PAPERS.md](docs/PAPERS.md).

---

## Module 00 — Orientation (Week 0) ✅

*Goal: know how the course works, have a working environment, and know how to
take a research paper apart — before any statistics.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 00.1 | How this course works | The method, the rules of engagement, how to use exercise/solution/review, environment setup | — |
| 00.2 | Your toolkit, tested | pandas diagnostic on market data; the `qrc` data package; first downloads; the offline synthetic switch | — |
| 00.3 | Anatomy of a research paper | The 12-step paper workflow; dissect an abstract/intro/tables | Jegadeesh & Titman (1993) — read only |
| 00.4 | Prices, returns, first charts | Close vs adjusted close on a dividend payer; simple vs log returns (preview) | — |
| 00.5 | How could this be wrong? | Tour of the biases; watch a "great strategy" get manufactured from noise | — |
| 00.6 | Review | Retrieval, set up your progress tracker & spaced-review system | — |
| 00.7 | Mini-project: First contact | SPY/QQQ/GLD study — returns, vol, drawdown, 5 research questions, data diary | — |

## Module 01 — Mathematical foundations (Weeks 1–2) ✅

*Goal: read the mathematical notation of quant papers fluently; compute
portfolio variance; run your first (unplanned) regression by hand. No proofs,
no calculus drills — only what research requires.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 01.1 | Summation & notation | Σ notation, indices (t, i, n), mean/variance in sigma form, returns as data | — |
| 01.2 | Functions & linearity | Linear payoffs, fee schedules, why finance loves linear models; composition | — |
| 01.3 | Exponents & logarithms | Compounding, log returns, additivity over time, geometric vs arithmetic means | — |
| 01.4 | Calculus intuition I: change | Derivative = slope = sensitivity; finite differences; convexity teaser | — |
| 01.5 | Calculus intuition II: optimization | Minima, gradient intuition, least squares as minimization (scipy) | — |
| 01.6 | Review | Retrieval + error log | — |
| 01.7 | Mini-project: return arithmetic you can trust | log/simple conversions, annualization done right, when log≈simple breaks | — |
| 01.8 | Vectors | Return & weight vectors, dot product = portfolio return, norms, vectorization | — |
| 01.9 | Matrices | The (dates × assets) data matrix, matrix-vector products, covariance matrix intro | — |
| 01.10 | Matrix multiplication & portfolio variance | wᵀΣw — the most important formula in portfolio math; diversification demo | — |
| 01.11 | Linear systems & regression geometry | Overdetermined Xβ≈y, projection, solve normal equations in NumPy | — |
| 01.12 | Optimization with constraints | Budget constraint Σw=1, min-variance portfolio via scipy, why constraints are real | — |
| 01.13 | Review + decode paper equations | Translate FF93's regression and JT93's portfolio rule from math to pseudocode | Fama & French (1993); JT (1993) equations |
| 01.14 | Mini-project: portfolio variance laboratory | Diversification curve; correlation's effect on risk; sensitivity analysis | — |

## Module 02 — Probability (Weeks 3–5) ✅

*Goal: think in distributions, expectations, and — critically — in "what else
could have happened". Every concept is welded to returns, portfolios, or
trading outcomes.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 02.1 | Random experiments & events | Sample spaces; tomorrow's return as a random variable in waiting | — |
| 02.2 | Probability rules | Axioms, complement, union; frequency vs subjective views; simulating frequencies | — |
| 02.3 | Conditional probability & Bayes | Base rates; why "80% of crashes had signal X" ≠ "X → crash"; signal confusion matrix | — |
| 02.4 | Random variables & distributions | Discrete vs continuous, PMF/PDF/CDF, distributions as models of returns | — |
| 02.5 | Expectation & variance | E[X], Var(X); trading expectancy; volatility as the SD of returns | — |
| 02.6 | Review | Retrieval + interleaved problems | — |
| 02.7 | Mini-project: expectancy simulator | win-rate × avg-win/avg-loss; simulate 1,000 equity curves; variance of outcomes | — |
| 02.8 | Covariance & correlation | Cov(X,Y), ρ; real asset correlations; correlation ≠ causation; rolling instability | — |
| 02.9 | Joint distributions & 2-asset portfolios | Portfolio mean & variance; the hedging math; perfect-correlation special case | — |
| 02.10 | Bernoulli & binomial | Win rates as Bernoulli; P(k winning days in n); binomial tails | — |
| 02.11 | The normal distribution | pdf, empirical rule, z-scores; why finance uses it; first QQ look at real returns | — |
| 02.12 | Law of large numbers | Sample mean convergence; how SLOW it is for noisy returns (simulation) | — |
| 02.13 | Review | Retrieval + interleaved problems | — |
| 02.14 | Mini-project: correlation study | ETF correlation matrix across regimes; write up when correlation fails | — |
| 02.15 | Central limit theorem | Sampling distribution of the mean, standard error, why t-stats exist at all | — |
| 02.16 | Random walks & near-efficient markets | Independence of returns; what martingale-ish prices imply for prediction | — |
| 02.17 | The law of small numbers | Why a 100-day track record is noise; gambler's fallacy; SE of the mean applied to returns | Tversky & Kahneman (1971) — excerpt |
| 02.18 | Monte Carlo & bootstrap preview | Simulating paths; resampling as parallel histories; seed discipline | — |
| 02.19 | Why you can't shuffle time series | Dependence, vol clustering preview, blocked alternatives, placebo logic | — |
| 02.20 | Review | Retrieval + interleaved problems | — |
| 02.21 | Module checkpoint: is a 55% win rate luck? | Full analysis by simulation + binomial/normal approximation; power; mini-report | — |

## Module 03 — Statistics (Weeks 6–7) ✅

*Goal: interrogate real return distributions with the right summary
statistics, and know exactly how each one can mislead.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 03.1 | Population vs sample | Parameters vs statistics; sampling bias; one backtest = one sample | — |
| 03.2 | Sampling distributions | Simulating the SE of the mean; estimator noise made visible | — |
| 03.3 | Descriptive statistics on returns | Mean/median/percentiles/IQR; robust vs non-robust; when median beats mean | — |
| 03.4 | Skewness & kurtosis | Formulas + intuition; fat tails in real returns; crash asymmetry | — |
| 03.5 | Outliers | Identification, winsorizing/trimming, distortion of mean & vol; 1987/2008/2020 | — |
| 03.6 | Review | Retrieval + interleaved problems | — |
| 03.7 | Mini-project: stylized-facts audit | Heavy tails, vol clustering, aggregational gaussianity on 3 assets | Cont (2001) — reproduce facts |
| 03.8 | Full EDA of daily returns | Structured workflow: histogram, density, QQ by hand; describing a distribution | — |
| 03.9 | Is the mean stable? | Rolling & subsample means; signal buried in noise (mean ~0.03% vs SD ~1%) | — |
| 03.10 | Volatility | Rolling vol, annualization, vol regimes; what vol does NOT tell you | — |
| 03.11 | Non-normality, quantified | Skew/kurt numbers as evidence; formal tests and their big-sample pathology | — |
| 03.12 | Missing data & frequency choices | NaN policy, ffill dangers; daily vs weekly vs monthly trade-offs | — |
| 03.13 | Review | Retrieval + interleaved problems | — |
| 03.14 | Module checkpoint: anatomy of a distribution | Full EDA mini-report on a chosen asset (first formal research report) | — |

## Module 04 — Statistical inference (Weeks 8–10) 🟨

*Goal: answer "could this be luck?" with machinery you understand from the
inside. Week 8 is authored; weeks 9–10 are specced below and in the module
README (authored to the same template).*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 04.1 | Estimation & standard error | Point estimates, bias/consistency intuition; SE of the mean return | — |
| 04.2 | Confidence intervals | What a CI actually means; CI for mean return; wide CIs vs strategy claims | — |
| 04.3 | Hypothesis testing | H0/H1, test statistics, p-values defined correctly (and the two wrong readings) | — |
| 04.4 | The t-test for mean returns | t-stat of daily/annual returns; reading t-stats in paper tables | JT (1993) Table 1 t-stats |
| 04.5 | Errors, power, effect size | Type I/II, power curves; statistical ≠ economic ≠ tradable | — |
| 04.6 | Review | Retrieval + interleaved problems | — |
| 04.7 | Mini-project: t-stat laboratory | How many years of data until a Sharpe-0.5 strategy reaches t=2? (simulation) | — |
| 04.8 | Two-sample & paired tests 🔲 | Strategy A vs B; paired designs; dependence between track records | — |
| 04.9 | The bootstrap 🔲 | Resampling returns; bootstrap CI for mean & Sharpe; block bootstrap for time series | — |
| 04.10 | Permutation tests 🔲 | Shuffling labels; why you can't shuffle time series (block/rank alternatives) | — |
| 04.11 | Multiple testing 🔲 | The 5% lottery: 100 null signals → ~5 "discoveries"; Bonferroni; Benjamini-Hochberg | — |
| 04.12 | Research application: the weekend effect 🔲 | Full small-paper reproduction: day-of-week mean returns, t-tests, multiple-testing audit | French (1980) — reproduce |
| 04.13 | Overlapping observations 🔲 | Why monthly overlapping returns inflate t-stats; HAC preview | — |
| 04.14 | Review 🔲 | Retrieval + interleaved problems | — |
| 04.15 | Mini-project: significance grill 🔲 | Take three published claims (t-stats) and interrogate power, effect size, multiplicity | Harvey, Liu & Zhu (2016) — excerpt |
| 04.16 | Reading inference in papers 🔲 | Work through a results table end-to-end: what is tested, what the stars mean | — |
| 04.17 | Effect size vs tradability 🔲 | Costs vs premium magnitude; minimum viable edge | — |
| 04.18 | Review 🔲 | Retrieval + error log | — |
| 04.19 | Review week / consolidation 🔲 | Spaced recall of modules 01–04; self-exam; error-log triage | — |
| 04.20 | Review week cont. 🔲 | Mixed problem set across all inference tools | — |
| 04.21 | Module checkpoint: does the effect survive? 🔲 | Full test + mini-report on a signal of your choosing | — |

## Module 05 — Financial data (Weeks 11–12) 🟨

*Goal: build a clean, honest research panel and know exactly which biases it
cannot escape. Week 11 is authored; week 12 is specced.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 05.1 | Prices: raw vs adjusted | What "adjusted" means; total-return reconstruction; why research uses adjusted | — |
| 05.2 | Corporate actions by hand | Split & dividend back-adjustment algorithm; verify against provider adj close | — |
| 05.3 | OHLC, volume, market cap, liquidity | Dollar volume, share counts; the screens papers apply (price > $5, liquidity) and why | — |
| 05.4 | Building a panel | Aligning N tickers; NaN structure = listing periods; join semantics; ffill dangers | — |
| 05.5 | Survivorship bias I | Today's-list backtests; the delisted-demo experiment; universe definition as a research decision | Brown, Goetzmann, Ibbotson & Ross (1992) — read |
| 05.6 | Review | Retrieval + interleaved problems | — |
| 05.7 | Mini-project: research panel v1 | 50-ticker panel (adj/raw/volume/actions) + data-quality report | — |
| 05.8 | Delisting returns 🔲 | What a delisting return is; why omitting it flatters longs and hinders shorts | Shumway (1997) — read |
| 05.9 | Survivorship bias II 🔲 | Quantify the bias: equal-weight today's-S&P vs SPY; strategy-dependent bias direction | — |
| 05.10 | Point-in-time data 🔲 | Index membership history; lookahead in universe selection; CRSP/WRDS landscape | — |
| 05.11 | Timestamps & availability 🔲 | When is a close a close; timezone pitfalls; fundamentals' publication lag | — |
| 05.12 | Reproducible pipelines 🔲 | Parquet caches, snapshots, seeds, data provenance; the research log | — |
| 05.13 | Review 🔲 | Retrieval + interleaved problems | — |
| 05.14 | Module checkpoint: bias audit report 🔲 | Formal audit of your panel: survivorship, selection, timestamps, actions | — |

## Module 06 — Regression (Weeks 13–15) 🔲

*Goal: OLS from the inside out — you derive it with NumPy before statsmodels
hides it — and you know exactly which standard errors financial data demands.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 06.1 | OLS from scratch | Normal equations (your module-01 code); fit by hand; compare to statsmodels | — |
| 06.2 | Coefficients & residuals | Interpretation, fitted values, residual structure | — |
| 06.3 | R², standard errors, t-stats | Sampling variation of β̂; CIs for coefficients | — |
| 06.4 | The GM assumptions | What each assumption buys; where returns data breaks each one | — |
| 06.5 | Heteroskedasticity | Vol differences across assets/times; White (robust) SEs | — |
| 06.6 | Review | | — |
| 06.7 | Mini-project: beta lab | Market-model betas for 10 stocks; rolling betas; stability | — |
| 06.8 | Autocorrelation & HAC | Overlapping returns; Newey–West SEs implemented and understood | — |
| 06.9 | Multicollinearity | VIF; collinear factors; what happens to t-stats | — |
| 06.10 | Diagnostics | Residual plots, QQ of residuals, influence/leverage basics | — |
| 06.11 | Outliers & robustness | Winsorized regressions (papers do this constantly) | — |
| 06.12 | Specification | Logs, dummies, interactions; regime dummies | — |
| 06.13 | Review | | — |
| 06.14 | Mini-project: predictive regression | Does lagged volume/vol predict returns? Honest R² interpretation | — |
| 06.15 | Fama–MacBeth | Why pooled OLS fails on panels; two-step cross-sectional regressions | — |
| 06.16 | Reading FF92 | Dissect the cross-sectional regressions; size, beta, BM | Fama & French (1992) — dissect |
| 06.17 | Rolling & expanding windows | Parameter stability as a research question | — |
| 06.18 | Which SE when | A decision table; overlapping observations; clustered dependence | — |
| 06.19 | Research application | Small cross-sectional sort + regression on your panel, caveats audited | FF92 — partial reproduction |
| 06.20 | Review | | — |
| 06.21 | Module checkpoint: cross-section lab | Mini-report: a characteristic vs future returns, done properly-ish | — |

## Module 07 — Asset pricing & factor models (Weeks 16–19) 🔲

*Goal: from CAPM to five factors; construct factors yourself, validate them
against Ken French's data, and reproduce the momentum paper.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 07.1 | Why CAPM exists | Systematic vs idiosyncratic risk; only one is priced | — |
| 07.2 | CAPM mechanics | Beta, the SML, estimating alpha/beta by regression | — |
| 07.3 | Testing CAPM | What the data showed; alpha as "the anomaly" | — |
| 07.4 | Market model vs CAPM | Benchmark choice; rolling beta; factor regression as performance evaluation | — |
| 07.5 | Evaluation via factors | "Is my strategy just beta?" | — |
| 07.6 | Review | | — |
| 07.7 | Mini-project: is my ETF just the market? | Sector ETFs on SPY; interpret alpha/beta | — |
| 07.8 | FF93 dissection | 2×3 sorts, the construction you will implement | Fama & French (1993) — dissect |
| 07.9 | Building size/BM sorts | Breakpoints, value/equal weights, on your panel | — |
| 07.10 | Building SMB & HML | Long-short construction; compare with official French factors (validation!) | FF93 — reproduce factors |
| 07.11 | Time-series factor regressions | 3-factor alphas and loadings | — |
| 07.12 | The intercept test | What a significant alpha means; GRS intuition | — |
| 07.13 | Review | | — |
| 07.14 | Mini-project: 3-factor regression lab | Regress your momentum deciles / ETFs on the 3 factors | — |
| 07.15 | JT93 dissection | Overlapping-portfolio construction in plain English | Jegadeesh & Titman (1993) — dissect |
| 07.16 | Implementing relative strength | 12-2 formation, skip month, decile portfolios on your panel | — |
| 07.17 | Reproducing the momentum table | Decile means, W−L spread, t-stats; compare to the paper's shape | JT93 — reproduce |
| 07.18 | Momentum crashes | Skew, the 2009 story, crash-hedged variants | Daniel & Moskowitz (2016) — excerpt |
| 07.19 | Carhart's fourth factor | UMD; 4-factor regressions | Carhart (1997) — use |
| 07.20 | Review | | — |
| 07.21 | Mini-project: momentum, first pass | Momentum on your panel; simple costs preview | — |
| 07.22 | Five factors | Read FF15; proxy RMW/CMA | Fama & French (2015) — dissect |
| 07.23 | Is HML redundant? | Replicate the alpha regressions that started the fight | FF15 — reproduce test |
| 07.24 | Profitability & investment | Quality screens in practice | — |
| 07.25 | Comparing factor models | Which alphas survive which model | — |
| 07.26 | The factor zoo | Hundreds of claimed factors; why t>3 | Harvey, Liu & Zhu (2016) — excerpt |
| 07.27 | Review | | — |
| 07.28 | Module checkpoint + capstone 1 kickoff | Momentum reproduction report outline; full 12-step worksheet | JT93 — full workflow |

## Module 08 — Time-series analysis (Weeks 20–22) 🔲

*Goal: lags done with total discipline, stationarity respected, spurious
regression reproduced (never forgotten), ARMA used where it belongs.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 08.1 | Lags & leads | shift() as THE look-ahead battleground; t vs t−1 discipline | — |
| 08.2 | Autocorrelation | ACF, ±2/√T bands, Ljung–Box | — |
| 08.3 | The ACFs that matter | returns ≈ 0; \|r\| and r² ≫ 0 — vol clustering formalized | — |
| 08.4 | Partial autocorrelation | Residual correlation intuition; PACF | — |
| 08.5 | White noise vs structure | "No autocorrelation" ≠ "no predictability" | — |
| 08.6 | Review | | — |
| 08.7 | Mini-project: ACF laboratory | Real + synthetic data side by side (you know the truth about the synthetic) | — |
| 08.8 | Stationarity | Strict vs weak; why nonstationarity breaks your statistics | — |
| 08.9 | Random walks & unit roots | Simulation; prices vs returns | — |
| 08.10 | Spurious regression | Reproduce the classic: regress independent random walks; get R²≈0.9 | Granger & Newbold (1974) — reproduce by simulation |
| 08.11 | The ADF test | Test regression, implementation, low power, structural breaks | — |
| 08.12 | Differencing | Trends, seasonality, over-differencing | — |
| 08.13 | Review | | — |
| 08.14 | Mini-project: is it stationary? | Prices, returns, vol — test properly and interpret honestly | — |
| 08.15 | AR models | What AR(p) assumes; fit to returns (≈ nothing) vs \|r\| (something) | — |
| 08.16 | MA & ARMA | Equivalence, identification via ACF/PACF | — |
| 08.17 | ARIMA & SARIMA | Integration; seasonality in vol & flows | — |
| 08.18 | Forecasting honestly | Time-aware splits; naive benchmarks; MSE/MAE | — |
| 08.19 | Forecast evaluation | Out-of-sample R²; Mincer–Zarnowitz; scaling traps | — |
| 08.20 | Review | | — |
| 08.21 | Module checkpoint | Variance-ratio test on an index (Lo–MacKinlay) + "beat the naive vol forecast" report | Lo & MacKinlay (1988) — reproduce-lite |

## Module 09 — Financial econometrics (Weeks 23–27) 🔲

*Goal: model the one thing that IS predictable — volatility — and the
multivariate structure (cointegration) behind pairs trading.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 09.1 | Conditional heteroskedasticity | ARCH(1): model + likelihood | Engle (1982) — read core |
| 09.2 | ARCH by hand | MLE with scipy | — |
| 09.3 | GARCH(1,1) | Persistence, long-run variance, half-life | Bollerslev (1986) — read core |
| 09.4 | GARCH by hand vs `arch` | Fit both; parameter interpretation | — |
| 09.5 | GARCH variants | t-innovations, EGARCH leverage; forecasting | — |
| 09.6 | Review | | — |
| 09.7 | Mini-project: fit GARCH | One asset, α+β, half-life, forecast path | — |
| 09.8 | Volatility horse race | Rolling vs EWMA vs GARCH | — |
| 09.9 | Evaluating vol forecasts | MZ regressions, QLIKE; R² of vol vs return forecasts | — |
| 09.10 | Realized volatility | Daily→monthly RV; √time scaling and when it lies | — |
| 09.11 | VaR & ES | Historical, parametric, GARCH-conditional | — |
| 09.12 | Backtesting risk models | Hit rates; independence of violations | — |
| 09.13 | Review | | — |
| 09.14 | Mini-project: vol forecast report | Full evaluation on your panel | — |
| 09.15 | Covariance matrices | Sample error when N≈T; simulation | — |
| 09.16 | Shrinkage & EWMA covariance | Ledoit–Wolf; risk stability | — |
| 09.17 | Min-variance from noisy Σ | Error maximization; why naive weighting wins often | — |
| 09.18 | Factor covariance | PCA-based Σ | — |
| 09.19 | Covariance in practice | Portfolio risk, beta/factor neutrality uses | — |
| 09.20 | Review | | — |
| 09.21 | Mini-project: covariance stability | Rolling Σ; eigenvalue wander | — |
| 09.22 | VAR | Systems, estimation, lag selection | — |
| 09.23 | Granger "causality" | What it is (predictability) and is NOT (causation) | — |
| 09.24 | VAR diagnostics | Stability; spurious causality; overfitting | — |
| 09.25 | VAR forecasting | Honest evaluation vs univariate benchmarks | — |
| 09.26 | Cointegration | Shared trends; correlation ≠ cointegration (demo) | — |
| 09.27 | Engle–Granger | 2-step test implemented; correct critical values | Engle & Granger (1987) — method |
| 09.28 | Johansen | Rank selection; EG vs Johansen | — |
| 09.29 | Error-correction models | Speed of adjustment; spread dynamics | — |
| 09.30 | Pairs selection | Distance vs cointegration vs factor-residual; multiplicity trap | — |
| 09.31 | Review | | — |
| 09.32 | Mini-project: VAR lab | Does vol Granger-cause returns? (and the reverse) | — |
| 09.33 | Module checkpoint | Full Engle–Granger study on a chosen pair + Gatev et al. 12-step worksheet | Gatev, Goetzmann & Rouwenhorst (2006) — dissect |

## Module 10 — Strategy research (Weeks 28–31) 🔲

*Goal: implement the classic strategy families and learn where each one
dies (costs, capacity, regimes). Evaluation ratchets up: simple spread
returns here, full framework in module 12, validation in module 13.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 10.1 | Cross-sectional momentum, refined | Skip month, weighting, industry neutrality | JT93 — extend |
| 10.2 | Time-series momentum | Sign autocorrelation; dissection | Moskowitz, Ooi & Pedersen (2012) — dissect |
| 10.3 | TSM implementation | On ETF futures proxies; crude costs | MOP — reproduce-lite |
| 10.4 | Trend following | MA rules; honest parameter grids (snooping awareness) | — |
| 10.5 | When momentum fails | Regimes, crashes, crowding | — |
| 10.6 | Review | | — |
| 10.7 | Mini-project: XSM vs TSM | Same panel, both families, compare | — |
| 10.8 | Short-term reversal | Dissection | Jegadeesh (1990); Lehmann (1990) — dissect |
| 10.9 | Reversal implementation | On your panel — with the survivorship audit reversal demands | Lehmann — reproduce-lite |
| 10.10 | Mean-reverting processes | OU process, simulation, half-life | — |
| 10.11 | MA-distance strategies | Detrended reversal; liquidity provision framing | — |
| 10.12 | Reversal vs costs | Turnover & spread arithmetic; the strategy that dies at costs | — |
| 10.13 | Review | | — |
| 10.14 | Mini-project: gross vs net | Reversal before/after costs; write the obituary | — |
| 10.15 | Pairs strategy build | Formation, z-score entry/exit, stop logic | Gatev et al. — extend |
| 10.16 | Pairs backtest, first pass | Vectorized, crude costs | — |
| 10.17 | Factor strategies in practice | Value (P/B, E/P), quality (ROE, margins), low-vol | — |
| 10.18 | Combining signals | Rank aggregation; diversification across signals | — |
| 10.19 | Event-driven: PEAD | Dissection; free-data approximation design | Bernard & Thomas (1989) — dissect |
| 10.20 | Review | | — |
| 10.21 | Mini-project: factor tilt | Long-only tilt portfolio with screens | — |
| 10.22 | PEAD mini-study | Earnings dates + SUE proxy on free data, caveats loud | Bernard & Thomas — approximation |
| 10.23 | Vol-managed portfolios | Dissection | Moreira & Muir (2017) — dissect |
| 10.24 | Implementing vol management | Scale by 1/σ̂² using module-09 forecasts | M&M — reproduce-lite |
| 10.25 | Microstructure I | Bid/ask, order types, spread costs; why daily backtests overstate | — |
| 10.26 | Microstructure II | Corwin–Schultz high-low spread estimator; impact (square-root law); ADV caps | Corwin & Schultz (2012) — implement |
| 10.27 | Review | | — |
| 10.28 | Module checkpoint: strategy cards | Three strategies documented: hypothesis → implementation → gross → net → failure modes | — |

## Module 11 — Portfolio construction (Weeks 32–33) 🔲

*Goal: turn signals into defensible portfolios — weights, constraints,
neutrality, leverage, turnover. A predictive signal is not automatically a
tradable strategy.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 11.1 | From signal to weights | Rank → quantile → weight maps | — |
| 11.2 | Weighting schemes | Equal, cap, inverse-vol; vol targeting | — |
| 11.3 | Position sizing | Risk budgeting; portfolio-level vol targeting | — |
| 11.4 | Constraints | Max weights, sector caps, no-short; cost of constraints | — |
| 11.5 | Turnover | What drives it; signal decay vs rebalancing | — |
| 11.6 | Review | | — |
| 11.7 | Mini-project: turnover anatomy | Momentum vs reversal vs factor tilts | — |
| 11.8 | Dollar & beta neutrality | Beta-hedging with your regression toolkit | — |
| 11.9 | Factor neutrality | Residualizing signals against factor exposures | — |
| 11.10 | Leverage | Margin mechanics, financing costs, call risk | — |
| 11.11 | Rebalancing | Frequency vs costs vs drift; no-trade bands | — |
| 11.12 | Optimal vs naive | Reproduce the 1/N result on ETFs | DeMiguel, Garlappi & Uppal (2009) — reproduce |
| 11.13 | Review | | — |
| 11.14 | Module checkpoint | A neutral, turnover-aware portfolio from one of your signals, documented | — |

## Module 12 — Backtesting & performance (Weeks 34–36) 🔲

*Goal: build your own research backtesting framework — vectorized, honest,
tested — plus the full performance/risk metric toolkit, from scratch.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 12.1 | The backtest contract | Positions known before returns; the shift invariant | — |
| 12.2 | Engine I: gross returns | Signals → positions → portfolio returns; hand-computed known-answer tests | — |
| 12.3 | Engine II: costs & turnover | Transaction costs; turnover accounting; net returns | — |
| 12.4 | Engine III: shorts & financing | Borrow costs, margin, leverage accounting | — |
| 12.5 | Testing your backtester | Property tests; synthetic invariants; bug-hunt fixtures | — |
| 12.6 | Review | | — |
| 12.7 | Mini-project: engine v1 | Complete + validation suite | — |
| 12.8 | Cost models | Commissions, spread, impact (square-root law); participation caps vs ADV | — |
| 12.9 | Cost sensitivity | Profitability vs cost grids; the death-cost of each strategy | — |
| 12.10 | Liquidity & capacity | Position size vs ADV; capacity estimation | — |
| 12.11 | Execution assumptions | Close vs next-open vs VWAP fills; sensitivity | — |
| 12.12 | Slippage & stale prices | When the close isn't there | — |
| 12.13 | Review | | — |
| 12.14 | Mini-project: capacity study | How big can your momentum strategy get? | — |
| 12.15 | Metrics I | CAGR, vol, Sharpe (annualization & its i.i.d. caveat) | — |
| 12.16 | Metrics II | Sortino, MDD, Calmar, win rate, profit factor, exposure | — |
| 12.17 | Tail risk | VaR, ES; drawdown distributions via bootstrap | — |
| 12.18 | Benchmarks | Alpha/beta decomposition; tracking error; information ratio | — |
| 12.19 | Attribution | Which positions/periods drove P&L | — |
| 12.20 | Review | | — |
| 12.21 | Module checkpoint | Full metrics + cost-sensitivity report for one strategy (capstone-ready) | — |

## Module 13 — Research validation (Weeks 37–39) 🔲

*Goal: the module that changes how you read everything. Bias bootcamp, honest
evaluation, multiple testing, deflated Sharpe. Habit: "how could this be wrong?"*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 13.1 | Look-ahead & leakage bug hunt | Broken-code specimens; find the leak; fix the shift | — |
| 13.2 | Leakage in ML pipelines | Fit scalers/encoders on train only; purging & embargo | — |
| 13.3 | Survivorship & selection, quantified | Redo module-05 demos at strategy level | — |
| 13.4 | Data snooping | Mine noise on real data → "discover" Sharpe > 1; write it up | — |
| 13.5 | Parameter overfitting | Heatmaps; plateaus vs spikes; walk-forward honesty | — |
| 13.6 | Review | | — |
| 13.7 | Mini-project: noise mining | Your own snooping experiment; the obituary | — |
| 13.8 | IS/OOS & walk-forward | Implement all three windows; when each lies | — |
| 13.9 | Time-series CV | Why K-fold leaks; purged k-fold; combinatorial (CSCV) | — |
| 13.10 | Multiple testing | Bonferroni; BH-FDR; implementing; zoo arithmetic | — |
| 13.11 | Deflated Sharpe ratio | Implement Bailey & López de Prado; apply to week-37 "discoveries" | Bailey & López de Prado (2014) — implement |
| 13.12 | Minimum track record length | Power analysis for strategies | — |
| 13.13 | Review | | — |
| 13.14 | Mini-project: deflate everything | Apply DSR/MinTRL to every backtest you've built | — |
| 13.15 | The factor zoo, read properly | Why t > 3; what this does to your priors | Harvey, Liu & Zhu (2016) — dissect |
| 13.16 | Post-publication decay | Arbitrage of anomalies; implications | McLean & Pontiff (2016) — dissect |
| 13.17 | Placebo tests | Negative controls; design placebos for your strategies | — |
| 13.18 | Subsamples & regimes | Bull/bear/high-vol; regime dependence | — |
| 13.19 | The research protocol | Pre-registration mindset; research log; exploration vs confirmation | — |
| 13.20 | Review | | — |
| 13.21 | Module checkpoint | Full validation report on your capstone-in-progress | — |

## Module 14 — Machine learning (Weeks 40–43) 🔲

*Goal: ML last, with the statistics to resist it. Baseline discipline,
leakage-proof pipelines, and a scaled-down reproduction of the landmark paper.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 14.1 | Where ML fits | Low SNR, nonstationarity, small effective N; baseline discipline | — |
| 14.2 | Regularized linear models | Ridge/lasso; standardization; purged CV for tuning | — |
| 14.3 | Logistic regression | Direction classification; imbalance; calibration | — |
| 14.4 | From forecast to P&L | Mapping probabilities to positions; metrics that matter | — |
| 14.5 | Feature engineering I | Lags, rolling stats, momentum/vol features; leakage traps | — |
| 14.6 | Review | | — |
| 14.7 | Mini-project: ridge horse race | vs naive baselines, honestly | — |
| 14.8 | Decision trees | Why they memorize noise | — |
| 14.9 | Random forests | Hyperparameters; OOB; stability | — |
| 14.10 | Gradient boosting | Tuning with purged CV | — |
| 14.11 | Feature importance | MDI vs permutation; correlated features; stability | — |
| 14.12 | Prediction stability | Retraining; regime shifts | — |
| 14.13 | Review | | — |
| 14.14 | Mini-project: GBM direction model | Leakage-proof end to end | — |
| 14.15 | PCA on returns | Statistical factors; eigenportfolios; choosing k | — |
| 14.16 | Clustering | K-means on returns; pairs candidates | — |
| 14.17 | Regime detection | Unsupervised regimes; HMM intuition | — |
| 14.18 | Gu–Kelly–Xiu dissection | Features, setup, findings | Gu, Kelly & Xiu (2020) — dissect |
| 14.19 | Scaled-down GKX | Monthly features → next-month ranking; RF vs linear; honest OOS | GKX — reproduce, scaled down |
| 14.20 | Review | | — |
| 14.21 | Mini-project: scaled-down GKX | Complete, with the honest OOS verdict | — |
| 14.22 | Neural nets on tables | Feedforward; why GBM usually wins here | — |
| 14.23 | Sequence models | RNN/LSTM/transformer concepts; cost/benefit | — |
| 14.24 | Overparameterization | Double descent intuition; regularization | — |
| 14.25 | ML research standards | Seeds & variance; reproducibility; reporting | — |
| 14.26 | The ML checklist | When ML is appropriate at all | — |
| 14.27 | Review | | — |
| 14.28 | Module checkpoint | ML strategy card + honest OOS report | — |

## Module 15 — Derivatives (Weeks 44–46) 🔲

*Goal: options through the research lens — Black-Scholes implemented, the
implied-vol surface built from free data, and the volatility risk premium
measured.*

| Day | Title | What you do | Paper hook |
|---|---|---|---|
| 15.1 | Forwards & futures | Payoffs, basis, roll, contango/backwardation | — |
| 15.2 | Options mechanics | Calls/puts, moneyness; payoff & P&L diagrams | — |
| 15.3 | Option data | Chains & expiries from yfinance; quirks of free data | — |
| 15.4 | Put-call parity | Derive, then verify on real quotes | — |
| 15.5 | Why researchers care | VRP, crash insurance, the map of options research | — |
| 15.6 | Review | | — |
| 15.7 | Mini-project: parity check | Live chains; bound violations and why they appear | — |
| 15.8 | Black-Scholes | Assumptions; implement with scipy | Black & Scholes (1973) — read core |
| 15.9 | The Greeks | Analytic + finite differences; delta-hedged P&L simulation | — |
| 15.10 | Implied volatility | Invert BS numerically (Newton + bisection); IV vs RV | — |
| 15.11 | The smile | Build the surface from chains; skew's information | — |
| 15.12 | Vol spreads | IV²−RV² as a signal | — |
| 15.13 | Review | | — |
| 15.14 | Mini-project: the surface | IV surface for one underlying; document its shape | — |
| 15.15 | Variance risk premium | VIX vs subsequent realized vol; compute the premium history | Carr & Wu (2009) — dissect |
| 15.16 | Short volatility | Carry vs crash risk; tail honesty (the XIV story) | Bondarenko (2014) — read |
| 15.17 | Options in portfolios | Overlays: protective puts, covered calls | — |
| 15.18 | Synthesis | The full pipeline, end to end, one last time | — |
| 15.19 | Review | | — |
| 15.20–21 | Module checkpoint | VRP mini-report + course completion self-assessment | — |

## Capstones (run alongside, finish after their prerequisite modules)

| Project | Seed module | Full version after | Source paper |
|---|---|---|---|
| [01_momentum](projects/01_momentum/) | 07 (week 19) | 12 + 13 | Jegadeesh & Titman (1993) |
| [02_reversal](projects/02_reversal/) | 10 (week 29) | 12 + 13 | Lehmann (1990); Jegadeesh (1990) |
| [03_factor_model](projects/03_factor_model/) | 07 (week 19) | 13 | FF93 / FF15 / Carhart |
| [04_pairs_trading](projects/04_pairs_trading/) | 09 (week 27) | 12 + 13 | Gatev, Goetzmann & Rouwenhorst (2006) |
| [05_volatility](projects/05_volatility/) | 09–10 (week 31) | 13 | Moreira & Muir (2017) or GARCH comparison |
| [06_original_research](projects/06_original_research/) | 15 (end) | — | a paper *you* choose, or your own hypothesis |

Each capstone follows the [9-notebook research standard](projects/README.md),
maintains a research log separating exploration from confirmation, and ends
with a formal [research report](templates/research_report.md).

# PAPERS — The Research Progression

Every paper in the course, in the order the learner meets them. Selection
criteria (in order): educational value, reproducibility with free data,
increasing methodological difficulty, relevance to systematic trading. Famous
papers that fail these tests are excluded.

**Roles:** 📖 read/dissect (workflow steps 1–5) · 🔨 reproduce-lite (core
pattern, free-data approximation, bias audited) · 🧪 reproduce (main tables,
side-by-side) · ⚙️ tool (method you implement and use).

**Access:** all are findable via DOI links, SSRN, author pages, or university
libraries. Where a paper's data is not free, the course reproduces the
*method* on a transparent universe and audits how the bias direction affects
results — an explicit learning objective, not a compromise we hide.

## Phase 1 — Reading papers before you know statistics (weeks 0–7)

| # | Paper | Role | Module | Data you need |
|---|---|---|---|---|
| 1 | Jegadeesh & Titman (1993), *Returns to Buying Winners and Selling Losers*, J. Finance | 📖 (recurring) | 00.3, 01.13, 04.4 | none yet — you read |
| 2 | Fama & French (1993), *Common Risk Factors in the Returns on Stocks and Bonds*, J. Financial Economics | 📖 (equations early; 🧪 later) | 01.13, 07 | Ken French library (free) |
| 3 | Tversky & Kahneman (1971), *Belief in the Law of Small Numbers*, Psychological Bulletin | 📖 excerpt | 02.17 | none — simulation instead |
| 4 | Cont (2001), *Empirical Properties of Asset Returns: Stylized Facts in Statistical Finance*, Quantitative Finance | ⚙️ (checklist of facts) | 03.7 | any daily prices |

## Phase 2 — First real reproductions (weeks 8–19)

| # | Paper | Role | Module | Data you need |
|---|---|---|---|---|
| 5 | French (1980), *Stock Returns and the Weekend Effect*, J. Financial Economics | 🧪 (first full mini-reproduction: day-of-week t-tests + multiple-testing audit) | 04.12 | index/ETF daily prices |
| 6 | Brown, Goetzmann, Ibbotson & Ross (1992), *Survivorship Bias in Performance Studies*, J. Finance | 📖 | 05.5 | none — demos with free data |
| 7 | Shumway (1997), *The Delisting Bias in CRSP's Nasdaq Data and Its Implications for the Size Effect*, J. Finance | 📖 | 05.8 | none — conceptual + demos |
| 8 | Fama & French (1992), *The Cross-Section of Expected Stock Returns*, J. Finance | 📖 + 🔨 (small sort/regression on your panel) | 06.16, 06.19 | your research panel |
| 9 | Fama & French (1993) — return of the king | 🧪 (build SMB/HML; validate vs official) | 07.10 | your panel + French library |
| 10 | Jegadeesh & Titman (1993) — full treatment | 🧪 (decile momentum, overlapping portfolios) | 07.15–17 | your panel |
| 11 | Carhart (1997), *On Persistence in Mutual Fund Performance*, J. Finance | ⚙️ (momentum factor, 4-factor model) | 07.19 | French library |
| 12 | Daniel & Moskowitz (2016), *Momentum Crashes*, J. Financial Economics | 📖 excerpt (skew, 2009) | 07.18 | index + panel |
| 13 | Fama & French (2015), *A Five-Factor Asset Pricing Model*, J. Financial Economics | 📖 + 🧪 (HML redundancy regressions) | 07.22–23 | French library |

## Phase 3 — Time series, volatility, pairs (weeks 20–31)

| # | Paper | Role | Module | Data you need |
|---|---|---|---|---|
| 14 | Granger & Newbold (1974), *Spurious Regressions in Econometrics*, J. Econometrics | 🧪 (reproduce by simulation — no data needed) | 08.10 | none — simulation |
| 15 | Lo & MacKinlay (1988), *Stock Market Prices Do Not Follow Random Walks*, Rev. Financial Studies | 🔨 (variance-ratio test on an index) | 08.21 | index daily prices |
| 16 | Engle (1982), *Autoregressive Conditional Heteroscedasticity…*, Econometrica | 📖 core + ⚙️ (ARCH(1) MLE by hand) | 09.1–2 | any daily prices |
| 17 | Bollerslev (1986), *Generalized Autoregressive Conditional Heteroskedasticity*, J. Econometrics | 📖 core + ⚙️ (GARCH(1,1) by hand + `arch`) | 09.3–4 | any daily prices |
| 18 | Engle & Granger (1987), *Co-Integration and Error Correction*, Econometrica | ⚙️ (2-step method) | 09.27 | pairs of prices |
| 19 | Gatev, Goetzmann & Rouwenhorst (2006), *Pairs Trading: Performance of a Relative-Value Arbitrage Rule*, RFS | 📖 + 🧪 (method on ETF/stock pairs) | 09.33, 10.15 | your panel |
| 20 | Moskowitz, Ooi & Pedersen (2012), *Time Series Momentum*, J. Financial Economics | 📖 + 🔨 (on ETF futures proxies) | 10.2–3 | ETF prices |
| 21 | Jegadeesh (1990), *Evidence of Predictable Behavior of Security Returns*, J. Finance; Lehmann (1990), *Fads, Martingales, and Market Efficiency*, QJE | 📖 + 🔨 (reversal pattern, survivorship audit) | 10.8–9 | your panel |
| 22 | Bernard & Thomas (1989), *Post-Earnings-Announcement Drift*, RFS | 📖 + approximation study | 10.19, 10.22 | earnings dates (yfinance) |
| 23 | Moreira & Muir (2017), *Volatility-Managed Portfolios*, J. Finance | 📖 + 🧪 (vol-scaled market & momentum) | 10.23–24 | index/ETF prices |
| 24 | Corwin & Schultz (2012), *A Simple Way to Estimate Bid-Ask Spreads from Daily Price Data*, J. Finance | ⚙️ (high-low spread estimator) | 10.26 | daily OHLC |

## Phase 4 — Portfolio, validation, ML, derivatives (weeks 32–46)

| # | Paper | Role | Module | Data you need |
|---|---|---|---|---|
| 25 | DeMiguel, Garlappi & Uppal (2009), *Optimal Versus Naive Diversification*, RFS | 🧪 (1/N vs optimized on ETFs) | 11.12 | ETF prices |
| 26 | Bailey & López de Prado (2014), *The Deflated Sharpe Ratio*, J. Portfolio Management | ⚙️ (implement, apply to snooped strategies) | 13.11 | your own backtests |
| 27 | Harvey, Liu & Zhu (2016), *…and the Cross-Section of Expected Returns*, RFS | 📖 (multiple testing, t>3) | 04.15, 07.26, 13.15 | none — read |
| 28 | McLean & Pontiff (2016), *Does Academic Research Destroy Stock Return Predictability?*, J. Finance | 📖 | 13.16 | none — read |
| 29 | Gu, Kelly & Xiu (2020), *Empirical Asset Pricing via Machine Learning*, RFS | 📖 + 🧪 scaled-down | 14.18–19 | your panel + a few features |
| 30 | Black & Scholes (1973), *The Pricing of Options and Corporate Liabilities*, J. Political Economy | 📖 core + ⚙️ (BS, Greeks, IV inversion) | 15.8 | option chains (yfinance) |
| 31 | Carr & Wu (2009), *Variance Risk Premiums*, RFS | 📖 + 🔨 (VIX vs subsequent RV) | 15.15 | VIX + index prices |
| 32 | Bondarenko (2014), *Variance Risk Premiums and Predictability of Returns*, J. Finance | 📖 | 15.16 | none — read |

## Why some famous papers are NOT here

- **Data-gated classics** (e.g., CRSP-heavy microstructure studies): not
  honestly reproducible with free data at this course's stage; the *methods*
  appear where free-data versions exist.
- **Fame ≠ pedagogy:** a paper earns its slot by what it teaches and by
  whether you can check it, not by citation count.
- **Deep theory first** (e.g., consumption-based asset pricing): the course
  teaches the empirical pipeline; theory enters through economic intuition
  (step 2) of each paper.

## Finding papers

DOIs resolve via any search engine; SSRN/author pages often host legitimate
free copies; university library access unlocks the rest. The Ken French Data
Library (free) is at
<https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html> —
`qrc.data.get_ff()` downloads the datasets directly.

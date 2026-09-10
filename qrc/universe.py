"""qrc.universe — ticker universes used throughout the course.

READ THIS BEFORE USING (module 05 will make you measure it):

Every list below is a *snapshot of today's survivors*. Historical backtests on
these universes carry survivorship bias: companies that went bankrupt, were
delisted, or were acquired are absent, and their often-terrible final returns
are invisible to you. The course uses these universes anyway — transparently —
because free data forces the trade-off, and because auditing that bias is
itself a core learning objective.

Universes
---------
core_etfs      : 12 liquid ETFs (equity indices, sectors, bonds, gold). Early
                 modules use these: diverse, liquid, almost no delisting risk.
research50     : 50 liquid US large caps with long histories. The workhorse
                 universe for cross-sectional projects (momentum, reversal,
                 factors). Deliberately survivorship-biased — audited in 05.
delisted_demo  : tickers that no longer exist (acquired/delisted). Used to
                 *show* what free data does and does not remember. Yahoo's
                 coverage of dead tickers is inconsistent — that inconsistency
                 is the lesson, not a bug to fix.
"""

from __future__ import annotations

CORE_ETFS = [
    "SPY",  # S&P 500
    "QQQ",  # Nasdaq-100
    "IWM",  # US small caps
    "GLD",  # gold
    "TLT",  # 20y treasuries
    "XLE",  # energy sector
    "XLF",  # financials
    "XLK",  # technology
    "XLI",  # industrials
    "XLP",  # consumer staples
    "XLU",  # utilities
    "XLV",  # health care
]

RESEARCH_50 = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA",
    "JPM", "BAC", "WFC", "GS", "MS",
    "XOM", "CVX", "COP", "SLB",
    "KO", "PEP", "PG", "JNJ", "PFE", "MRK", "LLY", "BMY", "UNH",
    "HD", "LOW", "WMT", "TGT", "COST", "MCD", "NKE", "SBUX", "DIS",
    "CMCSA", "V", "MA", "INTC", "AMD", "QCOM", "TXN", "AVGO",
    "ORCL", "IBM", "CSCO", "BA", "CAT", "GE", "LMT", "UPS",
]

# All of these once sat in major indices. None trade today under these symbols.
DELISTED_DEMO = [
    "TWX",   # Time Warner Inc.      — acquired by AT&T (2018)
    "CELG",  # Celgene               — acquired by Bristol-Myers Squibb (2019)
    "RTN",   # Raytheon              — merged into RTX (2020)
    "MON",   # Monsanto              — acquired by Bayer (2018)
    "AGN",   # Allergan              — acquired by AbbVie (2020)
    "LEH",   # Lehman Brothers       — bankrupt (2008)
]

_UNIVERSES = {
    "core_etfs": CORE_ETFS,
    "research50": RESEARCH_50,
    "delisted_demo": DELISTED_DEMO,
}


def load_universe(name: str) -> list[str]:
    """Return a course universe by name: 'core_etfs', 'research50', 'delisted_demo'."""
    try:
        return list(_UNIVERSES[name])
    except KeyError as e:
        raise ValueError(f"unknown universe {name!r}; available: {sorted(_UNIVERSES)}") from e

# Research Report — <Project / Paper, Author, Date>

*The standard write-up for every capstone (and a template for your own
research). Length: 4–8 pages. Precision beats volume. Every section is
mandatory; "we don't know yet" is an acceptable entry, an empty section is
not.*

## Research question

One paragraph. What did you set out to establish?

## Hypothesis

H₀ / H₁, stated before results. Reference your pre-registration (01_question
notebook) and note anything that changed after you saw data — with dates from
your research log.

## Economic intuition

Why should this exist? Who loses money to you, and why do they accept that?

## Data

Universe, frequency, period, sources, filters, cleaning decisions. Known
biases and their expected direction.

## Methodology

The method, in plain English first, then equations. The mapping from each
equation to code (file/cell references).

## Results

Key tables and figures. Separate **exploration** (informed your choices) from
**confirmation** (untouched data). Label them.

## Statistical significance

Test statistics, standard errors used (and why), p-values, and the
multiple-testing context (how many things did you or the literature try?).

## Economic significance

Expected return net of costs; Sharpe; turnover; how much capital could this
absorb; who can actually trade it.

## Trading implementation

Portfolio construction, rebalancing, execution assumptions, borrow/financing.

## Transaction costs

Model used, sensitivity of results to the cost assumption (the death-cost at
which the strategy is break-even).

## Out-of-sample results

Walk-forward / holdout results, honestly labeled. Sample sizes.

## Robustness tests

Subsamples, regimes, parameters, placebo tests, alternative specifications.
What broke, what survived.

## Limitations

Everything you know is wrong or incomplete with this study. Be specific.

## Possible biases

Checklist audit: look-ahead · leakage · survivorship · selection · data
snooping · overfitting · delisting · timestamps · corporate actions ·
unrealistic costs/liquidity.

## Conclusion

What you now believe, with what confidence, and why.

## Further research

The next three experiments you would run, in priority order.

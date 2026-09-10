# Day 13 — Review: Decode Real Paper Equations

Today's review has a single focus: **reading mathematical papers**. The
retrieval warm-ups and error-log triage are in `review.md`. The lesson is the
method, then the drills.

## The method for decoding an unfamiliar equation

1. **Identify the objects**: what is a scalar, a vector, a matrix? What are
   the indices and their ranges? (Subscripts carry the data structure.)
2. **Identify the operations**: sums (over what?), products (compounding?),
   expectations (over what randomness?), hats (estimates vs truths).
3. **Say it in words**, no symbols allowed.
4. **Write the loop** (pseudocode, indices explicit).
5. **Sanity-check dimensions**: does each product's inner dimension match?
   Does the output have the shape the surrounding text needs?

Do this to five equations and you'll never fear a methodology section again.

## The five drills (in exercise.ipynb)

1. **Expected return of a portfolio**: $\mathbb{E}[R_p] = \sum_i w_i \mathbb{E}[R_i]$
   — from Markowitz's world; say what it assumes about weights.
2. **Beta**: $\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$ —
   compute it for two assets; connect to day 11's slope (it IS the slope).
3. **The FF3 regression** (day 2's equation, now fully readable): write out
   the design matrix's columns for a given asset.
4. **Overlapping-portfolio return** (JT93): the month-$t$ return of a
   J-month strategy averages J portfolios formed at $t-J+1, \ldots, t$:
   $R_t = \frac{1}{J}\sum_{j=1}^{J} R^{(j)}_t$ — write the loop; explain why
   this smooths but also *serially correlates* the strategy's returns
   (module 04's HAC standard errors exist for exactly this).
5. **Sample skewness**:
   $g = \frac{1}{T}\sum_t \left(\frac{r_t - \bar{r}}{s}\right)^3$ — decode,
   implement, and explain what it measures (module 03 formalizes).

## Common mistakes

- Skipping step 5 (dimension checks) — most misread equations are shape
  errors.
- Reading expectations as guarantees ("E[R]=0.4% so I'll make 0.4%"):
  expectation is a *center of a distribution*, not a promise (module 02).

**Self-check:** decode any equation in Fama & French (1993) §? you choose —
the four steps, in writing.

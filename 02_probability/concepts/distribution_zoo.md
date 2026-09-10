# The Distribution Zoo (only the residents you'll actually meet)

## Bernoulli(p)
One trial, success probability p. Values {0, 1}.
E = p, Var = p(1−p). *Trading:* win/lose a day, a trade, a signal firing.

## Binomial(n, p)
Number of successes in n independent Bernoulli trials.
E = np, Var = np(1−p). *Trading:* "how many winning days in a year?" —
P(k wins in 252 days) with p = 0.5.

## Normal(μ, σ²)
The bell curve. Symmetric, thin tails (99.7% within 3σ).
*Trading:* the *approximation* every textbook makes and every crash
refutes. Useful for: sample means (CLT), log-returns over longer horizons,
modeling assumptions you will *test*, not trust.

## Standard normal Z
Normal(0, 1). z = (x − μ)/σ. The reference scale: "a −3σ day" is a z-score.
68-95-99.7 rule. *Everything* in inference (module 04) is measured on this scale.

## Student-t (mention)
Heavier tails than normal. Daily stock returns look much more like
standardized t(3–6) than normal — kurtosis 6–15 vs 3. (Module 03 measures;
module 09 uses t-innovations in GARCH.)

## Lognormal (mention)
If log-returns are normal, *prices* are lognormal: positive by construction,
right-skewed. This is why we do statistics in log space and money in levels.

## What you will NOT meet here
No Poisson queues, no exponential inter-arrivals, no beta priors — they
enter the course only if a paper drags one in (and when one does, it gets a
concept sheet of its own).

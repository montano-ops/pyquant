# Day 2 — Your Toolkit, Tested

## Warm-up retrieval (no notes)

1. From memory: what are the five rules of engagement?
2. What does `qrc` provide, and what does it deliberately *not* provide?
3. What is the 15-minute rule?

## 1. Why this day exists

This course assumes you know pandas and will not teach it. But research uses
pandas in specific, sometimes surprising ways, and being "fluent" in general
is not the same as being fast and *correct* on these operations. Today you
run a diagnostic: ~12 tasks, all of which appear in every empirical paper's
data section. Anything that takes you more than ~10 minutes or that you get
*wrong* (not slow — wrong) gets a targeted review pointer in the solution.

## 2. The operations research actually needs

**Slicing by date.** Papers say "sample period 1990–2020". In code:

```python
px = px.loc["2010-01-01":"2020-12-31"]        # label-based, both ends inclusive
```

Watch the inclusive ends — `iloc` slicing is not, and mixing them silently
changes sample periods between studies.

**Returns from prices.** The course convention (see
[conventions](../../concepts/course_conventions.md)):

```python
rets = px["SPY"].pct_change()          # simple returns, today's convention
```

`pct_change()` produces a NaN in the first row. Decide about NaNs *on
purpose*: `dropna()` here, because a NaN return means "no prior price", not
"missing data" — those are different things (module 05 hammers this).

**Annualizing.** Daily volatility → annual: multiply by √252 (why 252? why a
square root? module 02 answers both properly; for now, both are conventions
you must apply consistently).

```python
ann_vol = rets.std() * np.sqrt(252)
```

**Changing frequency.** Weekly returns from daily prices — *resample prices,
then take returns*, or aggregate daily returns over the week? Both appear in
papers; they differ in exactly one way you should notice today and understand
in module 01 (compounding):

```python
weekly_from_prices = px.resample("W-FRI").last().pct_change()
weekly_sum_of_logs = np.log(px).diff().resample("W-FRI").sum()   # log returns add!
```

**Rolling calculations.** Rolling volatility is the workhorse of empirical
finance:

```python
rolling_vol = rets.rolling(63).std() * np.sqrt(252)   # ~quarterly window
```

Rolling statistics answer "when?" — a static mean answers nothing about
stability, and stability is usually the question (module 03).

**Aligning assets.** Two assets with different histories:

```python
both = px[["SPY", "TLT"]].dropna()      # intersection — or .join(how="outer")?
```

Inner join = "only dates where both traded" (safe for comparisons); outer
join = "everything, NaN where missing" (needed for panels, dangerous for
pairwise stats). Papers' universes are built from exactly this choice.

## 3. A spot-the-bug preview (you'll see this again)

```python
rets = px.pct_change()
signal = rets.rolling(5).mean()          # 5-day momentum
strategy = (signal * rets).sum(axis=1)   # ← bug: today's signal × today's return
```

Even without knowing backtesting: *you compute the signal using day t's
return, then claim day t's return from it.* You'd be trading on information
you only have after the close. The fix is `signal.shift(1)`. This is
**look-ahead bias**, and it is the single most common way backtests lie. File
it; modules 08, 12, and 13 are largely about never doing this again.

## 4. Common mistakes on today's diagnostic

- `px.resample("W").last()` — ambiguous week end; use `"W-FRI"`.
- Computing returns *then* resampling with `.mean()` — averaging returns is
  almost never what anyone means.
- `rolling(63).std()` on prices instead of returns (units nonsense).
- Forgetting `dropna()` after `pct_change()` and letting one NaN poison a
  rolling window (63 NaNs, in fact).

## 5. Research connection

Open any empirical paper and find the "Data" section: *"We use daily closing
prices for NYSE/AMEX stocks from 1965–1989…"* Every clause maps to today's
operations: universe (columns), frequency (resample), period (slice), and
cleaning rules (NaN policy). When you reproduce a paper, you start by writing
*their* data section in *your* pandas — and the choices in this lesson are
where reproduction errors begin.

## 6. Reflection

1. Which diagnostic tasks felt automatic, and which required thought? The
   second list is your targeted review set.
2. The look-ahead bug in §3: in your own words, why is `signal.shift(1)` the
   fix, and what exactly does the unshifted version claim you knew?

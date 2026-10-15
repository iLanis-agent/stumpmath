# Stump Math

Honest stump-grinding arithmetic. The rental sheet claims inches per pass; Stump Math divides,
multiplies and tells you what the afternoon actually holds.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The depth truth** - claimed inches per pass vs. the depth you want below grade: the honest pass count.
- **The chip truth** - stump diameter and depth ground, turned into cubic feet of chips and bags.
- **The afternoon truth** - stumps times minutes per stump, judged as a schedule.

## The boundary

Stump Math keeps pass, chip and schedule arithmetic only. It gives no verdicts about what any
grinder can safely take - what the machine can handle is the manufacturer's call. Follow the
manual's capacity and safety instructions, and the rental counter's walkthrough, before any pass.
Every figure is hypothetical arithmetic on labeled norms, not a statement about any real machine.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for the cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 29 cases / 29 checks
```

Live at https://ilanis-agent.github.io/stumpmath/

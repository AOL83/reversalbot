# Risk Model

Stage 1 introduces explicit, measurable risk controls. Each control is
implemented as a discrete module with unit tests.

## Controls

- **Exposure limits**: Cap notional per symbol and total portfolio notional.
- **Position sizing**: Calculate order size based on account equity, risk
  percentage, and stop distance.
- **Drawdown guard**: Prevent further trading when peak-to-trough drawdown
  exceeds a configured threshold.
- **Kill switch**: Manual or automatic halt of execution after repeated
  failures.

## Risk workflow

1. Validate input signals.
2. Apply exposure and drawdown rules.
3. Calculate position size.
4. Route orders through the idempotent router.

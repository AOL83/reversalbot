# Risk Model (Stage 1)

Stage 1 defines **capital protection** rules and validates them through tests.

## Risk per trade
- Use fixed fractional risk (e.g., 0.5% of equity).
- Position size is computed from risk and stop distance.
- Never exceed configured maximum size or exposure caps.

## Exposure caps
- Max notional exposure per symbol.
- Max total notional exposure across portfolio.
- Risk checks reject orders that exceed caps.

## Drawdown guards
- Track equity peak.
- Trigger a kill switch if drawdown exceeds thresholds.

## Daily/weekly loss guards (Stage 2+)
- Daily and weekly loss caps will enforce time-based recovery.

## Stop layers
- **Hard stop** is mandatory (intent recorded even in mock mode).
- Optional time-based and volatility-based stop intents.

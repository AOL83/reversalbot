# Backtesting Specification

Stage 1 does not include a backtesting engine. The scaffold must, however,
prepare for it by maintaining deterministic order flow and clean separation
between strategy and execution.

## Requirements

- All decision inputs are logged.
- Order routing is deterministic.
- Risk checks are deterministic and unit-tested.

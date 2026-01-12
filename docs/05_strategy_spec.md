# Strategy Specification

Stage 1 does not implement real trading logic. The strategy layer is mocked to
exercise risk controls and the execution pipeline.

## Responsibilities

- Emit deterministic signals for testing.
- Provide traceable inputs for risk evaluation.
- Avoid any live market connectivity.

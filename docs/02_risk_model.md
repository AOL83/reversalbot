# Risk Model

Stage 1 provides foundational risk utilities:

- **Position sizing** based on equity, risk-per-trade, and stop distance.
- **Exposure limits** per-symbol and total notional caps.
- **Drawdown guard** that disables trading beyond configured drawdown.
- **Kill switch** states: active, paused, and killed.

These utilities must be enforced by the order router and manual controls.

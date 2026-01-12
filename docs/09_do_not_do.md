# Do Not Do (Anti-Patterns)

These are explicit failure patterns. If you see them in code or specs, stop and
fix immediately.

## This will blow you up
- Martingale, grid, or averaging-down schemes.
- No daily loss cap or drawdown guard.
- Trading during spread spikes or news without filters.
- Relying on a single stop without exchange-side protection concepts.
- Overleveraging or uncapped pyramiding.
- Ignoring slippage/fees in tests.
- 1m scalping without liquidity/spread guardrails.
- No idempotency or duplicate order protection.
- No monitoring or alerts.
- Editing strategy rules without updating specs/tests.

## Additional anti-patterns
- Disabling kill switch to "keep trading".
- Using live credentials in local configs.
- Ignoring partial fills or cancel/replace state.

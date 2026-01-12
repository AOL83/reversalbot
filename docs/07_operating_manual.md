# Operating Manual

## Startup
1. Validate config with `poetry run reversalbot --config <path> status`.
2. Use `run` once health checks are green.

## Emergency actions
- `pause` to stop new orders.
- `flatten` to close all positions.
- `kill` to lock trading until a manual reset.

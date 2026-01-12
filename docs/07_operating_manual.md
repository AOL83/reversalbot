# Operating Manual

## Running locally
```bash
poetry run reversalbot run --config configs/config.local.yaml
```

## Manual controls
- `pause`: stop new orders (positions can still be flattened).
- `resume`: resume order flow.
- `flatten`: close all open positions immediately.
- `kill`: trigger kill switch and flatten.
- `reset-kill`: unlock after explicit acknowledgment.

## Incident checklist
1. Kill the system and flatten all positions.
2. Snapshot logs and config.
3. Identify whether a kill trigger fired (risk/anomaly).
4. Document root cause and update specs/tests before resuming.

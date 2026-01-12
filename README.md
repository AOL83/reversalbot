# ReversalBot (Stage 1)

ReversalBot Stage 1 delivers a risk-first scaffold for a systematic trading system.
This stage focuses on configuration validation, safety controls, and mocked execution.
No real broker integrations or strategies are included.

## Goals
- Strict configuration validation with YAML + environment overrides.
- Safety controls: kill switch, pause/resume, flatten, and drawdown guard.
- Mocked execution path with idempotency guarantees.
- Monitoring hooks for anomaly detection and health checks.

## Non-Goals (Stage 1)
- No live exchange or broker connectors.
- No strategy or alpha logic.
- No full backtesting engine (only specs for Stage 2+).

## Quickstart
```bash
poetry install
poetry run reversalbot --config configs/config.example.yaml status
```

## CLI
```bash
poetry run reversalbot --config <path> run
poetry run reversalbot --config <path> status
poetry run reversalbot --config <path> pause
poetry run reversalbot --config <path> resume
poetry run reversalbot --config <path> flatten
poetry run reversalbot --config <path> kill
poetry run reversalbot --config <path> reset-kill
```

## Configuration
See `configs/README.md` and `configs/config.example.yaml` for schema and examples.
Environment overrides are supported via:

```
REVERSALBOT__SECTION__FIELD=value
```

## Development
```bash
poetry install
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy .
poetry run pytest -q
```

## License
MIT

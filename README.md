# ReversalBot (Stage 1 Scaffold)

ReversalBot is a **safety-first trading system scaffold** for cross-market execution (Forex + Crypto planned). Stage 1 focuses on **risk protection, kill-switch governance, and mock execution**—not strategy logic or live broker connectivity.

## What it is
- A production-grade repository structure with risk controls, safety specs, and mock execution.
- A minimal CLI to demonstrate **pause, resume, flatten, and kill** workflows.
- Spec-first documentation that defines rules before implementation.

## What it is **not** (Stage 1)
- No strategy/alpha logic.
- No real exchange/broker APIs.
- No full backtesting engine (interfaces and specs only).

## Safety-first foundations
- Hard-stop intent required for positions (even in mock mode).
- Kill switch with manual + auto triggers.
- Exposure limits, drawdown guards, and anomaly detection stubs.

## Repository structure
```
configs/                 # Example configuration and precedence
src/reversalbot/         # Source code
  risk/                  # Safety and risk models
  execution/             # Broker interfaces + mock execution
  monitoring/            # Alerts, anomaly detection, health
  manual_control/        # Pause/flatten/kill workflows
  main.py                # CLI entrypoint
  config.py              # Pydantic configuration
  logging.py             # Structured logging
  errors.py              # Custom exceptions

Docs
  docs/01_philosophy.md
  docs/02_risk_model.md
  docs/03_failure_modes.md
  docs/04_execution_spec.md
  docs/05_strategy_spec.md
  docs/06_backtesting_spec.md
  docs/07_operating_manual.md
  docs/08_glossary.md
  docs/09_do_not_do.md
```

## Quickstart
1) Install dependencies:
```bash
poetry install
```

2) Copy and edit config:
```bash
cp configs/config.example.yaml configs/config.local.yaml
```

3) Run the CLI using the mock broker:
```bash
poetry run reversalbot run --config configs/config.local.yaml
```

4) Use manual controls:
```bash
poetry run reversalbot status --config configs/config.local.yaml
poetry run reversalbot pause --config configs/config.local.yaml
poetry run reversalbot resume --config configs/config.local.yaml
poetry run reversalbot flatten --config configs/config.local.yaml
poetry run reversalbot kill --config configs/config.local.yaml
poetry run reversalbot reset-kill --config configs/config.local.yaml
```

## Modes
- **Manual mode (Stage 1)**: safety controls + mock execution.
- **Auto mode (Stage 2+)**: planned for strategy-driven execution.

## Stage plan
- **Stage 1 (current)**: risk foundations, kill switch, mock broker, CLI, tests, CI.
- **Stage 2**: strategy interface, signals, backtesting specifications, paper trading.
- **Stage 3**: live connectors, operational hardening, advanced monitoring.

## Disclaimer
This repository is educational and for scaffolding purposes only. It does **not** connect to live markets or provide investment advice.

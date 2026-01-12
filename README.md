# ReversalBot Stage 1 Scaffold

This branch provides the Stage 1 scaffold for ReversalBot. It includes risk
controls, anomaly detection, and mock execution. It does **not** place real
trades or contain live strategy logic.

## Quickstart

### 1) Install dependencies

```bash
pipx install poetry
poetry install
```

### 2) Configure

```bash
cp configs/config.example.yaml configs/config.yaml
```

Update `configs/config.yaml` as needed. Environment overrides are supported via
`REVERSALBOT__SECTION__KEY`.

### 3) Run the CLI

```bash
poetry run python -m reversalbot.cli --config configs/config.yaml
```

## Quality gates

```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy .
poetry run pytest -q
```

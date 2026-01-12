# Contributing to ReversalBot

Thanks for your interest in improving ReversalBot. This project is **spec-first** and safety-first.

## How to contribute
1. Read the docs in `docs/` and ensure your changes align with the risk model.
2. Open an issue to discuss any significant change.
3. Keep changes small and focused.

## Development setup
```bash
poetry install
```

## Quality gates
All changes must pass:
```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy .
poetry run pytest -q
```

## Style guide
- Python 3.12+
- Type hints everywhere
- Small modules and functions
- Update docs and tests alongside code changes

## Reporting security issues
Please see [SECURITY.md](SECURITY.md).

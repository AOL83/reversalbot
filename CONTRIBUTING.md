# Contributing

Thanks for your interest in ReversalBot.

## Development setup
1. Install Poetry.
2. Run `poetry install`.
3. Run the quality gates:
   - `poetry run ruff check .`
   - `poetry run ruff format --check .`
   - `poetry run mypy .`
   - `poetry run pytest -q`

## Pull requests
- Keep changes focused.
- Include tests for new behaviors.
- Ensure all quality gates pass locally.

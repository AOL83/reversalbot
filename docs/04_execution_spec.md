# Execution Spec (Stage 1)

Execution is mocked and deterministic.

- Orders are routed through an idempotent router.
- Kill switch and pause/resume states are enforced.
- Stop intent validation runs before broker submission.
- Mock broker maintains in-memory positions.

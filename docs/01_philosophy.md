# Stage 1 Philosophy

Stage 1 is a safety-first scaffold. It proves the structure of the system without
placing real trades. The emphasis is on guardrails, observability, and idempotent
execution so the core workflow can be exercised safely.

## Principles

1. **Risk before returns**: Every decision is bounded by exposure, drawdown, and
   kill-switch controls.
2. **Deterministic behavior**: Given the same inputs, the system produces the
   same outputs. This supports reproducible testing and incident analysis.
3. **Separation of concerns**: Strategy logic is isolated from execution and
   from safety systems.
4. **Auditability**: Every decision should be inspectable through logs and
   retained state.

## Non-goals

- Live trading
- Optimization
- Complex strategy logic

# Strategy Spec (Stage 2+)

Stage 1 contains **no strategy logic**. This document defines the future
interface only.

## Strategy module requirements
- Expose a `Strategy` interface that produces **orders** and **stop intents**.
- Accept market data and account context without side effects.
- Be deterministic for backtesting and simulation.
- Provide a versioned spec for any rule changes.

## Data inputs (Stage 2+)
- Bar data, ticks, and microstructure metrics.
- News/volatility flags (optional).

## Outputs
- Order intents with explicit risk metadata.
- Rationale metadata for monitoring and audits.

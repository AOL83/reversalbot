# Backtesting Spec (Stage 2+)

Stage 1 does not implement a backtest engine. This document defines
requirements only.

## Required features
- Fee and slippage models
- Order latency simulation
- Partial fill modeling
- Portfolio accounting with margin
- Time-based risk guards

## Validation
- Run tests against known fixtures.
- Include regression tests for past incidents.

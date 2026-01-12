"""Generic anomaly detection for Stage 1."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnomalyThresholds:
    max_spread_bps: int
    max_slippage_bps: int
    max_error_rate: float


@dataclass(frozen=True)
class AnomalyMetrics:
    spread_bps: int
    slippage_bps: int
    error_rate: float


def detect_anomalies(metrics: AnomalyMetrics, thresholds: AnomalyThresholds) -> list[str]:
    triggers: list[str] = []
    if metrics.spread_bps > thresholds.max_spread_bps:
        triggers.append("spread")
    if metrics.slippage_bps > thresholds.max_slippage_bps:
        triggers.append("slippage")
    if metrics.error_rate > thresholds.max_error_rate:
        triggers.append("error_rate")
    return triggers

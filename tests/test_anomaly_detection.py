from __future__ import annotations

from reversalbot.monitoring.anomaly_detection import (
    AnomalyMetrics,
    AnomalyThresholds,
    detect_anomalies,
)


def test_detect_anomalies() -> None:
    thresholds = AnomalyThresholds(max_spread_bps=10, max_slippage_bps=5, max_error_rate=0.02)
    metrics = AnomalyMetrics(spread_bps=15, slippage_bps=1, error_rate=0.03)
    triggers = detect_anomalies(metrics, thresholds)
    assert "spread" in triggers
    assert "error_rate" in triggers
    assert "slippage" not in triggers

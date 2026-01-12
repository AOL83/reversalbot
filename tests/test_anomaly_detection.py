from __future__ import annotations

from reversalbot.monitoring.anomaly_detection import AnomalyDetector


def test_anomaly_detection_flags_limits() -> None:
    detector = AnomalyDetector(max_spread_bps=5.0, max_slippage_bps=6.0, max_error_rate=0.02)
    issues = detector.evaluate(spread_bps=10.0, slippage_bps=1.0, error_rate=0.01)
    assert "spread_bps" in issues

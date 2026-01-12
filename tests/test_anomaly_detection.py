from __future__ import annotations

import pytest

from reversalbot.monitoring.anomaly_detection import AnomalyDetector


def test_anomaly_detection_detects_gap() -> None:
    detector = AnomalyDetector(max_price_gap_pct=5.0)

    assert detector.detect_price_gap(100.0, 106.0) is True


def test_anomaly_detection_requires_positive_previous() -> None:
    detector = AnomalyDetector(max_price_gap_pct=5.0)

    with pytest.raises(ValueError):
        detector.detect_price_gap(0.0, 100.0)

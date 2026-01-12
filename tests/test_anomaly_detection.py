from __future__ import annotations

from reversalbot.monitoring.anomaly import detect_anomalies


def test_detect_anomalies_flags_price_spike() -> None:
    result = detect_anomalies(
        previous_price=100.0,
        current_price=120.0,
        previous_volume=1000.0,
        current_volume=1500.0,
        max_price_change_pct=10.0,
        max_volume_spike=3.0,
    )

    assert result.triggered
    assert "price_change" in result.reasons

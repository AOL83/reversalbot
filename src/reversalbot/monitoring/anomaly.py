from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnomalyResult:
    triggered: bool
    reasons: list[str]


def detect_anomalies(
    *,
    previous_price: float,
    current_price: float,
    previous_volume: float,
    current_volume: float,
    max_price_change_pct: float,
    max_volume_spike: float,
) -> AnomalyResult:
    reasons: list[str] = []
    if previous_price > 0:
        price_change_pct = abs((current_price - previous_price) / previous_price) * 100
        if price_change_pct > max_price_change_pct:
            reasons.append("price_change")
    if previous_volume > 0:
        volume_ratio = current_volume / previous_volume
        if volume_ratio > max_volume_spike:
            reasons.append("volume_spike")
    return AnomalyResult(triggered=bool(reasons), reasons=reasons)

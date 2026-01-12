from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AnomalyDetector:
    max_price_gap_pct: float

    def detect_price_gap(self, previous_price: float, new_price: float) -> bool:
        if previous_price <= 0:
            raise ValueError("previous_price must be positive")
        gap_pct = abs(new_price - previous_price) / previous_price * 100
        return gap_pct >= self.max_price_gap_pct

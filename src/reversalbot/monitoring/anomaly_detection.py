from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnomalyDetector:
    max_spread_bps: float
    max_slippage_bps: float
    max_error_rate: float

    def evaluate(self, spread_bps: float, slippage_bps: float, error_rate: float) -> list[str]:
        issues: list[str] = []
        if spread_bps > self.max_spread_bps:
            issues.append("spread_bps")
        if slippage_bps > self.max_slippage_bps:
            issues.append("slippage_bps")
        if error_rate > self.max_error_rate:
            issues.append("error_rate")
        return issues

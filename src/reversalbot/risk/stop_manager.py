"""Stop intent validation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class StopIntent:
    hard_stop_price: float
    time_stop: timedelta | None = None
    volatility_stop_pct: float | None = None

    def validate(self) -> None:
        if self.hard_stop_price <= 0:
            raise ValueError("Hard stop price must be positive.")
        if self.time_stop is not None and self.time_stop.total_seconds() <= 0:
            raise ValueError("Time stop must be positive.")
        if self.volatility_stop_pct is not None and self.volatility_stop_pct <= 0:
            raise ValueError("Volatility stop must be positive.")

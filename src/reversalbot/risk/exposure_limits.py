"""Exposure limit checks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExposureLimits:
    max_notional_per_symbol: float
    max_total_notional: float

    def check(self, symbol_notional: float, total_notional: float) -> bool:
        if symbol_notional > self.max_notional_per_symbol:
            return False
        if total_notional > self.max_total_notional:
            return False
        return True

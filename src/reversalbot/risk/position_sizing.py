from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PositionSizer:
    risk_per_trade_pct: float
    max_notional: float

    def size_position(self, equity: float, entry_price: float, stop_price: float) -> float:
        if equity <= 0 or entry_price <= 0:
            return 0.0
        stop_distance = abs(entry_price - stop_price)
        if stop_distance <= 0:
            return 0.0
        risk_amount = equity * (self.risk_per_trade_pct / 100)
        quantity = risk_amount / stop_distance
        notional = quantity * entry_price
        if notional > self.max_notional:
            quantity = self.max_notional / entry_price
        return max(quantity, 0.0)

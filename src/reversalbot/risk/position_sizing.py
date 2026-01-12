from __future__ import annotations


def size_position(equity: float, risk_pct: float, stop_distance_pct: float) -> float:
    if stop_distance_pct <= 0:
        raise ValueError("stop_distance_pct must be positive")
    risk_amount = equity * (risk_pct / 100)
    position_size = risk_amount / (stop_distance_pct / 100)
    return position_size

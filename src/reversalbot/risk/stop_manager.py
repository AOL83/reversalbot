from __future__ import annotations


def compute_stop_price(entry_price: float, stop_distance_pct: float, side: str) -> float:
    if stop_distance_pct <= 0:
        raise ValueError("stop_distance_pct must be positive")
    if side not in {"long", "short"}:
        raise ValueError("side must be 'long' or 'short'")
    distance = entry_price * (stop_distance_pct / 100)
    return entry_price - distance if side == "long" else entry_price + distance

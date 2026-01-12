from __future__ import annotations


def calculate_position_size(
    account_equity: float,
    risk_per_trade: float,
    stop_distance: float,
) -> float:
    if account_equity <= 0:
        msg = "Account equity must be positive"
        raise ValueError(msg)
    if risk_per_trade <= 0 or risk_per_trade >= 1:
        msg = "Risk per trade must be between 0 and 1"
        raise ValueError(msg)
    if stop_distance <= 0:
        msg = "Stop distance must be positive"
        raise ValueError(msg)
    risk_amount = account_equity * risk_per_trade
    return risk_amount / stop_distance

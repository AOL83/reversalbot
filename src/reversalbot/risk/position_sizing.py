"""Deterministic position sizing."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PositionSizingResult:
    size: float
    risk_amount: float


def calculate_position_size(
    equity: float,
    risk_fraction: float,
    stop_distance: float,
    price: float,
    max_size: float | None = None,
) -> PositionSizingResult:
    if equity <= 0:
        raise ValueError("Equity must be positive.")
    if risk_fraction <= 0 or risk_fraction > 1:
        raise ValueError("Risk fraction must be within (0, 1].")
    if stop_distance <= 0:
        raise ValueError("Stop distance must be positive.")
    if price <= 0:
        raise ValueError("Price must be positive.")

    risk_amount = equity * risk_fraction
    raw_size = risk_amount / stop_distance
    if max_size is not None:
        raw_size = min(raw_size, max_size)
    size = raw_size / price
    return PositionSizingResult(size=size, risk_amount=risk_amount)

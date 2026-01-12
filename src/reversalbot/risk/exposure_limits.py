from __future__ import annotations


def within_exposure_limits(
    current_symbol_notional: float,
    current_total_notional: float,
    proposed_notional: float,
    max_notional_per_symbol: float,
    max_total_notional: float,
) -> bool:
    symbol_total = current_symbol_notional + proposed_notional
    total = current_total_notional + proposed_notional
    return symbol_total <= max_notional_per_symbol and total <= max_total_notional

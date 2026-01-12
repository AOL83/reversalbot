from __future__ import annotations


def within_exposure_limit(current_exposure: float, max_exposure: float) -> bool:
    return current_exposure <= max_exposure

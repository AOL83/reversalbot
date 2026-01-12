from __future__ import annotations

from reversalbot.risk.position_sizing import calculate_position_size


def test_position_sizing_basic() -> None:
    result = calculate_position_size(
        equity=10000,
        risk_fraction=0.01,
        stop_distance=100,
        price=50,
    )
    assert result.risk_amount == 100
    assert result.size == 0.02

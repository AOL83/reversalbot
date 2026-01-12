from __future__ import annotations

from reversalbot.risk.position_sizing import calculate_position_size


def test_position_sizing() -> None:
    size = calculate_position_size(account_equity=10000.0, risk_per_trade=0.01, stop_distance=50.0)
    assert size == 2.0

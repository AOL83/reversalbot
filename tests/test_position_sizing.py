from __future__ import annotations

from reversalbot.risk.position_sizing import PositionSizer


def test_position_sizing_caps_notional() -> None:
    sizer = PositionSizer(risk_per_trade_pct=1.0, max_notional=1000.0)

    quantity = sizer.size_position(equity=10000.0, entry_price=50.0, stop_price=45.0)

    assert quantity * 50.0 <= 1000.0
    assert quantity > 0

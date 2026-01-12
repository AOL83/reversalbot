from __future__ import annotations

import pytest

from reversalbot.risk.position_sizing import size_position


def test_size_position() -> None:
    position = size_position(equity=10000.0, risk_pct=1.0, stop_distance_pct=2.0)
    assert position == 5000.0


def test_size_position_invalid_stop() -> None:
    with pytest.raises(ValueError):
        size_position(equity=10000.0, risk_pct=1.0, stop_distance_pct=0.0)

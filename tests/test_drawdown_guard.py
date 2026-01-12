from __future__ import annotations

from reversalbot.risk.drawdown_guard import DrawdownGuard


def test_drawdown_guard_trips() -> None:
    guard = DrawdownGuard(max_drawdown_pct=10.0)

    assert guard.update(100.0)
    assert guard.update(95.0)
    assert not guard.update(85.0)
    assert guard.tripped

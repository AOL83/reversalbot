from __future__ import annotations

from reversalbot.risk.drawdown_guard import DrawdownGuard


def test_drawdown_guard_blocks_excessive_drawdown() -> None:
    guard = DrawdownGuard(max_drawdown_pct=10.0)
    assert guard.update(100.0) is True
    assert guard.update(95.0) is True
    assert guard.update(89.0) is False

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DrawdownGuard:
    max_drawdown_pct: float
    peak_equity: float = 0.0
    tripped: bool = False

    def update(self, equity: float) -> bool:
        if equity <= 0:
            return False
        if equity > self.peak_equity:
            self.peak_equity = equity
        drawdown_pct = ((self.peak_equity - equity) / self.peak_equity) * 100
        if drawdown_pct > self.max_drawdown_pct:
            self.tripped = True
        return not self.tripped

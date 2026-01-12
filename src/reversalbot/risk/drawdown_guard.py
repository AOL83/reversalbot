from __future__ import annotations


class DrawdownGuard:
    def __init__(self, max_drawdown_pct: float) -> None:
        if max_drawdown_pct <= 0:
            msg = "Max drawdown percent must be positive"
            raise ValueError(msg)
        self.max_drawdown_pct = max_drawdown_pct
        self.peak_equity = 0.0

    def update(self, current_equity: float) -> bool:
        if current_equity < 0:
            msg = "Equity cannot be negative"
            raise ValueError(msg)
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
        if self.peak_equity == 0:
            return True
        drawdown_pct = ((self.peak_equity - current_equity) / self.peak_equity) * 100
        return drawdown_pct <= self.max_drawdown_pct

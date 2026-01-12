from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StopIntent:
    stop_price: float
    take_profit_price: float | None = None
    validated: bool = False

    def validate(self) -> None:
        if self.stop_price <= 0:
            msg = "Stop price must be positive"
            raise ValueError(msg)
        if self.take_profit_price is not None and self.take_profit_price <= 0:
            msg = "Take profit price must be positive"
            raise ValueError(msg)
        self.validated = True

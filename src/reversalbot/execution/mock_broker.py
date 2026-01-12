from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Order:
    symbol: str
    side: str
    quantity: float
    price: float


@dataclass
class Fill:
    symbol: str
    side: str
    quantity: float
    price: float


@dataclass
class Position:
    symbol: str
    quantity: float
    average_price: float


class MockBroker:
    def __init__(self, slippage_bps: float = 0.0, spread_bps: float = 0.0) -> None:
        self.slippage_bps = slippage_bps
        self.spread_bps = spread_bps
        self.positions: dict[str, Position] = {}

    def submit_order(self, order: Order) -> Fill:
        exec_price = self._execution_price(order)
        fill = Fill(
            symbol=order.symbol,
            side=order.side.upper(),
            quantity=order.quantity,
            price=exec_price,
        )
        self._apply_fill(fill)
        return fill

    def _execution_price(self, order: Order) -> float:
        price = order.price
        adjustment = (self.slippage_bps + self.spread_bps) / 10000.0
        if order.side.upper() == "BUY":
            return price * (1 + adjustment)
        return price * (1 - adjustment)

    def _apply_fill(self, fill: Fill) -> None:
        delta = fill.quantity if fill.side == "BUY" else -fill.quantity
        position = self.positions.get(fill.symbol)
        if position is None:
            if delta != 0:
                self.positions[fill.symbol] = Position(
                    symbol=fill.symbol,
                    quantity=delta,
                    average_price=fill.price,
                )
            return

        old_qty = position.quantity
        new_qty = old_qty + delta
        if new_qty == 0:
            del self.positions[fill.symbol]
            return

        old_sign = _sign(old_qty)
        delta_sign = _sign(delta)
        new_sign = _sign(new_qty)

        if old_sign != 0 and delta_sign != 0 and old_sign != delta_sign:
            if new_sign == old_sign:
                position.quantity = new_qty
                return
            position.quantity = new_qty
            position.average_price = fill.price
            return

        position.average_price = (
            position.average_price * abs(old_qty) + fill.price * abs(delta)
        ) / abs(new_qty)
        position.quantity = new_qty


def _sign(value: float) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

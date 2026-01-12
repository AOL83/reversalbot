from __future__ import annotations

from dataclasses import replace

from reversalbot.domain.models import Side, Symbol
from reversalbot.execution.interfaces import Broker, Fill, Order, Position, build_fill


class MockBroker(Broker):
    def __init__(self, base_currency: str = "USD") -> None:
        self.base_currency = base_currency
        self._positions: dict[str, Position] = {}

    def submit_order(self, order: Order) -> Fill:
        fill = build_fill(order)
        symbol_key = order.symbol.value
        position = self._positions.get(symbol_key)
        if order.side == Side.BUY:
            position = self._apply_buy(position, order)
        else:
            position = self._apply_sell(position, order)
        if position is None or position.quantity == 0:
            self._positions.pop(symbol_key, None)
        else:
            self._positions[symbol_key] = position
        return fill

    def positions(self) -> list[Position]:
        return list(self._positions.values())

    def flatten(self) -> None:
        self._positions.clear()

    def _apply_buy(self, position: Position | None, order: Order) -> Position:
        if position is None:
            return Position(symbol=order.symbol, quantity=order.quantity, average_price=order.price)
        new_qty = position.quantity + order.quantity
        weighted_price = (
            position.average_price * position.quantity + order.price * order.quantity
        ) / new_qty
        return replace(position, quantity=new_qty, average_price=weighted_price)

    def _apply_sell(self, position: Position | None, order: Order) -> Position | None:
        if position is None:
            return Position(
                symbol=order.symbol,
                quantity=-order.quantity,
                average_price=order.price,
            )
        new_qty = position.quantity - order.quantity
        return replace(position, quantity=new_qty, average_price=position.average_price)


def build_symbol(value: str) -> Symbol:
    return Symbol(value=value)

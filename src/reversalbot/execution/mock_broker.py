"""Mock broker for Stage 1 execution."""

from __future__ import annotations

from dataclasses import dataclass, field

from reversalbot.execution.interfaces import Fill, Order, OrderSide, Position


@dataclass
class MockBroker:
    default_slippage_bps: int
    default_spread_bps: int
    positions: dict[str, Position] = field(default_factory=dict)

    def place_order(self, order: Order) -> Fill:
        order.stop_intent.validate()
        slippage = self.default_slippage_bps / 10000
        spread = self.default_spread_bps / 10000
        price = order.price
        if order.side is OrderSide.BUY:
            price *= 1 + slippage + spread
        else:
            price *= 1 - slippage - spread

        fill = Fill(
            order_id=order.order_id,
            symbol=order.symbol,
            side=order.side,
            quantity=order.quantity,
            price=price,
            slippage_bps=self.default_slippage_bps,
        )

        current = self.positions.get(order.symbol)
        new_qty = order.quantity if order.side is OrderSide.BUY else -order.quantity
        if current:
            total_qty = current.quantity + new_qty
            if total_qty == 0:
                self.positions.pop(order.symbol)
            else:
                avg_price = (
                    current.average_price * current.quantity + price * new_qty
                ) / total_qty
                self.positions[order.symbol] = Position(order.symbol, total_qty, avg_price)
        else:
            self.positions[order.symbol] = Position(order.symbol, new_qty, price)

        return fill

    def cancel_order(self, order_id: str) -> None:
        return None

    def get_positions(self) -> list[Position]:
        return list(self.positions.values())

    def flatten(self) -> list[Fill]:
        fills: list[Fill] = []
        for symbol, position in list(self.positions.items()):
            side = OrderSide.SELL if position.quantity > 0 else OrderSide.BUY
            quantity = abs(position.quantity)
            price = position.average_price
            fill = Fill(
                order_id=f"flatten-{symbol}",
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                slippage_bps=self.default_slippage_bps,
            )
            fills.append(fill)
            self.positions.pop(symbol)
        return fills

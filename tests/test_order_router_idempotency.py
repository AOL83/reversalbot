from __future__ import annotations

from reversalbot.domain.models import Side, Symbol
from reversalbot.execution.interfaces import Fill, Order
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.execution.order_router import IdempotentOrderRouter
from reversalbot.risk.kill_switch import KillSwitch
from reversalbot.risk.stop_manager import StopIntent


class CountingBroker(MockBroker):
    def __init__(self) -> None:
        super().__init__()
        self.calls = 0

    def submit_order(self, order: Order) -> Fill:
        if order.stop_intent is not None:
            assert order.stop_intent.validated is True
        self.calls += 1
        return super().submit_order(order)


def test_idempotency_same_key_returns_same_fill() -> None:
    broker = CountingBroker()
    router = IdempotentOrderRouter(broker=broker, kill_switch=KillSwitch())
    order = Order(
        order_id="1",
        symbol=Symbol("TEST"),
        side=Side.BUY,
        quantity=1.0,
        price=100.0,
        stop_intent=StopIntent(stop_price=95.0),
    )

    first = router.route(order, idempotency_key="abc")
    second = router.route(order, idempotency_key="abc")

    assert first == second
    assert broker.calls == 1

from __future__ import annotations

from reversalbot.execution.interfaces import OrderRequest, OrderSide
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.execution.order_router import OrderRouter
from reversalbot.risk.kill_switch import KillSwitch


def test_order_router_idempotency() -> None:
    broker = MockBroker()
    router = OrderRouter(broker=broker, kill_switch=KillSwitch())
    request = OrderRequest(symbol="ABC", side=OrderSide.BUY, quantity=1.0)

    first = router.submit_order(request, idempotency_key="key-1")
    second = router.submit_order(request, idempotency_key="key-1")

    assert first.order_id == second.order_id

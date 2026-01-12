from __future__ import annotations

from datetime import timedelta

from reversalbot.execution.interfaces import Order, OrderSide
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.execution.order_router import OrderRouter
from reversalbot.risk.kill_switch import KillSwitch
from reversalbot.risk.stop_manager import StopIntent


def test_order_router_idempotency() -> None:
    broker = MockBroker(default_slippage_bps=0, default_spread_bps=0)
    router = OrderRouter(broker=broker, kill_switch=KillSwitch())
    stop_intent = StopIntent(hard_stop_price=95.0, time_stop=timedelta(minutes=30))
    order = Order(
        order_id="order-1",
        symbol="BTCUSD",
        side=OrderSide.BUY,
        quantity=1.0,
        price=100.0,
        stop_intent=stop_intent,
        idempotency_key="idem-1",
    )
    fill1 = router.send_order(order)
    fill2 = router.send_order(order)
    assert fill1 == fill2

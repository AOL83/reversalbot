from __future__ import annotations

from reversalbot.execution.order_router import IdempotentOrderRouter, OrderRequest


def test_order_router_idempotent() -> None:
    router = IdempotentOrderRouter()
    order = OrderRequest(
        idempotency_key="abc123",
        symbol="AAPL",
        side="buy",
        quantity=10.0,
        price=150.0,
    )

    first = router.route(order)
    second = router.route(order)

    assert first == second
    assert first.status == "accepted"

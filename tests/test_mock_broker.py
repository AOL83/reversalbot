from __future__ import annotations

from reversalbot.execution.mock_broker import MockBroker, Order, Position


def test_short_cover_partial_keeps_average() -> None:
    broker = MockBroker()
    broker.positions["SPY"] = Position(symbol="SPY", quantity=-10, average_price=100)

    broker.submit_order(Order(symbol="SPY", side="BUY", quantity=5, price=90))

    position = broker.positions["SPY"]
    assert position.quantity == -5
    assert position.average_price == 100


def test_short_cover_full_removes_position() -> None:
    broker = MockBroker()
    broker.positions["SPY"] = Position(symbol="SPY", quantity=-10, average_price=100)

    broker.submit_order(Order(symbol="SPY", side="BUY", quantity=10, price=95))

    assert "SPY" not in broker.positions


def test_short_cover_flip_sets_new_average() -> None:
    broker = MockBroker()
    broker.positions["SPY"] = Position(symbol="SPY", quantity=-10, average_price=100)

    fill = broker.submit_order(Order(symbol="SPY", side="BUY", quantity=15, price=90))

    position = broker.positions["SPY"]
    assert position.quantity == 5
    assert position.average_price == fill.price

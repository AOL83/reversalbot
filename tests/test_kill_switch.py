from __future__ import annotations

import pytest

from reversalbot.domain.models import Side, Symbol
from reversalbot.errors import KillSwitchEngagedError, RouterPausedError
from reversalbot.execution.interfaces import Order
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.execution.order_router import IdempotentOrderRouter
from reversalbot.manual_control.flatten import flatten
from reversalbot.risk.kill_switch import KillSwitch, KillSwitchState


def test_kill_switch_transitions() -> None:
    kill_switch = KillSwitch()
    state = kill_switch.state
    assert state == KillSwitchState.ACTIVE

    kill_switch.pause()
    state = kill_switch.state
    assert state == KillSwitchState.PAUSED

    kill_switch.resume()
    state = kill_switch.state
    assert state == KillSwitchState.ACTIVE

    kill_switch.kill()
    state = kill_switch.state
    assert state == KillSwitchState.KILLED

    kill_switch.reset()
    state = kill_switch.state
    assert state == KillSwitchState.ACTIVE


def test_router_rejects_when_paused_or_killed() -> None:
    kill_switch = KillSwitch()
    broker = MockBroker()
    router = IdempotentOrderRouter(broker=broker, kill_switch=kill_switch)
    order = Order(
        order_id="1",
        symbol=Symbol("TEST"),
        side=Side.BUY,
        quantity=1.0,
        price=100.0,
    )

    kill_switch.pause()
    with pytest.raises(RouterPausedError):
        router.route(order, idempotency_key="paused")

    kill_switch.kill()
    with pytest.raises(KillSwitchEngagedError):
        router.route(order, idempotency_key="killed")


def test_flatten_clears_positions() -> None:
    broker = MockBroker()
    broker.submit_order(
        Order(
            order_id="1",
            symbol=Symbol("TEST"),
            side=Side.BUY,
            quantity=2.0,
            price=10.0,
        )
    )
    assert broker.positions()
    flatten(broker)
    assert broker.positions() == []

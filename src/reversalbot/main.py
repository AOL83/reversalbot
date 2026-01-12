from __future__ import annotations

import argparse
from pathlib import Path

from reversalbot.config import load_config
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.execution.order_router import IdempotentOrderRouter
from reversalbot.logging import build_logger
from reversalbot.manual_control.emergency_stop import kill, reset_kill
from reversalbot.manual_control.flatten import flatten
from reversalbot.manual_control.pause import pause, resume
from reversalbot.monitoring.health import check_health
from reversalbot.risk.kill_switch import KillSwitch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ReversalBot Stage 1 CLI")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/config.example.yaml"),
        help="Path to YAML config",
    )
    parser.add_argument(
        "command",
        choices=["run", "status", "pause", "resume", "flatten", "kill", "reset-kill"],
        help="Action to execute",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    config = load_config(args.config)
    logger = build_logger(config.app.run_id, config.logging.level)

    kill_switch = KillSwitch()
    broker = MockBroker(base_currency=config.broker.base_currency)
    _ = IdempotentOrderRouter(broker=broker, kill_switch=kill_switch)

    if args.command == "status":
        health = check_health()
        logger.info(
            "health_check",
            extra={"status": health.status, "checked_at": health.checked_at.isoformat()},
        )
        print(f"health={health.status} checked_at={health.checked_at.isoformat()}")
        return 0
    if args.command == "pause":
        pause(kill_switch)
        logger.info("paused")
        return 0
    if args.command == "resume":
        resume(kill_switch)
        logger.info("resumed")
        return 0
    if args.command == "flatten":
        flatten(broker)
        logger.info("flattened")
        return 0
    if args.command == "kill":
        kill(kill_switch)
        logger.info("killed")
        return 0
    if args.command == "reset-kill":
        reset_kill(kill_switch)
        logger.info("reset_kill")
        return 0

    logger.info("run_requested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

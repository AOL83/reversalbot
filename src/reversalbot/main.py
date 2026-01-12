"""CLI entrypoint for ReversalBot Stage 1."""

from __future__ import annotations

import argparse

from reversalbot.config import ReversalBotConfig, load_config
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.logging import configure_logging, get_logger
from reversalbot.manual_control.emergency_stop import emergency_stop
from reversalbot.manual_control.flatten import flatten_all
from reversalbot.manual_control.pause import pause, resume
from reversalbot.monitoring.health import heartbeat
from reversalbot.risk.kill_switch import KillSwitch


def _build_components(config: ReversalBotConfig) -> tuple[KillSwitch, MockBroker]:
    kill_switch = KillSwitch()
    broker = MockBroker(
        default_slippage_bps=config.broker.default_slippage_bps,
        default_spread_bps=config.broker.default_spread_bps,
    )
    return kill_switch, broker


def cmd_run(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    logger.info("Starting mock run", extra={"environment": config.app.environment})
    kill_switch, _broker = _build_components(config)
    status = heartbeat(message=f"kill_state={kill_switch.state}")
    logger.info("Heartbeat", extra={"timestamp": status.timestamp.isoformat()})
    logger.info("Run complete")
    print(f"Run ID: {run_id}")
    return 0


def cmd_status(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    kill_switch, broker = _build_components(config)
    logger = get_logger("reversalbot.status", run_id)
    positions = broker.get_positions()
    logger.info("Status", extra={"kill_state": kill_switch.state, "positions": len(positions)})
    print(f"Kill state: {kill_switch.state}")
    print(f"Open positions: {len(positions)}")
    return 0


def cmd_pause(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    kill_switch, _broker = _build_components(config)
    pause(kill_switch, "manual pause")
    logger = get_logger("reversalbot.pause", run_id)
    logger.info("Paused", extra={"kill_state": kill_switch.state})
    print("Paused")
    return 0


def cmd_resume(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    kill_switch, _broker = _build_components(config)
    resume(kill_switch, "manual resume")
    logger = get_logger("reversalbot.resume", run_id)
    logger.info("Resumed", extra={"kill_state": kill_switch.state})
    print("Resumed")
    return 0


def cmd_flatten(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    _kill_switch, broker = _build_components(config)
    fills = flatten_all(broker)
    logger = get_logger("reversalbot.flatten", run_id)
    logger.info("Flattened", extra={"fills": len(fills)})
    print(f"Flattened positions: {len(fills)}")
    return 0


def cmd_kill(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    kill_switch, broker = _build_components(config)
    fills = emergency_stop(kill_switch, broker, "manual kill")
    logger = get_logger("reversalbot.kill", run_id)
    logger.info("Killed", extra={"fills": len(fills)})
    print("Kill switch engaged")
    return 0


def cmd_reset_kill(config: ReversalBotConfig) -> int:
    logger, run_id = configure_logging(config.logging.level)
    kill_switch, _broker = _build_components(config)
    kill_switch.reset("manual reset")
    logger = get_logger("reversalbot.reset", run_id)
    logger.info("Kill switch reset", extra={"kill_state": kill_switch.state})
    print("Kill switch reset")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ReversalBot Stage 1 CLI")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ["run", "status", "pause", "resume", "flatten", "kill", "reset-kill"]:
        subparsers.add_parser(name)
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    config = load_config(args.config)
    if args.command == "run":
        return cmd_run(config)
    if args.command == "status":
        return cmd_status(config)
    if args.command == "pause":
        return cmd_pause(config)
    if args.command == "resume":
        return cmd_resume(config)
    if args.command == "flatten":
        return cmd_flatten(config)
    if args.command == "kill":
        return cmd_kill(config)
    if args.command == "reset-kill":
        return cmd_reset_kill(config)
    raise ValueError("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main())

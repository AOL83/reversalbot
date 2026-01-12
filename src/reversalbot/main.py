from __future__ import annotations

import argparse
from pathlib import Path

from reversalbot.config import load_config
from reversalbot.execution.mock_broker import MockBroker
from reversalbot.manual_control.control import ManualController
from reversalbot.risk.kill_switch import KillSwitch


def _build_controller() -> ManualController:
    broker = MockBroker()
    kill_switch = KillSwitch()
    return ManualController(broker=broker, kill_switch=kill_switch)


def cmd_run(args: argparse.Namespace) -> None:
    config = load_config(Path(args.config))
    controller = _build_controller()
    if controller.kill_switch.engaged:
        raise RuntimeError("Kill switch engaged")
    print(f"Running in {config.app.environment} mode with run_id={config.app.run_id}")


def cmd_status(_: argparse.Namespace) -> None:
    controller = _build_controller()
    print(f"paused={controller.paused}, kill_switch={controller.kill_switch.engaged}")


def cmd_pause(_: argparse.Namespace) -> None:
    controller = _build_controller()
    controller.pause()
    print("paused")


def cmd_resume(_: argparse.Namespace) -> None:
    controller = _build_controller()
    controller.resume()
    print("resumed")


def cmd_flatten(_: argparse.Namespace) -> None:
    controller = _build_controller()
    cancelled = controller.flatten()
    print(f"cancelled={cancelled}")


def cmd_kill(_: argparse.Namespace) -> None:
    controller = _build_controller()
    controller.kill("manual")
    print("kill switch engaged")


def cmd_reset_kill(_: argparse.Namespace) -> None:
    controller = _build_controller()
    controller.reset_kill()
    print("kill switch reset")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="reversalbot")
    parser.add_argument("--config", default="configs/config.example.yaml")

    subparsers = parser.add_subparsers(dest="command", required=True)

    commands = {
        "run": cmd_run,
        "status": cmd_status,
        "pause": cmd_pause,
        "resume": cmd_resume,
        "flatten": cmd_flatten,
        "kill": cmd_kill,
        "reset-kill": cmd_reset_kill,
    }

    for name, handler in commands.items():
        sub = subparsers.add_parser(name)
        sub.set_defaults(func=handler)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
from pathlib import Path

from reversalbot.config import load_config
from reversalbot.monitoring.health import check_health


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ReversalBot Stage 1 CLI")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/config.example.yaml"),
        help="Path to YAML config",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    _ = load_config(args.config)
    health = check_health()
    print(f"health={health.status} checked_at={health.checked_at.isoformat()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

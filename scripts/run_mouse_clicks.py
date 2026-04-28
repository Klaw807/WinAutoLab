from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
DEFAULT_POINTS_FILE = ROOT / "configs" / "mouse_points.json"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from winautolab.mouse import load_points_from_json, run_scheduled_clicks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run scheduled multi-point mouse clicks.")
    parser.add_argument(
        "points_file",
        nargs="?",
        default=str(DEFAULT_POINTS_FILE),
        help=f"JSON file containing click points (default: {DEFAULT_POINTS_FILE})",
    )
    parser.add_argument("--time", default="12:00:00", help="Trigger time in HH:MM:SS")
    parser.add_argument("--repeat-count", type=int, default=3)
    parser.add_argument("--repeat-interval", type=float, default=0.02)
    parser.add_argument("--no-preview", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    points = load_points_from_json(args.points_file)
    run_scheduled_clicks(
        points,
        target_time=args.time,
        repeat_count=args.repeat_count,
        repeat_interval_seconds=args.repeat_interval,
        preview=not args.no_preview,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

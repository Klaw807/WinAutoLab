from __future__ import annotations

import argparse
import time

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from winautolab.mouse import get_cursor_position, get_screen_size


def main() -> int:
    parser = argparse.ArgumentParser(description="Print the current mouse position after a delay.")
    parser.add_argument("--delay", type=float, default=3.0)
    args = parser.parse_args()

    print(f"Move the cursor to the target position. Waiting {args.delay} seconds...")
    time.sleep(args.delay)
    point = get_cursor_position()
    screen_width, screen_height = get_screen_size()
    print(f"Current mouse position: ({point.x}, {point.y}) on {screen_width}x{screen_height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

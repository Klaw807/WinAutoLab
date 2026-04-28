from __future__ import annotations

import argparse
import time

import pyautogui


def main() -> int:
    parser = argparse.ArgumentParser(description="Print the current mouse position after a delay.")
    parser.add_argument("--delay", type=float, default=3.0)
    args = parser.parse_args()

    print(f"Move the cursor to the target position. Waiting {args.delay} seconds...")
    time.sleep(args.delay)
    x, y = pyautogui.position()
    print(f"Current mouse position: ({x}, {y})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from winautolab.browser_forms import run_workflow


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a config-driven Selenium browser workflow.")
    parser.add_argument("config")
    args = parser.parse_args()
    run_workflow(args.config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


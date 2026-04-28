from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from winautolab.image_download import download_images


def main() -> int:
    parser = argparse.ArgumentParser(description="Download all images referenced by a web page.")
    parser.add_argument("url")
    parser.add_argument("--output", default="downloaded_images")
    args = parser.parse_args()

    saved_files = download_images(args.url, args.output)
    print(f"Downloaded {len(saved_files)} images into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


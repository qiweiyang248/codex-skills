#!/usr/bin/env python3
"""Export image filename and alt text audit rows."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
from pathlib import Path


def filename_from_src(src: str) -> str:
    path = urllib.parse.urlparse(src).path
    return Path(path).name


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_classified.json")
    ap.add_argument("--out", default="image_audit.csv")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    fields = [
        "page_url",
        "page_type",
        "image_role",
        "current_image_name",
        "recommended_file_name",
        "current_alt_text",
        "recommended_alt_text",
        "priority",
        "risk_level",
        "verification_method",
    ]
    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for page in data.get("pages", []):
            for idx, image in enumerate(page.get("images", []), start=1):
                current_alt = image.get("alt", "")
                current_name = filename_from_src(image.get("src", ""))
                writer.writerow(
                    {
                        "page_url": page.get("url", ""),
                        "page_type": page.get("page_type", ""),
                        "image_role": "Main Image" if idx == 1 else "Supporting Image",
                        "current_image_name": current_name,
                        "recommended_file_name": "",
                        "current_alt_text": current_alt,
                        "recommended_alt_text": "",
                        "priority": "P1" if not current_alt else "P2",
                        "risk_level": "Low",
                        "verification_method": "Confirm image filename and alt text in Shopify media or theme output.",
                    }
                )
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

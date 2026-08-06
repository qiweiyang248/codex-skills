#!/usr/bin/env python3
"""Export GEO recommendations into a CSV skeleton."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


FIELDS = [
    "page_url",
    "page_type",
    "issue_type",
    "current_value",
    "suggested_value",
    "target_field",
    "modification_method",
    "priority",
    "risk_level",
    "verification_method",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--answers", default="answer_structure.json")
    ap.add_argument("--entities", default="entity_signals.json")
    ap.add_argument("--out", default="geo-recommendations.csv")
    args = ap.parse_args()

    rows = []
    if Path(args.answers).exists():
        data = json.loads(Path(args.answers).read_text(encoding="utf-8"))
        for page in data.get("pages", []):
            for issue in page.get("issues", []):
                rows.append(
                    {
                        "page_url": page.get("url", ""),
                        "page_type": page.get("page_type", ""),
                        "issue_type": "Answer Structure",
                        "current_value": issue,
                        "suggested_value": "Add concise answer block, specs/FAQ/table content relevant to buyer questions.",
                        "target_field": "Page content",
                        "modification_method": "Shopify page/product/collection content update",
                        "priority": "P1",
                        "risk_level": "Low",
                        "verification_method": "Confirm rendered page includes visible answer structure.",
                    }
                )
    if Path(args.entities).exists():
        data = json.loads(Path(args.entities).read_text(encoding="utf-8"))
        gaps = data.get("entity_gaps", {})
        for key, missing in gaps.items():
            if missing:
                rows.append(
                    {
                        "page_url": "",
                        "page_type": "site",
                        "issue_type": "Entity Clarity",
                        "current_value": key,
                        "suggested_value": "Add real brand, product, policy, or schema signal. Do not invent unverifiable data.",
                        "target_field": "About/policy/schema",
                        "modification_method": "Content or JSON-LD recommendation",
                        "priority": "P1",
                        "risk_level": "Medium",
                        "verification_method": "Inspect page source and visible content.",
                    }
                )
    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

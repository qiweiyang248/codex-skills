#!/usr/bin/env python3
"""Check whether pages contain AI-citable answer structures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def contains_any(values: list[str], needles: list[str]) -> bool:
    text = " ".join(values).lower()
    return any(n in text for n in needles)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_classified.json")
    ap.add_argument("--out", default="answer_structure.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = []
    for page in data.get("pages", []):
        headings = []
        for vals in page.get("headings", {}).values():
            headings.extend(vals)
        has_faq = contains_any(headings, ["faq", "questions", "shipping", "returns", "warranty"])
        has_how_to = contains_any(headings, ["how to", "install", "installation", "use", "setup"])
        has_compare = contains_any(headings, ["vs", "compare", "comparison", "pros", "cons"])
        has_specs = contains_any(headings, ["spec", "size", "dimension", "material", "details"])
        issues = []
        if page.get("page_type") in {"product", "collection", "product_category"} and not has_faq:
            issues.append("FAQ or buyer objection block not detected")
        if page.get("page_type") == "product" and not has_specs:
            issues.append("Specs structure not detected")
        rows.append(
            {
                "url": page.get("url", ""),
                "page_type": page.get("page_type", ""),
                "has_faq": has_faq,
                "has_how_to": has_how_to,
                "has_compare": has_compare,
                "has_specs": has_specs,
                "issues": issues,
            }
        )
    Path(args.out).write_text(json.dumps({"pages": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Export an ecommerce operator-friendly SEO update sheet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


FIELDS = [
    "page_url",
    "page_type",
    "current_seo_title",
    "recommended_seo_title",
    "current_meta_description",
    "recommended_meta_description",
    "current_h1",
    "recommended_h1",
    "primary_keyword",
    "secondary_keywords",
    "search_intent",
    "content_gaps",
    "internal_link_suggestions",
    "schema_needed",
    "priority",
    "risk_level",
    "verification_method",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_classified.json")
    ap.add_argument("--out", default="page-seo-update-sheet.csv")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    with Path(args.out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for page in data.get("pages", []):
            h1s = page.get("headings", {}).get("h1", [])
            page_type = page.get("page_type", "")
            schema_needed = "Product" if page_type == "product" else "BreadcrumbList"
            if page_type == "collection":
                schema_needed = "BreadcrumbList; ItemList; FAQPage if FAQ is visible"
            if page_type == "product_category":
                schema_needed = "BreadcrumbList; ItemList; FAQPage if FAQ is visible"
            writer.writerow(
                {
                    "page_url": page.get("url", ""),
                    "page_type": page_type,
                    "current_seo_title": page.get("title", ""),
                    "recommended_seo_title": "",
                    "current_meta_description": page.get("meta_description", ""),
                    "recommended_meta_description": "",
                    "current_h1": " | ".join(h1s),
                    "recommended_h1": "",
                    "primary_keyword": "",
                    "secondary_keywords": "",
                    "search_intent": "",
                    "content_gaps": "",
                    "internal_link_suggestions": "",
                    "schema_needed": schema_needed,
                    "priority": "P1" if page_type in {"product", "collection", "product_category", "home"} else "P2",
                    "risk_level": "Low",
                    "verification_method": "Verify updated metadata, H1, and schema in rendered page source.",
                }
            )
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate required optimization-pack files and key CSV columns."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


REQUIRED_FILES = [
    "audit-report.md",
    "optimization-pack.md",
    "action-plan.md",
    "shopify-content-update.csv",
    "woocommerce-product-update.csv",
    "wordpress-page-update.csv",
    "image-alt-text-sheet.csv",
    "schema-jsonld-fixes.json",
    "internal-link-plan.md",
    "geo-content-plan.md",
    "implementation-checklist.md",
]

SHOPIFY_COLUMNS = [
    "handle",
    "product_title",
    "seo_title",
    "meta_description",
    "h1",
    "subtitle",
    "product_bullets",
    "accordion_faq",
    "specs_copy",
    "image_filename",
    "image_alt_text",
    "schema_recommendation",
]

IMAGE_COLUMNS = [
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

WOOCOMMERCE_COLUMNS = [
    "product_id",
    "sku",
    "slug",
    "product_name",
    "seo_title",
    "meta_description",
    "h1",
    "short_description",
    "product_description",
    "product_bullets",
    "accordion_faq",
    "attributes_specs",
    "image_filename",
    "image_alt_text",
    "schema_recommendation",
    "plugin_target",
]

WORDPRESS_COLUMNS = [
    "post_id",
    "post_type",
    "slug",
    "current_title",
    "seo_title",
    "meta_description",
    "h1",
    "intro_copy",
    "body_update",
    "faq_block",
    "internal_links",
    "schema_recommendation",
    "plugin_target",
]


def read_header(path: Path) -> list[str]:
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return next(reader, [])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs", default="outputs")
    ap.add_argument("--json-out", default="")
    args = ap.parse_args()

    out_dir = Path(args.outputs)
    result = {"missing_files": [], "column_issues": [], "valid": True}
    for name in REQUIRED_FILES:
        if not (out_dir / name).exists():
            result["missing_files"].append(name)

    checks = {
        "shopify-content-update.csv": SHOPIFY_COLUMNS,
        "woocommerce-product-update.csv": WOOCOMMERCE_COLUMNS,
        "wordpress-page-update.csv": WORDPRESS_COLUMNS,
        "image-alt-text-sheet.csv": IMAGE_COLUMNS,
    }
    for name, expected in checks.items():
        path = out_dir / name
        if path.exists():
            header = read_header(path)
            missing = [col for col in expected if col not in header]
            if missing:
                result["column_issues"].append({"file": name, "missing_columns": missing})

    schema_path = out_dir / "schema-jsonld-fixes.json"
    if schema_path.exists():
        try:
            json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result["column_issues"].append({"file": "schema-jsonld-fixes.json", "error": str(exc)})

    result["valid"] = not result["missing_files"] and not result["column_issues"]
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())

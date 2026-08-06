#!/usr/bin/env python3
"""Validate GeoSEO Engine output files and key CSV/JSON contracts."""

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
    "seo-priority-fixes.csv",
    "page-seo-update-sheet.csv",
    "image-alt-text-sheet.csv",
    "schema-jsonld-fixes.json",
    "internal-link-plan.md",
    "geo-content-plan.md",
    "ai-readiness-scorecard.csv",
    "geo-query-map.csv",
    "ai-citation-content-plan.md",
    "entity-schema-recommendations.json",
    "implementation-checklist.md",
]

PLATFORM_FILES = {
    "shopify": "shopify-content-update.csv",
    "woocommerce": "woocommerce-product-update.csv",
    "wordpress": "wordpress-page-update.csv",
}

RECOMMENDATION_COLUMNS = [
    "page_url",
    "page_type",
    "issue_type",
    "current_value",
    "suggested_value",
    "target_field",
    "modification_method",
    "seo_impact",
    "geo_impact",
    "conversion_impact",
    "priority",
    "risk_level",
    "verification_method",
]

PAGE_SEO_COLUMNS = [
    "page_url",
    "page_type",
    "current_seo_title",
    "recommended_seo_title",
    "current_meta_description",
    "recommended_meta_description",
    "current_h1",
    "recommended_h1",
    "primary_keyword",
    "search_intent",
    "priority",
    "verification_method",
]

AI_SCORE_COLUMNS = [
    "component",
    "score_0_5",
    "weighted_points",
    "evidence",
    "recommended_action",
    "priority",
    "verification_method",
]

GEO_QUERY_COLUMNS = [
    "topic",
    "ai_query",
    "buyer_intent",
    "current_coverage",
    "recommended_page_type",
    "citation_hook",
    "priority",
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
    ap.add_argument("--outputs", default="outputs/geoseo-engine")
    ap.add_argument(
        "--require-platform",
        choices=["none", "shopify", "woocommerce", "wordpress"],
        default="none",
    )
    ap.add_argument("--json-out", default="")
    args = ap.parse_args()

    out_dir = Path(args.outputs)
    result = {"missing_files": [], "column_issues": [], "valid": True}
    required_files = list(REQUIRED_FILES)
    if args.require_platform != "none":
        required_files.append(PLATFORM_FILES[args.require_platform])
    for name in required_files:
        if not (out_dir / name).exists():
            result["missing_files"].append(name)

    checks = {
        "seo-priority-fixes.csv": RECOMMENDATION_COLUMNS,
        "page-seo-update-sheet.csv": PAGE_SEO_COLUMNS,
        "shopify-content-update.csv": SHOPIFY_COLUMNS,
        "woocommerce-product-update.csv": WOOCOMMERCE_COLUMNS,
        "wordpress-page-update.csv": WORDPRESS_COLUMNS,
        "image-alt-text-sheet.csv": IMAGE_COLUMNS,
        "ai-readiness-scorecard.csv": AI_SCORE_COLUMNS,
        "geo-query-map.csv": GEO_QUERY_COLUMNS,
    }
    for name, expected in checks.items():
        path = out_dir / name
        if path.exists():
            header = read_header(path)
            missing = [col for col in expected if col not in header]
            if missing:
                result["column_issues"].append({"file": name, "missing_columns": missing})

    for json_name in ["schema-jsonld-fixes.json", "entity-schema-recommendations.json"]:
        json_path = out_dir / json_name
        if json_path.exists():
            try:
                json.loads(json_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                result["column_issues"].append({"file": json_name, "error": str(exc)})

    result["valid"] = not result["missing_files"] and not result["column_issues"]
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())

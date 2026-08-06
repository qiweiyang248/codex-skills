#!/usr/bin/env python3
"""Create a GeoSEO Engine output package from bundled templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


CORE_TEMPLATE_MAP = {
    "audit-report.md": "audit-report-template.md",
    "optimization-pack.md": "optimization-pack-template.md",
    "action-plan.md": "action-plan-template.md",
    "seo-priority-fixes.csv": "seo-priority-fixes-template.csv",
    "page-seo-update-sheet.csv": "page-seo-update-sheet-template.csv",
    "image-alt-text-sheet.csv": "image-alt-text-template.csv",
    "schema-jsonld-fixes.json": "schema-jsonld-fixes-template.json",
    "internal-link-plan.md": "internal-link-plan-template.md",
    "geo-content-plan.md": "geo-content-plan-template.md",
    "ai-readiness-scorecard.csv": "ai-readiness-scorecard-template.csv",
    "geo-query-map.csv": "geo-query-map-template.csv",
    "ai-citation-content-plan.md": "ai-citation-content-plan-template.md",
    "entity-schema-recommendations.json": "entity-schema-recommendations-template.json",
    "implementation-checklist.md": "implementation-checklist-template.md",
}

PLATFORM_TEMPLATE_MAP = {
    "shopify": {"shopify-content-update.csv": "shopify-content-update-template.csv"},
    "woocommerce": {
        "woocommerce-product-update.csv": "woocommerce-product-update-template.csv"
    },
    "wordpress": {"wordpress-page-update.csv": "wordpress-page-update-template.csv"},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--templates", default="../templates")
    ap.add_argument("--outputs", default="outputs/geoseo-engine")
    ap.add_argument(
        "--platform",
        choices=["none", "shopify", "woocommerce", "wordpress", "all"],
        default="none",
    )
    ap.add_argument("--include-llms", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    template_dir = Path(args.templates).resolve()
    output_dir = Path(args.outputs).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    created = []
    skipped = []
    template_map = dict(CORE_TEMPLATE_MAP)
    if args.platform == "all":
        for platform_map in PLATFORM_TEMPLATE_MAP.values():
            template_map.update(platform_map)
    elif args.platform != "none":
        template_map.update(PLATFORM_TEMPLATE_MAP[args.platform])
    if args.include_llms:
        template_map["llms-txt-draft.md"] = "llms-txt-draft-template.md"

    for output_name, template_name in template_map.items():
        src = template_dir / template_name
        dst = output_dir / output_name
        if dst.exists() and not args.overwrite:
            skipped.append(output_name)
            continue
        if not src.exists():
            raise FileNotFoundError(f"Missing template: {src}")
        shutil.copyfile(src, dst)
        created.append(output_name)
    print(f"Output directory: {output_dir}")
    print(f"Created/updated: {', '.join(created) if created else 'none'}")
    print(f"Skipped existing: {', '.join(skipped) if skipped else 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

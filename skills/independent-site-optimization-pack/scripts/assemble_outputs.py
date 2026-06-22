#!/usr/bin/env python3
"""Create the required optimization-pack output files from templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


TEMPLATE_MAP = {
    "audit-report.md": "audit-report-template.md",
    "optimization-pack.md": "optimization-pack-template.md",
    "action-plan.md": "action-plan-template.md",
    "shopify-content-update.csv": "shopify-content-update-template.csv",
    "woocommerce-product-update.csv": "woocommerce-product-update-template.csv",
    "wordpress-page-update.csv": "wordpress-page-update-template.csv",
    "image-alt-text-sheet.csv": "image-alt-text-template.csv",
    "schema-jsonld-fixes.json": "schema-jsonld-fixes-template.json",
    "internal-link-plan.md": "internal-link-plan-template.md",
    "geo-content-plan.md": "geo-content-plan-template.md",
    "implementation-checklist.md": "implementation-checklist-template.md",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--templates", default="../templates")
    ap.add_argument("--outputs", default="outputs")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    template_dir = Path(args.templates).resolve()
    output_dir = Path(args.outputs).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    created = []
    skipped = []
    for output_name, template_name in TEMPLATE_MAP.items():
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

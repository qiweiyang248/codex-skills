#!/usr/bin/env python3
"""Classify ecommerce page templates from URL patterns."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def classify(url: str) -> str:
    lower = url.lower()
    if "/products/" in lower:
        return "product"
    if "/product/" in lower or "post_type=product" in lower:
        return "product"
    if "/collections/" in lower:
        return "collection"
    if "/product-category/" in lower or "/shop/" in lower:
        return "product_category"
    if "/blogs/" in lower or "/blog/" in lower:
        return "blog"
    if "/category/" in lower or "/tag/" in lower:
        return "blog_archive"
    if "/pages/" in lower:
        if any(x in lower for x in ["about", "contact"]):
            return "about"
        if any(x in lower for x in ["shipping", "returns", "refund", "privacy", "terms", "warranty"]):
            return "policy"
        return "page"
    if any(x in lower for x in ["about", "contact"]):
        return "about"
    if any(x in lower for x in ["shipping", "returns", "refund", "privacy", "terms", "warranty"]):
        return "policy"
    if any(x in lower for x in ["?filter", "filter.", "sort_by", "variant=", "q="]):
        return "filter_or_search"
    path = lower.split("://", 1)[-1].split("/", 1)
    if len(path) == 1 or path[1] == "":
        return "home"
    return "unknown"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_parsed.json")
    ap.add_argument("--out", default="pages_classified.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    pages = data.get("pages", data if isinstance(data, list) else [])
    for page in pages:
        page["page_type"] = classify(page.get("url", ""))
    Path(args.out).write_text(json.dumps({"pages": pages}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out} with {len(pages)} classified pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

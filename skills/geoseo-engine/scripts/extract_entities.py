#!/usr/bin/env python3
"""Extract basic brand/product entity signals from parsed pages and JSON-LD."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def walk(obj: object):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk(item)


def load_schema(path: str) -> list[dict]:
    if not path or not Path(path).exists():
        return []
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    blocks: list[dict] = []
    for page in data.get("pages", []):
        for block in page.get("json_ld", []):
            if isinstance(block, dict):
                blocks.append({"url": page.get("url", ""), "page_type": page.get("page_type", ""), "data": block})
    return blocks


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", default="pages_classified.json")
    ap.add_argument("--schema", default="schema_matrix.json")
    ap.add_argument("--out", default="entity_signals.json")
    args = ap.parse_args()

    pages_data = json.loads(Path(args.pages).read_text(encoding="utf-8")) if Path(args.pages).exists() else {"pages": []}
    schema_blocks = load_schema(args.schema)
    organizations = []
    products = []
    same_as = set()
    for block in schema_blocks:
        for obj in walk(block["data"]):
            typ = obj.get("@type")
            types = typ if isinstance(typ, list) else [typ]
            if "Organization" in types:
                organizations.append({"url": block["url"], "name": obj.get("name", ""), "sameAs": obj.get("sameAs", [])})
                for link in obj.get("sameAs", []) if isinstance(obj.get("sameAs", []), list) else []:
                    same_as.add(link)
            if "Product" in types:
                products.append(
                    {
                        "url": block["url"],
                        "name": obj.get("name", ""),
                        "sku": obj.get("sku", ""),
                        "brand": obj.get("brand", {}),
                    }
                )

    about_pages = [p.get("url", "") for p in pages_data.get("pages", []) if p.get("page_type") == "about"]
    policy_pages = [p.get("url", "") for p in pages_data.get("pages", []) if p.get("page_type") == "policy"]
    output = {
        "organization_schema": organizations,
        "product_schema": products,
        "same_as": sorted(same_as),
        "about_pages": about_pages,
        "policy_pages": policy_pages,
        "entity_gaps": {
            "missing_organization_schema": not organizations,
            "missing_product_schema_count": len([p for p in pages_data.get("pages", []) if p.get("page_type") == "product"]) - len(products),
            "missing_about_page": not about_pages,
            "missing_policy_pages": not policy_pages,
        },
    }
    Path(args.out).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

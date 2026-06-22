#!/usr/bin/env python3
"""Simple objective SEO scoring for extracted pages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def page_score(page: dict) -> tuple[int, list[str]]:
    score = 100
    issues: list[str] = []
    title = page.get("title", "")
    meta = page.get("meta_description", "")
    h1s = page.get("headings", {}).get("h1", [])
    if not title:
        score -= 15
        issues.append("Missing SEO title")
    elif len(title) < 30 or len(title) > 70:
        score -= 5
        issues.append("SEO title length needs review")
    if not meta:
        score -= 15
        issues.append("Missing meta description")
    elif len(meta) < 110 or len(meta) > 170:
        score -= 5
        issues.append("Meta description length needs review")
    if len(h1s) != 1:
        score -= 15
        issues.append("H1 should be unique")
    if not page.get("canonical"):
        score -= 10
        issues.append("Missing canonical")
    if "noindex" in page.get("robots_meta", "").lower():
        score -= 20
        issues.append("Noindex detected")
    if page.get("word_count", 0) < 150 and page.get("page_type") in {"product", "collection", "product_category", "blog"}:
        score -= 10
        issues.append("Thin content risk")
    if page.get("page_type") == "product" and "Product" not in " ".join(page.get("schema_types", [])):
        score -= 10
        issues.append("Product schema not detected")
    return max(0, score), issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_classified.json")
    ap.add_argument("--schema", default="")
    ap.add_argument("--out", default="seo_scorecard.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    schema_by_url = {}
    if args.schema and Path(args.schema).exists():
        schema_data = json.loads(Path(args.schema).read_text(encoding="utf-8"))
        schema_by_url = {row["url"]: row.get("schema_types", []) for row in schema_data.get("pages", [])}
    rows = []
    for page in data.get("pages", []):
        page["schema_types"] = schema_by_url.get(page.get("url", ""), [])
        score, issues = page_score(page)
        rows.append({"url": page.get("url", ""), "page_type": page.get("page_type", ""), "score": score, "issues": issues})
    avg = round(sum(r["score"] for r in rows) / len(rows), 1) if rows else 0
    Path(args.out).write_text(json.dumps({"seo_score": avg, "pages": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}; SEO score {avg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

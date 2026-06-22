#!/usr/bin/env python3
"""Compute a lightweight GEO score from extracted signals."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


WEIGHTS = {
    "ai_crawl_access": 20,
    "entity_clarity": 20,
    "answer_structure": 20,
    "product_data_completeness": 15,
    "trust_authority_signals": 15,
    "ai_query_coverage": 10,
}


def crawl_access_score(path: str) -> int:
    if not path or not Path(path).exists():
        return 2
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    statuses = [r.get("status") for r in data.get("crawlers", [])]
    if not statuses:
        return 2
    blocked = statuses.count("blocked")
    partial = statuses.count("partially_blocked")
    if blocked >= 5:
        return 1
    if blocked or partial:
        return 3
    return 5


def entity_score(path: str) -> tuple[int, int]:
    if not path or not Path(path).exists():
        return 2, 2
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    gaps = data.get("entity_gaps", {})
    brand = 5
    product = 5
    if gaps.get("missing_organization_schema"):
        brand -= 2
    if gaps.get("missing_about_page"):
        brand -= 1
    if gaps.get("missing_policy_pages"):
        brand -= 1
    missing_products = gaps.get("missing_product_schema_count", 0)
    if missing_products > 0:
        product -= 2
    return max(0, brand), max(0, product)


def answer_score(path: str) -> int:
    if not path or not Path(path).exists():
        return 2
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = data.get("pages", [])
    if not rows:
        return 2
    issue_count = sum(len(r.get("issues", [])) for r in rows)
    if issue_count == 0:
        return 5
    if issue_count <= max(1, len(rows) // 3):
        return 4
    if issue_count <= len(rows):
        return 3
    return 2


def weighted(component_scores: dict[str, int]) -> int:
    total = 0.0
    for key, weight in WEIGHTS.items():
        total += (component_scores[key] / 5) * weight
    return round(total)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--crawler", default="ai_crawler_access.json")
    ap.add_argument("--entities", default="entity_signals.json")
    ap.add_argument("--answers", default="answer_structure.json")
    ap.add_argument("--out", default="geo_scorecard.json")
    args = ap.parse_args()

    brand, product = entity_score(args.entities)
    scores = {
        "ai_crawl_access": crawl_access_score(args.crawler),
        "entity_clarity": brand,
        "answer_structure": answer_score(args.answers),
        "product_data_completeness": product,
        "trust_authority_signals": 2,
        "ai_query_coverage": 2,
    }
    output = {
        "geo_score": weighted(scores),
        "component_scores_0_5": scores,
        "additional_scores": {
            "citability_score": scores["answer_structure"] * 20,
            "brand_entity_score": brand * 20,
            "product_entity_score": product * 20,
            "ai_crawler_access_score": scores["ai_crawl_access"] * 20,
            "query_coverage_score": scores["ai_query_coverage"] * 20,
            "external_authority_score": scores["trust_authority_signals"] * 20,
        },
    }
    Path(args.out).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}; GEO score {output['geo_score']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

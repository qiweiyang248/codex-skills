#!/usr/bin/env python3
"""Generate buyer-oriented AI query fan-out rows."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


PATTERNS = [
    "best {topic} for {use_case}",
    "{topic} size guide",
    "{topic} pros and cons",
    "how to install {topic}",
    "{topic} vs alternatives",
    "what to look for when buying {topic}",
    "is {topic} worth it for {use_case}",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", action="append", default=[])
    ap.add_argument("--use-case", default="home use")
    ap.add_argument("--csv-out", default="geo-query-map.csv")
    ap.add_argument("--json-out", default="geo-query-map.json")
    args = ap.parse_args()

    topics = args.topic or ["[product category]"]
    rows = []
    for topic in topics:
        for pattern in PATTERNS:
            query = pattern.format(topic=topic, use_case=args.use_case)
            rows.append(
                {
                    "topic": topic,
                    "ai_query": query,
                    "buyer_intent": "Commercial investigation",
                    "current_coverage": "",
                    "recommended_page_type": "Buying Guide" if "best" in query or "buying" in query else "FAQ/Guide",
                    "recommended_title": query.title(),
                    "recommended_url_slug": query.lower().replace(" ", "-").replace("/", "-"),
                    "required_entities": topic,
                    "required_tables": "Specs or comparison table where relevant",
                    "required_faq": "Answer the query directly",
                    "citation_hook": "A concise answer in the first 50 words.",
                    "internal_links": "Link to relevant product and collection pages",
                    "priority": "P1" if "best" in query or "size" in query else "P2",
                }
            )
    fields = list(rows[0].keys())
    with Path(args.csv_out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    Path(args.json_out).write_text(json.dumps({"queries": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.csv_out} and {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

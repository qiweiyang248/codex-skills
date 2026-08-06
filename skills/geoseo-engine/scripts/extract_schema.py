#!/usr/bin/env python3
"""Extract and summarize JSON-LD schema from parsed pages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def schema_types(obj: object) -> list[str]:
    found: list[str] = []
    if isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str):
            found.append(t)
        elif isinstance(t, list):
            found.extend(str(x) for x in t)
        for value in obj.values():
            found.extend(schema_types(value))
    elif isinstance(obj, list):
        for item in obj:
            found.extend(schema_types(item))
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_classified.json")
    ap.add_argument("--out", default="schema_matrix.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = []
    for page in data.get("pages", []):
        parsed_blocks = []
        types: list[str] = []
        for block in page.get("json_ld", []):
            try:
                obj = json.loads(block)
                parsed_blocks.append(obj)
                types.extend(schema_types(obj))
            except json.JSONDecodeError:
                parsed_blocks.append({"parse_error": block[:200]})
        rows.append(
            {
                "url": page.get("url", ""),
                "page_type": page.get("page_type", ""),
                "schema_types": sorted(set(types)),
                "json_ld": parsed_blocks,
            }
        )
    Path(args.out).write_text(json.dumps({"pages": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out} with {len(rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())

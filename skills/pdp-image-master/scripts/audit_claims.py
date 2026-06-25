#!/usr/bin/env python3
"""Audit PDP image claims from claims_audit.csv.

The script checks that claim rows have evidence when their status is supported,
and that risky claims are not marked supported without a source/value.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

RISKY_PATTERNS = [
    r"lead[- ]?free",
    r"bpa[- ]?free",
    r"food[- ]?grade",
    r"hypoallergenic",
    r"dermatologist",
    r"non[- ]?comedogenic",
    r"waterproof",
    r"leakproof",
    r"airtight",
    r"dishwasher[- ]?safe",
    r"heat[- ]?resistant",
    r"cold[- ]?resistant",
    r"anti[- ]?rust|rustproof",
    r"genuine leather",
    r"stainless steel",
    r"solid wood",
    r"hand[- ]?blown|handmade|mouth[- ]?blown",
    r"medical grade|clinical|clinically",
    r"fda|ce|fcc|ul|rohs|certified|certification",
    r"ipx\d|ip\d{2}",
    r"\b\d+\s?(ml|l|oz|gal|cm|mm|in|inch|ft|lb|kg|w|v|mah|hours?|hrs?)\b",
    r"#\s?1|best|most durable|professional grade|military grade",
]

SUPPORTED_STATUSES = {"supported", "visible", "user_approved"}
NEEDS_EVIDENCE_STATUSES = {"supported", "visible"}
ALLOWED_STATUSES = {
    "supported",
    "visible",
    "user_approved",
    "needs_confirmation",
    "unsupported_removed",
    "not_used",
}


def is_risky(claim: str) -> bool:
    text = claim.lower()
    return any(re.search(pattern, text) for pattern in RISKY_PATTERNS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit PDP claims CSV.")
    parser.add_argument("--claims", required=True, help="Path to claims_audit.csv")
    parser.add_argument("--strict", action="store_true", help="Treat risky user_approved claims without notes as failures")
    args = parser.parse_args()

    path = Path(args.claims).expanduser().resolve()
    if not path.exists():
        print(f"ERROR: claims file not found: {path}")
        return 1

    failures = 0
    warnings = 0

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required_cols = {"image_no", "claim", "claim_type", "evidence_source", "evidence_value", "status", "replacement_safe_wording", "notes"}
        missing_cols = required_cols - set(reader.fieldnames or [])
        if missing_cols:
            print("FAIL: missing columns: " + ", ".join(sorted(missing_cols)))
            return 1

        rows = list(reader)

    if not rows:
        print("WARN: claims_audit.csv has no claim rows")
        return 0

    for idx, row in enumerate(rows, start=2):
        claim = (row.get("claim") or "").strip()
        status = (row.get("status") or "").strip().lower()
        evidence_source = (row.get("evidence_source") or "").strip()
        evidence_value = (row.get("evidence_value") or "").strip()
        notes = (row.get("notes") or "").strip()

        if not claim:
            print(f"FAIL row {idx}: empty claim")
            failures += 1
            continue

        if status not in ALLOWED_STATUSES:
            print(f"FAIL row {idx}: invalid status `{status}` for claim `{claim}`")
            failures += 1
            continue

        if status in NEEDS_EVIDENCE_STATUSES and (not evidence_source or not evidence_value):
            print(f"FAIL row {idx}: `{status}` claim lacks evidence source/value: {claim}")
            failures += 1

        if is_risky(claim):
            if status not in SUPPORTED_STATUSES:
                print(f"WARN row {idx}: risky claim is not approved for use, keep out of image text: {claim}")
                warnings += 1
            elif status == "user_approved" and args.strict and not notes:
                print(f"FAIL row {idx}: risky user_approved claim needs notes explaining approval: {claim}")
                failures += 1
            elif status in {"supported", "visible"} and (not evidence_source or not evidence_value):
                print(f"FAIL row {idx}: risky supported/visible claim lacks evidence: {claim}")
                failures += 1

    if failures:
        print(f"FAIL: {failures} failure(s), {warnings} warning(s)")
        return 1

    print(f"PASS: audited {len(rows)} claim row(s), {warnings} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

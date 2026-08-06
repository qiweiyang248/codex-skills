#!/usr/bin/env python3
"""Check robots.txt rules for common AI crawlers."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path


CRAWLERS = [
    "GPTBot",
    "ChatGPT-User",
    "OAI-SearchBot",
    "ClaudeBot",
    "Claude-Web",
    "anthropic-ai",
    "PerplexityBot",
    "Perplexity-User",
    "CCBot",
    "Google-Extended",
    "Applebot-Extended",
    "Amazonbot",
    "Bytespider",
]


def fetch_robots(site_url: str) -> tuple[str, str]:
    if not urllib.parse.urlparse(site_url).scheme:
        site_url = "https://" + site_url
    root = urllib.parse.urlunparse((*urllib.parse.urlparse(site_url)[:2], "", "", "", ""))
    robots_url = urllib.parse.urljoin(root + "/", "robots.txt")
    try:
        with urllib.request.urlopen(robots_url, timeout=20) as res:
            return robots_url, res.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return robots_url, f"FETCH_ERROR: {exc}"


def parse_groups(robots_txt: str) -> list[dict[str, list[str]]]:
    groups: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] = {"agents": [], "rules": []}
    for raw in robots_txt.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, value = [x.strip() for x in line.split(":", 1)]
        key = key.lower()
        if key == "user-agent":
            if current["rules"]:
                groups.append(current)
                current = {"agents": [], "rules": []}
            current["agents"].append(value.lower())
        elif key in {"allow", "disallow"} and current["agents"]:
            current["rules"].append(f"{key}:{value}")
    if current["agents"] or current["rules"]:
        groups.append(current)
    return groups


def status_for(bot: str, groups: list[dict[str, list[str]]]) -> tuple[str, str]:
    bot_l = bot.lower()
    applicable = [g for g in groups if bot_l in g["agents"]] or [g for g in groups if "*" in g["agents"]]
    if not applicable:
        return "unknown", "No matching robots group found."
    rules = [r for g in applicable for r in g["rules"]]
    disallow_root = any(r.lower() == "disallow:/" for r in rules)
    allow_root = any(r.lower() == "allow:/" for r in rules)
    if disallow_root and not allow_root:
        return "blocked", "Disallow: / applies."
    if any(r.lower().startswith("disallow:") and r.split(":", 1)[1].strip() for r in rules):
        return "partially_blocked", "Specific disallow rules apply; review important product, collection, and guide paths."
    return "allowed", "No blocking Disallow rule detected."


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("site_url")
    ap.add_argument("--json-out", default="ai_crawler_access.json")
    ap.add_argument("--csv-out", default="ai_crawler_access.csv")
    args = ap.parse_args()

    robots_url, robots_txt = fetch_robots(args.site_url)
    groups = parse_groups(robots_txt)
    rows = []
    for bot in CRAWLERS:
        status, evidence = status_for(bot, groups)
        rows.append({"crawler": bot, "status": status, "evidence": evidence})

    Path(args.json_out).write_text(
        json.dumps({"robots_url": robots_url, "crawlers": rows}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    with Path(args.csv_out).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["crawler", "status", "evidence"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {args.json_out} and {args.csv_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

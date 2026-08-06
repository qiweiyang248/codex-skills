#!/usr/bin/env python3
"""Extract basic SEO fields from discovered pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


UA = "CodexIndependentSiteSEO/1.0 (+dry-run audit)"


def fetch_html(url: str, timeout: int = 20) -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            raw = res.read()
            charset = res.headers.get_content_charset() or "utf-8"
            return res.status, raw.decode(charset, errors="replace")
    except Exception as exc:  # noqa: BLE001
        return None, f"FETCH_ERROR: {exc}"


class SEOHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.headings: dict[str, list[str]] = {"h1": [], "h2": [], "h3": []}
        self.images: list[dict[str, str]] = []
        self.links: list[str] = []
        self.json_ld: list[str] = []
        self._capture: str | None = None
        self._script_type = ""
        self._buffer: list[str] = []
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        data = {k.lower(): v or "" for k, v in attrs}
        if tag == "title":
            self._capture = "title"
            self._buffer = []
        elif tag in self.headings:
            self._capture = tag
            self._buffer = []
        elif tag == "script":
            self._script_type = data.get("type", "").lower()
            if self._script_type == "application/ld+json":
                self._capture = "json_ld"
                self._buffer = []
        elif tag == "meta":
            key = data.get("name") or data.get("property")
            if key and data.get("content"):
                self.meta[key.lower()] = data["content"].strip()
        elif tag == "link":
            rel = data.get("rel", "").lower()
            href = data.get("href", "")
            if "canonical" in rel:
                self.canonical = href
        elif tag == "img":
            self.images.append(
                {
                    "src": data.get("src") or data.get("data-src") or "",
                    "alt": data.get("alt", ""),
                    "width": data.get("width", ""),
                    "height": data.get("height", ""),
                }
            )
        elif tag == "a" and data.get("href"):
            self.links.append(data["href"])

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._capture == "title" and tag == "title":
            self.title = " ".join("".join(self._buffer).split())
            self._capture = None
        elif self._capture in self.headings and tag == self._capture:
            text = " ".join("".join(self._buffer).split())
            if text:
                self.headings[self._capture].append(text)
            self._capture = None
        elif self._capture == "json_ld" and tag == "script":
            self.json_ld.append("".join(self._buffer).strip())
            self._capture = None
            self._script_type = ""

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._buffer.append(data)
        if data.strip() and self._capture != "json_ld":
            self._text.append(data.strip())

    @property
    def word_count(self) -> int:
        text = " ".join(self._text)
        return len(re.findall(r"\b\w+\b", text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="pages_raw.json")
    ap.add_argument("--out", default="pages_parsed.json")
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()

    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    pages = raw.get("pages", [])[: args.limit]
    parsed = []
    for url in pages:
        status, html = fetch_html(url)
        parser = SEOHTMLParser()
        if status and status < 400:
            parser.feed(html)
        parsed.append(
            {
                "url": url,
                "status": status,
                "title": parser.title,
                "meta_description": parser.meta.get("description", ""),
                "robots_meta": parser.meta.get("robots", ""),
                "canonical": parser.canonical,
                "headings": parser.headings,
                "word_count": parser.word_count,
                "images": parser.images,
                "links": parser.links,
                "json_ld": parser.json_ld,
            }
        )
    Path(args.out).write_text(json.dumps({"pages": parsed}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out} with {len(parsed)} parsed pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

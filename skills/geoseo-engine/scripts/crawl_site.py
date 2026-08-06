#!/usr/bin/env python3
"""Lightweight site discovery for ecommerce SEO audits."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


UA = "CodexGeoSEOEngine/1.0 (+read-only audit)"


def fetch_text(url: str, timeout: int = 20) -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            raw = res.read()
            charset = res.headers.get_content_charset() or "utf-8"
            return res.status, raw.decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body
    except Exception as exc:  # noqa: BLE001 - audit helper should keep going
        return None, f"FETCH_ERROR: {exc}"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        data = dict(attrs)
        href = data.get("href")
        if href:
            self.links.append(href)


def normalize_site_url(url: str) -> str:
    if not urllib.parse.urlparse(url).scheme:
        url = "https://" + url
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "", "", "", ""))


def same_host(url: str, root: str) -> bool:
    return urllib.parse.urlparse(url).netloc == urllib.parse.urlparse(root).netloc


def discover_sitemaps(site_url: str, robots_txt: str) -> list[str]:
    sitemaps: list[str] = []
    for line in robots_txt.splitlines():
        if line.lower().startswith("sitemap:"):
            sitemaps.append(line.split(":", 1)[1].strip())
    default = urllib.parse.urljoin(site_url + "/", "sitemap.xml")
    if default not in sitemaps:
        sitemaps.append(default)
    return sitemaps


def parse_sitemap(xml_text: str) -> tuple[list[str], list[str]]:
    urls: list[str] = []
    nested: list[str] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return urls, nested
    for elem in root.iter():
        if elem.tag.endswith("loc") and elem.text:
            loc = elem.text.strip()
            if loc.endswith(".xml") or "sitemap" in loc:
                nested.append(loc)
            else:
                urls.append(loc)
    return urls, nested


def homepage_links(site_url: str) -> list[str]:
    status, html = fetch_text(site_url)
    if status is None or status >= 400:
        return []
    parser = LinkParser()
    parser.feed(html)
    urls: list[str] = []
    for href in parser.links:
        absolute = urllib.parse.urljoin(site_url + "/", href)
        parsed = urllib.parse.urlparse(absolute)
        clean = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
        if same_host(clean, site_url):
            urls.append(clean)
    return sorted(set(urls))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("site_url")
    ap.add_argument("--out", default="pages_raw.json")
    ap.add_argument("--max-pages", type=int, default=200)
    args = ap.parse_args()

    site_url = normalize_site_url(args.site_url)
    robots_url = urllib.parse.urljoin(site_url + "/", "robots.txt")
    robots_status, robots_txt = fetch_text(robots_url)
    sitemaps = discover_sitemaps(site_url, robots_txt if robots_status and robots_status < 400 else "")

    pages: list[str] = []
    seen_sitemaps: set[str] = set()
    queue = list(sitemaps)
    while queue and len(pages) < args.max_pages:
        sitemap = queue.pop(0)
        if sitemap in seen_sitemaps:
            continue
        seen_sitemaps.add(sitemap)
        status, xml_text = fetch_text(sitemap)
        if status is None or status >= 400:
            continue
        urls, nested = parse_sitemap(xml_text)
        pages.extend([u for u in urls if same_host(u, site_url)])
        queue.extend(nested[:20])

    if not pages:
        pages = homepage_links(site_url)

    output = {
        "site_url": site_url,
        "robots_url": robots_url,
        "robots_status": robots_status,
        "robots_txt": robots_txt if robots_status and robots_status < 400 else "",
        "sitemaps": sorted(seen_sitemaps or set(sitemaps)),
        "pages": sorted(set(pages))[: args.max_pages],
    }
    Path(args.out).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out} with {len(output['pages'])} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

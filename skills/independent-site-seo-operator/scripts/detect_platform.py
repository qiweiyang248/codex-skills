#!/usr/bin/env python3
"""Detect Shopify, WooCommerce, and WordPress ecommerce platform signals."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path


UA = "CodexIndependentSitePlatformDetector/1.0 (+dry-run audit)"


def fetch_text(url: str, timeout: int = 20) -> tuple[int | None, str, str]:
    if not urllib.parse.urlparse(url).scheme:
        url = "https://" + url
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            raw = res.read()
            charset = res.headers.get_content_charset() or "utf-8"
            return res.status, res.geturl(), raw.decode(charset, errors="replace")
    except Exception as exc:  # noqa: BLE001
        return None, url, f"FETCH_ERROR: {exc}"


def detect_from_text(url: str, html: str) -> dict:
    lower = (url + "\n" + html).lower()
    signals = {
        "shopify": ["cdn.shopify.com", "shopify.theme", "shopify-section", "myshopify.com", "/products/", "/collections/"],
        "woocommerce": [
            "woocommerce",
            "wp-content/plugins/woocommerce",
            "single-product",
            "product_cat",
            "add_to_cart_button",
            "/product/",
            "/product-category/",
            "?post_type=product",
        ],
        "wordpress": ["wp-content", "wp-includes", "wordpress", "wp-json", "yoast", "rank-math", "aioseo"],
    }
    hits = {platform: [s for s in values if s in lower] for platform, values in signals.items()}
    if hits["shopify"]:
        platform = "shopify"
    elif hits["woocommerce"]:
        platform = "woocommerce"
    elif hits["wordpress"]:
        platform = "wordpress"
    else:
        platform = "unknown"
    return {
        "platform": platform,
        "confidence": "high" if hits.get(platform) and len(hits[platform]) >= 2 else "medium" if platform != "unknown" else "low",
        "signals": hits,
        "output_routing": {
            "shopify": "outputs/shopify-content-update.csv",
            "woocommerce": "outputs/woocommerce-product-update.csv",
            "wordpress": "outputs/wordpress-page-update.csv",
            "unknown": "outputs/page-seo-update-sheet.csv",
        }.get(platform, "outputs/page-seo-update-sheet.csv"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("site_url")
    ap.add_argument("--html-file", default="")
    ap.add_argument("--out", default="platform-detection.json")
    args = ap.parse_args()

    if args.html_file:
        final_url = args.site_url
        status = None
        html = Path(args.html_file).read_text(encoding="utf-8", errors="replace")
    else:
        status, final_url, html = fetch_text(args.site_url)
    result = detect_from_text(final_url, html)
    result.update({"site_url": args.site_url, "final_url": final_url, "status": status})
    Path(args.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}; platform={result['platform']} confidence={result['confidence']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Detect Shopify, WooCommerce, and WordPress ecommerce platform signals."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path


UA = "CodexGeoSEOEngine/1.0 (+read-only platform detection)"


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
    # Route shapes are weak evidence because custom WordPress and headless sites
    # commonly expose Shopify-like /products/ and /collections/ URLs.
    signals = {
        "shopify": {
            "cdn.shopify.com": 5,
            "shopify.theme": 5,
            "myshopify.com": 5,
            "shopify-section": 3,
            "shopify-payment-button": 3,
            "/products/": 0.5,
            "/collections/": 0.5,
        },
        "woocommerce": {
            "wp-content/plugins/woocommerce": 6,
            "woocommerce": 3,
            "wc-ajax": 3,
            "woocommerce_params": 3,
            "single-product": 2,
            "product_cat": 2,
            "add_to_cart_button": 2,
            "?add-to-cart=": 2,
            "/product/": 0.5,
            "/product-category/": 0.5,
            "?post_type=product": 1,
        },
        "wordpress": {
            "wp-content": 4,
            "wp-includes": 4,
            "wp-json": 3,
            "api.w.org": 3,
            "wordpress": 2,
            "yoast": 2,
            "rank-math": 2,
            "aioseo": 2,
        },
    }
    hits = {
        platform_name: [signal for signal in weighted if signal in lower]
        for platform_name, weighted in signals.items()
    }
    scores = {
        platform_name: sum(weighted[signal] for signal in hits[platform_name])
        for platform_name, weighted in signals.items()
    }

    ecommerce_scores = {name: scores[name] for name in ("shopify", "woocommerce")}
    ecommerce_platform = max(ecommerce_scores, key=ecommerce_scores.get)
    if ecommerce_scores[ecommerce_platform] >= 3:
        platform = ecommerce_platform
        # Prefer WooCommerce on a clear WordPress foundation when ecommerce
        # scores tie; Shopify-like paths alone must never override this.
        if (
            ecommerce_scores["shopify"] == ecommerce_scores["woocommerce"]
            and scores["wordpress"] >= 3
            and scores["woocommerce"] > 0
        ):
            platform = "woocommerce"
    elif scores["wordpress"] >= 3:
        platform = "wordpress"
    else:
        platform = "unknown"

    winning_score = scores.get(platform, 0)
    if platform in ecommerce_scores:
        # WordPress is the expected foundation of WooCommerce, not a competing
        # platform classification.
        competing_scores = [
            score for name, score in ecommerce_scores.items() if name != platform
        ]
    else:
        competing_scores = [
            scores["shopify"],
            scores["woocommerce"],
        ]
    margin = winning_score - max(competing_scores, default=0)
    if platform == "unknown":
        confidence = "low"
    elif winning_score >= 5 and margin >= 2:
        confidence = "high"
    elif winning_score >= 3:
        confidence = "medium"
    else:
        confidence = "low"
    return {
        "platform": platform,
        "confidence": confidence,
        "signals": hits,
        "scores": scores,
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

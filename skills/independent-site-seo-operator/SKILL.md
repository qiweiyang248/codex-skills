---
name: independent-site-seo-operator
description: Shopify-first, WooCommerce-aware independent ecommerce SEO operator for technical SEO, on-page SEO, product page SEO, category/collection SEO, image SEO, internal linking, and JSON-LD fixes. Use when Codex is asked to audit or optimize SEO for Shopify, WooCommerce, WordPress ecommerce, or independent ecommerce sites; produce SEO titles, meta descriptions, H1s, FAQs, image alt text, schema recommendations, platform-specific CSV update sheets, or dry-run implementation plans for ecommerce pages.
---

# Independent Site SEO Operator

## Overview

Use this skill to audit and optimize ecommerce SEO for Shopify-first, WooCommerce-aware independent sites serving US/EU markets. Produce executable SEO assets, not only commentary: reports, platform-specific update sheets, schema JSON-LD, image alt text sheets, internal link recommendations, and dry-run code-change plans.

## Invocation Fit

Use this skill when the user asks for independent site SEO, Shopify SEO, product page SEO, collection page SEO, title/meta/H1/FAQ rewrites, image SEO, schema, sitemap/robots/canonical review, or SEO-ready content updates.

If the user asks for SEO plus GEO plus conversion in one package, prefer `independent-site-optimization-pack`.

## Inputs

Accept partial input and infer missing context from the site when possible.

- Site URL or local site files.
- Market, default `US/EU`.
- Platform, default auto-detect with Shopify priority and WooCommerce/WordPress ecommerce fallback.
- Product category, default infer from product and collection pages.
- Target pages, default sample homepage, products, collections, blogs/guides, about, and policy pages.
- Competitors, optional. If missing, recommend competitor research steps instead of inventing claims.
- Output directory, default `outputs/` under the current task workspace.

## Workflow

1. Discover the site.
   - Fetch `robots.txt`, sitemap XML, and homepage links.
   - Detect Shopify URL patterns: `/products/`, `/collections/`, `/blogs/`, `/pages/`.
   - Detect WooCommerce/WordPress patterns: `/product/`, `/product-category/`, `/shop/`, `/category/`, `/tag/`, `/wp-content/`, WooCommerce schema/classes, and WordPress generator hints.
   - Sample representative templates before writing recommendations.
2. Run objective extraction.
   - Use scripts in `scripts/` when network or local HTML access is available.
   - Extract title, meta description, canonical, robots meta, H1/H2/H3, word count, images, internal links, and JSON-LD.
3. Classify pages.
   - Classify as home, product, collection, blog, page, policy, search/filter, or unknown.
   - For Shopify, treat `/collections/` as collection pages.
   - For WooCommerce, treat `/product-category/` as product category pages and `/product/` as product pages.
   - For WordPress ecommerce content, treat posts/pages as blog, guide, page, or policy based on URL and headings.
   - Flag faceted/filter URLs and duplicate thin category/collection pages.
4. Audit SEO modules.
   - Technical SEO: crawlability, sitemap, robots, canonical, noindex, redirects, HTTPS/www consistency, speed hints, mobile first-screen usability.
   - On-page SEO: title, meta description, H1 uniqueness, heading intent, URL clarity, keyword fit, internal links.
   - Product SEO: product title, model/size/color/function clarity, above-the-fold value, bullets, specs, usage/install content, reviews, FAQ, Product/Offer schema.
   - Collection SEO: buyer-intent title, intro copy, filter logic, related collections, FAQ, breadcrumb and ItemList/Breadcrumb schema.
   - Image SEO: filenames, alt text, image role, compression/WebP, lazy loading.
   - Schema: Organization, WebSite, BreadcrumbList, Product, Offer, AggregateRating, Review, FAQPage, HowTo, Article/BlogPosting.
5. Produce concrete fixes.
   - Rewrite copy in market-ready English.
   - Avoid keyword stuffing, vague claims, and unsupported "premium" language.
   - Include before/after examples where the current value exists.
6. Prioritize.
   - Calculate `Priority Score = Impact x Confidence x Ease`.
   - Use P0 for crawl/index/main conversion blockers, P1 for ranking or core page conversion issues, P2 for content expansion and authority growth.
7. Output files.
   - Write reports, CSVs, JSON-LD, and implementation checklists.
   - Choose platform-specific CSVs: Shopify -> `shopify-content-update.csv`; WooCommerce -> `woocommerce-product-update.csv`; WordPress pages/posts -> `wordpress-page-update.csv`.
   - Do not modify live Shopify, WordPress, WooCommerce, theme, or plugin code by default.

## Required Recommendation Fields

Every recommendation row must include:

- Page URL
- Page Type
- Issue Type
- Current Value
- Suggested Value
- Target Field
- Modification Method
- Priority
- Risk Level
- Verification Method

## Platform-Specific Content Fields

When Shopify product pages are involved, output CSV or Markdown tables with these fields:

- `handle`
- `product_title`
- `seo_title`
- `meta_description`
- `h1`
- `subtitle`
- `product_bullets`
- `accordion_faq`
- `specs_copy`
- `image_filename`
- `image_alt_text`
- `schema_recommendation`

When WooCommerce product pages are involved, output `woocommerce-product-update.csv` or Markdown tables with these fields:

- `product_id`
- `sku`
- `slug`
- `product_name`
- `seo_title`
- `meta_description`
- `h1`
- `short_description`
- `product_description`
- `product_bullets`
- `accordion_faq`
- `attributes_specs`
- `image_filename`
- `image_alt_text`
- `schema_recommendation`
- `plugin_target`

When WordPress pages or posts are involved, output `wordpress-page-update.csv` or Markdown tables with these fields:

- `post_id`
- `post_type`
- `slug`
- `current_title`
- `seo_title`
- `meta_description`
- `h1`
- `intro_copy`
- `body_update`
- `faq_block`
- `internal_links`
- `schema_recommendation`
- `plugin_target`

## Code And Theme Fix Rules

Default to dry-run only. If theme code, Liquid, WordPress theme templates, child theme files, SEO plugin settings, schema plugin settings, `functions.php`, JSON-LD, `robots.txt`, sitemap, canonical, or schema changes are needed, output:

- File path
- Current issue
- Suggested modification
- Unified diff patch
- Rollback method
- Verification method

For Shopify, express code recommendations as Liquid/theme dry-run patches. For WooCommerce/WordPress, express code recommendations as theme template, child theme, SEO plugin, schema plugin, or `functions.php` dry-run patches. Only edit local files after the user explicitly asks to execute changes. Never claim a live Shopify or WordPress site was changed unless the user provided access and explicitly requested it.

## Scoring

SEO score is 0-100:

- 20% Crawl and index foundations
- 20% Metadata and headings
- 20% Ecommerce content completeness
- 15% Schema and structured data
- 15% Internal links and site architecture
- 10% Image SEO and performance hints

Priority:

- P0: fix immediately. Blocks crawling, indexing, canonicalization, product discovery, or purchase path.
- P1: fix within 30 days. Affects rankings, CTR, schema eligibility, and core product/collection conversion.
- P2: fix in 60-90 days. Supports content depth, authority, and long-term growth.

## Output Files

Create or update these files when running the skill:

- `outputs/seo-audit-report.md`
- `outputs/seo-priority-fixes.csv`
- `outputs/page-seo-update-sheet.csv`
- `outputs/image-alt-text.csv`
- `outputs/woocommerce-product-update.csv` when WooCommerce product pages are identified
- `outputs/wordpress-page-update.csv` when WordPress pages/posts need updates
- `outputs/schema-jsonld/product-schema.json`
- `outputs/schema-jsonld/faq-schema.json`

## References

Load only what is needed:

- `references/shopify-seo-checklist.md` for audit coverage.
- `references/platform-output-mapping.md` for Shopify, WooCommerce, and WordPress output selection.
- `references/product-page-seo-template.md` for product page output.
- `references/collection-page-seo-template.md` for collection page output.
- `references/image-seo-rules.md` for filename and alt text standards.
- `references/schema-rules.md` for JSON-LD decisions.
- `references/ecommerce-keyword-mapping.md` for mapping page type to intent.
- `references/conversion-review-checklist.md` for SEO-adjacent conversion checks.

## Scripts

Use scripts for objective extraction and CSV/JSON output:

- `scripts/detect_platform.py`
- `scripts/crawl_site.py`
- `scripts/extract_page_data.py`
- `scripts/classify_templates.py`
- `scripts/extract_schema.py`
- `scripts/check_images.py`
- `scripts/score_seo.py`
- `scripts/export_seo_csv.py`

Scripts are helpers, not the final strategy. After running scripts, apply judgment to buyer intent, copy quality, conversion clarity, and implementation risk.

## Quality Rules

- Write for US/EU ecommerce buyers in clear English.
- Prefer specific size, material, fit, installation, warranty, shipping, compatibility, and use-case language.
- Avoid unsupported superlatives, vague "premium quality" claims, "perfect for everyone", and generic AI-sounding filler.
- Keep SEO titles near 50-65 characters when practical.
- Keep meta descriptions near 140-160 characters when practical.
- Require one clear H1 per page.
- Keep FAQ answers specific and useful.
- Never invent reviews, ratings, certifications, media mentions, or competitor facts.

## Final Response Format

When done, summarize:

1. Output files created.
2. Highest-priority P0/P1 fixes.
3. CSV or JSON-LD files ready for Shopify operations.
4. Any items that need user approval before local or live code edits.

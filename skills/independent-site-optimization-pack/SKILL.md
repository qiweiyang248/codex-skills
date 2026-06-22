---
name: independent-site-optimization-pack
description: Orchestrator skill for Shopify-first, WooCommerce-aware independent ecommerce growth audits that combine SEO, GEO, and conversion review into an executable optimization package. Use when Codex is asked to fully audit Shopify, WooCommerce, WordPress ecommerce, or independent ecommerce sites; produce platform-specific SEO plus GEO optimization packs, Shopify/WooCommerce/WordPress content update CSVs, image alt sheets, schema JSON-LD fixes, internal link plans, GEO content plans, action plans, or dry-run implementation checklists without directly changing live code.
---

# Independent Site Optimization Pack

## Overview

Use this orchestrator to produce a complete independent-site growth optimization package for Shopify-first, WooCommerce-aware ecommerce sites in US/EU markets. It combines SEO foundations, GEO/AI search readiness, and conversion review into files Codex can continue executing later.

Default behavior is dry-run output only. Do not modify live Shopify, WordPress, WooCommerce, theme, plugin, or production files unless the user explicitly says "execute changes", "modify files", "submit PR", or equivalent.

## Invocation Fit

Use this skill when the user asks to fully audit an independent ecommerce site, improve SEO plus GEO plus conversion, create a Shopify/WooCommerce/WordPress content update package, or output an executable optimization plan.

If the user asks only for SEO, use `independent-site-seo-operator`. If the user asks only for AI search visibility or GEO, use `independent-site-geo-operator`.

## Inputs

Proceed with partial input and infer missing context from the site.

- Site URL or local site files.
- Market, default `US/EU`.
- Platform, default auto-detect with Shopify priority and WooCommerce/WordPress ecommerce fallback.
- Product category, default infer from pages.
- Target pages, default homepage, products, collections, blogs/guides, about, policy pages.
- Competitors, optional. If absent, mark competitor research as a recommended step.
- Whether execution is allowed. Default `dry-run only`.
- Output directory, default `outputs/`.

## Orchestration Workflow

1. Gather input and constraints.
   - Confirm market, platform, category, target pages, and whether the user asked for dry-run only or execution.
   - If information is missing, infer before asking. Ask only if a missing detail would materially change the work.
2. Discover site structure.
   - Fetch or inspect robots, sitemap, homepage links, representative page templates, and platform signals.
   - Classify product, collection/category, blog/guide, WordPress page/post, policy, about, and utility pages.
   - Route Shopify pages to Shopify outputs, WooCommerce products/categories to WooCommerce outputs, and WordPress pages/posts to WordPress outputs.
3. Run SEO workflow.
   - Use sibling skill `../independent-site-seo-operator/SKILL.md` when available.
   - Use its scripts and references for crawl, metadata, page type, image, schema, and CSV extraction.
4. Run GEO workflow.
   - Use sibling skill `../independent-site-geo-operator/SKILL.md` when available.
   - Use its scripts and references for AI crawler access, entity clarity, answer structure, query fan-out, and citation planning.
5. Review conversion.
   - Evaluate above-the-fold clarity, offer clarity, CTA path, trust signals, product detail completeness, image decision support, FAQ placement, and mobile purchase friction.
6. Prioritize by business impact.
   - Calculate `Priority Score = Impact x Confidence x Ease`.
   - Prioritize fixes that improve SEO, GEO, and conversion together.
7. Generate the optimization package.
   - Write all required output files.
   - Include copy-ready recommendations, platform-specific CSVs, JSON-LD, internal links, GEO content plan, and implementation checklist.
8. If the user later says "execute changes".
   - Read `outputs/action-plan.md`.
   - Start with a dry-run implementation plan.
   - Apply local changes step by step only where files are accessible.
   - Never edit live Shopify admin, WordPress admin, WooCommerce product data, production theme, or plugin settings without explicit access and approval.

## Required Output Files

The final output package must contain exactly these files at minimum:

- `outputs/audit-report.md`
- `outputs/optimization-pack.md`
- `outputs/action-plan.md`
- `outputs/shopify-content-update.csv`
- `outputs/woocommerce-product-update.csv` when WooCommerce products are identified
- `outputs/wordpress-page-update.csv` when WordPress pages/posts need updates
- `outputs/image-alt-text-sheet.csv`
- `outputs/schema-jsonld-fixes.json`
- `outputs/internal-link-plan.md`
- `outputs/geo-content-plan.md`
- `outputs/implementation-checklist.md`

Extra supporting files are allowed only when they make execution clearer.

## Required Recommendation Fields

Every optimization item must include:

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

## Platform-Specific Update Files

For Shopify product pages, prefer CSV or Markdown update tables with:

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

For WooCommerce product pages, create `outputs/woocommerce-product-update.csv` with:

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

For WordPress pages/posts, create `outputs/wordpress-page-update.csv` with:

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

## Code, Liquid, Robots, Sitemap, Canonical, And Schema Fixes

When changes touch theme code, Liquid, WordPress theme templates, child theme files, SEO plugin settings, schema plugin settings, `functions.php`, JSON-LD, `robots.txt`, sitemap, canonical tags, or schema, output:

- File path
- Current issue
- Suggested modification
- Unified diff patch
- Rollback method
- Verification method

Keep these as dry-run recommendations unless the user explicitly asks to execute local changes.

Implementation routing:

- Shopify: Liquid, theme snippets, JSON templates, Shopify app/theme settings.
- WooCommerce: product/category fields, product attributes, WooCommerce CSV, child theme template overrides, SEO plugin fields, schema plugin settings, `functions.php` snippets.
- WordPress pages/posts: page/post fields, block editor content, SEO plugin fields, schema plugin fields, theme templates, child theme, or `functions.php` snippets.
- If a plugin is detected, target it by name. If not, keep the recommendation plugin-neutral and include safer alternatives.

## Scoring

SEO score:

- 20% Crawl and index foundations
- 20% Metadata and headings
- 20% Ecommerce content completeness
- 15% Schema and structured data
- 15% Internal links and architecture
- 10% Image SEO and performance hints

GEO score:

- 20% AI Crawl Access
- 20% Entity Clarity
- 20% Answer Structure
- 15% Product Data Completeness
- 15% Trust and Authority Signals
- 10% AI Query Coverage

Conversion score:

- 25% Above-the-fold clarity
- 20% Offer clarity
- 15% Trust signals
- 15% CTA path
- 15% Product detail completeness
- 10% Mobile experience

Priority:

- P0: immediate. Blocks crawl, index, canonical correctness, main conversion path, or core entity understanding.
- P1: within 30 days. Affects rankings, AI citation, schema eligibility, or core page conversion.
- P2: 60-90 days. Content expansion, authority building, long-term topic coverage.

## References And Templates

Load only what is needed:

- `references/priority-scoring.md`
- `references/final-output-standard.md`
- `references/ecommerce-growth-principles.md`
- `references/platform-output-mapping.md`
- `templates/audit-report-template.md`
- `templates/optimization-pack-template.md`
- `templates/action-plan-template.md`
- `templates/shopify-content-update-template.csv`
- `templates/woocommerce-product-update-template.csv`
- `templates/wordpress-page-update-template.csv`
- `templates/image-alt-text-template.csv`
- `templates/schema-jsonld-fixes-template.json`
- `templates/internal-link-plan-template.md`
- `templates/geo-content-plan-template.md`
- `templates/implementation-checklist-template.md`

## Scripts

Use scripts for package assembly and validation:

- `scripts/assemble_outputs.py` to create required output files from templates.
- `scripts/validate_output_pack.py` to verify required files and CSV columns.
- `scripts/detect_platform.py` to route Shopify, WooCommerce, and WordPress outputs.

Use SEO and GEO sibling scripts for extraction when available.

## Quality Rules

- Produce an optimization pack, not a generic report.
- Use market-ready English for ecommerce content.
- Avoid unsupported claims, fake third-party mentions, keyword stuffing, and low-quality AI-search pages.
- State assumptions clearly when data is missing.
- Make every recommendation executable by Shopify operations, content, or development.
- Keep risk levels practical: Low for content and CSV updates, Medium for theme/schema changes, High for indexation, robots, canonical, or large template changes.

## Final Response Format

When done, summarize:

1. Required files created.
2. Top P0/P1 actions.
3. Which files are ready for Shopify operations.
4. What remains dry-run and requires explicit approval before execution.

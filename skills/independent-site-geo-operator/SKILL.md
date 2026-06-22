---
name: independent-site-geo-operator
description: Generative Engine Optimization and AI search readiness operator for Shopify, WooCommerce, WordPress ecommerce, and independent ecommerce sites. Use when Codex is asked to audit or improve ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews, answer engine visibility, AI crawler access, entity clarity, citation readiness, query fan-out coverage, llms.txt guidance, or AI-citable content plans across ecommerce platforms.
---

# Independent Site GEO Operator

## Overview

Use this skill to evaluate and improve AI search visibility for ecommerce sites. GEO here means Generative Engine Optimization, Answer Engine Optimization, AI Search Visibility, and LLM Citation Readiness.

Treat SEO as the foundation, GEO as the structured answer and entity layer, and conversion as the business outcome.

## Invocation Fit

Use this skill when the user asks whether AI systems can understand, cite, recommend, or compare a brand, product, or category. Use it for AI crawler access, entity clarity, AI-ready product data, query fan-out, citation hooks, and content plans for buying guides, comparison pages, FAQ hubs, size guides, and installation guides.

If the user asks for a complete SEO plus GEO plus conversion package, prefer `independent-site-optimization-pack`.

## Inputs

Accept partial input and infer missing details from the website.

- Site URL or local HTML/files.
- Market, default `US/EU`.
- Platform, default auto-detect with Shopify priority and WooCommerce/WordPress ecommerce fallback.
- Brand and product category, default infer from site.
- Target pages, default homepage, product pages, collection pages, about page, policy pages, and guide/blog pages.
- Known external authority sources, optional.
- Output directory, default `outputs/`.

## Workflow

1. Confirm crawl and discovery access.
   - Check `robots.txt` for major AI crawlers.
   - Do not automatically recommend allowing every bot; weigh content rights, privacy, and business goals.
2. Extract entity signals.
   - Brand name, product names, model numbers, category relationship, sameAs links, Organization schema, Product schema, policies, contact information, social profiles, and platform-specific product/category structures.
3. Review product entity completeness.
   - Model, size, color, material, functions, use case, installation, specs, price, availability, warranty, certifications, and compatibility.
4. Review answer structure.
   - Check whether pages answer: what it is, who it is for, what problem it solves, why choose it, how to choose size/model, how to install/use it, specs, pros/cons, and comparisons.
5. Review citation readiness.
   - Look for concise definitions, quote-worthy conclusions, structured specs tables, comparison tables, FAQs, How-to steps, buyer guides, review summaries, real examples, images, and videos.
6. Build query fan-out.
   - Generate buyer questions around product, use case, size, installation, alternatives, pros/cons, and comparisons.
7. Review external authority.
   - Identify real channels: YouTube reviews, forums, Reddit, creator content, third-party reviews, press/blog mentions, indexed social content, Google Merchant Center/product feed.
   - Never suggest fake mentions or manufactured authority.
8. Score and prioritize.
   - Score AI readiness and produce prioritized fixes with concrete content recommendations.
9. Output files.
   - Produce report, scorecard, query map, citation content plan, llms.txt draft if relevant, and entity schema recommendations.
   - If implementation recommendations mention platform code, map Shopify to Liquid/theme patches and WooCommerce/WordPress to theme template, child theme, SEO plugin, schema plugin, or `functions.php` dry-run patches.

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

## AI Crawler Review

Check these user agents where possible:

- GPTBot
- ChatGPT-User
- OAI-SearchBot
- ClaudeBot
- Claude-Web
- anthropic-ai
- PerplexityBot
- Perplexity-User
- CCBot
- Google-Extended
- Applebot-Extended
- Amazonbot
- Bytespider

For ecommerce sites, default recommendation is to keep core product, brand, and guide content crawlable unless the user has content licensing, privacy, or security concerns.

## Scoring

GEO score is 0-100:

- 20% AI Crawl Access
- 20% Entity Clarity
- 20% Answer Structure
- 15% Product Data Completeness
- 15% Trust and Authority Signals
- 10% AI Query Coverage

Also output:

- Citability Score
- Brand Entity Score
- Product Entity Score
- AI Crawler Access Score
- Query Coverage Score
- External Authority Score

Priority:

- P0: bot access or entity issues that block discovery or correct brand/product understanding.
- P1: missing answer structures, product specs, schema, FAQ, or core buyer questions on priority pages.
- P2: new content, comparison pages, guides, third-party authority building, and long-term topic coverage.

## llms.txt Guidance

`llms.txt` can be a useful auxiliary file for AI ecosystem discovery, but it is not a Google AI ranking requirement and must not be presented as a magic fix. Prefer clear crawlable pages, useful content, structured data, and truthful entity signals.

## Platform-Aware GEO Implementation

- Shopify: recommend copy updates, product/collection content, Liquid JSON-LD, theme snippets, and app/theme settings as dry-run patches.
- WooCommerce: recommend product/category copy, product attributes, short descriptions, long descriptions, WooCommerce product CSV fields, SEO plugin fields, schema plugin settings, child theme templates, and `functions.php` snippets as dry-run patches.
- WordPress pages/posts: recommend post/page title, SEO title, meta description, intro copy, FAQ blocks, internal links, Article/FAQ/HowTo schema plugin settings, and editor-ready content updates.
- Do not assume a specific plugin. If Yoast, Rank Math, AIOSEO, WooCommerce SEO, or a schema plugin is detected, target that plugin; otherwise keep recommendations plugin-neutral.

## Output Files

Create or update these files when running the skill:

- `outputs/geo-audit-report.md`
- `outputs/ai-readiness-scorecard.csv`
- `outputs/geo-query-map.csv`
- `outputs/ai-citation-content-plan.md`
- `outputs/llms-txt-draft.md`
- `outputs/entity-schema-recommendations.json`

## References

Load only what is needed:

- `references/ai-search-readiness-checklist.md` for audit coverage.
- `references/geo-scoring-model.md` for scoring.
- `references/entity-clarity-framework.md` for brand and product entity checks.
- `references/citation-readiness-framework.md` for citable content patterns.
- `references/query-fanout-framework.md` for buyer question expansion.
- `references/llms-txt-guidance.md` for cautious llms.txt usage.
- `references/external-authority-framework.md` for real authority signals.
- `references/platform-output-mapping.md` for Shopify, WooCommerce, and WordPress implementation routing.

## Scripts

Use scripts for objective extraction and exports:

- `scripts/check_ai_crawlers.py`
- `scripts/extract_entities.py`
- `scripts/score_geo.py`
- `scripts/generate_query_fanout.py`
- `scripts/check_answer_structure.py`
- `scripts/export_geo_csv.py`

Scripts are helpers. Codex must still judge content specificity, truthfulness, market fit, and whether a page is genuinely useful to buyers.

## Quality Rules

- Do not frame GEO as mysticism or a substitute for SEO fundamentals.
- Do not generate low-quality long-tail pages just to target AI queries.
- Do not invent reviews, awards, citations, social proof, certifications, or third-party mentions.
- Prefer tables, FAQs, comparisons, real specs, installation guidance, policy clarity, and concise answer blocks.
- Keep recommendations executable as page copy, schema, internal links, or content briefs.

## Final Response Format

When done, summarize:

1. Output files created.
2. AI readiness score and biggest blockers.
3. Top GEO content opportunities.
4. Any crawler, schema, or llms.txt changes that need user approval before implementation.

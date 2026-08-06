---
name: geoseo-engine
description: Unified SEO, Generative Engine Optimization (GEO), AI search readiness, and conversion diagnostic engine for independent ecommerce sites built with Shopify, WooCommerce, WordPress, or custom platforms. Use when Codex is asked to audit or optimize an independent site; diagnose technical SEO, on-page SEO, product and collection SEO, image SEO, internal links, schema, crawl/index issues, AI crawler access, entity clarity, citation readiness, answer structure, query fan-out coverage, trust, conversion, or produce prioritized implementation plans, platform CSVs, JSON-LD fixes, content roadmaps, and dry-run optimization packages.
---

# GeoSEO Engine

## Purpose

Run one coordinated independent-site audit instead of separate SEO, GEO, and conversion passes. Collect evidence once, score each discipline consistently, deduplicate recommendations, and produce an executable optimization package.

Treat SEO as the discovery foundation, GEO as the entity and answer layer, and conversion as the business outcome.

## Operating Modes

Choose the smallest mode that satisfies the request:

1. **Diagnostic**: inspect the site and return scores, evidence, blockers, and prioritized recommendations.
2. **Full optimization pack**: create reports, update sheets, schema fixes, internal-link plans, GEO query maps, and implementation checklists.
3. **Implementation**: modify accessible local files only after explicit authorization. Keep live Shopify, WordPress, WooCommerce, plugins, themes, and production systems unchanged unless the user explicitly authorizes those exact changes and provides access.

Default to read-only diagnostic or dry-run output. Do not interpret “audit,” “analyze,” or “optimize” as permission to edit a live site.

## Inputs

Proceed with partial input and infer safe defaults:

- Site URL or local site files.
- Market and language; infer from the site, otherwise default to its primary visible market.
- Platform; auto-detect Shopify, WooCommerce, WordPress, or custom.
- Product category and business model; infer from representative pages.
- Target pages; default to homepage, products, collections/categories, guides/blog, about, contact, and policy pages.
- Competitors; optional. Research them when current evidence is needed and a web research capability is available.
- Output directory; default to `outputs/geoseo-engine/`.

State assumptions and distinguish measured facts, public evidence, estimates, and inference.

## Workflow

### 1. Discover and classify

- Fetch `robots.txt`, declared and common sitemap locations, homepage links, and representative templates.
- Detect platform signals with `scripts/detect_platform.py`.
- Crawl conservatively with `scripts/crawl_site.py`; respect page limits and avoid authenticated, checkout, account, and destructive routes.
- Classify home, product, collection/category, guide/blog, about, policy, search/filter, utility, and duplicate/legacy routes.
- Record HTTP status, redirect chain, title, meta description, canonical, robots meta, headings, word count, images, internal links, and JSON-LD.
- Sample representative templates before making sitewide claims.

### 2. Audit SEO

Evaluate:

- Crawl and index foundations: robots, sitemaps, status codes, redirects, canonicals, noindex, faceted URLs, duplicate routes, orphan pages, HTTPS and host consistency.
- Metadata and intent: titles, meta descriptions, H1 uniqueness, heading structure, URL clarity, keyword-to-page mapping, search intent, and CTR readiness.
- Ecommerce templates: product identity, variants, specs, price, availability, shipping, returns, warranty, reviews, FAQs, collection copy, filters, breadcrumbs, and related items.
- Structured data: Organization, WebSite, BreadcrumbList, Product, Offer, AggregateRating, Review, ItemList, FAQPage, HowTo, and Article/BlogPosting. Recommend only schema supported by visible facts.
- Images and performance hints: filenames, meaningful alt text, dimensions, responsive sources, compression, modern formats, lazy loading, and excessive DOM/media payload.
- Architecture: navigation, breadcrumbs, internal links, topic clusters, pagination, search pages, and sitemap coverage.

Load only the relevant SEO references:

- `references/shopify-seo-checklist.md`
- `references/product-page-seo-template.md`
- `references/collection-page-seo-template.md`
- `references/image-seo-rules.md`
- `references/schema-rules.md`
- `references/ecommerce-keyword-mapping.md`
- `references/conversion-review-checklist.md`

### 3. Audit GEO and AI search readiness

Evaluate:

- AI crawler policy for GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, CCBot, Google-Extended, Applebot-Extended, Amazonbot, and Bytespider where observable.
- Brand and product entity clarity: names, legal/contact identity, product IDs, category relationships, sameAs links, policies, Organization and Product schema, and consistent facts across pages.
- Product data completeness: material, size, model, variant, use case, compatibility, price, availability, shipping, warranty, certification, care, and support.
- Answer structure: concise definitions, buyer questions, comparisons, pros/cons, selection guidance, steps, tables, FAQs, and quote-worthy conclusions.
- Citation readiness: verifiable claims, first-party evidence, structured specifications, real examples, media, policy clarity, and external authority.
- Query fan-out: brand, product, category, use case, alternatives, comparison, sizing, installation/use, troubleshooting, care, shipping, warranty, and trust queries.
- `llms.txt` only as an optional discovery aid; never present it as a ranking requirement or substitute for crawlable content.

Load only the relevant GEO references:

- `references/ai-search-readiness-checklist.md`
- `references/geo-scoring-model.md`
- `references/entity-clarity-framework.md`
- `references/citation-readiness-framework.md`
- `references/query-fanout-framework.md`
- `references/external-authority-framework.md`
- `references/llms-txt-guidance.md`

### 4. Review conversion and trust

Inspect above-the-fold clarity, offer comprehension, primary CTA path, product decision support, mobile friction, checkout readiness, payment choices, delivery expectations, return and warranty clarity, contact identity, reviews, certifications, social proof, and lead capture.

Do not invent traffic, conversion, revenue, reviews, certifications, awards, or competitor facts. Identify missing analytics access instead of estimating private metrics as facts.

### 5. Score and prioritize

Produce separate 0–100 scores:

- **SEO**: crawl/index 20%, metadata/headings 20%, ecommerce content 20%, schema 15%, architecture/internal links 15%, image SEO/performance hints 10%.
- **GEO**: AI crawl access 20%, entity clarity 20%, answer structure 20%, product data 15%, trust/authority 15%, query coverage 10%.
- **Conversion**: first-screen clarity 25%, offer clarity 20%, trust 15%, CTA path 15%, product detail completeness 15%, mobile experience 10%.
- **Overall GeoSEO readiness**: SEO 40%, GEO 35%, conversion 25%.

Attach a confidence level to each score based on crawl coverage and data access.

Prioritize with `Impact x Confidence x Ease`:

- **P0**: crawl/index/canonical blockers, broken purchase paths, or facts that prevent correct entity understanding.
- **P1**: ranking, AI citation, schema eligibility, product decision, or trust issues to address within 30 days.
- **P2**: content depth, authority, experimentation, and 60–90 day growth opportunities.

Merge duplicate recommendations. Prefer fixes that improve SEO, GEO, and conversion together.

### 6. Generate executable outputs

For every recommendation include:

- Page URL
- Page type
- Issue type
- Evidence/current value
- Suggested value
- Target field or file
- Modification method
- SEO/GEO/conversion impact
- Priority
- Risk level
- Verification method
- Rollback method when implementation changes code or configuration

For a full optimization pack, create at minimum:

- `audit-report.md`
- `optimization-pack.md`
- `action-plan.md`
- `seo-priority-fixes.csv`
- `page-seo-update-sheet.csv`
- `image-alt-text-sheet.csv`
- `schema-jsonld-fixes.json`
- `internal-link-plan.md`
- `geo-content-plan.md`
- `ai-readiness-scorecard.csv`
- `geo-query-map.csv`
- `ai-citation-content-plan.md`
- `entity-schema-recommendations.json`
- `implementation-checklist.md`

Add platform files only when applicable:

- Shopify: `shopify-content-update.csv`
- WooCommerce: `woocommerce-product-update.csv`
- WordPress pages/posts: `wordpress-page-update.csv`
- `llms-txt-draft.md` only when it is relevant and labeled optional.

Use `scripts/assemble_outputs.py` to initialize the package and `scripts/validate_output_pack.py` to validate required files and columns.

## Platform Routing

Read `references/platform-output-mapping.md` after platform detection.

- Shopify: route content to product, collection, page/blog, metafield, and image fields; route code to Liquid, theme snippets, JSON templates, and app/theme settings.
- WooCommerce: route content to product/category fields, attributes, tabs, and media; route code to child-theme templates, WooCommerce hooks, SEO/schema plugins, and `functions.php` dry-run patches.
- WordPress: route content to pages/posts and blocks; route code to themes, child themes, SEO/schema plugins, and `functions.php` dry-run patches.
- Custom sites: map recommendations to the observed CMS, application routes, templates, components, APIs, feeds, and deployment workflow without pretending a known platform exists.

For code, robots, sitemap, canonical, and schema changes, provide a dry-run patch, risk, rollback, and verification plan before execution.

## Scripts

Use deterministic helpers where applicable:

- Discovery: `detect_platform.py`, `crawl_site.py`, `extract_page_data.py`, `classify_templates.py`
- SEO: `extract_schema.py`, `check_images.py`, `score_seo.py`, `export_seo_csv.py`
- GEO: `check_ai_crawlers.py`, `extract_entities.py`, `check_answer_structure.py`, `generate_query_fanout.py`, `score_geo.py`, `export_geo_csv.py`
- Packaging: `assemble_outputs.py`, `validate_output_pack.py`

Treat scripts as evidence helpers, not substitutes for buyer-intent, content-quality, or implementation-risk judgment.

## Quality Rules

- Write recommendations in the site's market language; provide implementation copy in the requested language.
- Prefer specific, verifiable product, policy, and service language over generic “premium” claims.
- Keep SEO titles near 50–65 characters and meta descriptions near 140–160 characters when practical.
- Require one clear H1 per indexable page.
- Avoid keyword stuffing, doorway pages, fake authority, fabricated citations, and low-value AI-query pages.
- Cite current public sources when web research is used and separate external evidence from inference.
- Report limitations when analytics, Search Console, Merchant Center, server logs, CMS, or code access is unavailable.

## Validation

Before declaring a full pack complete:

1. Run the Skill Creator `quick_validate.py` against the skill folder.
2. Compile every Python script.
3. Run representative `--help` or fixture tests for all script families.
4. Assemble a fresh output package and run `validate_output_pack.py`.
5. Run a bounded read-only audit against one reachable independent ecommerce site.
6. Confirm no dependency points to the retired Skill folders.

## Final Response

Summarize:

1. Scores, confidence, and biggest blockers.
2. Top P0/P1 opportunities that improve SEO and GEO together.
3. Output files created and platform files ready for operations.
4. Dry-run changes that require explicit approval before implementation.

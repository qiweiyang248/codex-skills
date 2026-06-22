# Platform Output Mapping For GEO

Use this mapping to keep GEO recommendations executable across ecommerce platforms.

## Shopify

- Content targets: product description, collection description, page/blog content, metafields, image alt text.
- Code targets: Liquid, theme snippets, JSON templates, Shopify app/theme settings.
- Structured data targets: Product, Offer, FAQPage, BreadcrumbList, Organization JSON-LD.

## WooCommerce

- Content targets: product name, short description, long description, product attributes, product categories, product tabs, image alt text.
- Code targets: child theme template overrides, WooCommerce template hooks, SEO plugin fields, schema plugin settings, `functions.php` snippets.
- Structured data targets: Product, Offer, FAQPage, BreadcrumbList, Organization JSON-LD through WooCommerce core, SEO plugin, or schema plugin.

## WordPress Pages And Posts

- Content targets: page title, post title, intro copy, body content, FAQ blocks, tables, internal links.
- Code targets: theme templates, child theme, SEO plugin fields, schema plugin fields, `functions.php` snippets.
- Structured data targets: Article, BlogPosting, FAQPage, HowTo, Organization, BreadcrumbList.

## Dry-run Rule

For all platforms, recommendations touching code, plugin settings, schema generation, robots, sitemap, or canonical tags must include file path or plugin target, current issue, suggested modification, unified diff patch where file-based, rollback method, and verification method.

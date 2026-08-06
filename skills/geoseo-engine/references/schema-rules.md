# Schema Rules

Use JSON-LD that reflects visible page content. Do not invent ratings, reviews, prices, availability, certifications, or policies.

## Recommended Types

- Organization: homepage/about, with real `name`, `url`, `logo`, `sameAs`, and contact where available.
- WebSite: homepage, with SearchAction only if on-site search exists.
- BreadcrumbList: product, collection, blog, and guide pages.
- Product: product pages only.
- Offer: product pages when price, currency, availability, and URL are known.
- AggregateRating and Review: only when visible reviews exist.
- FAQPage: only when the FAQ is visible on page.
- HowTo: installation or step-by-step guide pages.
- Article or BlogPosting: editorial pages.

## Theme Or Code Fix Output

For any Liquid, JSON-LD, canonical, robots, sitemap, or theme code recommendation include:

- File path
- Current issue
- Suggested modification
- Unified diff patch
- Rollback method
- Verification method

## Verification

- Validate JSON syntax.
- Test with Google Rich Results Test or Schema Markup Validator where applicable.
- Confirm generated fields match visible content and live product data.

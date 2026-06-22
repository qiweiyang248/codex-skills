# Platform Output Mapping

Use this mapping after platform detection.

## Platform Detection Signals

Shopify:

- URL patterns: `/products/`, `/collections/`, `/blogs/`, `/pages/`.
- HTML signals: `cdn.shopify.com`, `Shopify.theme`, `shopify-section`, `myshopify.com`.
- Schema/app signals: Shopify Product JSON-LD, Shopify storefront scripts.

WooCommerce:

- URL patterns: `/product/`, `/product-category/`, `/shop/`, `?post_type=product`.
- HTML signals: `woocommerce`, `wp-content/plugins/woocommerce`, `single-product`, `product_cat`, `add_to_cart_button`.
- Schema signals: Product schema from WooCommerce or WooCommerce SEO plugins.

WordPress:

- URL/content signals: `/wp-content/`, `/wp-includes/`, WordPress generator meta, REST API links, `/category/`, `/tag/`, author/date archives.
- Plugin signals: Yoast, Rank Math, AIOSEO, schema plugins, WooCommerce SEO extensions.

## Output Routing

- Shopify product pages -> `shopify-content-update.csv`.
- WooCommerce product pages -> `woocommerce-product-update.csv`.
- WordPress pages/posts -> `wordpress-page-update.csv`.
- Image updates across all platforms -> `image-alt-text-sheet.csv` or `image-alt-text.csv`.
- JSON-LD/schema fixes across all platforms -> `schema-jsonld-fixes.json` or `schema-jsonld/*.json`.

## Code Recommendation Routing

- Shopify -> Liquid, theme snippets, JSON templates, Shopify theme/app settings.
- WooCommerce -> product/category fields, product attributes, WooCommerce CSV, child theme template overrides, SEO plugin fields, schema plugin settings, `functions.php` snippets.
- WordPress pages/posts -> page/post fields, block editor content, SEO plugin fields, schema plugin settings, theme templates, child theme, `functions.php` snippets.

## Safety

Always output dry-run patches first. Do not edit live admin content, production themes, plugin settings, or `functions.php` without explicit user approval and an accessible local codebase.

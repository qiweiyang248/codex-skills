# Platform Output Mapping

Use this reference to route outputs after site discovery.

## Platform Detection

Shopify signals:

- `/products/`, `/collections/`, `/blogs/`, `/pages/`
- `cdn.shopify.com`, `Shopify.theme`, `shopify-section`, `myshopify.com`

WooCommerce signals:

- `/product/`, `/product-category/`, `/shop/`, `?post_type=product`
- `woocommerce`, `wp-content/plugins/woocommerce`, `single-product`, `product_cat`, `add_to_cart_button`

WordPress signals:

- `/wp-content/`, `/wp-includes/`, WordPress generator meta, REST API links
- `/category/`, `/tag/`, author/date archives
- Yoast, Rank Math, AIOSEO, schema plugin markers

## Output Files By Platform

Always create the core package files:

- `outputs/audit-report.md`
- `outputs/optimization-pack.md`
- `outputs/action-plan.md`
- `outputs/image-alt-text-sheet.csv`
- `outputs/schema-jsonld-fixes.json`
- `outputs/internal-link-plan.md`
- `outputs/geo-content-plan.md`
- `outputs/implementation-checklist.md`

Create platform files as needed:

- Shopify product updates -> `outputs/shopify-content-update.csv`
- WooCommerce product updates -> `outputs/woocommerce-product-update.csv`
- WordPress page/post updates -> `outputs/wordpress-page-update.csv`

## Code Recommendation Routing

- Shopify -> Liquid, theme snippets, JSON templates, Shopify theme/app settings.
- WooCommerce -> product/category fields, product attributes, WooCommerce CSV, child theme template overrides, SEO plugin fields, schema plugin settings, `functions.php` snippets.
- WordPress pages/posts -> block editor content, page/post fields, SEO plugin fields, schema plugin settings, theme templates, child theme, `functions.php` snippets.

## Verification

- Shopify: rendered page source, theme preview, Shopify admin field review, rich result validation.
- WooCommerce: product edit screen, product CSV import preview, rendered product/category page source, SEO/schema plugin preview, rich result validation.
- WordPress: page/post editor, SEO plugin preview, rendered page source, rich result validation.

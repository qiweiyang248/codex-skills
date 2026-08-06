# Final Output Standard

The optimization package must create these files:

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

Every recommendation must include:

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

For theme, Liquid, robots, sitemap, canonical, or schema fixes include:

- File path
- Current issue
- Suggested modification
- Unified diff patch
- Rollback method
- Verification method

Default to dry-run only. Execute local changes only after the user explicitly asks to execute modifications.

## Platform Routing

- Shopify -> `shopify-content-update.csv`; code suggestions use Liquid/theme snippets/JSON templates.
- WooCommerce -> `woocommerce-product-update.csv`; code suggestions use WooCommerce product/category fields, child theme template overrides, SEO plugin fields, schema plugin settings, or `functions.php` dry-run patches.
- WordPress pages/posts -> `wordpress-page-update.csv`; code suggestions use page/post fields, block editor content, SEO plugin fields, schema plugin settings, child theme templates, or `functions.php` dry-run patches.

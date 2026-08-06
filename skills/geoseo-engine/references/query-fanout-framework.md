# Query Fan-out Framework

Generate buyer questions around the product category and page intent.

## Fan-out Types

- Best product for use case.
- Size or fit selection.
- Product type comparison.
- Installation or setup.
- Material, durability, care, or maintenance.
- Compatibility.
- Pros and cons.
- Alternatives and competitor comparison.
- Policy questions: shipping, returns, warranty.

## Example Pattern

For `[product type]`:

- best `[product type]` for `[use case]`
- `[variant A]` vs `[variant B]`
- what size `[product type]` for `[space/use case]`
- how to install `[product type]`
- `[material/function]` pros and cons
- is `[product type]` worth it for `[buyer]`

## Output Columns

```csv
topic,ai_query,buyer_intent,current_coverage,recommended_page_type,recommended_title,recommended_url_slug,required_entities,required_tables,required_faq,citation_hook,internal_links,priority
```

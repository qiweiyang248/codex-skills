# Universal PDP Image Rules

These rules apply to all ecommerce product detail image sets unless a category reference overrides or tightens them.

## Conversion Strategy

A PDP image set should follow shopper decision flow:

1. Recognize product instantly.
2. Feel desire or identity fit.
3. Understand the main buyer reason.
4. See the product in a believable scene.
5. Understand how it works or how it is used.
6. Trust material/detail/quality.
7. Understand scale, fit, compatibility, or placement.
8. Confirm specs, package contents, and final trust facts.

## Image-Level Rule

Every image must have exactly one dominant sales job. Secondary callouts are allowed only when they support the main job and do not reduce clarity.

## Buyer-Point Translation

Convert product facts into buyer reasons.

Examples:

- Feature: compact size → Buyer reason: fits on a crowded desk / travels easily / stores neatly
- Feature: metal body → Buyer reason: premium feel / durable daily use / gift-worthy finish
- Feature: transparent material → Buyer reason: see contents instantly / elegant display / easy refills
- Feature: adjustable strap → Buyer reason: fits more people / easier daily carry

## Layout Rules

Before generating or composing, define zones:

- Product zone
- Headline zone
- Supporting callout zone
- Icon/footer zone
- Negative space / breathing area

Keep text away from:

- Product logos and labels
- Mechanisms, seams, connectors, edges, texture, or close-up details
- Faces, hands, or functional gestures
- Transparent products where text may become illegible

Use consistent margins and type hierarchy across the set.

## Text Rules

- Prefer short, buyer-facing headlines.
- Avoid long paragraphs.
- Use 1 headline + 1 to 3 short callouts per image as a default maximum.
- Use exact specs only when provided.
- Avoid false urgency, fake awards, fake reviews, fake guarantees, fake certifications, or platform logos.
- Do not include claims that the product cannot support through evidence.

## Visual Quality Rules

- Product realism matters more than decorative complexity.
- Preserve product identity and proportions.
- Use believable materials, shadows, reflections, and lighting.
- Match scene props to category and price point.
- Avoid irrelevant props that imply extra included items.
- Do not make the product look like a different material, size, color, or variant.
- Keep the image set visually unified: repeated framing, typography, icon style, spacing, background logic, and color system.

## Independent-Site PDP Style

For independent websites, images can be more premium and brand-led than marketplace-only images.

Recommended style choices:

- Larger product hero moments
- More lifestyle scene depth
- More emotional/gifting/identity storytelling
- Cleaner typography and fewer cluttered badges
- Stronger art direction than supplier catalog images
- More credible real-use frames to reduce AI/render distrust

## Benchmark Adaptation

When benchmarks are provided:

Extract:

- Image order and shopper logic
- Product framing and crop ratios
- Background systems
- Typography and icon grammar
- Color palette and contrast level
- Scene realism level
- Callout density
- Proof types and spec layout

Do not blindly copy. Adapt the logic to the user's product, brand, evidence, and category.

## Claim Safety

A claim may be used only when it is:

1. Explicitly present in product data, spreadsheet, supplier note, certificate, spec sheet, manual, packaging, or brand file.
2. Directly visible in the product image.
3. Explicitly approved by the user in the current task.

When evidence is incomplete:

- Use softer visual-only wording.
- Move the claim to `missing_evidence`.
- Do not place it into image text.

## Conservative Replacement Examples

- Unsupported “waterproof” → “designed for daily use” or remove
- Unsupported “medical grade” → remove
- Unsupported “leakproof” → “secure cap design” only if visible
- Unsupported “premium material” → show close-up without naming material
- Unsupported “fits all” → “adjustable fit” only if visible or specified
- Unsupported “professional grade” → “clean, polished finish” only if visible

## Prompt Template

Use this image prompt structure inside `pdp_plan.md` or `pdp_prompts.md`:

```markdown
### Image XX — filename

- Buyer job:
- Headline:
- Visual scene:
- Product source image(s):
- Layout zones:
- Text overlay:
- Required evidence:
- Claim status:
- Category reference:
- Generation/editing prompt:
- Negative constraints:
```

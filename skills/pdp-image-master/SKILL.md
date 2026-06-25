---
name: pdp-image-master
description: Use for ecommerce PDP/product detail image planning, generation specs, image-set QA, and batch SKU image workflows for independent websites and marketplaces. Trigger on 详情图, 商品详情图, 电商详情图, 独立站详情图, PDP images, product listing images, SKU image sets, 主图, 卖点图, A+ style images, Shopify product images, conversion-focused product photos. Builds buyer-facing image sequences from product photos/evidence, chooses category rules from the image/product context, audits claims, preserves originals, and outputs reviewable files. Do not use for general graphic design unrelated to product sales pages.
---

# PDP Image Master

## Purpose

Use this skill to create, improve, critique, or QA ecommerce product detail image sets for independent websites and marketplace listings. The goal is to turn product photos and product evidence into a coherent, conversion-focused PDP image system: strong main image, buyer-benefit images, real-use scene images, function/detail proof, scale/fit proof, and specification/trust images.

This is a universal ecommerce PDP skill. Do not hard-code one product category. Determine the product category, shopper intent, scene style, and required proof from the product image, file/folder names, spreadsheet/product data, benchmark references, and user instructions.

## High-Priority Strategy Override

For premium independent-site PDPs, lifestyle products, men's gifts, cigar/barware/home-bar products, or any user request that asks for higher conversion, stronger brand taste, or non-Amazon creative direction, read and apply `references/pdp-image-strategy-v2.md` before planning or generating images.

This strategy override has priority over generic sequence, layout, and copy defaults. Evidence safety remains higher priority: do not invent materials, package contents, certifications, reviews, performance claims, warranty, stock, shipping, or other unsupported facts.

## When to Use

Use this skill when the task involves any of the following:

- 详情图, 商品详情图, 电商详情图, 独立站详情图, 主图, 卖点图, SKU 图组, 上架图
- PDP images, product detail page images, product listing images, A+ style images
- Turning raw product photos into conversion-focused image sets
- Planning or writing prompts for image generation/editing
- Auditing existing product image sets for claim safety, sequence, layout, or visual consistency
- Preparing batch workflows for many SKUs
- Creating product image manifests, contact sheets, QA reports, or claim audits

## When Not to Use

Do not use this skill for:

- General posters, logos, banners, or social graphics that are not product detail/listing images
- Pure copywriting without image planning or image QA
- Unsupported medical, safety, certification, legal, capacity, or performance claims
- Final batch generation before the first SKU/style direction is approved, unless the user explicitly approved full automation

## Codex Operating Modes

Before starting, choose one mode based on the user request. If the mode is obvious, proceed without asking.

### PLAN_ONLY

Use when the user wants a strategy, image sequence, prompts, or critique, but not actual image generation/editing.

Outputs:

- `pdp_manifest.json` when enough inputs exist
- `pdp_plan.md`
- optional `claims_audit.csv`

### PROMPT_ONLY

Use when the user only needs generation/editing prompts.

Outputs:

- `pdp_prompts.md`
- optional `pdp_manifest.json`

### GENERATE_SINGLE_SKU

Use when producing or editing a full image set for one SKU/product.

Outputs:

- `pdp_manifest.json`
- image files in an output folder
- `contact_sheet.jpg` if image files were created or reviewed
- `claims_audit.csv`
- `qa_report.md`

### BATCH_PREP

Use when preparing many SKUs before running generation.

Outputs:

- `pdp_manifest.json` or `batch_manifest.json`
- per-SKU plan folders or a batch plan
- claim/evidence readiness report
- first-SKU recommendation

### BATCH_RUN

Use only when the user explicitly approved batch automation or provided an approved first-SKU template.

Outputs:

- per-SKU output folders
- per-SKU manifests and QA reports
- batch summary report
- batch contact sheets when useful

### QA_ONLY

Use when auditing an existing image set.

Outputs:

- `qa_report.md`
- optional `claims_audit.csv`
- optional `contact_sheet.jpg`

## Required Input Handling

Collect what is available, then proceed conservatively. Do not block the task unless a missing field prevents safe execution.

Preferred inputs:

- Product image(s), folder, or SKU folder
- Product name and category if known
- Selling points, materials, dimensions, capacity, compatibility, package contents, variants
- Spreadsheet columns, supplier notes, certificates, spec sheets, product parameters, or user-provided proof files
- Target market language and platform requirements
- Benchmark images, style references, competitor PDP examples, or brand guidelines
- Desired output count, dimensions, and file format

Defaults when unspecified:

- Output count: 8 images per SKU
- Size: `1000x1000`
- Working format: PNG
- Upload-ready format: JPEG acceptable if requested
- Language: use the user's requested market language; if not specified, infer from channel/context and keep text concise
- Style: premium independent-site product visual system, adapted to category and benchmark references

Ask only when the missing input is blocking, such as target language, exact output size required by a platform, whether to run a full batch, or whether to use a risky unsupported claim.

## Required Workflow

### 1. Classify the product from evidence and images

Identify:

- Product type and likely category
- Visible features and materials
- Use scenario, user task, emotional role, and gifting/identity role
- Price positioning: budget, mid-market, premium, luxury, technical, playful, minimalist, etc.
- Required proof: safety, size, compatibility, material, capacity, before/after, fit, use steps, contents, certification, warranty, or care instructions

Always consult `references/category-routing.md` first. If the product matches a category reference, apply that reference after the universal rules. If no reference matches, use universal PDP logic and create a category-specific plan from the image/product evidence.

### 2. Analyze benchmarks before designing

When benchmark files or examples are provided:

- Extract reusable principles: sequence, visual hierarchy, typography, color system, image framing, callout style, proof logic, scene realism, and repeated section grammar
- Adapt the principles to the user's brand/category
- Do not copy proprietary claims, exact layouts, or competitor-specific styling
- When benchmark and evidence conflict, evidence wins

### 3. Build an evidence map before writing claims

For each claim that may appear in image text, create or update `claims_audit.csv`.

Claim types requiring evidence:

- Material, coating, finish, safety, food-contact, skin-contact, child/pet safety
- Capacity, dimensions, weight, compatibility, package contents
- Certification, standard, patent, compliance, warranty
- Performance, durability, speed, waterproofing, leakproofing, heat resistance, battery life
- Comparison or superiority claims such as “better than,” “#1,” “most durable,” “professional grade”
- Health, beauty, medical, or transformation claims

Evidence can be:

- Explicit spreadsheet/product data
- Supplier notes, certificates, spec sheets, manuals, packaging text, or brand files
- Directly visible product attributes in the product image
- User approval in the current task

If evidence is missing, keep the claim out of image text and place it in `missing_evidence`.

### 4. Translate sell points into buyer reasons

Do not start from “what the product has.” Start from:

- What customer job it solves
- What moment or scene it belongs in
- What discomfort, uncertainty, or objection it removes
- What identity, taste, gift value, or lifestyle it signals
- What comparison friction it reduces

Each image must have one dominant buyer-facing sales job.

### 5. Plan the complete image set before generation

For every planned image, define:

- Image number and filename
- Buyer job
- Headline or text overlay
- Visual scene and composition
- Layout zones: product zone, headline zone, info/callout zone, footer/icon zone
- Required evidence and claim status
- Category-specific proof requirement
- Prompt or editing instruction
- Negative constraints

### 6. Generate visual direction first

For a first SKU, new category, or premium independent-site PDP:

- Prioritize integrated visual quality, material realism, lighting, product desirability, and believable scenes
- Avoid script-only composition as the final output when the user expects premium product visuals
- Use deterministic scripts for contact sheets, file checks, claim audits, metadata, and packaging
- Build templates only after the visual direction is accepted

### 7. Preserve originals and write reviewable outputs

Never overwrite source images. Write generated or edited images to a clear output folder, ideally inside or next to the SKU folder.

Recommended folder:

```text
<sku-or-product-folder>/pdp_output/
  pdp_manifest.json
  pdp_plan.md
  claims_audit.csv
  01_main.png
  02_desire.png
  03_buyer_task.png
  04_real_use.png
  05_function.png
  06_detail_proof.png
  07_scale_fit.png
  08_specs_trust.png
  contact_sheet.jpg
  qa_report.md
  metadata/
    alt_text.csv
    pdp_copy.md
```

### 8. Verify before finalizing

Check:

- File count and naming
- Dimensions and format
- Source images preserved
- Text legibility and safe margins
- Product not covered by text
- One main sales job per image
- Style consistency across the set
- Claims supported by evidence or removed
- Category-specific proof is addressed
- Contact sheet exists when useful

Use scripts in `scripts/` when available.

## Required Output Contract

Create the following files unless the user requests otherwise or the mode does not require them.

### `pdp_manifest.json`

Treat this as the source of truth for SKU, inputs, outputs, claims, category routing, and approval state.

Minimum schema:

```json
{
  "project": "pdp-image-master",
  "mode": "PLAN_ONLY | PROMPT_ONLY | GENERATE_SINGLE_SKU | BATCH_PREP | BATCH_RUN | QA_ONLY",
  "sku": "",
  "product_name": "",
  "detected_category": "",
  "category_references_used": [],
  "target_market_language": "",
  "output_dir": "",
  "image_count": 8,
  "size": "1000x1000",
  "format": "png",
  "input_images": [],
  "evidence_sources": [],
  "benchmark_sources": [],
  "visual_direction_status": "draft | approved | rejected | qa_only",
  "batch_approval_status": "not_requested | first_sku_required | approved_full_batch",
  "claims": [],
  "missing_evidence": [],
  "outputs": []
}
```

### `pdp_plan.md`

Must include:

- Product/category summary
- Buyer persona and purchase motivation
- Visual direction
- Category-specific risks and proof requirements
- Image-by-image table
- Prompts or editing instructions
- Missing input/evidence notes

### `claims_audit.csv`

Columns:

```csv
image_no,claim,claim_type,evidence_source,evidence_value,status,replacement_safe_wording,notes
```

Allowed status values:

- `supported`
- `visible`
- `user_approved`
- `needs_confirmation`
- `unsupported_removed`
- `not_used`

### `qa_report.md`

Must include:

- Summary verdict: pass / needs fix / blocked by missing evidence
- File checks
- Layout checks
- Text/legibility checks
- Claim checks
- Category-specific checks
- Batch readiness, if relevant
- Prioritized fix list

## Universal PDP Image Sequence

Use 8 images by default. Adapt count and order when the platform, benchmark, or product requires it, but keep shopper decision flow intact.

### 1. Premium main image

Goal: immediate product recognition and click appeal.

- Product-first, clean, premium, low text or no text
- Show distinctive silhouette, material, set contents, or hero angle
- Avoid clutter that hides the product

### 2. Desire / identity / gift image

Goal: make the product emotionally desirable.

- Show who it is for and what owning/gifting it signals
- Use lifestyle, occasion, aspiration, or taste
- For non-gift categories, translate this into lifestyle fit or brand world

### 3. Buyer task / problem-solution image

Goal: convert feature into buying reason.

- One real customer job or pain point
- Headline should answer “why should I care?”
- Use category-specific scenario, not generic marketing copy

### 4. Real-use trust image

Goal: make the product feel physically real and trustworthy.

- Human interaction, natural environment, hand scale, surface texture, believable shadows/reflections, or authentic use context
- Premium realism, not messy or low-end UGC unless the brand specifically wants that

### 5. Function / how-it-works image

Goal: show how the product is used.

- Steps, motion, parts, before/after, fit, placement, operation, compatibility, or transformation
- Avoid claims that cannot be visually/evidentially supported

### 6. Material / detail / craftsmanship proof image

Goal: prove product quality.

- Close-up of material, finish, construction, texture, seam, edge, mechanism, ingredient texture, component, or craft detail
- Only use material, safety, certification, or durability claims when supported

### 7. Scale / fit / compatibility image

Goal: remove size/fit uncertainty.

- Show product relative to body, hand, room, desk, shelf, bag, device, pet, appliance, or standard scene object
- Use exact dimensions only when provided

### 8. Specification / package / trust close image

Goal: close remaining rational objections.

- Size, package contents, verified specs, variant choices, care instructions, compatibility, warranty, or what is included
- Keep it clean and structured
- Missing evidence should be omitted, not guessed

## Visual System Rules

- Make the product the hero in every image.
- Use a consistent art direction across all images in one SKU set.
- Maintain consistent typography, spacing, icon style, border radius, shadow style, and callout grammar.
- Use separate layout zones for product, headline, callouts, and footer.
- Text must not cover important product details, faces, hands, mechanisms, labels, or material textures.
- Keep text short. A shopper should understand the image in about 3 seconds.
- Prefer believable material rendering over over-polished AI/perfect-render aesthetics.
- Use scene context that matches the product category and price positioning.
- Avoid irrelevant props that change the perceived product category or imply unsupported package contents.
- Avoid fake badges, seals, certifications, star ratings, awards, or platform logos unless provided.

## Category Routing

Always read `references/category-routing.md` before applying category rules.

Available category references:

- `references/category-beverage-contact.md` — drinkware, barware, bottles, decanters, cups, beverage-contact products
- `references/category-apparel-accessories.md` — clothing, bags, wearable accessories, fit/style products
- `references/category-beauty-personal-care.md` — beauty tools, skincare devices, personal care, cosmetics packaging
- `references/category-electronics-appliances.md` — electronics, smart devices, small appliances, lighting, charging products
- `references/category-home-kitchen.md` — home, kitchen, storage, decor, furniture, organization products
- `references/category-jewelry-gifts.md` — jewelry, keepsakes, premium gifts, personalized items
- `references/category-tools-outdoor-pet.md` — tools, outdoor, auto accessories, sports, pet products

When a product fits multiple categories, apply the strictest claim/proof rules. Example: a heated pet bowl is both pet and electronics; apply both pet safety and electronics safety cautions.

## Batch Workflow Rules

For batch work:

1. Build or update `batch_manifest.json`.
2. Group SKUs by detected category, product type, image availability, and visual direction.
3. Choose one representative first SKU per group.
4. Create first-SKU outputs and contact sheet.
5. Do not continue to full batch unless the user explicitly approves the direction or has already approved full automation.
6. After approval, apply the same visual system while preserving SKU-specific evidence and image details.
7. Do not reuse unsupported claims across SKUs.
8. Generate per-SKU QA reports and a batch summary.

## Project Review and Skill Update Protocol

There is no automatic periodic review in this skill.

Run a project review only when:

- The user asks for a review
- A first-SKU direction is approved and the user asks to capture learning
- A major rejection/failure needs a retrospective
- The user asks to update the skill

Do not silently edit this skill. Propose the smallest useful rule first and wait for explicit user approval.

Project review template:

```markdown
## PDP Project Review

- Product/category:
- Inputs used:
- User-approved decisions:
- Rejected or revised decisions:
- Prompt or workflow changes that helped:
- Evidence-sensitive claims checked:
- Reusable principle candidates:
- One-off preferences that should not become global rules:
- Recommended skill update, if any:
```

Skill update proposal template:

```markdown
## Proposed Skill Update

- Proposed new rule:
- Evidence from project:
- Applicable scenarios:
- Impacted section/file:
- Why it improves conversion, trust, visual quality, or workflow reliability:
- Risk or possible conflict:
- Recommendation:
```

## Script Usage

Use scripts when files are available and the task requires deterministic checking.

Suggested commands:

```bash
python scripts/validate_pdp_outputs.py --manifest path/to/pdp_manifest.json
python scripts/audit_claims.py --claims path/to/claims_audit.csv
python scripts/make_contact_sheet.py --image-dir path/to/pdp_output --out path/to/pdp_output/contact_sheet.jpg
```

If scripts are unavailable, perform the same checks manually and state the limitation.

## Final Response Expectations

When completing a task, summarize:

- What was created or checked
- Output folder/files
- Category detected and references used
- Any unsupported or missing claims removed
- Approval needed before batch, if applicable
- Top fixes or next action

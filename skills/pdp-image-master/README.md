# PDP Image Master

Codex skill for ecommerce PDP and product-detail image planning, prompt creation, QA, and batch SKU image workflows.

## What It Does

- Plans conversion-focused product image sequences.
- Builds image generation or editing prompts from product evidence.
- Audits claims, layout, naming, dimensions, and PDP image consistency.
- Supports single-SKU and batch SKU workflows.
- Keeps unsupported material, certification, safety, performance, and package-content claims out of image text.

## Main Files

- `SKILL.md` - primary skill instructions.
- `references/` - category routing, category-specific rules, and premium PDP strategy.
- `scripts/` - deterministic QA helpers for claims, manifests, and contact sheets.
- `agents/openai.yaml` - agent configuration.

## Usage

Invoke explicitly in Codex:

```text
$pdp-image-master PLAN_ONLY: help me plan 8 independent-site PDP images for this SKU.
```

```text
$pdp-image-master QA_ONLY: audit this product image folder for claims, layout, dimensions, and naming.
```

See `README-install.md` and `README-storage-plan.md` for local installation and storage notes.


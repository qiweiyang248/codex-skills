# PDP Image Master Storage Notes

This skill belongs to **Layer 2: personal reusable skills**.

It should be stored as editable source here:

```text
~/codex-workspace/skills-src/pdp-image-master/
```

Codex should discover it through this user-level symlink:

```text
~/.agents/skills/pdp-image-master -> ~/codex-workspace/skills-src/pdp-image-master
```

This skill should **not** create a separate long-term Codex instruction layer. PDP tasks, SKU folders, and product-output folders are just working data, not durable Codex guidance.

Recommended explicit invocation:

```text
$pdp-image-master QA_ONLY：审一下这个 SKU 的详情图，不要生成新图。
```

```text
$pdp-image-master PLAN_ONLY：根据产品图、表格证据和 benchmark 做 8 张独立站详情图方案，先不要生成图片。
```

This package sets `allow_implicit_invocation: false`, so Codex will not auto-trigger this skill merely because a prompt mentions images or ecommerce. Explicit `$pdp-image-master` invocation still works.

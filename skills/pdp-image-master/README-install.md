# PDP Image Master — Install Notes

## Recommended locations

For a personal skill available in every Codex project:

```bash
mkdir -p ~/.agents/skills
cp -R pdp-image-master ~/.agents/skills/pdp-image-master
```

For one ecommerce repository only:

```bash
mkdir -p <repo-root>/.agents/skills
cp -R pdp-image-master <repo-root>/.agents/skills/pdp-image-master
```

Do not use `codx/skills/` unless it is just your own storage folder. Codex discovers local skills from `.agents/skills` or `$HOME/.agents/skills`.

## Usage examples

Explicit invocation:

```text
$pdp-image-master 帮我给这个 SKU 做 8 张独立站详情图，先做 plan 和 prompts，不要批量跑。
```

```text
$pdp-image-master QA 这个产品文件夹里的 PDP 图片，检查 claims、尺寸、命名、contact sheet。
```

```text
$pdp-image-master 读取这个表格和产品图，先做 BATCH_PREP，只生成第一个 SKU 的方案和联系表。
```

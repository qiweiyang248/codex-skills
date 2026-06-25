#!/usr/bin/env python3
"""Create a simple contact sheet for PDP image review."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a PDP contact sheet.")
    parser.add_argument("--image-dir", required=True, help="Directory containing PDP images")
    parser.add_argument("--out", required=True, help="Output contact sheet path, e.g. contact_sheet.jpg")
    parser.add_argument("--thumb", type=int, default=320, help="Thumbnail size in pixels")
    parser.add_argument("--cols", type=int, default=4, help="Number of columns")
    args = parser.parse_args()

    try:
        from PIL import Image, ImageDraw, ImageFont  # type: ignore
    except Exception:
        print("ERROR: Pillow is required. Install with `pip install pillow`.")
        return 1

    image_dir = Path(args.image_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()
    images = sorted([p for p in image_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS])

    images = [p for p in images if p.resolve() != out]
    if not images:
        print(f"ERROR: no images found in {image_dir}")
        return 1

    thumb = args.thumb
    label_h = 34
    pad = 16
    cols = max(1, args.cols)
    rows = math.ceil(len(images) / cols)
    sheet_w = cols * thumb + (cols + 1) * pad
    sheet_h = rows * (thumb + label_h) + (rows + 1) * pad

    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 14)
    except Exception:
        font = ImageFont.load_default()

    for idx, path in enumerate(images):
        row = idx // cols
        col = idx % cols
        x = pad + col * (thumb + pad)
        y = pad + row * (thumb + label_h + pad)

        with Image.open(path) as img:
            img = img.convert("RGB")
            img.thumbnail((thumb, thumb))
            bg = Image.new("RGB", (thumb, thumb), "white")
            px = (thumb - img.width) // 2
            py = (thumb - img.height) // 2
            bg.paste(img, (px, py))
            sheet.paste(bg, (x, y))

        label = path.name
        if len(label) > 42:
            label = label[:39] + "..."
        draw.text((x, y + thumb + 8), label, fill="black", font=font)

    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=92)
    print(f"PASS: wrote contact sheet to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

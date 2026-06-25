#!/usr/bin/env python3
"""Validate a PDP image output folder from pdp_manifest.json.

Checks:
- manifest exists and is valid JSON
- output_dir exists
- expected image count exists
- naming uses numeric prefixes
- dimensions match manifest.size when Pillow is installed
- source/input images are not listed as outputs
- contact sheet and QA report presence

This script is intentionally conservative. It does not judge visual quality; it catches
repeatable file/package mistakes that Codex can fix deterministically.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
PREFIX_RE = re.compile(r"^\d{2}[_-].+")


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: manifest not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def parse_size(value: str | None) -> tuple[int, int] | None:
    if not value:
        return None
    match = re.match(r"^(\d+)x(\d+)$", value.strip().lower())
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def list_images(output_dir: Path) -> list[Path]:
    return sorted(
        [p for p in output_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
    )


def check_dimensions(images: list[Path], expected_size: tuple[int, int] | None) -> list[str]:
    if expected_size is None:
        return ["WARN: manifest.size is missing or not in WIDTHxHEIGHT format; skipped dimension checks."]

    try:
        from PIL import Image  # type: ignore
    except Exception:
        return ["WARN: Pillow is not installed; skipped dimension checks. Install with `pip install pillow`."]

    messages: list[str] = []
    for path in images:
        try:
            with Image.open(path) as img:
                if img.size != expected_size:
                    messages.append(f"FAIL: {path.name} size {img.size[0]}x{img.size[1]} != expected {expected_size[0]}x{expected_size[1]}")
        except Exception as exc:
            messages.append(f"FAIL: could not open image {path.name}: {exc}")
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PDP output package.")
    parser.add_argument("--manifest", required=True, help="Path to pdp_manifest.json")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).expanduser().resolve()
    manifest = load_json(manifest_path)

    output_dir_value = manifest.get("output_dir") or manifest_path.parent
    output_dir = Path(output_dir_value)
    if not output_dir.is_absolute():
        output_dir = (manifest_path.parent / output_dir).resolve()

    messages: list[str] = []
    failures = 0
    warnings = 0

    if not output_dir.exists():
        print(f"FAIL: output_dir does not exist: {output_dir}")
        return 1

    images = list_images(output_dir)
    image_count = int(manifest.get("image_count") or 0)
    if image_count and len(images) != image_count:
        messages.append(f"FAIL: found {len(images)} image files, expected {image_count}")

    if not images:
        messages.append("FAIL: no image files found in output_dir")

    for image in images:
        if not PREFIX_RE.match(image.stem):
            messages.append(f"WARN: image file lacks ordered prefix: {image.name}")

    input_images = {Path(p).name for p in manifest.get("input_images", []) if isinstance(p, str)}
    overlap = [img.name for img in images if img.name in input_images]
    if overlap:
        messages.append("FAIL: output images appear to overwrite or duplicate source image names: " + ", ".join(overlap))

    expected_size = parse_size(str(manifest.get("size") or ""))
    messages.extend(check_dimensions(images, expected_size))

    if not (output_dir / "contact_sheet.jpg").exists() and not (output_dir / "contact_sheet.png").exists():
        messages.append("WARN: contact_sheet.jpg/png not found")

    if not (output_dir / "qa_report.md").exists():
        messages.append("WARN: qa_report.md not found")

    if not (output_dir / "claims_audit.csv").exists():
        messages.append("WARN: claims_audit.csv not found")

    for msg in messages:
        print(msg)
        if msg.startswith("FAIL"):
            failures += 1
        elif msg.startswith("WARN"):
            warnings += 1

    if failures == 0 and (warnings == 0 or not args.strict):
        print(f"PASS: validated {len(images)} image files in {output_dir}")
        return 0

    if failures == 0 and args.strict and warnings:
        print(f"FAIL: {warnings} warning(s) treated as failure due to --strict")
        return 1

    print(f"FAIL: {failures} failure(s), {warnings} warning(s)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

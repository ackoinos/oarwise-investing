"""
Process OWI logo PNGs for web use:
  1. Knock out the solid black background to transparency
  2. Auto-crop the transparent padding so the logo fills its canvas

The source logos are white line-art on an opaque black background inside a
square canvas. On a dark site the black block still shows as a box and the
excess padding makes the actual mark tiny. This fixes both.

Usage:
  python process-logos.py

Outputs (alongside sources in ../images):
  logo-horizontal-clear.png
  logo-square-clear.png
"""
import sys
from pathlib import Path
from PIL import Image

IMAGES = Path(__file__).resolve().parent.parent / "images"

# Pixels darker than this (max channel) become transparent.
# Below LOW: fully transparent. Above HIGH: solid white. Between: soft edge.
LOW_THRESHOLD = 24
HIGH_THRESHOLD = 120


def knock_out_black(img: Image.Image) -> Image.Image:
    """Recolor every kept pixel to pure white; use brightness only to derive a
    clean alpha ramp between LOW and HIGH so strokes stay solid and crisp."""
    img = img.convert("RGBA")
    px = img.getdata()
    out = []
    span = HIGH_THRESHOLD - LOW_THRESHOLD
    for r, g, b, a in px:
        v = max(r, g, b)
        if v <= LOW_THRESHOLD:
            out.append((255, 255, 255, 0))          # background -> transparent
        elif v >= HIGH_THRESHOLD:
            out.append((255, 255, 255, 255))         # stroke -> solid white
        else:
            alpha = int((v - LOW_THRESHOLD) / span * 255)  # anti-aliased edge
            out.append((255, 255, 255, alpha))
    img.putdata(out)
    return img


def autocrop(img: Image.Image, pad: int = 8) -> Image.Image:
    bbox = img.getbbox()  # bounding box of non-zero (non-transparent) region
    if not bbox:
        return img
    left, top, right, bottom = bbox
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(img.width, right + pad)
    bottom = min(img.height, bottom + pad)
    return img.crop((left, top, right, bottom))


def process(src_name: str, dst_name: str) -> None:
    src = IMAGES / src_name
    dst = IMAGES / dst_name
    if not src.exists():
        print(f"MISSING {src}", file=sys.stderr)
        return
    img = Image.open(src)
    before = img.size
    img = knock_out_black(img)
    img = autocrop(img)
    img.save(dst)
    print(f"OK  {src_name} {before} -> {dst_name} {img.size}")


if __name__ == "__main__":
    process("logo-horizontal.png", "logo-horizontal-clear.png")
    process("logo-square.png", "logo-square-clear.png")

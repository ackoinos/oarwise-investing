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


def knock_out_black(img: Image.Image, ink=(255, 255, 255)) -> Image.Image:
    """Recolor every kept pixel to `ink`; use brightness only to derive a
    clean alpha ramp between LOW and HIGH so strokes stay solid and crisp.
    Default ink is white (for the dark theme); pass ink=(0,0,0) for a dark
    line-art version suitable for a light background."""
    img = img.convert("RGBA")
    px = img.getdata()
    out = []
    span = HIGH_THRESHOLD - LOW_THRESHOLD
    for r, g, b, a in px:
        v = max(r, g, b)
        if v <= LOW_THRESHOLD:
            out.append((ink[0], ink[1], ink[2], 0))          # background -> transparent
        elif v >= HIGH_THRESHOLD:
            out.append((ink[0], ink[1], ink[2], 255))         # stroke -> solid ink
        else:
            alpha = int((v - LOW_THRESHOLD) / span * 255)     # anti-aliased edge
            out.append((ink[0], ink[1], ink[2], alpha))
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


def process(src_name: str, dst_name: str, ink=(255, 255, 255)) -> None:
    src = IMAGES / src_name
    dst = IMAGES / dst_name
    if not src.exists():
        print(f"MISSING {src}", file=sys.stderr)
        return
    img = Image.open(src)
    before = img.size
    img = knock_out_black(img, ink=ink)
    img = autocrop(img)
    img.save(dst)
    print(f"OK  {src_name} {before} -> {dst_name} {img.size} ink={ink}")


BLACK = (12, 12, 14)  # near-black ink for light theme (matches text color)

# Raw originals live in images/original/ as CDN hashes (untouched white-on-black).
# Generate DARK-INK transparent versions for the light theme from those raws.
LIGHT_JOBS = [
    ("original/66b3e7af31293577647b5d96.png", "logo-wide-dark.png"),        # horizontal lockup
    ("original/66b3e8d1f487dd6c84e886d4.png", "logo-stacked-dark.png"),     # stacked lockup
    ("original/670df1ac38ad6b39b9aeeeb6.png", "icon-mindset-dark.png"),
    ("original/670df2280d429d83b41b39c0.png", "icon-financial-dark.png"),
    ("original/670df692bd239006d0c1b75d.png", "icon-group-dark.png"),
    ("original/670deef1b23cb134cd5d67b1.png", "icon-certification-dark.png"),
]


if __name__ == "__main__":
    # dark-ink line-art for the light theme
    for src, dst in LIGHT_JOBS:
        process(src, dst, ink=BLACK)

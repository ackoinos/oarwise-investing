"""
Build a multi-size favicon.ico from the stacked OWI logo.

The white line-art is placed on the brand-black square so it stays visible
against light browser tab bars. Emits 16/32/48 sizes in one .ico.

Usage:  python make-favicon.py
Output: ../favicon.ico
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"


def main():
    logo = Image.open(IMAGES / "logo-stacked.png").convert("RGBA")

    # Square black canvas, logo centered with padding.
    side = max(logo.size) + 60
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 255))
    x = (side - logo.width) // 2
    y = (side - logo.height) // 2
    canvas.alpha_composite(logo, (x, y))

    out = ROOT / "favicon.ico"
    canvas.save(out, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"OK  wrote {out.name}  {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()

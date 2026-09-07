"""
Build a 1200x630 Open Graph social share card:
  hero water photo -> dark brand overlay -> centered white logo + tagline.

Usage:  python make-social-card.py
Output: ../images/social-card.jpg
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IMAGES = Path(__file__).resolve().parent.parent / "images"
W, H = 1200, 630
TAN = (198, 172, 143)


def load_font(size, bold=True):
    # Try common Windows fonts; fall back to PIL default.
    candidates = [
        r"C:\Windows\Fonts\poppins-semibold.ttf",
        r"C:\Windows\Fonts\segoeuisemibold.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def main():
    # 1. background: hero water, cover-cropped to 1200x630
    bg = Image.open(IMAGES / "hero-water.jpg").convert("RGB")
    scale = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * scale), int(bg.height * scale)), Image.LANCZOS)
    left = (bg.width - W) // 2
    top = (bg.height - H) // 2
    bg = bg.crop((left, top, left + W, top + H))

    # 2. dark overlay for legibility (vertical gradient, darker at bottom)
    overlay = Image.new("L", (1, H))
    for y in range(H):
        overlay.putpixel((0, y), int(150 + 70 * (y / H)))  # 150..220 alpha
    overlay = overlay.resize((W, H))
    dark = Image.new("RGB", (W, H), (0, 0, 0))
    bg = Image.composite(dark, bg, overlay)

    draw = ImageDraw.Draw(bg)

    # 3. logo (stacked, transparent white) centered upper area
    logo = Image.open(IMAGES / "logo-stacked.png").convert("RGBA")
    logo_h = 240
    logo_w = int(logo.width * (logo_h / logo.height))
    logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
    bg.paste(logo, ((W - logo_w) // 2, 70), logo)

    # 4. tagline
    tagline = "Empower Your Oars"
    sub = "Mindset Mastery  \u00b7  Financial Literacy Coaching"
    f_tag = load_font(58)
    f_sub = load_font(30)

    tw = draw.textlength(tagline, font=f_tag)
    draw.text(((W - tw) / 2, 360), tagline, font=f_tag, fill=(255, 255, 255))

    sw = draw.textlength(sub, font=f_sub)
    draw.text(((W - sw) / 2, 440), sub, font=f_sub, fill=TAN)

    # 5. thin accent line
    draw.line([(W / 2 - 120, 505), (W / 2 + 120, 505)], fill=TAN, width=2)

    out = IMAGES / "social-card.jpg"
    bg.save(out, quality=85)
    print(f"OK  wrote {out.name} ({bg.size})  {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()

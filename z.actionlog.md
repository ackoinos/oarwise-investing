# Oar Wise Investing - Action Log

# 2026-09-06 - User Request

> "yes, let's try a static rebuild. then get this into git"

**Actions Taken:**
- Created `projects/koinos/oarwise-investing/` project folder
- Built v1 static site: `index.html` (hero, about, 4 programs, approach, contact/CTA, footer) + `styles.css` (dark charcoal + tan + green theme, Poppins/Inter, responsive, mobile nav, scroll reveal)
- Added `z.readme.md`, `todo.md`, `.gitignore`
- Initialized git repo and made the first commit

---

# 2026-09-06 - User Request

> "what about the graphics?" / "yes, and go with option a"

**Actions Taken:**
- Pulled 8 real brand assets from the original HighLevel site (logo x2, Darren headshot, 4 program icons). Renamed CDN hashes to readable names in `images/`, kept raw originals in `images/original/`.
- Wired real graphics into `index.html`: nav + footer logo, Darren's photo in About, four matching program icons, favicon + OG social image (square logo).
- Shifted theme to true black (option A) in `styles.css` to match white-on-black brand assets; kept tan accent. Added logo/footer-logo/program-icon image styles.
- Verified all 6 image paths resolve, no leftover placeholders, HTML tags balanced. Updated readme + todo. Committed.

---

# 2026-09-06 - User Request

> "cosmetically, how can we improve this?"

**Actions Taken:**
- `styles.css` cosmetic polish pass (all CSS-only, no new image deps):
  - Fixed program-icon crop (cover -> contain + padding, bigger tile with subtle tan radial)
  - Hero depth: layered radial glows, faint animated "current" texture (::before, reduced-motion safe), tan/green water-line accent under hero (::after)
  - Buttons: tan gradient + soft glow on hover
  - About photo: offset tan accent frame (editorial)
  - Section rhythm: top hairline borders + faint corner glows on About/Programs/Approach so sections read as distinct panels
  - Eyebrow labels: leading tan tick + more letter-spacing
- Verified CSS brace/paren balance. Committed.

---

# 2026-09-06 - User Request

> "any way we can find a stock image for the whitewater?" / "let's try cand4"

**Actions Taken:**
- Sourced hero backdrop candidates from Unsplash (free commercial license, no attribution required). Downloaded 6, eyeballed each.
- Selected cand4: wooden rowboats moored at a mountain lake (Lago di Braies) - literal oar/rowboat tie-in to the brand.
- Pulled full-res (1920px, ~486KB) as `images/hero-water.jpg`, wired into hero via `.hero-bg` layer with dark brand-tinted overlay for legibility. Added text-shadow to hero h1/subtitle, brightened subtitle.
- Removed the now-redundant animated "current" texture (photo carries the visual now) + orphaned keyframe. Deleted reject candidates folder.
- Verified CSS balance, image paths, hero markup. Updated readme. Committed.

---

# 2026-09-06 - User Request

> "the logo on the top and bottom are unrecognizable"

**Actions Taken:**
- Diagnosed: logo PNGs had an opaque black background (A:255) and heavy padding inside a square canvas, so on the dark site they showed as a black box with a tiny squashed mark. Also found the two source files were mislabeled (the "horizontal" file was actually the stacked/vertical logo and vice versa).
- Wrote `scripts/process-logos.py` (Pillow): knocks out black to transparency, recolors kept pixels to pure white with a clean alpha ramp (first pass dimmed thin strokes; fixed via binary-ish knockout), auto-crops padding.
- Verified objectively: all solid pixels are pure white (11741/11741, 7634/7634), crisp edges, transparent bg.
- Produced `logo-wide.png` (437x135) + `logo-stacked.png` (249x396). Wired the wide transparent logo into nav + footer, adjusted logo height. Favicon/OG still use square original.
- Verified image paths + HTML. Updated readme. Committed.

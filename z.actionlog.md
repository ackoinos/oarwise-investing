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

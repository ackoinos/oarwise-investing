# Oar Wise Investing - Website

Static rebuild of oarwiseinvesting.com (originally a GoHighLevel funnel-builder page).

## Client
- **Owner:** Darren Cameron (church friend of Anthony)
- **Business:** Oar Wise Investing - "Empower Your Oars" one-on-one coaching (mindset mastery + financial literacy)
- **Contact:** info@oarwiseinvesting.com
- **Arrangement:** favor / pro bono rebuild (same as Harmony Myotherapy)

## The Site
- Single-page responsive static site (HTML/CSS, vanilla JS) - no build step
- Sections: Hero, About (Darren), Programs (4), Approach/Why It Works, Contact/CTA, Footer
- Fonts: Poppins (headlines) + Inter (body)
- Palette: deep charcoal (#14151a / #0f1014) + warm tan (#c6ac8f) + green accent (#4bb573), carried over from the original dark theme
- Mobile nav, scroll reveal animations, sticky header that shrinks on scroll

## Original Site (what we replaced)
- Built on GoHighLevel (HighLevel) funnel builder - leadconnectorhq.com CDN, msgsndr storage
- 245KB of machine-generated HTML + heavy JS runtime (phone-input libs, ecommerce/cart CSS, FontAwesome) for a simple landing page
- Locked into a monthly subscription; Darren does not own the code
- Content fully inventoried before rebuild (hero, bio, 4 programs, CTA, footer)

## Deployment Pipeline (local > UAT > prod)
Same pattern as harmony-myotherapy.

1. **Local (dev):** Edit files, preview by opening `index.html` in a browser. Zero cost.
2. **UAT (GitHub Pages):** Push to GitHub -> auto-deploys to a Pages URL. Free. Client review link for Darren.
   - Repo: https://github.com/ackoinos/oarwise-investing (public)
   - **Live UAT link (send to Darren): https://ackoinos.github.io/oarwise-investing/**
3. **Prod (Netlify):** Manual publish once approved, then point oarwiseinvesting.com at it.

## Graphics
Real brand assets were pulled from the original HighLevel site and reused (they are on-brand: white line-art on black with a signature water-ripple motif). Renamed from CDN hashes to readable names:
Darren has TWO official brand lockups (both pulled from his original site, both true to form - we did not re-orient or invent anything):
- **Horizontal lockup** (oars + "OWI" + ripples in a row) -> `images/logo-wide.png`. Used in nav + footer. Standard placement for a website header; this is what his own site used.
- **Stacked/vertical lockup** (oars over "OWI" over ripples) -> `images/logo-stacked.png`. Used for square/favicon contexts.

Using the horizontal lockup in the header and the stacked lockup as a square icon is normal brand practice and is NOT inconsistent with a vertically-formatted business card. **Open question for Darren:** confirm which lockup is his primary/canonical mark so we honour it. Never stretch either lockup - each is placed at its natural aspect ratio.

All logos and the four program icons were processed to transparency: the raw source files had an opaque black background baked in (which showed as black boxes on the dark site and, when stretched, squashed the mark). `scripts/process-logos.py` knocks the black out to transparency, recolors kept pixels to pure white, and autocrops padding so each mark sits cleanly at its own aspect ratio.

- `images/logo-wide.png` / `images/logo-stacked.png` - cleaned transparent lockups (in use)
- `images/icon-*.png` - cleaned transparent program icons (in use)
- `images/logo-horizontal.png` / `images/logo-square.png` - raw originals (opaque black bg) kept as source. logo-square still referenced for favicon/social (black bg is acceptable at favicon size)
- `scripts/process-logos.py` - reproducible cleanup (knockout + autocrop) via Pillow
- `images/darren.jpg` - Darren's headshot (whitewater backdrop), About section
- `images/icon-mindset.png` - Mindset Mastery program (head + lightbulb + gear)
- `images/icon-financial.png` - Financial Literacy program (person reading, $ signs)
- `images/icon-group.png` - Group Coaching program (group + lightbulb + gear)
- `images/icon-certification.png` - Certification program (certificate + ribbon)
- `images/original/` - untouched CDN-hash originals kept as source archive
- `images/hero-water.jpg` - hero backdrop: wooden rowboats moored at a mountain lake (Lago di Braies). Sourced from Unsplash (license: free for commercial use, no attribution required). Ties the "Empower Your Oars" theme to a literal oar/rowboat image. Sits behind a dark brand-tinted overlay for text legibility.

Theme shifted to true black (option A) to match the white-on-black brand assets, with tan (#c6ac8f) retained as the accent for buttons/headings and green (#4bb573) for small cues.

## Two theme versions
There are two versions of the site so the client can compare:
- **Dark** (default): `index.html` + `styles.css` -- true black, white line-art logo/icons.
- **Light**: `index-light.html` + `styles-light.css` -- warm cream/white with dark text, DARK line-art logo/icons (`*-dark.png`). The hero keeps the mountain-lake water photo (still dark with overlay) in both versions.
- Footers cross-link the two ("Light theme" / "Dark theme").
- Light-theme logo/icon assets are generated by `scripts/process-logos.py` from the raw originals with `ink=(12,12,14)`.
- The light page is `noindex` so it doesn't compete with prod in search. Pick a winner before go-live and make it `index.html`.
- **Bold/edgy**: `index-edgy.html` + `styles-edgy.css` -- dark ink-blue base, electric green->cyan gradient accent, oversized uppercase type, glowing CTAs, neon card edges. Modern-startup energy. Uses the white line-art assets (dark base). Also `noindex`.
- All three footers cross-link (Dark / Light / Bold).

## Outstanding / TODO
See `todo.md`. Key open items:
- Confirm the booking/CTA target (Calendly, or keep a HighLevel booking link if he uses the CRM side)
- Confirm whether Darren is tied into HighLevel's CRM before killing the subscription
- Real Terms & Conditions / Privacy Policy content (currently placeholder links)
- Optional: generate a proper multi-res favicon.ico from the square logo (done)
- Create GitHub repo and push (done -- live at https://ackoinos.github.io/oarwise-investing/)

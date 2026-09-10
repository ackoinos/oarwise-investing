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

---

# 2026-09-06 - User Request

> "we really should keep the logo true to form... if the other items like business cards are formatted vertically, it's going to create confusion... Also the logos for the other section look funny with the black and white logo against the background."

**Actions Taken:**
- Clarified brand handling: Darren has TWO official lockups (horizontal + stacked), both pulled from his own site. Using horizontal in nav and stacked for favicon is standard practice, not inconsistent with a vertical business card. Neither is stretched. Added a todo to confirm his PRIMARY lockup with him.
- Confirmed source filenames were swapped: logo-square.png = the horizontal lockup (437x135), logo-horizontal.png = the stacked lockup (249x396). Mapped by content, not filename.
- Extended `process-logos.py` to also process the 4 program icons. Gave all 4 icons the same black-knockout-to-transparency treatment so they float as white line-art on the cards instead of sitting in mismatched black tiles.
- Simplified `.program-icon` CSS: removed the dark tile background + border, icons now sit transparent on the card.
- Verified all 6 assets: pure-white solid pixels, 61-87% transparent backgrounds. Verified HTML paths + CSS balance. Updated readme + todo. Committed.

---

# 2026-09-06 - User Request

> "anything else we can do?" / "let's do 1-5"

**Actions Taken:**
- SEO/polish pass (items 1-5):
  1. Added JSON-LD ProfessionalService schema (founder Darren Cameron + Mindset/Financial offers) + robots, canonical, theme-color meta.
  2. Generated favicon.ico (16/32/48) from the stacked logo on brand-black (`scripts/make-favicon.py`).
  3. Created sitemap.xml + robots.txt.
  4. Generated 1200x630 social share card (hero water + stacked logo + "Empower Your Oars" + tan subtitle) via `scripts/make-social-card.py`; wired to og:image/twitter:image with width/height/alt.
  5. Added `scroll-margin-top: 88px` on section[id] so the sticky header no longer covers headings on anchor clicks.
- Verified: JSON-LD parses valid, all assets resolve, CSS + HTML balanced. Updated todo. Committed.

---

# 2026-09-06 - User Request

> "let's put it in git and generate a url for darren to access"

**Actions Taken:**
- Social card was already committed (b0d6f3f). Created public GitHub repo ackoinos/oarwise-investing and pushed main.
- Enabled GitHub Pages (main branch, root). Build succeeded.
- Verified live: page returns 200 with correct title; social-card.jpg, logo-wide.png, hero-water.jpg, styles.css, favicon.ico, sitemap.xml, robots.txt all serve 200.
- **UAT link for Darren: https://ackoinos.github.io/oarwise-investing/**
- Updated readme with repo + live URL.

---

# 2026-09-06 - User Request

> "when hitting the hamburger, this happens:" (mobile menu was semi-transparent, hero text bleeding through)

**Actions Taken:**
- Root cause: mobile dropdown background was rgba(15,16,20,0.98) sitting inside a translucent, backdrop-blurred header over true-black content, so hero text showed through.
- Fixed: dropdown now solid #000 with a drop shadow. Header goes fully opaque when menu open via `.menu-open` class (JS toggle) + `:has()` fallback.
- Verified CSS balance + JS consistency. Committed + pushed (UAT auto-updates).

---

# 2026-09-06 - User Request

> "hmmm... even the local copy still has this issue" (mobile menu still transparent after first fix)

**Actions Taken:**
- First fix (solid dropdown bg) didn't resolve it -> real root cause was `backdrop-filter: blur` + translucent rgba header background bleeding the hero through the dropdown region.
- Definitive fix: removed backdrop-filter entirely. Header is now transparent at top (over hero), solid #0a0a0c once scrolled. Menu-open forces solid #000 header (!important) regardless of scroll position, so the dropdown never shows bleed-through.
- Verified: zero backdrop-filter refs, no translucent header bg, CSS balanced. Committed + pushed.

---

# 2026-09-06 - User Request

> "wait! that didn't work. look at the menu, about ways to empower, schedule a call is on top of why it works" (+ keep frosted glass)

**Actions Taken:**
- Restored frosted glass on header (backdrop blur + translucent bg), but menu-open state now drops backdrop-filter to none + solid #000 so the mobile dropdown never bleeds.
- Fixed the real remaining bug: mobile menu items overlapping (Schedule a Call on top of Why It Works). Cause was `max-height: 380px` clip too tight + no gap, squeezing flex items. Fixed with max-height 70vh, gap 6px, `li { flex: 0 0 auto }`, `a { display: block }`.
- Verified CSS balance. Committed + pushed.

---

# 2026-09-06 - User Request

> "cynthia, my girlfriend, said she doesn't like the black. she likes the hero though... can we make another version?"

**Actions Taken:**
- Created a LIGHT theme variant so both can be compared: `index-light.html` + `styles-light.css` (warm cream/white, dark text, darker tan + deeper green accents). Hero kept as-is (mountain-lake water photo, dark with overlay).
- Extended `process-logos.py` with an `ink` param; generated dark line-art logo/icon variants from raw originals (`logo-wide-dark`, `logo-stacked-dark`, `icon-*-dark`) for use on light backgrounds. Fixed the wide/stacked filename swap.
- Nav shows white logo over the dark hero at top, swaps to dark logo once scrolled onto the light page (+ mobile-menu-open forces dark). Footer stays dark so keeps white logo.
- Footers cross-link the two themes. Light page set noindex so it doesn't compete with prod.
- Verified all dark-variant assets resolve, single robots tag, CSS balanced. Committed + pushed.

---

# 2026-09-06 - User Request

> "some of the buttons have a faint black border around it"

**Actions Taken:**
- Cause: base `.btn` has `border: 2px solid transparent`; on the gradient primary buttons the transparent border box let a faint hairline edge show (visible on light theme, latent on dark).
- Fix: `.btn-primary` now `border: none` with padding bumped +2px (16px 32px, lg 19px 42px) to preserve size. Applied to both styles.css and styles-light.css.
- Verified both CSS balance. Committed + pushed.

---

# 2026-09-06 - User Request

> "when i scroll, i can still see the black" (light theme)

**Actions Taken:**
- Defensive fix: changed light-theme `.hero` base background from #000 to cream (var(--bg-alt)) and set explicit `html { background: var(--bg) }` so no black flashes during scroll momentum/overscroll.
- Asked user to clarify whether they mean an overscroll flash vs the dark hero itself, since the fix differs.
- Verified CSS balance. (Commit pending clarification.)

---

# 2026-09-06 - User Request

> "can we produce a 3rd edgier version?"

**Actions Taken:**
- Built a 3rd "Bold/edgy" theme: `index-edgy.html` + `styles-edgy.css`. Dark ink-blue base (#06070d), electric green->cyan gradient accent (#17e6a0 / #2fd6ff), oversized uppercase type, gradient-clipped headline em, glowing gradient CTAs, sharper corners, neon top-border on program-card hover, gradient border ring on the About photo. Hero keeps the water photo with a more vivid colored wash.
- Uses the existing white line-art assets (dark base). noindex like the light preview.
- Cross-linked all three themes in every footer (Dark / Light / Bold).
- Verified edgy CSS balance, single robots tag, all assets resolve. Committed + pushed.

---

# 2026-09-06 - User Request

> "the hero background. you can see the mountains, but not the boats nor the oars at the bottom."

**Actions Taken:**
- The boats/oars (the oar-metaphor payoff) sit at the bottom of the photo but the crop favored the top and the overlay was heaviest at the bottom, burying them.
- Fixed across all three themes: background-position 30% -> 72% (pulls boats into frame while keeping peaks), and reworked the hero overlay to be lighter through the mid/lower band (was 55-72% black at bottom) so the boats read.
- Verified all three CSS balance. Committed + pushed.

---

# 2026-09-08 - User Request

> Darren replied: likes the dark version, gave booking link (corrected to https://oarwiseinvesting.com/schedule-call-6978-4164), on Mastermind.com platform paying monthly, undecided whether to stay.

**Actions Taken:**
- Verified the booking URL resolves (HTTP 200, title "Schedule Your Call With Darren Cameron").
- Wired it into the contact-section "Schedule a Call" button across all three themes (replacing the mailto placeholder). Nav/hero/program CTAs still scroll to #contact where the booking button lives (clean funnel). Email kept as secondary contact.
- Noted client decision (dark wins) + open question re: Mastermind.com usage in todo. Committed + pushed.

**Follow-up (same day):**
- Promoted dark as the sole public version: removed the Dark/Light/Bold cross-links from all three footers. Kept index-light + index-edgy (and their CSS) as reference/alternate files, still noindex, not linked.
- Drafted reply to Darren (`reply-to-darren.md`): dark confirmed, booking link wired, and the Mastermind question (just the site vs the business tools) to inform his stay/switch decision.
- Committed + pushed.

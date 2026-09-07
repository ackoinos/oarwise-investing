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
3. **Prod (Netlify):** Manual publish once approved, then point oarwiseinvesting.com at it.

## Graphics
Real brand assets were pulled from the original HighLevel site and reused (they are on-brand: white line-art on black with a signature water-ripple motif). Renamed from CDN hashes to readable names:
- `images/logo-horizontal.png` - nav + footer logo (crossed oars + "OWI" + ripples)
- `images/logo-square.png` - favicon + social share image
- `images/darren.jpg` - Darren's headshot (whitewater backdrop), About section
- `images/icon-mindset.png` - Mindset Mastery program (head + lightbulb + gear)
- `images/icon-financial.png` - Financial Literacy program (person reading, $ signs)
- `images/icon-group.png` - Group Coaching program (group + lightbulb + gear)
- `images/icon-certification.png` - Certification program (certificate + ribbon)
- `images/original/` - untouched CDN-hash originals kept as source archive
- `images/hero-water.jpg` - hero backdrop: wooden rowboats moored at a mountain lake (Lago di Braies). Sourced from Unsplash (license: free for commercial use, no attribution required). Ties the "Empower Your Oars" theme to a literal oar/rowboat image. Sits behind a dark brand-tinted overlay for text legibility.

Theme shifted to true black (option A) to match the white-on-black brand assets, with tan (#c6ac8f) retained as the accent for buttons/headings and green (#4bb573) for small cues.

## Outstanding / TODO
See `todo.md`. Key open items:
- Confirm the booking/CTA target (Calendly, or keep a HighLevel booking link if he uses the CRM side)
- Confirm whether Darren is tied into HighLevel's CRM before killing the subscription
- Real Terms & Conditions / Privacy Policy content (currently placeholder links)
- Optional: generate a proper multi-res favicon.ico from the square logo
- Create GitHub repo and push

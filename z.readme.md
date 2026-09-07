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

## Outstanding / TODO
See `todo.md`. Key open items:
- Get Darren's headshot for the About section (`images/darren.jpg`)
- Confirm the booking/CTA target (Calendly, or keep a HighLevel booking link if he uses the CRM side)
- Confirm whether Darren is tied into HighLevel's CRM before killing the subscription
- Real Terms & Conditions / Privacy Policy content (currently placeholder links)
- Favicon + apple-touch-icon
- Create GitHub repo and push

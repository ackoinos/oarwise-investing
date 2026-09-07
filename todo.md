# Oar Wise Investing - To Do

## In Progress
- [x] Assess original site (GoHighLevel funnel)
- [x] Build v1 static rebuild (index.html + styles.css)
- [x] Initialize git repo + first commit

## Content
- [x] Darren's headshot wired into About section (reused from original site)
- [x] Real brand logo + program icons wired in (reused from original site)
- [x] Favicon / apple-touch-icon set to square logo PNG
- [ ] Confirm program details / topic bullets are accurate
- [ ] Real Terms & Conditions page/content
- [ ] Real Privacy Policy page/content
- [ ] Optional: generate a proper multi-res favicon.ico from the square logo

## Functionality
- [ ] Wire "Schedule a Call" CTA to the real booking link (Calendly or HighLevel)
- [ ] Decide contact method: mailto (current) vs a proper form (Netlify Forms is free)

## SEO / Polish (done 2026-09-06)
- [x] JSON-LD structured data (ProfessionalService + founder + offers)
- [x] robots/canonical/theme-color meta
- [x] favicon.ico (16/32/48) from stacked logo
- [x] sitemap.xml + robots.txt
- [x] 1200x630 social share card (og:image)
- [x] scroll-margin-top so sticky header doesn't cover section headings

## Nice-to-have (needs Darren's input)
- [ ] Testimonials / social proof section (1-2 client quotes) - highest-converting element
- [ ] Confirm areaServed in JSON-LD (currently "CA" for Canada - adjust if wrong)

## Decisions
- [ ] Confirm with Darren whether he uses HighLevel for CRM/email/booking, or just the website
      (if just the website, static rebuild saves the monthly subscription)
- [ ] Confirm Darren's PRIMARY logo lockup (horizontal vs stacked) so the site matches his
      business cards / print materials. Currently: horizontal in nav/footer, stacked for favicon.

## Deploy
- [ ] Create GitHub repo (public, for free Pages)
- [ ] Push -> GitHub Pages UAT link for Darren to review
- [ ] Netlify prod deploy once approved
- [ ] Point oarwiseinvesting.com DNS at Netlify

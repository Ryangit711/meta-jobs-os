# SYSTEM SOURCES — QBIT 1 Sweep Registry

## Primary Job Boards (Sweep Every FETCH)
- **Indeed** — indeed.ca — general job board, broadest coverage
- **LinkedIn** — linkedin.com/jobs — professional network, company pages
- **Glassdoor** — glassdoor.ca — salary data + job listings
- **Workopolis** — workopolis.com — Canadian-focused
- **Jooble** — jooble.ca — aggregator, catches cross-posted roles
- **Google Jobs** — google.com/search?q=jobs — aggregator, surfaces roles from all boards
- **Hiring Cafe** — hiring.cafe — curated tech/startup roles

## Company Career Pages (Sweep Per Pipe)

### T PIPE (Tech/BigTech)
- Clio — clio.com/about/careers
- Shopify — shopify.com/careers
- Amazon — amazon.jobs
- 1Password — 1password.com/jobs
- Tailscale — tailscale.com/careers
- DoorDash — doordash.com/careers
- Indeed — indeed.com/careers
- Jobber — jobber.com/careers

### I PIPE (Internal Strategy/Corporate)
- lululemon — lululemon.com/careers
- TELUS — telus.com/careers
- Vancity — vancity.com/careers
- Methanex — methanex.com/careers
- Providence Healthcare — providencehealthcare.org/careers
- BC Cancer — bccancer.bc.ca/careers
- Aritzia — aritzia.com/careers
- Arc'teryx — arcteryx.com/careers

### C PIPE (Consulting)
- Deloitte — deloitte.com/careers
- EY — ey.com/careers
- KPMG — kpmg.com/careers
- PwC — pwc.com/careers
- Accenture — accenture.com/careers
- MBB (McKinsey, BCG, Bain) — respective career portals

### S PIPE (Startups)
- Procurify — procurify.com/careers
- Ada — ada.com/careers
- Hiive — hiive.com/careers
- EvenUp — evenup.com/careers
- Practice Better — practicebetter.com/careers
- Thinkific — thinkific.com/careers
- EviSmart — evismart.com/careers
- Brex — brex.com/careers

## Greenhouse Boards (Check All Each FETCH)
- Greenhouse common: Brex, Hootsuite, EviSmart, Thinkific, Practice Better
- Test new slugs each run: GitLab, Zapier, Notion, Canva, Stripe, HubSpot

## ATS Tech Spec Reference (JOBS-OS Vault)
- Per-platform ATS parsing rules: `32_ATS_TECH_SPEC.md` in JOBS-OS vault
  - Greenhouse: DOCX, Arial/Calibri, 10-12pt, 0.75-1in margins, single column, no headers
  - Workday: DOCX, Arial/Calibri/Times New Roman, 10-12pt, contact info in body (not header)
  - Lever: DOCX, Liberation Sans/Calibri, 10-11pt, 0.75in margins, simple section headers
  - ICIMS: DOCX preferred, standard fonts, single column, no tables
  - SAP SuccessFactors: DOCX, Calibri 10-11pt, generic section headers
- Cross-reference gen_docx.py CONFIG before generating any DOCX

## Apify Fallback
- When webfetch returns blank/truncated, use APIFY_FETCH.py

## Community Intel
- Reddit — r/vancouverjobs, r/cscareerquestions, r/consulting, r/startups
- X.com — finance/startup job posts

---

## Add/Remove Protocol
- **Add:** Append to relevant section above + update AGENTS.md QBIT 1 inline list
- **Remove:** Delete from relevant section + update AGENTS.md QBIT 1 inline list
- **Reason for change** must be logged in data/thought_log/

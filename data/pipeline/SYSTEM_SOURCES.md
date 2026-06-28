# SYSTEM SOURCES — QBIT 1 Sweep Registry

## Primary Job Boards (Sweep Every FETCH — 13 Total)
- **Indeed** — indeed.ca — general job board, broadest coverage
- **LinkedIn** — linkedin.com/jobs — professional network, company pages
- **Glassdoor** — glassdoor.ca — salary data + job listings
- **Workopolis** — workopolis.com — Canadian-focused
- **Jooble** — jooble.ca — aggregator, catches cross-posted roles
- **Google Jobs** — google.com/search?q=jobs — aggregator, surfaces roles from all boards
- **Hiring Cafe** — hiring.cafe — curated tech/startup roles
- **Eluta.ca** — eluta.ca — aggregates directly from company career pages (finds hidden roles)
- **SimplyHired** — simplyhired.ca — aggregator, different coverage from Indeed
- **Monster Canada** — monster.ca — legacy board, unique corporate listings
- **ZipRecruiter** — ziprecruiter.ca — aggregator, strong for US-in-Canada roles
- **Otta** — otta.com — curated tech/startup roles at scale-ups
- **BCjobs.ca** — bcjobs.ca — BC-specific corporate and local roles

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

## Dedup + ATS Feasibility + Route Guidance Protocol

### Phase 2b — Dedup (Same Job on Multiple Sources)
Every job found across multiple sources is collapsed into ONE entry. The FETCH table shows each job once. Dedup key: company name + role title + location must match (approximate fuzzy match — same company + same role level = same job even if title has minor variation).

### Phase 2c — ATS Feasibility Check
For each dedup'd job, identify company's ATS platform. Cross-reference against ATS Tech Spec section above:

| ATS | DOCX Pass? | Gotcha | Risk |
|-----|-----------|--------|------|
| **Greenhouse** | ✅ Yes | Liberation Sans/Calibri 10-11pt, 0.75in margins | Low |
| **Workday** | ✅ Yes (with care) | Contact info MUST be in body (not header). Arial/Calibri only | Medium — header content skipped |
| **Oracle Cloud** | ✅ Yes | Calibri 11pt, 0.75in margins, simple section headers | Low |
| **Lever** | ✅ Yes | Liberation Sans/Calibri 10-11pt, no tables | Low |
| **ICIMS** | ✅ Yes | Standard fonts, single column | Low |
| **SAP SuccessFactors** | ✅ Yes | Calibri 10-11pt, generic headers | Low |
| **Taleo** | ⚠️ Caution | Legacy — prefers DOCX, can mangle formatting | Medium — test before submit |
| **BambooHR** | ✅ Yes | Standard DOCX works | Low |
| **Unknown** | ⚠️ Verify | Use DOCX with generic format (Calibri 11pt, 0.75in, no headers) | Flag for manual check |

Flag: ✅ Pass / ⚠️ Verify (format spec check needed) / ❌ Blocked (with reason + fix)

### Phase 2d — Route Guidance
For each job, determine best application route. Priority:

1. **Company career page** (best — direct feed, no third-party filter)
2. **ATS direct portal** (Workday/Greenhouse/Oracle direct URLs — skip middleman)
3. **LinkedIn Easy Apply** (only if career page doesn't exist or is broken)
4. **Primary board** (Indeed/Google Jobs/SimplyHired — general, acceptable fallback)
5. **Third-party board** (Workopolis/ZipRecruiter — lowest priority)

**Rule:** If job found on career page AND on Indeed → recommend career page. If only on Indeed → recommend Indeed. If only on Otta/Hiring Cafe → that's a direct-source board, recommend that source.

Add column to FETCH table: **Apply Via** — one of "Company site", "ATS portal", "LinkedIn", "Indeed", "Otta", "Hiring Cafe", "[Board name]"

---

## Deep Scan Career Pages (Phase 4b — Top Targets)

Used during Deep Company Scan to scrape ALL open roles at a company, not just what job boards returned.

The key URLs below point to the career portal's **full listings page** (not a search filtered by keyword) so ALL roles are visible in one scrape.

### C PIPE (Consulting) — Deep Scan URLs
| Company | Career Portal URL | Notes |
|---------|------------------|-------|
| Deloitte | https://careers.deloitte.ca/search-jobs | Canada portal — search by business area |
| EY / EY-Parthenon | https://eyglobal.yello.co/jobs | Global Yello portal — filter by Canada |
| KPMG | https://careers.kpmg.ca/search-jobs | Canada portal |
| PwC | https://www.pwc.com/ca/en/careers.html | Canada career page |
| Accenture | https://www.accenture.com/ca-en/careers | Canada careers |
| McKinsey | https://www.mckinsey.com/careers/search-jobs | Global — filter by Canada |
| BCG | https://careers.bcg.com/search-jobs | Global — filter by Canada |
| Bain | https://www.bain.com/careers | Global portal |

### T PIPE (Tech/BigTech) — Deep Scan URLs
| Company | Career Portal URL | Notes |
|---------|------------------|-------|
| Clio | https://www.clio.com/about/careers/ | Lever portal |
| Shopify | https://www.shopify.com/careers | Greenhouse |
| Amazon | https://www.amazon.jobs/en-gb/search?base_query=&loc_query=Vancouver%2C+BC%2C+Canada | Filter to Vancouver |
| 1Password | https://1password.com/jobs | Greenhouse |
| Indeed | https://www.indeed.com/careers | Careers page |

### I PIPE (Internal Strategy/Corporate) — Deep Scan URLs
| Company | Career Portal URL | Notes |
|---------|------------------|-------|
| TELUS | https://careers.telus.com/search-jobs | Canada portal |
| lululemon | https://www.lululemon.com/careers | Workday |
| Aritzia | https://www.aritzia.com/en/careers.html | Careers page |
| Arc'teryx | https://www.arcteryx.com/ca/en/careers | Workday |

### S PIPE (Startups) — Deep Scan URLs
| Company | Career Portal URL | Notes |
|---------|------------------|-------|
| Procurify | https://procurify.com/careers/ | Lever |
| Ada | https://ada.com/careers/ | Lever |
| Hiive | https://hiive.com/careers | Lever |
| EvenUp | https://www.evenup.com/careers | Lever |

### Protocol
1. During Phase 4b (Deep Company Scan), open the career portal URL for each top target
2. Scrape all visible job listings (title, location, department)
3. Cross-check against the same filters as Phase 4
4. Add any new fitting roles to the company's CURATED entry
5. If the URL returns a filtered search by default, look for an "All Jobs" or "Browse All" link
6. If JS-rendered and webfetch can't parse → try Apify fallback; if both fail, skip gracefully

## Add/Remove Protocol
- **Add:** Append to relevant section above + update AGENTS.md QBIT 1 inline list
- **Remove:** Delete from relevant section + update AGENTS.md QBIT 1 inline list
- **Reason for change** must be logged in data/thought_log/

---
name: shoot-deployer
description: "Triggered by SHOOT [company], SHOOT [company] --all [roles], or paste JD. Before generation: reads data/learned/ for relevant lessons + data/pipeline/ for existing tracking. After generation: writes to data/pipeline/PIPELINE.md. After YES: transitions pipeline to ✅, auto-starts networking timer, generates DOCX. Full 16-section depth, cross-skill wired."
---

# SHOOT DEPLOYER — Full 16-Section Application Package

## Cross-Skill Wiring (Auto-Executed)

### Before Generation (Data Inputs)
```
Step A1: READ data/pipeline/PIPELINE.md
  → Check if this company/role already tracked
  → If already SHOT/SUBMITTED → warn user, ask if resubmit

Step A2: READ data/learned/ for relevant lessons
  → READ data/learned/pipes.md — find success/fail for this pipe
  → READ data/learned/[company].md if exists — company-specific lessons
  → READ data/learned/keywords.md — keywords that won/lost for similar roles
  → READ data/learned/skill_gaps.md — flagged gaps for this company/pipe
  → INJECT lessons into section generation (DNA, keywords, archetype)

Step A3: CALCULATE trust tier
  → Tier 1 (Trust): fit ≥85% AND familiar pipe AND salary listed AND past success in pipe
  → Tier 2 (Normal): fit 70-84% OR unfamiliar pipe OR no salary data
  → Tier 3 (Strategic): fit <70% OR new company type OR confusing JD
  → SHOW tier in output header
```

### After Generation (Data Outputs)
```
Step B1: WRITE to data/pipeline/PIPELINE.md
  → ADD row: [company] | [role] | [salary] | [pipe] | 🔵 SHOT | [today] | T+0 | "Awaiting approval"
  → If --all multi-role: add one row per role
  → If row already exists (resubmit): UPDATE status to 🔵

Step B2: WRITE to data/jobs.json if not exists (create with {})
  → Add to applied.exclusion list for this company (so FETCH skips it)

Step B3: DISPLAY output with pipeline row shown
```

### After User Says YES (Approval → Auto-Trigger Chain)
```
Step C1: TRANSITION pipeline row: 🔵 SHOT → ✅ SUBMITTED
  → WRITE to data/pipeline/PIPELINE.md: set stage = ✅, set T+0 = today

Step C2: GENERATE DOCX via document-engine
  → Convert LaTeX resume + cover letter to DOCX
  → Save to date folder

Step C3: AUTO-START networking timer
  → WRITE to data/networking_log.json: company, T+0 date, personas, message templates
  → Networking footer auto-shows cadence from this point

Step C4: Git commit + push

Step C5: SHOW next action: "AUTO-APPLY [company] | AUTO-APPLY --manual (phone)"
```

---

## Source Truth Anchors (JOBS-OS Primary)
- Unified format: `35_UNIFIED_SHOOT_FORMAT.md`
- Infiltration layer: `37_INFILTRATION_LAYER.md`
- ATS specs: `04_ATS_NUANCE_DB.md` + `32_ATS_TECH_SPEC.md`
- Corpus: `01_MASTER_CORPUS.md`
- Resume rules: Tailscale style (AGENTS.md rules section)
- Cover letter rules: AGENTS.md cover letter format section
- Networking: AGENTS.md networking section
- Consulting: `CONSULTING_OS.md`
- Positioning by Pipe: AGENTS.md — POSITIONING BY PIPE FRAMEWORK section
- Multi-Role Limit: AGENTS.md — Multi-Role Application Limit kernel rule
- Learned data: `data/learned/[company].md`, `data/learned/pipes.md`, `data/learned/keywords.md`
- Pipeline: `data/pipeline/PIPELINE.md`
- Jobs log: `data/jobs.json`

## Multi-Role Workflow (Same Company, Multiple Roles)

When applying to 2-3 roles at the same company (see Multi-Role Strategy section 4):

**Shared across all roles:**
- Section 2 (Company Scout) — covers ALL roles at the company
- Section 3 (Hiring Process Reveal) — one per company
- Section 4 (Multi-Role Strategy) — the strategy for THIS company specifically

**Per-role (generated for EACH role):**
- Section 1 (HEADER) — role-specific
- Section 5 (CORE Alignment) — per role
- Section 6 (DNA EXTRACTION) — per role (each JD uses different language)
- Section 7-8 (ATS, Device) — shared (same platform)
- Section 9-12 (Resume, Cover Letter) — independently customized per role
- Section 13 (LinkedIn) — shared personas, role-specific messages
- Section 14-16 (Interview, Checklist, Follow-Up) — per role

**Cover letter cross-reference:** Each cover letter must acknowledge the other application:
> "I've also applied to [other role] because my background bridges both [skill A] and [skill B]. Applying to both demonstrates my genuine interest in [company] and my conviction that I can add value across teams."

**Format:** `SHOOT [company] --all [role1, role2, role3]` generates a single master document with shared sections + per-role variants.

---

## The 16 Sections (Every Job, Every Time)

### 1. HEADER
Company, Role, Team, Salary (range + midpoint), Location, Fit Score, Pipe, Wave, NOC, TEER, Archetype, **Trust Tier**

**Pipe positioning pre-selected:** Run the decision tree from POSITIONING BY PIPE FRAMEWORK in AGENTS.md. Read company DNA → select pipe frame → blend if needed → choose archetype. All 16 sections flow from this selection.

**Archetype locked:** Once selected, this archetype (A/B/C) is enforced across ALL 16 sections. Resume, cover letter, interview script — same archetype. No drift.

### 2. COMPANY SCOUT (All Relevant Roles)
**Permanent constitutional section — kills fear by showing the full landscape.**
- Scout ALL roles at the target company relevant to Aman's profile
- Show in table: Role, Level, Salary, Status (live/stale/shot/below floor)
- Highlight Best 3 with 1-liner why
- Even roles below salary floor are listed (so Aman knows what exists)

### 3. HIRING PROCESS REVEAL (How This Company Hires)
**Permanent constitutional section — kills fear by knowing the script.**
- Stage-by-stage process: what happens, duration, who you meet
- Experienced-hire specific rules (what they skip vs campus recruits)
- Key tips per stage (case interview? behavioral? take-home?)
- Timeline: how long from apply to offer
- What NOT to worry about (psychometric tests? assessment centres?)
- General company hiring philosophy (meritocratic? pedigree-focused? culture-first?)

### 4. MULTI-ROLE STRATEGY + ESOTERIC KNOWLEDGE
**Permanent constitutional section — insider knowledge that only company insiders know. Turns "how many jobs to apply for" from guesswork into strategy.**
- **Count recommendation:** How many roles Aman should apply to at THIS company (1/2/3 ceiling-4). Sources: Scale.jobs says 2-3, Frontline Source says 3-4 over sustained period, CNBC 2026 says multiple apps = desperate unless coherent, Indeed says 1-2 months gap. Consensus: 2-3 optimal, 4 absolute ceiling. Never more.
- **Coherence rule:** Roles must be same level + related function (Sr Mgr Strategy + Sr Mgr M&A = coherent. Sr Mgr Strategy + Analyst = career confusion)
- **Cadence recommendation:** Space X (1 week? 2 weeks?). Don't fire same day. Stagger.
- **ATS insider knowledge:** Does this company's ATS flag multi-applicants positively (shows initiative) or negatively (spray-and-pray)? Does it notify the recruiter? Does it keep rejected candidates in a talent pool?
- **Back-door path:** What's the optimal route — referral, direct apply, recruiter reach-out? Does this company have a generalist pipeline for experienced hires?
- **Rejection cooldown:** 6 months same role, no wait for different role at same company
- **Transparency rule:** If asked in interview, be honest about other applications — frame as genuine interest in the company
- **Cover letter cross-reference (if multi-role):** Each cover letter acknowledges the other application(s).

### 5. CORE Alignment Matrix
One-liner + Table: `JD Requirement → Aman's Map` (what they need → what he's done)

### 6. DNA EXTRACTION
- Company background + market position
- Language Registry (exact words they use — these go into resume at 2-4% density)
- Value System (what they reward)
- Cultural Cues (how they communicate)
- Anti-Patterns (what they hate — never include these)
- **Learned lessons from data/learned/ injected here** (keywords that worked/failed for similar companies)

### 7. ATS SPECS
- Platform (Greenhouse/Workday/Lever/Ashby/etc.)
- Font, Size, Format, Margins, Section Headers, Special Rules
- DOCX per spec, 100% parseable

### 8. DEVICE MAP
- Hardware they issue, OS, peripherals, IT policy, Day 1 prep

### 9. RESUME TEXT (Plain)
- Tailscale style: Name+contact centered, Professional Summary (3-4 sentences), Core Competencies (pipe-separated), Experience (Company — Title | Location, metrics bullets), Education, Technical Proficiency
- LOCAL CANADIAN IN BC framing — no immigration language
- Archetype enforced: resume text matches chosen archetype (A: builder verbs, B: operator verbs, C: strategist verbs)
- In code fence for proofreading

### 10. RESUME LATEX (.tex source)
- Full LaTeX source with proper formatting
- `\textbf{Company} \hfill \textbf{Title}` pattern
- `\begin{itemize}` for bullets
- Liberation Sans 10pt

### 11. COVER LETTER TEXT (Plain)
- 6-paragraph narrative mirroring company DNA
- Archetype enforced: same archetype as resume
- If multi-role: includes cross-reference to the other role(s) applied
- Header: `[NAME]` / Date: DD/MM/YYYY / Vancouver, BC, Canada
- Closing: Best regards, `[NAME]` / Phone: `[PHONE]` / Email: `[EMAIL]` / LinkedIn: `[LINKEDIN]`
- In code fence for proofreading

### 12. COVER LETTER LATEX (.tex source)
- Full LaTeX with mailto + https hyperlinks

### 13. LINKEDIN OUTREACH (4-Tier)
- T+0: Connect + note to IC/Associate
- T+3: Follow-up to Manager/Director
- T+7: Value-add to Sr IC/Manager
- T+14: Final nudge to Exec Sponsor
- Each with full message text + persona rationale

### 14. INTERVIEW CHEAT SHEET
- 60-sec pitch (archetype-locked)
- 5 Q&A with specific answers (not generic)
- 3 STAR stories (Profitability, Credibility, Visibility pillars)
- Keywords to use, anti-patterns to avoid
- "One year from now" question
- Rejection response script

### 15. CHECKLIST (18+ Items)
- DNA extracted? ATS keywords at 2-4%? Title aligned? No immigration language? DOCX ready? etc.
- Company scout completed? Hiring process revealed? Provenance verified? Multi-role strategy defined?
- data/learned/ read? Archetype locked across all sections?
- Pipeline updated? Trust tier assigned?

### 16. FOLLOW-UP + FINOPS
- T+0 through T+28 cadence with conditional triggers
- FinOps: negotiation targets, walk-away floor, benefits leverage

## Execution Protocol (Concrete Steps)

### On SHOOT Trigger
```
 1. READ data/pipeline/PIPELINE.md → check for existing entries
 2. READ data/learned/pipes.md + data/learned/[company].md + data/learned/keywords.md
 3. RUN LinkedIn Profile Audit → check alignment with target company/role
 4. CALCULATE trust tier
 5. RUN Semantic Layer (10 questions)
 6. GENERATE 16 sections (with learned lessons injected)
 7. RUN provenance auto-verify (cross-ref every claim with Master Corpus)
 8. SHOW full 16-section in chat (with trust tier + provenance pass/fail)
 9. SHOW LinkedIn Audit output (aligned/misaligned items)
10. WRITE row to data/pipeline/PIPELINE.md (🔵 SHOT)
11. WRITE to data/jobs.json (company added to exclusion)
```

### On YES (Approval) — Auto-Trigger Chain
```
1. TRANSITION data/pipeline/PIPELINE.md: 🔵 → ✅, set T+0 = today
2. GENERATE DOCX via document-engine
3. WRITE to data/networking_log.json: auto-start cadence (T+0/3/7/14)
4. Git commit + push
5. DISPLAY: "Ready for AUTO-APPLY. | Phone mode: AUTO-APPLY --manual"
```

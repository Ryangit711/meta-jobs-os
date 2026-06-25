---
name: resume-writer
description: "Triggered when generating section 6-7 of a SHOOT package, or by ALCHEMIZE command. Produces ATS-optimized resumes in Tailscale reference style. Always generates both plain text (for proofreading) and LaTeX source (for DOCX generation). Pure ATS mastery — no job-listing metadata in document body."
---

# RESUME WRITER — ATS-Tailored Resume Generator

## Source Truth Anchors
- Tailscale reference style (AGENTS.md hard rules, JOBS-OS)
- ATS specs: `04_ATS_NUANCE_DB.md` + `32_ATS_TECH_SPEC.md` (JOBS-OS)
- Truth anchor: `01_MASTER_CORPUS.md` (JOBS-OS)
- Infiltration: `37_INFILTRATION_LAYER.md` (JOBS-OS)

## Style Rules (Tailscale Reference — Mandatory)

### Structure (Exactly This Order)
1. **Name + Contact** — Centered. Name, phone, email, LinkedIn, location
2. **Professional Summary** — 3-4 sentences. Narrative, not keyword-stuffed. Company-agnostic tone with company-specific keywords woven in.
3. **Core Competencies** — Pipe-separated keywords. 10-15 terms from Language Registry.
4. **Professional Experience** — Reverse chronological. Format: `Company — Title | Location` / Date range. Clean 1-line bullets with metrics. No sub-headings within experience.
5. **Education** — Degree, institution, year. Skip GPA.
6. **Technical Proficiency** — Pipe-separated tools and platforms.

### Formatting
- 1 page max (except senior consulting roles — 2 pages acceptable)
- Liberation Sans 10pt
- Clean, single-column
- No tables, graphics, icons (ATS cannot parse them)
- No PR/work permit/immigration language
- No `**Target:**` / `**Company:**` / `**Max:**` fluff lines
- Pure resume — not a job-listing metadata document

### Alchemy Rules
- Every bullet starts with a strong verb from Language Registry
- Metrics on every bullet (real metrics from Master Corpus)
- Masquerade: use THEIR vocabulary for YOUR achievements
- ATS keywords at 2-4% density (count tokens / total words)
- Pass the HUMAN test: read aloud. Does it sound like a person wrote it? If too perfect, add imperfection.
- NO-LIE check: every claim must be in Master Corpus

## Output
### 1. Plain Text (code fence)
### 2. LaTeX Source (code fence)
- With `\textbf{Company} \hfill \textbf{Title}`
- `\begin{itemize}` for bullets
- Proper hyperlinks for email and LinkedIn
- Can be compiled directly

## ATS Compliance Check (Silent, Auto-Run)
1. Length check: ≤1 page (≤2 for senior consulting)
2. Placeholder check: `[NAME]`/`[PHONE]`/`[EMAIL]`/`[LINKEDIN]` exist
3. NO-LIE check: every claim cross-referenced against Master Corpus
4. PR check: NO immigration language anywhere
5. ATS format check: per company's ATS platform rules
6. If any red flag → fix before display

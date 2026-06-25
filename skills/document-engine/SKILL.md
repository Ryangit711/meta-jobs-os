---
name: document-engine
description: "Triggered whenever document generation is needed — after proofreading approval in SHOOT, or when user requests DOCX/PDF/XLSX output. Uses professional-grade document creation pipelines with validation, schema compliance, and format-specific rules."
---

# DOCUMENT ENGINE — Professional Document Generation

## Source Truth Anchors
- Office file patterns: anthropics/skills (docx, pdf, xlsx skills)
- JOBS-OS: `39_FILE_GENERATOR.py`, `DOCX_GENERATOR.py`, `LOCAL_GENERATOR.py`

## DOCX Generation (Primary — for All Applications)

### Pipeline
1. Take approved LaTeX source (from SHOOT sections 7 and 9)
2. Strip LaTeX markup → plain content
3. Insert real identity from local_config.json
4. Generate .docx via docx-js (Node.js) or python-docx
5. Validate against schema (ISO/IEC 29500)
6. Verify hyperlinks (mailto:, https://) are clickable
7. Verify fonts, margins, section headers match ATS spec

### Scripts
```
scripts/office/unpack.py     — Unpack .docx to raw XML
scripts/office/pack.py       — Repack XML to .docx
scripts/office/validate.py   — Validate against OOXML schema
scripts/office/soffice.py    — LibreOffice headless wrapper
scripts/accept_changes.py    — Accept tracked changes in .docx
```

### ATS Compliance (Auto-Check)
- Font matches company ATS spec (Liberation Sans / Arial / Times New Roman)
- Margins per spec
- Section headers properly tagged
- Single-column, no tables/graphics/icons
- <500KB, selectable text
- No headers/footers content

## PDF Generation (Secondary — for Job Guides, Cheat Sheets, Reference)
- Reserved for: CALLBACK_READY DNA sheets, job guides, reference documents
- NOT for resumes or cover letters (unless ATS explicitly requires PDF, then DOCX + PDF both)
- Use reportlab or pandoc + wkhtmltopdf

## XLSX Generation (For Compensation Trackers, Analytics)
- Use openpyxl for formulas + formatting
- pandas for data analysis
- Mandatory formula recalculation via scripts/recalc.py (LibreOffice-based)
- Zero formula error requirement (no #REF!, #DIV/0!, #VALUE!, #N/A!, #NAME?)
- Financial modeling conventions: blue=inputs, black=formulas, green=cross-sheet refs

## Naming Convention
```
resumes/[Company]_Resume_[NAME].docx
cover_letters/[Company]_Cover_Letter_[NAME].docx
CALLBACK_READY/[Company]_DNA.md
```

## Output Locations
- Linux work dir: `APPLICATION_PACKAGES/[Company]/`
- OneDrive mirror: `/mnt/c/Users/owner/OneDrive/JOBS-OS-2026/APPLICATION_PACKAGES/[Company]/`
- All .docx gitignored (never pushed to GitHub)

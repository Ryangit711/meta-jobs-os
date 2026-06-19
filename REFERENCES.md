# REFERENCES.md — Skill-to-Source Mapping

Every skill in this system derives its content rules, alchemy, and depth from the original JOBS-OS repo. Nothing is invented here — only re-packaged into modular skills.

| Skill | JOBS-OS Source | anthropics/skills Pattern |
|-------|----------------|---------------------------|
| `fetch-engine` | `33_FETCH_ENGINE.py`, FETCH 8-PHASE PROTOCOL (AGENTS.md) | — |
| `shoot-deployer` | `35_UNIFIED_SHOOT_FORMAT.md`, 13-section format (AGENTS.md) | — |
| `dna-extraction` | `37_INFILTRATION_LAYER.md`, `03_AGNOSTIC_FRAMING.md` | — |
| `resume-writer` | Tailscale style rules, `04_ATS_NUANCE_DB.md`, `32_ATS_TECH_SPEC.md`, `01_MASTER_CORPUS.md` | — |
| `cover-letter-writer` | `37_INFILTRATION_LAYER.md`, `12_COVER_LETTERS.md` | — |
| `interview-prep` | `05_INTERVIEW_ALCHEMY.md`, CALLBACK_READY protocol | — |
| `networking-cadence` | Networking section (AGENTS.md), Constitutional Amendment #11 | — |
| `salary-negotiation` | `06_NEGOTIATION_PLAYBOOK.md`, `16_COMPENSATION_DB.md` | — |
| `rejection-handler` | `10_REJECTION_RECOVERY.md`, Amendment #20 (A-L) | — |
| `thought-log` | Constitutional Amendment #23 (AGENTS.md) | — |
| `social-distill` | `40_SOCIAL_DISTILL.md`, `INSTAGRAM_DISTILL.py`, `REDDIT_DISTILL.py`, `LINKEDIN_DISTILL.py` | — |
| `contact-engine` | `CONTACT_ENGINE.py`, Constitutional Amendment #18 | — |
| `document-engine` | `39_FILE_GENERATOR.py`, `DOCX_GENERATOR.py`, `LOCAL_GENERATOR.py` | `docx`, `pdf`, `xlsx` skills |
| `system-health` | DIAGNOSE PROTOCOL, REFRESH 6-PHASE PROTOCOL (AGENTS.md) | — |
| `skill-creator` | — | `skill-creator` skill |
| `eval/` infrastructure | — | `skill-creator/agents/`, `eval-viewer/` |
| `scripts/` utilities | — | `docx/scripts/`, `xlsx/scripts/` |

## The Deal

**Nothing from JOBS-OS is overwritten or simplified.** Every skill preserves:
- The DNA extraction depth
- The 13-section completeness
- The ATS compliance rigour
- The networking cadence automation
- The interview alchemy
- The salary negotiation strategy
- The NO-LIE truth anchor
- The privacy protocol
- The dual-write discipline

**What skills ADD that JOBS-OS doesn't have:**
- Modular loading (less context waste, faster responses)
- Quantitative eval suite (prove improvements, detect regressions)
- Test harness (A/B test every change before deploying)
- Professional document pipeline (validate, verify, render)
- Shared office utility scripts
- Abstracted patterns (MCP tools, theme consistency, skill creation)
- Portable skill registry (register in any AI tool)

## File Structure Comparison

### JOBS-OS (Original — Untouched)
```
JOBS-OS-2026/
├── AGENTS.md            ← 2000+ lines, holds EVERYTHING
├── 01_MASTER_CORPUS.md  ← Truth anchor
├── 02-32_*.md           ← 30+ numbered modules
├── 33-40_*.py           ← Python scripts
└── data/                ← Persistent data
```

### META-JOBS-OS (Modular Evolution)
```
meta-jobs-os/
├── AGENTS.md            ← ~300 lines, just kernel + skill loader
├── skills/              ← 15 load-on-demand specialists
├── eval/                ← Quantitative test infrastructure
├── template/            ← Skill creation scaffold
├── spec/                ← Agent Skills spec reference
├── scripts/             ← Shared document utilities
└── REFERENCES.md        ← This file — maps everything to source
```

### To regenerate the full system from source:
1. `git clone git@github.com:Ryangit711/JOBS-OS-2026.git` (truth anchor)
2. `git clone git@github.com:Ryangit711/meta-jobs-os.git` (modular evolution)
3. symlink or copy JOBS-OS content into meta-jobs-os `reference/` directory
4. Run `python3 LOCAL_GENERATOR.py` to generate real-name files
5. Start work via `AGENTS.md` bootstrap kernel

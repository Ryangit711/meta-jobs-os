# ABHIMANYU 2.0: The Modular Evolution

## What This Is

This is the **skill-architecture upgrade** of the original JOBS-OS system.

The original JOBS-OS is a monolithic operating system for job search — one AGENTS.md kernel, 40+ numbered modules, 15+ Python scripts. It works. It's powerful. But its power is locked inside a single massive prompt that an AI must load entirely for any single command.

**ABHIMANYU 2.0 preserves every bit of that alchemy** — the DNA extraction, the 13-section format, the infiltration layer, the networking cadence, the interview scripts. Nothing is simplified. Nothing is flattened. The depth is untouched.

What changes is the **container**: from monolith to modular skill architecture.

## Architecture

```
ABHIMANYU-2.0/
├── AGENTS.md              ← Bootstrap kernel (~300 lines, not 2000+)
│                              Loads only the skill needed for current command
│
├── skills/                ← Self-contained, load-on-demand specialists
│   ├── fetch-engine/         ← 8-phase pipeline (triggers on "FETCH")
│   ├── shoot-deployer/       ← 13-section package (triggers on "SHOOT")
│   ├── dna-extraction/       ← Company DNA analysis
│   ├── resume-writer/        ← ATS-optimized Tailscale-style resumes
│   ├── cover-letter-writer/  ← DNA-alchemized cover letters
│   ├── interview-prep/       ← Callback-ready cheat sheets
│   ├── networking-cadence/   ← Multi-touch outreach tracker
│   ├── salary-negotiation/   ← Offer analysis + negotiation
│   ├── rejection-handler/    ← Rejection → opportunity protocol
│   ├── contact-engine/       ← Contact + multi-channel cadence
│   ├── social-distill/       ← Instagram/Reddit/LinkedIn intel
│   ├── document-engine/      ← DOCX/PDF generation pipeline
│   ├── system-health/        ← DIAGNOSE, REFRESH, STATUS
│   └── skill-creator/        ← Meta-skill: create/improve skills
│
├── eval/                  ← Quantitative test infrastructure
│   ├── suite/                ← Test prompts + assertions per skill
│   ├── agents/               ← Grader, comparator, analyzer
│   └── viewer/               ← HTML review page
│
├── template/SKILL.md      ← Scaffold for creating new skills
├── spec/                  ← Agent Skills specification
├── scripts/               ← Shared file utilities
├── REFERENCES.md          ← Every skill → original JOBS-OS source
└── OMNI_SYNC.sh           ← Propagate to all AI tool configs
```

## The Core Upgrade: Skill-as-Plugin

Each `skill/` folder contains a `SKILL.md` with YAML frontmatter:

```yaml
---
name: resume-writer
description: "Triggered when user says SHOOT, ALCHEMIZE, or 'write a resume'..."
---
```

The AI loads **only** the skill(s) relevant to the current command. Not the entire system. This means:
- **More context free** for the actual alchemy work
- **Faster responses** (less irrelevant text in context)
- **Testable** — each skill has an eval suite with quantitative assertions
- **Swappable** — improve one skill without touching others
- **Portable** — skills can be registered in any AI tool that supports them

## What Comes From Where

| Component | Source |
|-----------|--------|
| All content/alchemy/format rules | `github.com/Ryangit711/JOBS-OS-2026` |
| Skill architecture pattern | `github.com/anthropics/skills` |
| Eval + benchmarking infra | `github.com/anthropics/skills` (skill-creator) |
| Document engine (DOCX/PDF/XLSX) | `github.com/anthropics/skills` (docx/pdf/xlsx skills) |
| MCP tool patterns | `github.com/anthropics/skills` (mcp-builder) |
| Theme/design consistency | `github.com/anthropics/skills` (theme-factory) |

## The Deal

- The original JOBS-OS repo is **untouched**. It's the permanent truth anchor.
- **ABHIMANYU 2.0** is the **evolution layer** — a modular skill system wrapped around that truth.
- Every skill references its JOBS-OS source files explicitly (see `REFERENCES.md`).
- Skills can be developed, tested, and improved independently.
- The endgame is identical: payroll → paycheck → PR → freedom.

## Quick Start

```bash
git clone git@github.com:Ryangit711/ABHIMANYU-2.0.git
# Read AGENTS.md to begin
# Skills load dynamically as you issue commands
```

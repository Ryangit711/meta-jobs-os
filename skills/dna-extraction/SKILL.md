---
name: dna-extraction
description: "Triggered by ATOMIZE, SCORE, or as embedded step in SHOOT. Analyzes a company's DNA from their JD, website, and public materials. Extracts Language Registry, Value System, Cultural Cues, and Anti-Patterns. Also handles archetype selection and fit scoring."
---

# DNA EXTRACTION — Company Alchemy Engine

## Source Truth Anchors
- Infiltration layer: `37_INFILTRATION_LAYER.md` (JOBS-OS)
- Agnostic framing: `03_AGNOSTIC_FRAMING.md` (JOBS-OS)
- Master Corpus: `01_MASTER_CORPUS.md` (JOBS-OS)
- Consulting OS: `CONSULTING_OS.md` (JOBS-OS)
- Three perception modes: Authentic / Hybrid / Machiavellian (JOBS-OS kernel)

## Extraction Protocol

### Step 1: Company Research
- Read JD thoroughly (if pasted) — extract nouns, verbs, adjectives
- Fetch company website, about page, careers page
- Identify industry, size, stage, funding, culture signals

### Step 2: Language Registry
List the exact words and phrases the company uses in their JD and materials:
- Expected: [terms they use]
- Avoided: [terms they'd reject]
- These words MUST appear in resume at 2-4% density

### Step 3: Value System
What does this company reward?
- Check their stated values vs demonstrated values (Glassdoor, reviews)
- Map to Aman's real capabilities

### Step 4: Cultural Cues
- Communication style: formal/casual/direct/consultative
- Decision-making: top-down/consensus/data-driven
- Pace: fast/measured/structured

### Step 5: Anti-Patterns
- What would annoy/harm this specific hiring manager
- Language/direction that signals "not a fit"
- These words/approaches are FORBIDDEN in output

### Step 6: Archetype Selection
- **A: Builder-Consultant** — For consulting firms, internal strategy, transformation roles
- **B: Operator** — For ops/execution roles, startups, scale-up
- **C: Strategist** — For corporate strategy, BizOps, RevOps, MBB
- Self-select based on JD language. If unsure, show user both and ask.

### Step 7: Fit Score
- Score against Master Corpus on: Skill match, Title parity, Industry alignment, Salary fit, ATS compatibility
- Output: `Fit: [XX]% — Gap: [specific missing items]`

## Output Formats

### ATOMIZE (raw analysis)
```json
{
  "compliance": { "noc": "XXXXX", "teer": "0/1", "salary_check": "pass/fail" },
  "work_decode": { "title": "...", "archetype": "A/B/C", "core_needs": [...] },
  "outreach": { "personas": [...], "connection_routes": [...] },
  "finops": { "range": "$X-$Y", "midpoint": "$Z", "walk_away": "$W" }
}
```

### SCORE (fit assessment)
- Fit percentage
- Gap analysis (specific missing skills)
- Recommended archetype
- Key alchemy tips

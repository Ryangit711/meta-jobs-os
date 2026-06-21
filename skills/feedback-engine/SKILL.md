---
name: feedback-engine
description: "Triggered by LEARN [company] [outcome], or auto-triggered when REJECTED, OFFER, or CALLBACK is logged. Closes the loop: outcome → analysis → system update. Every rejection or offer changes the system permanently."
---

# FEEDBACK ENGINE — Systemic Learning Loop

## Core Principle
The system is alive. Every outcome feeds back. A rejection doesn't just sting — it sharpens. An offer doesn't just land — it validates. Nothing is wasted.

## Trigger
- `LEARN [company] [outcome]` — manual
- Auto-triggered when pipeline stage changes to ❌ REJECTED, 💰 OFFER, or 📞 CALLBACK
- `LEARN [company] --deep` — full analysis (5-10 min, multi-source)

---

## The Learning Protocol (Run on Every Outcome)

### Step 1: Capture the Outcome
```
Company: [name]
Role: [title]
Stage reached: [applied / screening / interview 1 / interview 2 / final / offer]
Outcome: [offer / callback / rejection / ghosted]
Date: [YYYY-MM-DD]
What was said (if anything): [verbatim feedback]
```

### Step 2: Analyze Why (Decision Tree)

**If OFFER or CALLBACK:**
```
What worked?
  → Which pipe positioning? (C/T/I/S)
  → Which archetype? (A/B/C)
  → Which keywords resonated?
  → Which STAR story landed?
  → What made this application different?
→ RECORD in data/learned/[company].md
→ DOUBLE DOWN on these patterns in future SHOOTs
```

**If REJECTION or GHOSTED:**
```
Why?
  → Skill gap? (what specific skill was missing?)
  → Experience gap? (industry? level? years?)
  → Positioning mismatch? (wrong pipe? wrong archetype?)
  → ATS failure? (wrong keywords? format?)
  → Culture fit? (company DNA misread?)
  → Timing? (hiring freeze? internal candidate?)
→ RECORD in data/learned/[company].md
→ ADJUST system (see Step 3)
```

### Step 3: Update the System (The Critical Step)

Based on analysis, make ONE or MORE of these updates:

| Finding | System Change |
|---------|--------------|
| Wrong pipe positioning | Update `data/learned/[company].md` with correct pipe. Add to company DNA. |
| Wrong archetype | Update company profile with correct archetype for future. |
| Missing keywords | Add to `data/learned/keywords.md`. Update DNA extraction for similar companies. |
| ATS format failure | Update ATS spec for this platform in DNA extraction. |
| Skill gap | Log in `data/learned/skill_gaps.md`. If critical, train or reframe. |
| Salary mismatch | Adjust salary band for this company/role type. |
| Red flag detected | Add to company anti-patterns. Blacklist if warranted. |

### Step 4: Write the Lesson

Append to `data/learned/[company].md`:
```markdown
## [YYYY-MM-DD] — [outcome] for [role]

**What happened:** [details]
**Why I think:** [analysis]
**System change made:** [what was updated]
**Lesson for future:** [one-sentence takeaway]
```

### Step 5: Propagate

If the lesson is general (not company-specific), update the relevant system component:
- DNA extraction → add/remove keywords
- Positioning framework → adjust archetype guidance
- ATS specs → update format rules
- Kernel rules → add new insight
- Target list → remove similar companies if pattern repeats

---

## Data Files

| File | Purpose |
|------|---------|
| `data/learned/[company].md` | Per-company learning file |
| `data/learned/keywords.md` | Keywords that won/lost interviews |
| `data/learned/skill_gaps.md` | Skills flagged as missing by rejections |
| `data/learned/pipes.md` | Pipe positioning success/fail log |
| `data/learned/salary.md` | Salary data from offers/rejections |

---

## Auto-Learning (Triggered Without Command)

When pipeline stage changes:
- ❌ REJECTED → auto-run LEARN [company] rejection-light (quick capture)
- 💰 OFFER → auto-run LEARN [company] offer (capture what worked)
- 📞 CALLBACK → auto-log (wait for final outcome before full analysis)
- Ghosted > 30 days → auto-mark as rejection, run light analysis

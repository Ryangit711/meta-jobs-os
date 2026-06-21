---
name: feedback-engine
description: "Triggered by LEARN [company] [outcome], LEARN [company] --deep, or auto-signal from pipeline-tracker on ❌/💰/📞. Closes the loop: outcome → analysis → system update → pipeline sync. Every rejection or offer changes the system permanently. Cross-wired: reads from pipeline, writes to learned files, signals back to pipeline."
---

# FEEDBACK ENGINE — Systemic Learning Loop

## Cross-Skill Wiring

### Inputs (Read From)
| Source | What | When |
|--------|------|------|
| `pipeline-tracker` | company, role, outcome, stage_reached | Auto-signal on ❌/💰/📞 |
| `data/pipeline/PIPELINE.md` | Current pipeline state for this job | On manual LEARN |
| `data/learned/[company].md` | Previous lessons for this company | Always |
| User | Additional context ("they said I lacked X") | On LEARN --deep |

### Outputs (Write To)
| Target | What | When |
|--------|------|------|
| `data/learned/[company].md` | Lesson appended | Every LEARN |
| `data/learned/pipes.md` | Pipe success/fail updated | Every LEARN |
| `data/learned/keywords.md` | Keywords that won/lost | Every LEARN |
| `data/learned/skill_gaps.md` | Flagged skills | If rejection cites skill gap |
| `data/learned/salary.md` | Offer salary data | If 💰 OFFER with amount |
| `pipeline-tracker` | Signal: stage update | If outcome changes pipeline |

---

## Trigger
- Auto-signal from pipeline-tracker on ❌/💰/📞
- `LEARN [company] [outcome]` — manual
- `LEARN [company] --deep` — full analysis (5-10 min, multi-source)

---

## The Learning Protocol (Run on Every Outcome)

### Step 1: Capture the Outcome
```
READ pipeline for job context: company, role, stage_reached, date submitted
COLLECT from user (if manual) or from pipeline signal:
  Outcome: [offer / callback / rejection / ghosted]
  Stage reached: [applied / screening / interview 1 / interview 2 / final / offer]
  What was said (if anything): [verbatim feedback]
  Offer amount (if 💰): [amount]
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
→ UPDATE data/learned/pipes.md: +1 success for this pipe
→ UPDATE data/learned/keywords.md: +1 win for used keywords
→ DOUBLE DOWN on these patterns in future SHOOTs
```

**If REJECTION or GHOSTED:**
```
Why?
  → Skill gap? (what specific skill was missing?) → WRITE to data/learned/skill_gaps.md
  → Experience gap? (industry? level? years?)
  → Positioning mismatch? (wrong pipe? wrong archetype?) → UPDATE data/learned/pipes.md
  → ATS failure? (wrong keywords? format?) → UPDATE data/learned/keywords.md: +1 loss
  → Culture fit? (company DNA misread?)
  → Timing? (hiring freeze? internal candidate?)
→ RECORD in data/learned/[company].md
→ UPDATE data/learned/pipes.md: +1 failure for this pipe
```

### Step 3: Update the System (The Critical Step)

Based on analysis, make ONE or MORE of these updates:

| Finding | System Change | File Written |
|---------|--------------|--------------|
| Wrong pipe positioning | Update company DNA for this company | `data/learned/[company].md` |
| Wrong archetype | Add note for similar future companies | `data/learned/pipes.md` |
| Missing keywords | Add to learned keywords as "lost" | `data/learned/keywords.md` |
| ATS format failure | Update ATS spec for this platform | `data/learned/[company].md` |
| Skill gap identified | Log for training or reframing | `data/learned/skill_gaps.md` |
| Salary mismatch | Adjust salary data | `data/learned/salary.md` |
| Red flag detected | Add to company anti-patterns | `data/learned/[company].md` |

### Step 4: Write the Lesson

Append to `data/learned/[company].md`:
```
## [YYYY-MM-DD] — [outcome] for [role]

**What happened:** [details]
**Why I think:** [analysis]
**System change made:** [what was updated]
**Lesson for future:** [one-sentence takeaway]
```

### Step 5: Propagate to Pipeline

```
SIGNAL pipeline-tracker:
  IF outcome == offer AND accepted → transition to 🏁 ARCHIVED
  IF outcome == offer AND rejected → transition to ❌ REJECTED
  IF outcome == rejection → transition to ❌ REJECTED
  IF outcome == ghosted > 30 days → transition to ❌ GHOSTED
  UPDATE next_action: "Learned from outcome"
```

### Step 6: Propagate to System (General Lessons)

If the lesson is general (not company-specific), update the relevant system component:
- DNA extraction → add/remove keywords
- Positioning framework → adjust archetype guidance
- ATS specs → update format rules
- Kernel rules → add new insight
- Target list → remove similar companies if pattern repeats

---

## Data Files

| File | Purpose | Auto-Create |
|------|---------|-------------|
| `data/learned/[company].md` | Per-company learning file | On first LEARN for this company |
| `data/learned/keywords.md` | Keywords that won/lost interviews | Yes (template exists) |
| `data/learned/skill_gaps.md` | Skills flagged as missing by rejections | Yes (template exists) |
| `data/learned/pipes.md` | Pipe positioning success/fail log | Yes (template exists) |
| `data/learned/salary.md` | Salary data from offers/rejections | Yes (created on first offer) |

---

## Auto-Learning (Triggered Without Command)

When pipeline signal received:
- ❌ REJECTED → auto-run light LEARN (capture stage + any feedback, no deep analysis)
- 💰 OFFER → auto-run full LEARN (capture what worked + salary data)
- 📞 CALLBACK → auto-log (wait for final outcome before full analysis)
- Ghosted > 30 days → auto-mark as rejection, run light analysis

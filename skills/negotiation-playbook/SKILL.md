---
name: negotiation-playbook
description: "Triggered by NEGOTIATE [company] [offer], or auto-signal from pipeline-tracker on 💰 OFFER. Reads benchmarks from data/learned/salary.md + pipeline context (other pending offers). Generates negotiation strategy. Writes outcome back to data/learned/salary.md. Cross-wired: signals pipeline-tracker on resolution."
---

# NEGOTIATION PLAYBOOK — Executable Strategy

## Cross-Skill Wiring

### Inputs (Read From)
| Source | What | When |
|--------|------|------|
| `pipeline-tracker` (auto-signal) | company, role, offer_amount | On 💰 OFFER |
| `data/learned/salary.md` | Company-specific + pipe-specific benchmarks | On trigger |
| `data/pipeline/PIPELINE.md` | Other pending offers/interviews (for multi-offer strategy) | On trigger |
| `data/learned/[company].md` | Previous outcomes/lessons for this company | On trigger |
| User | Any specific constraints or preferences | Manual NEGOTIATE command |

### Outputs (Write To)
| Target | What | When |
|--------|------|------|
| `data/learned/salary.md` | Offer amount + company benchmark | After offer resolved |
| `data/pipeline/PIPELINE.md` | Update stage + next_action | After resolution |
| `pipeline-tracker` (signal) | Transition to 🏁 or ❌ | After final decision |

---

## Execution Protocol

### Step 1: On Trigger — Gather Intelligence
```
1. READ data/learned/salary.md:
   → Find company-specific benchmarks (if any)
   → Find pipe-specific baseline (C/T/I/S)
2. READ data/pipeline/PIPELINE.md:
   → Count other pending offers (💰 count)
   → Count active interviews (📞 count)
   → Calculate multi-offer leverage
3. READ data/learned/[company].md:
   → Past outcomes, lessons, red flags
4. CALCULATE:
   → Offer vs market range: [offer] vs [pipe baseline]
   → Multi-offer status: [X] other offers pending → LEVERAGE HIGH/MEDIUM/LOW
   → BATNA: best alternative if this offer is rejected
```

### Step 2: Generate Strategy
```
BASED ON analysis:
  IF multiple offers pending (≥2):
    → Load MULTI-OFFER STALLING protocol (see below)
    → Primary anchor: highest other offer
  IF single offer + active interviews:
    → Load DELAY protocol: "I have a few conversations wrapping up next week"
  IF only offer + no pipeline:
    → Load STANDARD protocol: negotiate within market range
```

### Step 3: Present Strategy
```
SHOW:
  ┌────────────────────────────────────────────────────────────┐
  │  NEGOTIATION STRATEGY — [company] [role]                   │
  │  Offer: $[amount]                                          │
  │  Market range: $[low]-$[high]                              │
  │  Your target: $[target]  ·  Walk-away: $[floor]            │
  │  Multi-offer leverage: [HIGH/MEDIUM/LOW] ([N] other offers)│
  │  Recommended anchor: $[anchor]                             │
  │  Script: [selected script from library]                    │
  │  Timeline: [T+0 to T+7 plan]                              │
  └────────────────────────────────────────────────────────────┘
```

### Step 4: Execute (User Acts)
User negotiates using the script. Report back:
- "Accepted at $[final_amount]"
- "Rejected — counter not met"
- "Still waiting — delayed to [date]"

### Step 5: Record Outcome
```
WRITE to data/learned/salary.md:
  → Company | Role | Band | Offer/Estimate | Date | Source = "negotiation"
UPDATE data/pipeline/PIPELINE.md:
  → If accepted: transition to 🏁 ARCHIVED, record final salary
  → If rejected: transition to ❌ REJECTED
SIGNAL pipeline-tracker: stage update applied
```

---

## Multi-Offer Stalling Protocol (Critical for 10-12 Day Objective)

**When:** You have offer #1 but expect offer #2 within 3-10 days.
**Goal:** Delay offer #1 without losing it.

### Script: Initial Response to Offer #1
```
"Thank you so much — I'm really excited about this opportunity.
I have a few other conversations in final stages that I want to respect
by giving them a fair conclusion. Could we set a decision date for [day 12]?
I want to make sure I'm giving this decision the full consideration it deserves."
```

### If They Push for Earlier
```
"I completely understand the timeline. Would it work if I give you my
decision by [day 10]? That gives me enough time to wrap up the other
conversations properly and come back with a clear yes."
```

### If They Need an Answer Now (Exploding Offer)
```
"I really want to join [company], but I'd be doing both of us a disservice
if I didn't properly consider all my options. If you need an answer today,
I'll have to respectfully decline — but if you can give me until [day X],
I'm very confident I'll say yes."
```

### Stalling Timeline
```
T+0: Receive offer #1 → "Thank you, I need [X] days"
T+1: Check in with offer #2 recruiter → "Any update on timeline?"
T+3: Re-evaluate: can offer #1 wait longer? 
T+[X-1]: Final decision on offer #1
If offer #2 arrives → compare both → negotiate against each other
```

### Comparing Two Offers
```
Create comparison table:
  Factor          | Offer #1 | Offer #2
  Base salary     | $X       | $Y
  Total comp Y1   | $X       | $Y
  Role scope      | [desc]   | [desc]
  Growth path     | [desc]   | [desc]
  Culture fit     | [score]  | [score]
  Location/flex   | [desc]   | [desc]

Use offer #2 to negotiate offer #1 up (and vice versa):
  "I have another offer at [$higher]. I'd prefer [company #1] because [reason],
  but I need you to at least match the base. Can you do $[target]?"
```

---

## Standard Scripts Library

### Anchoring
```
Recruiter: "The offer is $X."
You: [pause 3 seconds]
You: "I appreciate the offer. Based on my experience leading a $17M exit,
building from 3 to 70 people, and the market value for this role at companies
like [peer company], I was targeting $[target]. Is there flexibility?"
```

### What's Your Number?
```
You: "I don't want to throw out a number outside your range. Based on the
role scope and my background, $[target-$target+10K] is fair market value.
Does that align with your budget?"
```

### Can't Move on Base
```
You: "I understand. Can we look at:
  → Signing bonus ($10-20K)
  → Performance bonus guarantee (first year)
  → Additional equity / RSUs
  → Extended vesting cliff
  → Professional development budget
  → Extra vacation week"
```

### Competing Offer
```
You: "I have another offer at [$amount]. I'd prefer to join your team because
[reason], but I need you to match or exceed this to make it work.
Can you do $[target]?"
```

### The Close
```
You: "If you can get to $[target] + [key term], I'm ready to sign today.
When can you come back to me?"
```

---

## Walk-Away Analysis

| Factor | Green (Accept) | Yellow (Consider) | Red (Walk) |
|--------|---------------|-------------------|------------|
| Base salary | ≥ $[target] | $[target-10K] to $[target] | < $[floor] |
| Total comp Y1 | ≥ $[total_target] | $[total_target-15K] to $[total_target] | < $[total_floor] |
| Role scope | Matches expectation | Slightly different | Completely different |
| Growth potential | Clear path | Unclear | Dead end |
| Culture | Good fit | Unknown | Red flags |
| Location | Remote/Vancouver | Hybrid limited | On-site elsewhere |

---

## Offer Response Timeline

| Time | Action |
|------|--------|
| T+0 | Receive offer → "Thank you, I need a few days to review" |
| T+1 | Gather intel, prepare counter |
| T+2 | Send counter or delay request |
| T+4 | Follow up if no response |
| T+[deadline] | Final decision |
| Sign | Record in `data/learned/salary.md`, update pipeline to 🏁 |

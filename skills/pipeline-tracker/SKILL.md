---
name: pipeline-tracker
description: "Triggered by TRACK, TRACK [company], TRACK --stats, or auto-executed whenever a pipeline write/update occurs. Reads PIPELINE.md, formats display, handles all writes to PIPELINE.md. Cross-wired: signals feedback-engine on ❌/💰, signals negotiation-playbook on 💰, signals networking-cadence on ✅."
---

# PIPELINE TRACKER — Live Kanban (Executable)

## Core Principle
You never ask "where was I?" You say TRACK and see everything. Every skill writes to PIPELINE.md through this tracker. No direct file manipulation.

---

## Data File
`data/pipeline/PIPELINE.md` — auto-maintained. Never manually edited. All writes go through this skill.

---

## Execution: On TRACK Trigger

### Step 1: Read Pipeline
```
READ data/pipeline/PIPELINE.md
PARSE table rows → list of jobs with stages
CREATE hashmap: company + role → {stage, salary, pipe, T+, next_action}
```

### Step 2: Calculate Countdowns
```
For each ✅ SUBMITTED job:
  T+ = today - T+0_date
  If T+ == 3 AND networking not sent → set next_action = "Follow up"
  If T+ == 7 AND networking not sent → set next_action = "Connect IC"
  If T+ == 14 AND networking not sent → set next_action = "Value-add note"
  If T+ > 30 AND stage == ✅ → auto-transition to ❌ GHOSTED
```

### Step 3: Calculate Stats
```
total_jobs = count(all)
active_jobs = count(🟢 + 🔵 + ✅ + 📞)
offers = count(💰)
rejections = count(❌)
callback_rate = callbacks / (callbacks + rejections) * 100
offer_rate = offers / (callbacks) * 100  # if callbacks > 0
```

### Step 4: Display Table
```
╔══════════════════════════════════════════════════════════════════════════╗
║  📊 PIPELINE — [active] active · [💰] offers · [✅] submitted · [🟢] live  ║
║  Callback rate: [X]%  ·  Offer rate: [Y]%                              ║
╠══════════════════════════════════════════════════════════════════════════╣
║ [stage] [company] [role] [pipe] [salary] [stage_str] [T+] [next_action]║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Execution: On Pipeline Write (Called by Other Skills)

### Add Job (🟢 or 🔵)
```
Function: pipeline_add(company, role, salary, pipe, stage)
1. READ data/pipeline/PIPELINE.md
2. Check if company+role already exists → if yes, SKIP (no duplicates)
3. APPEND row: [company] | [role] | [salary] | [pipe] | [stage] | [today] | [T+ or —] | [next_action]
4. WRITE to data/pipeline/PIPELINE.md
5. Return: "Added [company] [role] as [stage]"
```

### Transition Stage
```
Function: pipeline_transition(company, role, new_stage, options={})
1. READ data/pipeline/PIPELINE.md
2. FIND row matching company+role
3. UPDATE stage to new_stage
4. IF new_stage == ✅: set T+0 = today, set next_action = "Networking cadence started"
5. IF new_stage == 📞: set next_action = "Interview prep"
6. IF new_stage == 💰: set next_action = "Negotiate"
   → SIGNAL: feedback-engine.trigger_learn(company, role, "offer")
   → SIGNAL: negotiation-playbook.trigger(company, role, offer_amount)
7. IF new_stage == ❌: set next_action = "Learn from rejection"
   → SIGNAL: feedback-engine.trigger_learn(company, role, "rejection")
8. IF new_stage == 🏁: remove from active table, add to archive
9. WRITE to data/pipeline/PIPELINE.md
10. Return: "[company] [role] transitioned to [new_stage]"
```

### Update Next Action
```
Function: pipeline_set_action(company, role, action)
1. READ → FIND → UPDATE next_action column → WRITE
```

---

## Commands

| Command | Execution |
|---------|-----------|
| `TRACK` | Run Steps 1-4 (full display) |
| `TRACK [company]` | READ → FILTER by company → DISPLAY filtered rows |
| `TRACK --active` | READ → FILTER where stage not ❌/🏁 → DISPLAY |
| `TRACK --offers` | READ → FILTER where stage == 💰 → DISPLAY |
| `TRACK --rejected` | READ → FILTER where stage == ❌ → DISPLAY + lessons from data/learned/ |
| `TRACK --stale` | READ → FILTER where T+ > 7 AND stage same → DISPLAY + prompt "Hold or archive?" |
| `TRACK --next` | READ → FILTER where next_action not empty → DISPLAY |
| `TRACK --stats` | Run Step 3 only → DISPLAY stats banner |
| `TRACK --export` | READ → convert to JSON → WRITE data/pipeline/pipeline_export.json → DISPLAY path |

---

## Auto-Transition Rules (Run on Every TRACK + Every Pipeline Write)

Checked automatically — no command needed:
1. ✅ + T+ > 30 → ❌ GHOSTED (auto-learn triggered)
2. 🔵 + no activity > 14 days → ⏸ HOLD (flag to user)
3. 📞 + no activity > 60 days → 🏁 ARCHIVED (dead lead)
4. 💰 → auto-trigger negotiation playbook + feedback engine

---

## Cross-Skill Signals (Auto-Fired)

| Event | Signal Sent To | Data Passed |
|-------|---------------|-------------|
| Stage → ❌ | `feedback-engine (light LEARN)` | company, role, outcome="rejection", stage_reached |
| Stage → 💰 | `feedback-engine (full LEARN)` + `negotiation-playbook` | company, role, outcome="offer" |
| Stage → ✅ | `networking-cadence (start timer)` | company, role, T+0=today, personas from SHOOT |
| Stage 📞 → 💰 or ❌ | `feedback-engine (resolve pending)` | company, role, final outcome |

All signals are instructions to load + execute the target skill. No data leaves the system.

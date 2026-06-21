---
name: pipeline-tracker
description: "Triggered by TRACK, TRACK [company], or auto-updated every time a pipeline stage changes. Maintains the live kanban of every job in the system. No mental tracking — the system remembers."
---

# PIPELINE TRACKER — Live Kanban

## Core Principle
You have one job: think. The system tracks every application, every stage, every next action. You never ask "where was I?" — you just say TRACK.

---

## Data Source
`data/pipeline/PIPELINE.md` — auto-maintained. Never edit manually.

---

## State Machine (Every Job)

```
🟢 FETCHED → 🔵 SHOT → ✅ SUBMITTED → 📞 CALLBACK → 💰 OFFER
                                       → ❌ REJECTED → 🏁 ARCHIVED
                 → ⏸ HOLD
```

| Stage | Meaning | Auto-Transition |
|-------|---------|-----------------|
| 🟢 FETCHED | Job discovered, awaiting SHOOT | → 🔵 after SHOOT command |
| 🔵 SHOT | Package written, awaiting approval | → ✅ after YES |
| ✅ SUBMITTED | Application sent | → auto-track T+0 date |
| 📞 CALLBACK | Interview invitation | → manual (user reports) |
| 💰 OFFER | Offer received | → manual |
| ❌ REJECTED | Rejection received | → auto-learn triggered |
| ⏸ HOLD | Paused for strategy | → manual |
| 🏁 ARCHIVED | Final state | auto after 90 days |

---

## Commands

| Command | Action |
|---------|--------|
| `TRACK` | Show full pipeline table |
| `TRACK [company]` | Show that company's jobs |
| `TRACK --active` | Show only non-archived jobs |
| `TRACK --offers` | Show offers only |
| `TRACK --rejected` | Show rejections + lessons |
| `TRACK --stale` | Show jobs with no activity in 7+ days |
| `TRACK --next` | Show only jobs needing action today |
| `TRACK --stats` | Pipeline metrics (apply rate, callback rate, offer rate) |
| `TRACK --export` | Export as JSON for analysis |

---

## Auto-Maintenance Rules

1. Every SHOOT → auto-adds job to pipeline as 🔵
2. Every YES → auto-transitions to ✅, sets T+0 = today
3. Every CALLBACK/OFFER/REJECTION reported → auto-updates stage + triggers learning
4. Jobs stale > 14 days at 🔵 → auto-flag as ⏸ HOLD, prompt user
5. Every TRACK output → show NEXT ACTION for each row
6. T+ countdown auto-calculated from submission date

---

## Display Format

```
╔══════════════════════════════════════════════════════════════════════════╗
║  📊 PIPELINE — 8 active · 3 offers · 5 submitted · 2 in progress     ║
╠══════════════════════════════════════════════════════════════════════════╣
║ 🟢 Deloitte      Sr Mgr Strategy  C   $180K  LIVE    —     FETCH next ║
║ 🔵 lululemon     Prog Mgr         T   $150K  SHOT    D3    APPROVE?   ║
║ ✅ TELUS         Cat Mgr          I   $130K  SUBMIT  D7    Follow up  ║
║ 📞 Clio          Rev Ops          T   $145K  CALLBK  D12   Prep       ║
║ 💰 Hiive         Ops Lead         S   $140K  OFFER   D5    Negotiate  ║
║ ❌ EvenUp        Strategy         T   $155K  REJ     D8    Learn      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

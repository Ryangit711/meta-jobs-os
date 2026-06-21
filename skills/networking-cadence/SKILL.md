---
name: networking-cadence
description: "Triggered by SUBMITTED [company], YES, or auto-triggered after every YES (no SUBMITTED needed). Networking timer auto-starts when user approves a SHOOT. Proactive prompts at T+0, T+3, T+7, T+14 without user command. Zero manual touch — fully automated networking tracker."
---

# NETWORKING CADENCE — Automated Outreach Tracker

## Source Truth Anchors
- Networking rules: AGENTS.md Networking section (JOBS-OS)
- Constitutional Amendment #11 (Fully Automated Networking Tracker)
- Contact Engine: `CONTACT_ENGINE.py` (JOBS-OS)

## System

### Data Store
- `data/networking_log.json` — NEVER deleted, reset, or archived. Permanent system memory.
- Pipeline data at `data/pipeline/PIPELINE.md` — auto-synced.

### Seed Flow (On YES — Auto-Triggered, No SUBMITTED Command Needed)

Every YES auto-starts the networking timer. The system tracks T+0 from the approval date. No SUBMITTED command needed.

When YES is given:
1. Auto-set T+0 = today
2. Read company's SHOOT package → extract personas + message templates
3. Calculate all T+0 through T+14 dates from approval date
4. Write to `data/networking_log.json`
5. Show auto-cadence in footer

If submission hasn't happened yet (T+0), the system reminds: "Submit [company] first."
1. Read company's SHOOT package → extract personas + message templates
2. Calculate all T+0 through T+14 dates from submission date
3. Write to `data/networking_log.json` with `today` as `last_checked`
4. Set `hook_active: true`

### Response Flow (Every Output)
1. Read `data/networking_log.json`
2. Compute countdown for ALL pending actions
3. Append AUTO-NETWORKING footer at end:

```
╔═══════════════════════════════════════════════════════╗
║  📡 AUTO-NETWORKING                                    ║
║  🎯 T+[N]: [action] for [company] — due today         ║
║  ⏳ T+[N]: [action] for [company]                      ║
║  ⏳ T+[N]: [action] for [company]                      ║
║  Say LINKEDIN CONNECT [name] to send, or SKIP.        ║
╚═══════════════════════════════════════════════════════╝
```

### Confirmation Flow (On YES)
- If one action due today → auto-log as sent, compute next action
- If multiple due today → ask "Which one? [company list]"
- Update `data/networking_log.json`

### Persona Tracking Rules
- Up to 4 personas per company (IC/Associate, Manager/Director, Sr IC/Manager, Exec Sponsor)
- If persona RESPONDS → mark "engaged", stop messaging that persona
- If NO_RESPONSE after T+7 of their last message → switch to next persona
- Never double-message a non-responsive connection
- Always remind unless responded

### Status Updates
- `STATUS [company] [status]`: pending, submitted, live_interviewing, rejected, offer, closed
- When all messages sent: "✅ [Company] cadence complete — waiting for response"
- Tracker stays in "pending" until user updates

## Commands
- `SUBMITTED [company]` — Register submission + seed cadence
- `YES` — Confirm sent, advance cadence
- `LOGNET [company]` — Manually log a networking message
- `NETSTAT` — Show full networking log
- `STATUS [company] [status]` — Update company status
- `SUBMITDATE [company] YYYY-MM-DD` — Change submission date (recalculates cadence)

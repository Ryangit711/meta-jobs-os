---
name: networking-cadence
description: "Triggered by SUBMITTED [company], YES, LOGNET, NETSTAT, or networking countdown checks. Manages the multi-channel outreach tracking system. Handles auto-seeding cadences, sending confirmations, status updates, and countdown display. Zero manual touch — fully automated networking tracker."
---

# NETWORKING CADENCE — Automated Outreach Tracker

## Source Truth Anchors
- Networking rules: AGENTS.md Networking section (JOBS-OS)
- Constitutional Amendment #11 (Fully Automated Networking Tracker)
- Contact Engine: `CONTACT_ENGINE.py` (JOBS-OS)

## System

### Data Store
- `data/networking_log.json` — NEVER deleted, reset, or archived. Permanent system memory.

### Seed Flow (On SUBMITTED [company])
1. Read company's SHOOT package → extract personas + message templates
2. Calculate all T+0 through T+14 dates from submission date
3. Write to `data/networking_log.json` with `today` as `last_checked`
4. Set `hook_active: true`

### Response Flow (Every Output)
1. Read `data/networking_log.json`
2. Compute countdown for ALL pending actions
3. Append NETWORKING COUNTDOWN footer at end:

```
╔═══════════════════════════════════════════════════════╗
║  📡 NETWORKING COUNTDOWN                              ║
║  🎯 DUE TODAY: [action] for [company]                 ║
║  ⏳ [N] DAYS: [action] for [company]                  ║
║  Ready to send? Reply YES when done.                  ║
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

---
name: contact-engine
description: "Triggered by CONTACT command variants. Manages the contact database, generates DNA-tailored cold emails and LinkedIn messages, and tracks multi-channel outreach cadence (LinkedIn + Email parallel tracks)."
---

# CONTACT ENGINE — Multi-Channel Outreach

## Source Truth Anchors
- Contact Engine: `CONTACT_ENGINE.py` (JOBS-OS)
- Constitutional Amendment #18

## Data Store
- `data/contacts.json` — local-only, gitignored

## Flow

### Registration
User says: `CONTACT [Name] [Company] [Role] [Email]`
- System caches in `data/contacts.json`
- Returns: "Registered [Name] at [Company]. Ready to generate outreach."

### Message Generation
- `CONTACT [Name] email` — Generate DNA-tailored cold email
- `CONTACT [Name] linkedin` — Generate LinkedIn connect message
- Messages use company DNA from the most recent SHOOT package for that company

### Two-Channel Cadence (Per Contact)
| Day | LinkedIn Track | Email Track |
|-----|---------------|-------------|
| T+0 | Connect + note | — |
| T+1 | — | Intro email |
| T+3 | Engage (like/comment) | Follow-up |
| T+7 | DM | Check-in |
| T+14 | Final nudge | Final nudge |

### Tracking
- `CONTACT [Name] cadence` — Show full two-channel cadence
- `CONTACT [Name] sent` — Log message as sent, auto-advance
- `CONTACT LIST` — Show all cached contacts with pending actions
- Follow-up reminders appear in NETWORKING COUNTDOWN footer

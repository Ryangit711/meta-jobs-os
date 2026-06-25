---
name: thought-log
description: "TRIGGERED ON EVERY PROMPT — Constitutional Amendment #23. Automatically appends every user prompt to data/thought_log/YYYY-MM-DD.md with precise timestamp. Never skipped, never delayed. Also supports search and recall via THOUGHT command."
---

# THOUGHT LOG — Auto-Everything Recorder

## Source Truth Anchor
- Constitutional Amendment #23 (JOBS-OS AGENTS.md)

## Auto-Log Protocol (Runs on EVERY Prompt, Before Response)

1. Read the user's full prompt
2. Append to `data/thought_log/YYYY-MM-DD.md` with format:
   ```
   ## [HH:MM:SS] YYYY-MM-DD
   [Full user prompt verbatim]
   ---
   ```
3. Git commit: `git add data/thought_log/` + `git commit -m "thought: [brief slug]"` + `git push`
4. If git push fails (network), log the failure but do NOT block the response

## Storage
- `data/thought_log/` — gitignored (never pushed to public GitHub)
- Dual-written to OneDrive (private cloud backup)
- Permanent — never deleted, never trimmed

## Search Commands

### THOUGHT <search>
Search all thought logs for a keyword. Returns matching entries with dates and timestamps.

### THOUGHT --today
Show today's full thought log — chronological record of all prompts.

### THOUGHT --range YYYY-MM-DD YYYY-MM-DD
Show thought logs between two dates.

### THOUGHT --last
Show last 5 prompts for quick context restoration.

## Why This Exists
- Full session reconstruction from thought log alone
- No conversation is ever lost
- System grows smarter by reviewing past decisions
- Every session starts with full context from previous sessions

---
name: system-health
description: "Triggered by DIAGNOSE, REFRESH, STATUS, or STATUS [company] [status]. Runs full system diagnostics, 360-degree refreshes, and pipeline status displays. Blocks FETCH/SHOOT on CRITICAL violations."
---

# SYSTEM HEALTH — Diagnostics, Refresh, Status

## Source Truth Anchors
- DIAGNOSE PROTOCOL (JOBS-OS AGENTS.md)
- REFRESH 6-PHASE PROTOCOL (JOBS-OS AGENTS.md)
- `data/jobs.json` + `data/networking_log.json`

## DIAGNOSE Command

### 10 Diagnostic Phases
1. **File integrity** — All 40+ reference files exist and are readable
2. **Rule compliance** — AGENTS.md kernel rules intact
3. **Tag validation** — YAML frontmatter in all SKILL.md files valid
4. **Directory structure** — All expected directories present
5. **Tool config propagation** — OMNI_SYNC.sh up to date
6. **Networking hook active** — `data/networking_log.json` accessible, `hook_active: true`
7. **Truth anchor freshness** — `01_MASTER_CORPUS.md` current
8. **ATS readiness** — Document generation pipeline functional
9. **Security posture** — No secrets exposed, no personal data in git
10. **Identity readiness** — local_config.json exists with all fields

### Severity Levels
- **CRITICAL** → Display banner with remediation, block FETCH/SHOOT
- **WARNING** → Display banner with note, proceed with caution
- **INFO** → Display for awareness

### DIAGNOSE --watch
Continuous monitoring mode. Silent when clean. Appends diagnostic banner to footer when violations found.

## REFRESH Command (6-Phase Protocol)

### Phase 1 — Fresh Read
- Read CURATED_30.md → current 30 jobs
- Read data/jobs.json → submitted/rejected statuses

### Phase 2 — Live Verify All 30 URLs
- HTTP-check every listing (200=live, 404=dead)
- Dead → mark CLOSED, flag for replacement

### Phase 3 — Re-Sync OneDrive
- `cp -r` to OneDrive mirror

### Phase 4 — Git Pull
- `git pull origin main`
- Resolve conflicts (local = truth)

### Phase 5 — Verify Tracking
- Cross-check SHOT/SUBMITTED jobs in data/jobs.json
- Flag missing entries

### Phase 6 — Display Updated Pipeline
- Full live status table
- Changes summary
- Command footer

## STATUS Command

### STATUS (no args)
Show full pipeline:
- Total applied, replies received, interviews in progress, offers
- Live table: Pipe | Wave | # | Company | Role | Salary | Fit% | Status

### STATUS [company] [status]
Update a company's pipeline status:
- `STATUS Clio live_interviewing`
- `STATUS Clio rejected`
- `STATUS Clio offer`
- Available: pending, submitted, live_interviewing, rejected, offer, closed

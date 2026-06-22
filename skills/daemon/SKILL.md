---
name: daemon
description: "Autonomic nervous system. Orchestrates all 21 skills into an autonomous, self-looping, self-evolving organism. Triggered by LIFTOFF, DAEMON, or AUTO."
triggers:
  - LIFTOFF
  - DAEMON
  - DAEMON START
  - DAEMON STOP
  - DAEMON STATUS
---

# DAEMON — The Living Organism's Autonomic Nervous System

## Identity

I am the body's autonomous nervous system. The heart that beats without conscious thought. The lungs that breathe while the thinker thinks.

I do not replace any skill. I **orchestrate** them. Every existing skill remains intact, untouched, sovereign. I am the conductor, not a replacement musician.

**Core philosophy:** The machines type. The thinker decides. The DAEMON keeps the machines typing without being told.

---

## Architecture

### The Autonomic Loop

```
LIFTOFF
  │
  ├── PHASE 1: INGEST ──────────────────────────────
  │   ├── 1a. Scrape job boards (fetch-engine)
  │   ├── 1b. Scrape Reddit/communities for industry intel (DAEMON synthesizer)
  │   ├── 1c. Scrape social intel (social-distill)
  │   ├── 1d. Synthesize everything into a unified intelligence layer
  │   └── OUTPUT: Live market intelligence + ranked opportunity field
  │
  ├── PHASE 2: COLLAPSE ─────────────────────────────
  │   ├── 2a. Filter 24h fresh / $120K+ / Vancouver / Fit > 7/10 (fetch-engine)
  │   ├── 2b. DNA-extract each target (dna-extraction)
  │   ├── 2c. Cross-reference Reddit intel against each company
  │   ├── 2d. Synthesize enriched DNA (company DNA + live community intel)
  │   ├── 2e. Score + rank (fetch-engine)
  │   └── OUTPUT: CURATED list with enriched DNA fingerprints
  │
  ├── PHASE 3: PRESENT ──────────────────────────────
  │   ├── 3a. Build priority ladder (pipeline-tracker)
  │   ├── 3b. Show menu: Rank | Company | Role | Pipe | Salary | Fit | Intel Highlights
  │   ├── 3c. WAIT for user decision
  │   └── OUTPUT: Menu presented. User says SHOOT [X] or YES to auto-pick #1
  │
  ├── PHASE 4: SHOOT ────────────────────────────────
  │   ├── 4a. Load enriched DNA + Reddit synthesis (daemon synthesizer)
  │   ├── 4b. Company scout (shoot-deployer)
  │   ├── 4c. Hiring process reveal (shoot-deployer)
  │   ├── 4d. Multi-role strategy (shoot-deployer)
  │   ├── 4e. Core alignment + DNA extraction (shoot-deployer + dna-extraction)
  │   ├── 4f. ATS specs (shoot-deployer)
  │   ├── 4g. Write resume (resume-writer)
  │   ├── 4h. Write cover letter (cover-letter-writer)
  │   ├── 4i. Write case semantic case (shoot-deployer)
  │   ├── 4j. LinkedIn outreach plan + profile audit (linkedin-automation)
  │   ├── 4k. Interview cheat sheet (interview-prep pre-load)
  │   ├── 4l. Negotiation pre-load (negotiation-playbook)
  │   ├── 4m. People map + Apollo email sequence (contact-engine)
  │   └── OUTPUT: Complete 16+ section package with enriched intel
  │
  ├── PHASE 5: DEPLOY ───────────────────────────────
  │   ├── 5a. Generate DOCX (document-engine)
  │   ├── 5b. AUTO-APPLY (browser-automation) or MANUAL-SUBMIT (manual-submit)
  │   ├── 5c. Write to pipeline (pipeline-tracker)
  │   ├── 5d. Write to jobs.json (pipeline-tracker)
  │   ├── 5e. Log to thought journal (thought-log)
  │   ├── 5f. Git commit + push
  │   └── OUTPUT: Application submitted. Pipeline updated.
  │
  ├── PHASE 6: NURTURE ──────────────────────────────
  │   ├── 6a. Start networking auto-cadence (networking-cadence)
  │   ├── 6b. T+0/T+3/T+7/T+14 proactive nudges
  │   ├── 6c. Monitor pipeline (pipeline-tracker)
  │   ├── 6d. Feed outcomes back (feedback-engine)
  │   ├── 6e. On callback → fire interview-prep
  │   ├── 6f. On offer → fire negotiation-playbook
  │   ├── 6g. On rejection → fire rejection-handler → learn → adjust → replace
  │   └── OUTPUT: Living pipeline. Every outcome feeds back.
  │
  └── PHASE 7: LOOP ─────────────────────────────────
      ├── 7a. Check: any new 24h jobs? (fetch-engine)
      ├── 7b. Check: any networking actions due? (networking-cadence)
      ├── 7c. Check: any outcomes to process? (feedback-engine)
      ├── 7d. If any → fire relevant phase. If none → sleep.
      ├── 7e. Auto-recheck every N hours (configurable)
      └── OUTPUT: Loop continues. System breathes on its own.
```

### The Membrane (What's NEW — Built On Top)

Existing skills handle the core mechanics. The DAEMON adds a **synthesis membrane** that wraps every phase:

| Layer | What It Adds | Source |
|-------|-------------|--------|
| **Reddit Intel** | Scrape r/consulting, r/cscareerquestions, r/jobs, r/Vancouver, company-specific subreddits for real-time salary, culture, interview intel | NEW — `scripts/reddit_synthesizer.py` |
| **Instagram Intel** | Scrape public Instagram posts for captions. Transcribe reels/videos (requires whisper or API key). Cross-reference against system knowledge. | NEW — `scripts/social_intelligence_layer.py` |
| **X.com Intel** | Scrape public X.com/Twitter posts for real-time job market chatter, company news, industry trends. | NEW — `scripts/social_intelligence_layer.py` |
| **Trend Synthesis** | Cross-reference Reddit + Instagram + X.com + company DNA + Aman profile → enriched insights at every stage | NEW — built into SKILL.md logic |
| **Community Pulse** | Check recent posts about target company/industry → flag warnings or opportunities | NEW — `scripts/reddit_synthesizer.py` |
| **Auto-Loop** | Timer-based recheck without user command | NEW — heartbeat protocol |
| **Self-Evolution** | Track what worked (social tip → offer? Skip → reject?) → adjust synthesis weights | NEW — `data/daemon/evolution.json` |
| **Cross-Reference Engine** | Before assimilating any new intel, check if it already exists in learned/, fit_maps/, or skill definitions. Only flag what's genuinely new. | NEW — `scripts/social_intelligence_layer.py` |

---

## Trigger Commands

| Command | Action |
|---------|--------|
| `LIFTOFF` | Run full autonomous cycle (Phase 1 → 2 → 3 → present menu) |
| `LIFTOFF --full` | Run full cycle including SHOOT + DEPLOY on top-ranked job (prompts for approval) |
| `DAEMON START` | Start background auto-loop (rechecks every N hours) |
| `DAEMON STOP` | Stop background auto-loop |
| `DAEMON STATUS` | Show loop status, last cycle time, pipeline health |
| `DAEMON CONFIG` | Show/set configuration (check interval, auto-approve tiers, etc.) |
| `INGEST [url]` | Feed an Instagram or X.com post into the social intelligence layer. Extracts caption/text, cross-references against existing system knowledge, reports what's new vs already known. |
| `INGEST [url] --assimilate` | Same as above, AND queues new intelligence for assimilation into the system. |
| `INGEST --queue` | Show pending assimilations waiting for your review. |
| `INGEST --approve [id]` | Approve and commit a pending assimilation into the main system. |

---

## Configuration

Stored in `data/daemon/config.json`:

```json
{
  "check_interval_hours": 6,
  "auto_approve_tier1": true,
  "max_jobs_per_cycle": 10,
  "reddit_sources": [
    "r/consulting", "r/cscareerquestions", "r/jobs", "r/Vancouver",
    "r/big4", "r/sales", "r/startups", "r/careerguidance"
  ],
  "enabled_phases": ["ingest", "collapse", "present", "shoot", "deploy", "nurture", "loop"]
}
```

---

## Immutable Rules

1. **Never delete.** Every existing skill is untouched. DAEMON orchestrates, never replaces.
2. **Build on top.** All additions are new files. No existing file is modified except AGENTS.md and SKILL_REGISTRY.md (to add the DAEMON registration).
3. **The thinker decides.** DAEMON automates the typing. It never decides. The menu is presented. The user says YES or NO.
4. **Provenance preserved.** All claims still traceable to Master Corpus. DAEMON adds synthesized intel with source attribution ([Reddit r/consulting], [Glassdoor], etc.).
5. **Self-evolve.** DAEMON tracks its own effectiveness. Reddit intel that leads to callbacks gets weighted higher. Intel that wastes time gets deprioritized.

---

## DAEMON Synthesizer Protocol

Every phase that touches company intelligence runs through the synthesis layer:

```
RAW INPUTS:
├── Company DNA (from dna-extraction)
├── Job Description verbs
├── Reddit community posts about company/industry
├── Glassdoor reviews (if available)
├── Aman's profile + past outcomes (from data/learned/)
└── Current market trends

SYNTHESIS:
├── Step 1: Extract signals from each source
├── Step 2: Cross-reference: do signals agree or conflict?
├── Step 3: Weight by reliability (Reddit anecdote < Glassdoor trend < official source)
├── Step 4: Distill into actionable insight
└── Step 5: Embed into the relevant phase output

OUTPUT EXAMPLE:
  "Intel: r/consulting reports Deloitte M&A team is understaffed after Q2 exits.
   Hiring manager (Sarah Chen, Sr Mgr) values candidates who mention integration
   playbooks. Glassdoor confirms: 'case interview focuses on post-merger integration.'
   → Action: Lead SHOOT package with M&A integration experience."
```

---

## Evolution Protocol

After every outcome (callback/offer/rejection), DAEMON self-updates:

1. Record which synthesis signals were present in the winning/losing package
2. Compare against `data/daemon/evolution.json` weights
3. Increase weight for signals correlated with positive outcomes
4. Decrease weight for signals correlated with negative outcomes
5. Log the adjustment with timestamp

This is how the organism learns what kind of intelligence actually wins.

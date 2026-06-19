---
name: interview-prep
description: "Triggered when user says 'callback from [company]', 'interview from [company]', 'got an email', 'got a call', or any signal of interview invitation. Loads company DNA sheet, stage-maps the response, and generates full prep materials."
---

# INTERVIEW PREP — Callback-Ready Protocol

## Source Truth Anchors
- Interview alchemy: `05_INTERVIEW_ALCHEMY.md` (JOBS-OS)
- Infiltration layer: `37_INFILTRATION_LAYER.md` (JOBS-OS)
- Master Corpus: `01_MASTER_CORPUS.md` (JOBS-OS)
- CALLBACK_READY sheets from FETCH Phase 6

## Protocol

### Step 1: Stage-Map the Response
Determine which stage:
1. Email/callback → phone screen
2. Phone screen passed → video interview
3. Video passed → in-person/onsite
4. In-person passed → offer negotiation

Generate the next stage's preparation materials.

### Step 2: Pull Company DNA
- Read `CALLBACK_READY/[Company]_DNA.md` from date folder
- If not found, run DNA Extraction on the company

### Step 3: Generate Stage-Specific Scripts

#### Phone Screen Prep
- 60-second pitch (alchemized to company + stage)
- Answers to top 5 questions for THIS company (not generic)
- Voicemail script if they call during sleep hours (10am-4pm)
- Best return-call window (after 4pm PT)

#### Video Interview Prep
- Camera setup, lighting, background tips
- 5 company-specific Q&A with full answers
- 3 STAR stories from Master Corpus (Profitability/Credibility/Visibility pillars)
- Keywords to use, anti-patterns to avoid
- "One year from now" question at the end

#### In-Person/Onsite Prep
- Company culture — dress code, communication style
- Device/workspace familiarization per Device Map
- Case study or presentation prep if applicable
- Questions to ask at each level (IC → Manager → Director → Exec)

### Step 4: Generate Cheat Sheet
- 60-sec pitch
- 5 Q&A with specific answers
- 3 STAR stories with metrics
- Keywords list
- Anti-patterns list
- Rejection response script (never ghost a rejection — reply gracefully within 48h)

### Step 5: Update Tracking
- Update status to `live_interviewing` in data/jobs.json
- Set next action date
- Show countdown for follow-up

## Stage-Specific Infiltration (From 37_INFILTRATION_LAYER.md)
- ATS stage: keywords at 2-4%, title alignment, format compliance
- Phone screen: energy, clarity, listen more than talk, use 3 value words
- Video: environment matters, look at camera, show you did homework
- In-person: mirror their energy, ask about their challenges, be the solution
- Orientation: be early, listen, write everything down, ask about communication preferences
- Hallway: be human, ask about their weekend, remember names

---
name: manual-submit
description: "Triggered when AUTO-APPLY is called but browser automation is unavailable (Termux, phone, no Chrome). Generates a complete step-by-step submission guide so the user can apply from any device. No automation = no excuse."
---

# MANUAL SUBMIT — Phone / Termux Fallback

## Core Principle
The system never stops because of a device constraint. If browser-use can't run, the system generates an exact blueprint for human hands. Every field mapped. Every paste ready. The user just follows instructions.

---

## When This Activates

Auto-detected conditions:
- `uname -a` contains `android` or `termux`
- `which google-chrome` or `which chromium` returns empty
- `node -e "require('playwright')"` throws error
- User explicitly says `MANUAL-SUBMIT [company]`
- `AUTO-APPLY [company] --manual`

---

## Output: The Submission Blueprint

### 1. URL
```
Direct application link: https://careers.deloitte.ca/jobs/[id]
```

### 2. ATS Type
```
Platform: Workday
Multi-page? Yes (5 pages)
Max upload size: 10MB
Format accepted: .docx, .pdf
```

### 3. Field Mapping (Page by Page)

Page 1 — Personal Information
```
┌─────────────────────────────┬──────────────────────────────┐
│ Field                       │ Value / Action               │
├─────────────────────────────┼──────────────────────────────┤
│ First Name                  │ Aman                          │
│ Last Name                   │ Kumar                         │
│ Email                       │ amankumar7111@outlook.com     │
│ Phone                       │ +1 236-885-2285              │
│ Location (City)             │ Vancouver                     │
│ Location (Province)         │ British Columbia              │
│ Country                     │ Canada                        │
│ LinkedIn URL                │ linkedin.com/in/aman1776      │
│ Portfolio / Website         │ (skip)                        │
│ How did you hear about us?  │ LinkedIn                      │
│ Work authorization          │ Yes - Permanent Resident      │
│ Require visa sponsorship?   │ No                            │
└─────────────────────────────┴──────────────────────────────┘
```

Page 2 — Resume Upload
```
┌─────────────────────────────┬──────────────────────────────┐
│ Field                       │ Value / Action               │
├─────────────────────────────┼──────────────────────────────┤
│ Upload Resume               │ Use file: [filename.docx]    │
│                             │ Located at: [path]           │
│ Upload Cover Letter         │ Use file: [filename.docx]    │
│                             │ Located at: [path]           │
└─────────────────────────────┴──────────────────────────────┘
```

Page 3 — Additional Information
```
┌─────────────────────────────┬──────────────────────────────┐
│ Question                    │ Answer                       │
├─────────────────────────────┼──────────────────────────────┤
│ [question 1]                │ [answer]                     │
│ [question 2]                │ [answer]                     │
└─────────────────────────────┴──────────────────────────────┘
```

Page 4 — Voluntary Disclosures
```
┌─────────────────────────────┬──────────────────────────────┐
│ Field                       │ Selection                    │
├─────────────────────────────┼──────────────────────────────┤
│ Gender                      │ Prefer not to say            │
│ Veteran status              │ No                           │
│ Disability                  │ Prefer not to say            │
│ Race/Ethnicity              │ Prefer not to say            │
└─────────────────────────────┴──────────────────────────────┘
```

Page 5 — Review & Submit
```
→ Review all entries
→ Check consent box
→ Click SUBMIT
→ Screenshot confirmation
```

### 4. File Bundle
```
Files to transfer to phone:
├── 01_Resume_[Company]_[Role].docx
├── 02_CoverLetter_[Company]_[Role].docx
└── 03_Submission_Blueprint.md (this file)
```

### 5. Post-Submit
```
After submit:
1. Screenshot confirmation page
2. Tell me: SUBMITTED [company] (or I detect from your message)
3. I will:
   → UPDATE data/pipeline/PIPELINE.md: transition to ✅ SUBMITTED
   → WRITE to data/jobs.json: mark as applied
   → SIGNAL networking-cadence: start T+0 timer
4. T+0 = today → networking auto-starts
```

---

## Phone Workflow (step-by-step for user)

```
1. Open the URL on your phone browser
2. Keep this guide open (split screen or second device)
3. Fill each field as mapped above
4. Upload files (download from git/OneDrive to phone first)
5. Submit
6. Screenshot confirmation
7. Tell me: SUBMITTED [company]
```

---

## Edge Cases

| Situation | Response |
|-----------|----------|
| Field label differs slightly | Use closest match — ATS fields are standardized |
| File won't upload on phone | Convert to PDF in browser (Google Docs) |
| Page layout different from mapping | Fill what matches, skip what doesn't |
| Application requires account creation | Create account with gmail, tell me after |
| Redirects to different ATS | Pause, tell me the URL, I'll remap |

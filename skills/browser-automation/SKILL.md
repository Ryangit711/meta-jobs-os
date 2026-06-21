---
name: browser-automation
description: "Launched when user says AUTO-APPLY or BROWSER. Auto-detects phone mode (Termux/Android/no Chrome) and falls back to MANUAL SUBMIT mode — generates exact field-by-field submission blueprint. Never blocks on device constraints."
triggers:
  - "AUTO-APPLY [company]"
  - "AUTO-APPLY --all"
  - "AUTO-APPLY [company] --manual"
  - "MANUAL-SUBMIT [company]"
  - "BROWSER [command]"
source: "github.com/browser-use/browser-use"
---

## Capability

Uses browser-use AI agent to control a real browser — navigate, click, type, fill forms, extract data, submit applications.

## Key Use Cases for ABHIMANYU

### 1. AUTO-APPLY [company]
Navigate to the company's career page, find the job posting, fill in the application form with Aman's profile data, upload resume DOCX, and submit.

**Process:**
1. Verify job URL is still active (200 check)
2. Open career page via browser-use agent
3. Agent reads the form fields and maps them to Aman's profile:
   - Name → `[NAME]`
   - Email → `[EMAIL]`
   - Phone → `[PHONE]`
   - Resume upload → path to generated DOCX
   - Cover letter → paste from SHOOT output
   - Additional questions → answered from Master Corpus
4. Preview filled form (user approves)
5. Submit
6. Log to `data/jobs.json` (if not exists → create: `{"applied":{}, "excluded":[], "last_updated": "YYYY-MM-DD"}`)
7. SIGNAL pipeline-tracker: transition [company] [role] to ✅ SUBMITTED
8. WRITE to `data/pipeline/PIPELINE.md`: update stage to ✅, set T+0 = today
9. DISPLAY: "✅ [company] submitted. Networking cadence running."

### 2. FETCH Enhancement
When webfetch returns blank/truncated for a JS-heavy career page (Lever, Ashby, Workday, HiringCafe), fall back to browser-use:
```
browser-use navigate <career-page-url>
browser-use extract job-listings
```

### 3. JD Extraction
For any job posting URL, extract full structured text:
```
browser-use navigate <job-url>
browser-use extract job-description
```

### 4. ATS Detection
Navigate to company career page, detect which ATS platform they use (Greenhouse, Lever, Workday, etc.):
```
browser-use navigate <careers-url>
browser-use detect-ats-platform
```

## CLI Usage

```bash
# Basic navigation
browser-use open https://example.com

# Interact with page
browser-use state                    # See clickable elements
browser-use click 5                  # Click element by index
browser-use type "Hello"             # Type text
browser-use fill "name" "Aman"       # Fill form field

# Extract data
browser-use screenshot page.png
browser-use extract job-description

# Tab management
browser-use tab list
browser-use tab new <url>
browser-use tab select <targetId>
browser-use tab close
```

## Phone Mode / Manual Fallback

When browser-use is unavailable (Termux, Android, no Chrome), AUTO-APPLY auto-detects and switches to manual-submit mode:

### Auto-Detection
```
if uname contains "android" or "termux" → PHONE_MODE=true
if which google-chrome OR which chromium returns empty → PHONE_MODE=true
if node -e "require('playwright')" throws → PHONE_MODE=true
```

### Behavior in Phone Mode
`AUTO-APPLY [company]` generates:
1. `03_Submission_Blueprint_[Company].md` — exact field-by-field mapping
2. Resume + cover letter files (same as always)
3. Step-by-step phone submission workflow
4. Post-submit instructions (SUBMITTED [company])

Manual override: `AUTO-APPLY [company] --manual` forces manual mode even on desktop.

## Integration Notes

- Requires `pip install browser-use` or `browser-use[core]`
- Works with logged-in Chrome for authenticated career sites
- Cloud version available for CAPTCHA solving and proxy rotation
- Phone mode: no dependencies needed — pure markdown blueprint generation
- All automated submissions must be user-approved before actual submit

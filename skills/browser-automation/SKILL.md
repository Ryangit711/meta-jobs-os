---
name: browser-automation
description: "Launched when user says AUTO-APPLY, BROWSER, or auto-triggered during FETCH/SHOOT for JS-heavy sites that webfetch can't handle."
triggers:
  - "AUTO-APPLY [company]"
  - "AUTO-APPLY --all"
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
6. Log to `data/jobs.json`

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

## Integration Notes

- Requires `pip install browser-use` or `browser-use[core]`
- Works with logged-in Chrome for authenticated career sites
- Cloud version available for CAPTCHA solving and proxy rotation
- All automated submissions must be user-approved before actual submit

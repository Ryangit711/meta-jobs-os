---
name: linkedin-automation
description: "Launched when user says LINKEDIN, or for automating LinkedIn networking tasks via OpenCLI. Also handles LinkedIn Profile Audit — checks profile alignment with application narrative before every SHOOT."
triggers:
  - "LINKEDIN [command]"
  - "LINKEDIN CONNECT [name]"
  - "LINKEDIN INBOX"
  - "LINKEDIN SEARCH [query]"
  - "LINKEDIN JOB-DETAIL [url]"
  - "OPTIMIZE LINKEDIN [company]"
source: "github.com/jackwender/OpenCLI"
---

## Capability

Uses OpenCLI's browser bridge to control your logged-in Chrome session — LinkedIn actions via CLI, no manual browser needed.

## Key Use Cases for ABHIMANYU

### 1. LINKEDIN CONNECT [name/title]
Send connection requests to hiring managers, recruiters, peers — automatically with DNA-tailored notes:
```
opencli linkedin connect "Jane Doe" --note "Admired your work on [company]'s growth strategy. Would love to connect."
```

### 2. LINKEDIN INBOX
Read LinkedIn messages — check for recruiter responses, interview invitations:
```
opencli linkedin inbox --limit 10
```

### 3. LINKEDIN SEARCH [query]
Search LinkedIn for jobs matching specific criteria:
```
opencli linkedin search "Director of Operations Vancouver" --limit 20
```

### 4. LINKEDIN JOB-DETAIL [url]
Extract full job posting details from a LinkedIn job URL:
```
opencli linkedin job-detail "https://linkedin.com/jobs/view/..."
```

### 5. LINKEDIN SAFE-SEND
Send safe, professional messages through LinkedIn:
```
opencli linkedin safe-send --recipient "Jane Doe" --message "..."
```

### 6. LINKEDIN SALESNAV
For Sales Navigator users — advanced search and lead discovery:
```
opencli linkedin salesnav-search --filters "location=Vancouver,function=Operations"
```

### 7. LINKEDIN POST-ANALYTICS
Track engagement on LinkedIn posts:
```
opencli linkedin post-analytics --post-url "..."
```

## Networking Cadence Integration

OpenCLI LinkedIn automation directly supports the networking cadence from `skills/networking-cadence/SKILL.md`:

| Cadence Step | OpenCLI Command |
|-------------|-----------------|
| T+0: Connect + note | `LINKEDIN CONNECT [name] --note "[DNA note]"` |
| T+3: Follow-up | `LINKEDIN SAFE-SEND --recipient [name] --message "[follow-up]"` |
| T+7: Value-add | `LINKEDIN SAFE-SEND --recipient [name] --message "[article/insight]"` |
| T+14: Final | `LINKEDIN SAFE-SEND --recipient [name] --message "[final check-in]"` |

## Setup

1. Install OpenCLI: `npm install -g @jackwener/opencli`
2. Install Browser Bridge extension from Chrome Web Store
3. Run `opencli doctor` to verify setup
4. Logged into LinkedIn in your Chrome — OpenCLI uses your session

## Available Commands

```
opencli linkedin connect     — Send connection request with note
opencli linkedin inbox       — Read LinkedIn messages
opencli linkedin job-detail  — Extract job posting details
opencli linkedin jobs-preferences — View/set job preferences
opencli linkedin post-analytics  — Track post engagement
opencli linkedin posts       — View your posts
opencli linkedin profile-experience — View profile experience
opencli linkedin profile-read — Read a profile
opencli linkedin safe-send   — Send safe message
opencli linkedin search      — Search LinkedIn
opencli linkedin salesnav-search — Sales Navigator search
opencli linkedin salesnav-inbox — Sales Navigator inbox
opencli linkedin salesnav-message — Sales Navigator messages
opencli linkedin sent-invitations — View sent invitations
opencli linkedin thread-snapshot — View message thread
opencli linkedin timeline    — View timeline
```

## LinkedIn Profile Audit (Run Before Every SHOOT)

**Purpose:** Recruiters check LinkedIn before calling. If your profile tells a different story than your resume, you lose trust before you start. This audit ensures alignment.

### Audit Checklist (Generate Before SHOOT Output)

```
For the target company [company] and role [role]:

1. HEADLINE alignment:
   → Current headline: [current]
   → SHOOT headline: [from resume/cover]
   → ❌ MISMATCH if they differ → fix headline

2. ABOUT section alignment:
   → Does the About section lead with the same narrative as the Professional Summary?
   → ❌ If not → rewrite to match resume summary

3. EXPERIENCE alignment:
   → Do job titles match the masquerade from the resume?
   → Do date ranges match?
   → Do descriptions use the same keywords as resume ATS section?
   → ❌ MISMATCH if any differ

4. SKILLS alignment:
   → Are the top 3 skills the same as the resume's Core Competencies?
   → ❌ If not → reorder skills to match

5. RECOMMENDATIONS:
   → Do any recommendations contradict the current narrative?
   → ❌ If so → hide or archive problematic recommendations

6. ACTIVITY:
   → Is the recent activity appropriate for a professional currently seeking?
   → ❌ If not → advise user to clean up

7. COMPANY-FOCUSED OPTIMIZATION:
   → Does the profile contain keywords from the target company's DNA?
   → ❌ If not → add relevant keywords to About + Skills

8. OPEN TO WORK:
   → Is "Open to Work" set correctly? (visible to recruiters only, not public?)
   → ❌ If public → advise setting to recruiters-only
```

### Output
```
╔══════════════════════════════════════════════════════════════════════════╗
║  LINKEDIN PROFILE AUDIT — [company]                                   ║
║  ✅ Headline aligned: [current headline]                              ║
║  ❌ About section needs rewrite → suggest new text                    ║
║  ✅ Experience titles aligned                                          ║
║  ❌ Skills need reorder → put [keyword] first                         ║
║  ✅ Recommendations fine                                               ║
║  ✅ Recent activity appropriate                                        ║
║  🛠 Action needed: Rewrite About section + reorder skills             ║
╚══════════════════════════════════════════════════════════════════════════╝
```

User applies changes via LinkedIn UI or says `LINKEDIN APPLY-AUDIT` to apply via OpenCLI.

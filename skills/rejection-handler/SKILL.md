---
name: rejection-handler
description: "Triggered when user says 'rejected', 'didn't get it', or shares a rejection email. Executes the Rejection → Opportunity protocol — reply gracefully, learn from it, auto-replace the role."
---

# REJECTION HANDLER — Opportunity Protocol

## Source Truth Anchors
- Rejection recovery: `10_REJECTION_RECOVERY.md` (JOBS-OS)
- Constitutional amendments from batch distill (Amendment #20 sections A-L)

## Protocol

### Step 1: Acknowledge
- Validate the feeling briefly. One sentence. Then move to action.

### Step 2: Reply Gracefully (Within 48h)
- Thank them for their time and consideration
- Express continued interest in the company
- Ask to be kept in mind for future opportunities
- Professional, warm, zero resentment

**Script template:**
```
Subject: [Role] — [NAME]

Dear [Recruiter Name],

Thank you for letting me know. I appreciate the time your team spent reviewing my application.

While this particular role didn't work out, I remain genuinely interested in [Company Name] and the work you're doing. If there are other roles where my background in [key domain] could be valuable, I'd welcome the opportunity to be considered.

Please keep me in mind as your hiring needs evolve.

Best regards,
[NAME]
```

### Step 3: Log the Learning
- Log cause in `data/jobs.json` (ATS? Fit? Screen? Format?)
- Update fit databases — never make same mistake twice
- Self-Learning Loop (Constitutional Amendment #5): every result makes system smarter

### Step 4: Auto-Replace (Within Same Day)
- Mark role as REJECTED in tracking
- Pull next best job from current date's unculled pool
- Show for approval
- SHOOT same-day replacement

### Step 5: Psychological Reset
- Rejection is data, not judgment
- Most careers die because people talk themselves out of trying, not from lack of talent
- The right role is still out there — the system just eliminated a wrong fit
- Re-enter the FETCH → SHOOT → YES → REPEAT cycle

## Why This Works
Hiring plans change constantly at every company:
- Chosen candidates reject offers (30-40% rate)
- New hires leave within 90 days
- Budgets open up for additional positions
- Different departments need similar skills
- The person who replied to the rejection gracefully gets the call when these happen

---
name: social-distill
description: "Triggered by DISTILL command variants: DISTILL INSTAGRAM, DISTILL REDDIT, DISTILL LINKEDIN. Harvests intelligence from social sources to augment FETCH and SHOOT with salary data, interview intel, cultural reviews, and people discovery."
---

# SOCIAL DISTILL — Intelligence Layer

## Source Truth Anchors
- Social Distill architecture: `40_SOCIAL_DISTILL.md` (JOBS-OS)
- Instagram: `INSTAGRAM_DISTILL.py` (JOBS-OS)
- Reddit: `REDDIT_DISTILL.py` (JOBS-OS)
- LinkedIn: `LINKEDIN_DISTILL.py` (JOBS-OS)

## Layer 1: Instagram Distill
- Scrapes ONLY authenticated user's saved posts (never followers, feed, stories, DMs)
- Text-only: captions, comments, hashtags, mentions. No images.
- Audio transcription for video/reel posts via SpeechRecognition
- OCR for image text via OCR.space
- Categories: salary, interview, resume, networking, career advice, company review, negotiation
- Credentials in `secrets.json` (gitignored)

**Commands:**
- `DISTILL INSTAGRAM` — Scrape saved posts
- `DISTILL INSTAGRAM --search [term]` — Search existing distill
- `DISTILL INSTAGRAM --report` — Generate curated reference

## Layer 2: Reddit Distill
- Uses `old.reddit.com` with requests + BeautifulSoup — no API key needed
- Searches 8+ subreddits: cscareerquestions, sales, consulting, jobs, careerguidance, askamanager, salary, interviewpreparations
- Rate-limited: 1 req/2 seconds
- Cached in `data/social_distill/reddit_*.json`

**Commands:**
- `DISTILL REDDIT [company]` — Full intel scrape
- `DISTILL REDDIT [company] --salary` — Salary data only
- `DISTILL REDDIT [company] --interview` — Interview prep
- `DISTILL REDDIT [company] --culture` — Culture reviews

## Layer 3: LinkedIn Distill
- Uses Apify actors for structured data extraction
- Job cross-verification via LinkedIn Job Scraper
- People discovery (recruiters, HMs, team members) via LinkedIn People Scraper
- Apify API key in `secrets.json`

**Commands:**
- `DISTILL LINKEDIN [company]` — Cross-verify + people discovery
- `DISTILL LINKEDIN [company] --jobs` — Job verification only
- `DISTILL LINKEDIN [company] --people` — People discovery only

## Integration
- All layers feed INTO SHOOT generation
- Intel from Instagram scripts + Reddit salary data + LinkedIn people discovery + Contact Engine emails converge in every 13-section package
- All scraped data is local-only, never committed, never pushed

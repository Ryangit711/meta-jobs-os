#!/usr/bin/env python3
"""
Phase 4b — Deep Company Scan
ABHIMANYU 2.0 Modular Skill Architecture

Scrapes ALL open roles from target company career pages using crawl4ai.
Discovers roles that job boards miss. Flags companies with 2+ fitting roles.
Builds on top of existing system. Zero core changes.

Usage:
    python deep_scan.py                          # Scan all pipes
    python deep_scan.py --pipe C                 # Scan consulting only
    python deep_scan.py --company Deloitte       # Scan one company
    python deep_scan.py --pipe C --company EY    # Combine filters
    python deep_scan.py --format json            # JSON output only
    python deep_scan.py --output-dir ./results   # Custom output dir
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path


# ─── Config ───────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
DEFAULT_CONFIG = SCRIPT_DIR / "deep_scan_config.json"


def load_config(path=None):
    path = path or DEFAULT_CONFIG
    with open(path) as f:
        return json.load(f)


CONFIG = load_config()


# ─── Logging ──────────────────────────────────────────────────────────────

class Logger:
    def __init__(self):
        self.lines = []
        self.errors = []

    def info(self, msg):
        self.lines.append(f"[INFO] {msg}")
        print(msg)

    def warn(self, msg):
        self.lines.append(f"[WARN] {msg}")
        print(f"  ⚠  {msg}")

    def error(self, msg):
        self.lines.append(f"[ERROR] {msg}")
        self.errors.append(msg)
        print(f"  ✖  {msg}")

    def success(self, msg):
        self.lines.append(f"[OK] {msg}")
        print(f"  ✔  {msg}")

    def result(self, msg):
        self.lines.append(f"[RESULT] {msg}")
        print(f"     {msg}")


logger = Logger()


# ─── Scoring Engine ──────────────────────────────────────────────────────

def load_master_keywords(config):
    """Load scoring keywords from config."""
    kw = config.get("scoring", {})
    title_kw = [k.lower() for k in kw.get("title_keywords", [])]
    exclude_kw = [k.lower() for k in kw.get("exclude_keywords", [])]
    weight_boost = [k.lower() for k in kw.get("weight_boost", [])]
    blocked_locs = [l.lower() for l in kw.get("fit_filters", {}).get("blocked_locations", [])]
    allowed_locs = [l.lower() for l in kw.get("fit_filters", {}).get("allowed_locations", [])]
    return title_kw, exclude_kw, weight_boost, allowed_locs, blocked_locs


INCLUDE_KW, EXCLUDE_KW, BOOST_KW, ALLOWED_LOCS, BLOCKED_LOCS = load_master_keywords(CONFIG)


def score_job(title, location, company):
    """Score a job listing against Master Corpus keywords. Returns (fit_pct, passes_filters)."""
    title_lower = (title or "").lower()
    location_lower = (location or "").lower()
    company_lower = (company or "").lower()

    match_count = sum(1 for kw in INCLUDE_KW if kw in title_lower)
    exclude_match = any(kw in title_lower for kw in EXCLUDE_KW)

    if exclude_match:
        return 0, False

    # Base score from keyword matches (max 70%)
    max_kw = len(INCLUDE_KW)
    base = min(match_count / max(max_kw * 0.15, 1), 0.70) * 100

    # Location bonus (max 20%)
    loc_bonus = 0
    if any(loc in location_lower for loc in ALLOWED_LOCS):
        loc_bonus = 20
    elif any(loc in company_lower for loc in ["telus", "lululemon", "shopify", "amazon", "clio", "1password"]):
        loc_bonus = 10

    # Blocked location penalty
    if any(bl in location_lower for bl in BLOCKED_LOCS):
        if not any(al in location_lower for al in ["remote", "vancouver"]):
            return 0, False

    # Boost keywords (max +10%)
    boost = 0
    if match_count >= 2:
        boost = min(sum(1 for kw in BOOST_KW if kw in title_lower or kw in company_lower or kw in location_lower), 10)

    fit = min(base + loc_bonus + boost, 100)

    passes_filters = fit >= 25  # Low bar for discovery — pipe will filter further
    return round(fit), passes_filters


# ─── Job Parsing ─────────────────────────────────────────────────────────

def extract_jobs_from_markdown(markdown_text, company_name, source_url):
    """Extract job listings from career page markdown using pattern matching.
    
    Works with most career page formats. Returns list of dicts.
    """
    if not markdown_text or len(markdown_text.strip()) < 50:
        return []

    jobs = []
    lines = markdown_text.split("\n")

    # Patterns that indicate a job listing line
    job_patterns = [
        # "Job Title — Location" or "Job Title | Location"
        re.compile(r'^\s*[-*]\s*(.+?)\s*[—–\-|]\s*(.+)$'),
        # Links containing /jobs/ or /careers/ with text
        re.compile(r'\[(.+?)\]\(.*?(?:/jobs/|/careers/|/job/|/position/).*?\)'),
        # Simple bullet that looks like a job title
        re.compile(r'^\s*[-*]\s+(.+?)$'),
    ]

    # First pass: look for links to job pages
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Skip navigation/UI text
        if any(skip in stripped.lower() for skip in ["search", "filter", "sort by", "page", "loading",
                                                       "sign in", "log in", "register", "cookie",
                                                       "privacy", "terms", "©", "all rights"]):
            continue

        # Try each pattern
        for pat in job_patterns:
            m = pat.match(stripped)
            if m:
                title = m.group(1).strip()
                loc = m.group(2).strip() if m.lastindex >= 2 else ""
                jobs.append({
                    "title": title,
                    "location": loc,
                    "company": company_name,
                    "url": source_url,
                })
                break

    # Second pass: dedup by title (fuzzy)
    seen = set()
    deduped = []
    for job in jobs:
        key = job["title"].lower().strip()
        if key and key not in seen:
            seen.add(key)
            # Filter out non-job entries
            if len(key) > 5 and not any(skip in key for skip in
                                         ["home", "about", "contact", "search", "view all",
                                          "join our", "careers", "our values", "life at",
                                          "benefits", "culture", "diversity", "apply now"]):
                deduped.append(job)

    return deduped


# ─── Crawl4AI Integration ────────────────────────────────────────────────

def check_crawl4ai():
    """Verify crawl4ai is installed. Returns True if ready."""
    try:
        import crawl4ai
        return True
    except ImportError:
        return False


async def scrape_career_page(url, company_name, retries=2):
    """Scrape a career page using crawl4ai with stealth.
    
    Returns the markdown content, or None on failure.
    """
    try:
        from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
    except ImportError:
        logger.error(f"crawl4ai not installed. Run: pip install -r requirements.txt")
        return None

    browser_config = BrowserConfig(
        headless=True,
        enable_stealth=True,
        user_agent_mode="random",
    )

    run_config = CrawlerRunConfig(
        magic=True,
        simulate_user=True,
        word_count_threshold=10,
        excluded_tags=["nav", "footer", "header", "script", "style"],
        wait_until="networkidle",
        page_timeout=60000,
    )

    for attempt in range(retries + 1):
        try:
            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(url=url, config=run_config)
                if result.success and result.markdown:
                    return result.markdown
                else:
                    logger.warn(f"{company_name}: crawl returned no content (attempt {attempt + 1})")
        except Exception as e:
            logger.warn(f"{company_name}: crawl failed (attempt {attempt + 1}): {e}")
            if attempt < retries:
                await asyncio.sleep(2)
            else:
                logger.error(f"{company_name}: all {retries + 1} attempts failed")

    return None


# ─── Company Scanner ─────────────────────────────────────────────────────

async def scan_company(company, pipe_label):
    """Scan a single company's career page. Returns scan result dict."""
    name = company["name"]
    url = company["url"]
    slug = company.get("slug", name.lower().replace(" ", "_"))

    logger.info(f"\n{'─' * 50}")
    logger.info(f"Scanning {name} ({pipe_label})")
    logger.info(f"  URL: {url}")

    # Scrape
    markdown = await scrape_career_page(url, name, retries=CONFIG.get("retry_count", 2))

    if not markdown:
        return {
            "company": name,
            "pipe": pipe_label,
            "slug": slug,
            "url": url,
            "status": "failed",
            "jobs": [],
            "fitting_jobs": [],
            "error": "Scrape returned no content",
        }

    # Extract jobs
    raw_jobs = extract_jobs_from_markdown(markdown, name, url)
    logger.result(f"  Found {len(raw_jobs)} raw job listings")

    # Score and filter
    scored_jobs = []
    fitting_jobs = []
    for job in raw_jobs:
        fit, passes = score_job(job["title"], job["location"], name)
        job["fit_score"] = fit
        job["passes_filters"] = passes
        scored_jobs.append(job)
        if passes:
            fitting_jobs.append(job)

    # Sort by fit score desc
    scored_jobs.sort(key=lambda x: x["fit_score"], reverse=True)

    if fitting_jobs:
        logger.success(f"  → {len(fitting_jobs)} fitting role(s) found")
        for j in fitting_jobs:
            logger.result(f"    {j['fit_score']:2d}%  {j['title']}  —  {j['location'] or 'N/A'}")
    else:
        logger.warn(f"  No fitting roles found")

    return {
        "company": name,
        "pipe": pipe_label,
        "slug": slug,
        "url": url,
        "status": "scraped",
        "jobs": scored_jobs,
        "fitting_jobs": fitting_jobs,
        "job_count": len(raw_jobs),
        "fitting_count": len(fitting_jobs),
        "error": None,
    }


async def scan_pipe(pipe_key, pipe_config):
    """Scan all companies in a pipe. Returns aggregate result."""
    pipe_label = pipe_config.get("label", pipe_key)
    logger.info(f"\n{'=' * 55}")
    logger.info(f"  {pipe_label} ({pipe_key} PIPE)")
    logger.info(f"{'=' * 55}")

    companies = pipe_config.get("companies", [])
    if not companies:
        logger.warn(f"No companies configured for {pipe_key}")
        return {"pipe": pipe_key, "label": pipe_label, "results": []}

    results = []
    for company in companies:
        result = await scan_company(company, pipe_label)
        results.append(result)

    return {"pipe": pipe_key, "label": pipe_label, "results": results}


# ─── Output Generation ──────────────────────────────────────────────────

def generate_markdown(all_results, output_dir):
    """Generate readable markdown output with per-company + summary sections."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Deep Company Scan — {timestamp}",
        "",
        f"Auto-generated by Phase 4b Deep Scanner (crawl4ai)",
        "",
    ]

    total_fitting = 0
    hot_companies = []

    for pipe_result in all_results:
        pipe_label = pipe_result["label"]
        lines.append(f"## {pipe_label} ({pipe_result['pipe']} PIPE)")
        lines.append("")

        for r in pipe_result["results"]:
            if r["status"] == "failed":
                lines.append(f"### {r['company']}")
                lines.append(f"- Status: ❌ Failed — {r.get('error', 'Unknown error')}")
                lines.append(f"- URL: {r['url']}")
                lines.append("")
                continue

            lines.append(f"### {r['company']} ({r['pipe']})")
            lines.append(f"- Status: ✅ Scraped")
            lines.append(f"- Total jobs found: {r['job_count']}")
            lines.append(f"- Fitting roles: {r['fitting_count']}")
            lines.append(f"- URL: {r['url']}")
            lines.append("")

            if r["fitting_jobs"]:
                lines.append("| # | Role | Location | Fit % |")
                lines.append("|---|------|----------|:-----:|")
                for i, j in enumerate(r["fitting_jobs"], 1):
                    loc = j.get("location", "N/A") or "N/A"
                    lines.append(f"| {i} | {j['title']} | {loc} | {j['fit_score']}% |")
                lines.append("")

                total_fitting += r["fitting_count"]
                if r["fitting_count"] >= 2:
                    r["hot"] = True
                    hot_companies.append(r)
            else:
                lines.append("No matching roles found.")
                lines.append("")

    # Hot companies summary
    if hot_companies:
        lines.append("---")
        lines.append("## 🔥 HOT COMPANIES (2+ Fitting Roles — Priority Boost)")
        lines.append("")
        for r in hot_companies:
            roles = ", ".join(f"{j['title']} ({j['fit_score']}%)" for j in r["fitting_jobs"])
            boost = "+3%" if r["fitting_count"] == 2 else "+5%"
            lines.append(f"- **{r['company']}** ({r['pipe']}) — {r['fitting_count']} roles — Priority boost: {boost}")
            lines.append(f"  {roles}")
        lines.append("")

    # Summary
    lines.append("---")
    lines.append("## Summary")
    lines.append("")
    scanned = sum(1 for pr in all_results for r in pr["results"] if r["status"] == "scraped")
    failed = sum(1 for pr in all_results for r in pr["results"] if r["status"] == "failed")
    lines.append(f"- Companies scanned: {scanned}")
    lines.append(f"- Companies failed: {failed}")
    lines.append(f"- Total fitting roles discovered: {total_fitting}")
    lines.append(f"- Hot companies flagged: {len(hot_companies)}")

    output = "\n".join(lines)

    # Write
    scan_file = output_dir / f"deep_scan_{timestamp[:10]}.md"
    with open(scan_file, "w") as f:
        f.write(output)
    logger.success(f"Written: {scan_file}")

    return str(scan_file)


def generate_json(all_results, output_dir):
    """Generate JSON output for programmatic consumption by pipeline."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    output = {
        "scan_timestamp": timestamp,
        "config": {
            "master_corpus": CONFIG.get("master_corpus_path"),
            "score_keywords_count": len(INCLUDE_KW),
        },
        "results": {},
        "hot_companies": [],
        "summary": {
            "total_companies_scanned": 0,
            "total_companies_failed": 0,
            "total_jobs_found": 0,
            "total_fitting_jobs": 0,
            "hot_companies_count": 0,
        },
    }

    for pipe_result in all_results:
        pipe_key = pipe_result["pipe"]
        output["results"][pipe_key] = []
        for r in pipe_result["results"]:
            entry = {
                "company": r["company"],
                "pipe": r["pipe"],
                "url": r["url"],
                "slug": r["slug"],
                "status": r["status"],
                "error": r.get("error"),
                "job_count": r.get("job_count", 0),
                "fitting_count": r.get("fitting_count", 0),
                "jobs": r.get("jobs", []),
                "fitting_jobs": r.get("fitting_jobs", []),
            }
            output["results"][pipe_key].append(entry)

            if r["status"] == "scraped":
                output["summary"]["total_companies_scanned"] += 1
                output["summary"]["total_jobs_found"] += r.get("job_count", 0)
                output["summary"]["total_fitting_jobs"] += r.get("fitting_count", 0)
            else:
                output["summary"]["total_companies_failed"] += 1

            if r.get("fitting_count", 0) >= 2:
                output["hot_companies"].append({
                    "company": r["company"],
                    "pipe": r["pipe"],
                    "fitting_count": r["fitting_count"],
                    "priority_boost": "+3%" if r["fitting_count"] == 2 else "+5%",
                    "roles": [j["title"] for j in r.get("fitting_jobs", [])],
                })

    output["summary"]["hot_companies_count"] = len(output["hot_companies"])

    json_file = output_dir / f"deep_scan_{timestamp[:10]}.json"
    with open(json_file, "w") as f:
        json.dump(output, f, indent=2, default=str)
    logger.success(f"Written: {json_file}")

    return str(json_file)


def generate_curated_injection(all_results):
    """Generate a CURATED_30.md injection snippet for fitting jobs.
    
    This can be manually appended to the CURATED_30.md file or
    referenced during the FETCH process.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"## Deep Scan Results — {timestamp} (Phase 4b Auto-Scanner)",
        "",
        "| Pipe | Company | Role | Fit % | Location |",
        "|:----:|:--------|:-----|:-----:|:---------|",
    ]

    for pipe_result in all_results:
        for r in pipe_result["results"]:
            for j in r.get("fitting_jobs", []):
                loc = j.get("location", "N/A") or "N/A"
                fit = j.get("fit_score", 0)
                lines.append(f"| {r['pipe']} | {r['company']} | {j['title']} | {fit}% | {loc} |")

    # Hot companies section
    hot = [r for pr in all_results for r in pr["results"] if r.get("fitting_count", 0) >= 2]
    if hot:
        lines.append("")
        lines.append("### 🔥 Priority Boost Companies")
        for r in hot:
            boost = "+3%" if r["fitting_count"] == 2 else "+5%"
            roles = "; ".join(j["title"] for j in r["fitting_jobs"])
            lines.append(f"- **{r['company']}** ({r['pipe']}): {roles} — Boost: {boost}")

    return "\n".join(lines)


# ─── Main ───────────────────────────────────────────────────────────────

def parse_args():
    parser = argparse.ArgumentParser(
        description="Phase 4b Deep Company Scan — crawl4ai career page scraper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deep_scan.py                          # Scan all configured companies
  python deep_scan.py --pipe C                 # Consulting pipe only
  python deep_scan.py --company Deloitte       # Single company
  python deep_scan.py --format json            # JSON output only
  python deep_scan.py --output-dir ./out       # Custom output directory
        """,
    )
    parser.add_argument("--pipe", choices=["C", "T", "I", "S"],
                        help="Scan only this pipe")
    parser.add_argument("--company", type=str,
                        help="Scan only this company (by name, case-insensitive partial match)")
    parser.add_argument("--output-dir", type=str,
                        help=f"Output directory (default: ./deep_scan_output/)")
    parser.add_argument("--format", choices=["markdown", "json", "both"], default="both",
                        help="Output format (default: both)")
    parser.add_argument("--config", type=str,
                        help=f"Path to config JSON (default: {DEFAULT_CONFIG})")
    return parser.parse_args()


async def main():
    args = parse_args()

    # Load config
    config_path = args.config or DEFAULT_CONFIG
    if not os.path.exists(config_path):
        print(f"Error: Config not found at {config_path}")
        sys.exit(1)
    global CONFIG, INCLUDE_KW, EXCLUDE_KW, BOOST_KW, ALLOWED_LOCS, BLOCKED_LOCS
    CONFIG = load_config(config_path)
    INCLUDE_KW, EXCLUDE_KW, BOOST_KW, ALLOWED_LOCS, BLOCKED_LOCS = load_master_keywords(CONFIG)

    # Verify crawl4ai
    if not check_crawl4ai():
        print("\n  crawl4ai is not installed.")
        print("  Run the following commands:")
        print(f"    pip install -r {SCRIPT_DIR / 'requirements.txt'}")
        print("    python -m playwright install chromium")
        print()
        sys.exit(1)

    # Setup output directory
    output_dir = Path(args.output_dir) if args.output_dir else Path(CONFIG.get("output_dir", "deep_scan_output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Phase 4b — Deep Company Scan                              ║")
    print("║  Scrapes ALL open roles from target career pages           ║")
    print("║  Using: crawl4ai (stealth browser + JS rendering)          ║")
    print(f"║  Date:  {datetime.now().strftime('%Y-%m-%d %H:%M')}                    ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    # Filter pipes
    pipes_config = CONFIG.get("pipes", {})
    if args.pipe:
        if args.pipe not in pipes_config:
            print(f"Error: Pipe '{args.pipe}' not found in config")
            sys.exit(1)
        pipes_to_scan = [(args.pipe, pipes_config[args.pipe])]
    else:
        pipes_to_scan = list(pipes_config.items())

    # Filter company within pipes
    if args.company:
        company_lower = args.company.lower()
        filtered = []
        for pipe_key, pipe_cfg in pipes_to_scan:
            matching = [c for c in pipe_cfg.get("companies", []) if company_lower in c["name"].lower()]
            if matching:
                filtered.append((pipe_key, {**pipe_cfg, "companies": matching}))
        pipes_to_scan = filtered
        if not pipes_to_scan:
            print(f"Error: Company '{args.company}' not found in any pipe")
            sys.exit(1)

    # Run scans
    all_results = []
    start_time = time.time()
    for pipe_key, pipe_cfg in pipes_to_scan:
        result = await scan_pipe(pipe_key, pipe_cfg)
        all_results.append(result)

    elapsed = time.time() - start_time

    # Output
    print()
    print("─" * 55)
    print("  GENERATING OUTPUTS")
    print("─" * 55)
    print()

    md_file = None
    json_file = None

    if args.format in ("markdown", "both"):
        md_file = generate_markdown(all_results, output_dir)

    if args.format in ("json", "both"):
        json_file = generate_json(all_results, output_dir)

    # CURATED injection
    curated_snippet = generate_curated_injection(all_results)
    curated_path = output_dir / "curated_injection.md"
    with open(curated_path, "w") as f:
        f.write(curated_snippet + "\n")
    logger.success(f"Written: {curated_path}")

    # Console summary
    total_fitting = sum(r["fitting_count"] for pr in all_results for r in pr["results"])
    total_scanned = sum(1 for pr in all_results for r in pr["results"] if r["status"] == "scraped")
    total_failed = sum(1 for pr in all_results for r in pr["results"] if r["status"] == "failed")

    hot = [r for pr in all_results for r in pr["results"] if r.get("fitting_count", 0) >= 2]

    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  SCAN COMPLETE                                              ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print(f"║  Companies scanned:  {total_scanned}")
    print(f"║  Companies failed:   {total_failed}")
    print(f"║  Fitting roles:      {total_fitting}")
    print(f"║  Hot companies:      {len(hot)}")
    print(f"║  Time:               {elapsed:.1f}s")
    if md_file:
        print(f"║  Markdown:           {md_file}")
    if json_file:
        print(f"║  JSON:               {json_file}")
    print(f"║  CURATED snippet:    {curated_path}")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    # Fire list
    if hot:
        print("🔥 HOT COMPANIES TO TARGET:")
        for r in hot:
            boost = "+3%" if r["fitting_count"] == 2 else "+5%"
            print(f"  • {r['company']} ({r['pipe']}) — {r['fitting_count']} roles — Priority {boost}")
        print()


# ─── Entry Point ────────────────────────────────────────────────────────

if __name__ == "__main__":
    asyncio.run(main())

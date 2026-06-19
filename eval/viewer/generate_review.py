#!/usr/bin/env python3
"""eval viewer — generates self-contained HTML review page for eval results.

Usage:
    python3 eval/viewer/generate_review.py eval/suite/resume-writer.json results/resume-writer/

Generates eval/viewer/output/review.html — open in browser to review.
"""
import json, os, sys, datetime

def generate_review(suite_path, results_dir):
    with open(suite_path) as f: suite = json.load(f)
    skill_name = suite.get("skill", "unknown")

    results = {}
    if os.path.exists(results_dir):
        for fname in os.listdir(results_dir):
            if fname.endswith(".json"):
                with open(os.path.join(results_dir, fname)) as f:
                    test_id = fname.replace(".json", "")
                    results[test_id] = json.load(f)

    html = f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><title>Eval Review — {skill_name}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 960px; margin: 40px auto; padding: 0 20px; background: #0a0a0a; color: #e0e0e0; }}
h1 {{ border-bottom: 2px solid #d4a574; padding-bottom: 10px; }}
.pass {{ color: #4caf50; }} .fail {{ color: #f44336; }}
.test {{ background: #1a1a1a; border-radius: 8px; padding: 16px; margin: 16px 0; }}
.assertion {{ padding: 8px; margin: 4px 0; border-left: 3px solid #333; }}
.assertion.pass {{ border-left-color: #4caf50; }}
.assertion.fail {{ border-left-color: #f44336; }}
.summary {{ font-size: 1.2em; margin: 16px 0; }}
pre {{ background: #111; padding: 12px; border-radius: 4px; overflow-x: auto; }}
</style></head><body>
<h1>Eval Review — {skill_name}</h1>
<p>Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
<div class="summary">"""
    total_assertions = 0
    total_passed = 0
    for test in suite.get("tests", []):
        tid = test["id"]
        r = results.get(tid, {})
        test_assertions = r.get("assertions", test.get("assertions", []))
        passed = sum(1 for a in test_assertions if a.get("passed"))
        total_test = len(test_assertions)
        total_assertions += total_test
        total_passed += passed
        html += f'<div class="test"><h3>{tid}: {test["prompt"][:80]}...</h3>'
        html += f'<div class="summary">Passed: {passed}/{total_test}</div>'
        for a in test_assertions:
            cls = "pass" if a.get("passed") else "fail"
            html += f'<div class="assertion {cls}">{a["id"]}: {"✅ PASS" if a.get("passed") else "❌ FAIL"} — {a.get("evidence", "no evidence")}</div>'
        html += '</div>'

    pct = (total_passed / total_assertions * 100) if total_assertions else 0
    html += f'</div><div class="summary" style="font-size:1.4em;text-align:center;">Overall: {total_passed}/{total_assertions} ({pct:.0f}%)</div>'
    html += '</body></html>'

    outdir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "review.html")
    with open(outpath, "w") as f: f.write(html)
    print(f"[OK] Review page: {outpath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_review.py <suite.json> [results-dir]")
        sys.exit(1)
    suite_path = sys.argv[1]
    results_dir = sys.argv[2] if len(sys.argv) > 2 else f"results/{os.path.basename(suite_path).replace('.json','')}"
    generate_review(suite_path, results_dir)

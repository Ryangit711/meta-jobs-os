# EVAL INFRASTRUCTURE — Prove Every Improvement

Skills enable a superpower the original JOBS-OS doesn't have: **objective measurement of whether changes actually help.**

## Architecture

```
eval/
├── README.md              ← This file
├── suite/                 ← Test prompts + assertions per skill
│   ├── fetch-engine.json
│   ├── shoot-deployer.json
│   ├── resume-writer.json
│   ├── cover-letter-writer.json
│   ├── dna-extraction.json
│   └── ...
├── agents/                ← Sub-agent instructions for grading
│   ├── grader.md           ← Evaluates assertions against outputs
│   ├── comparator.md       ← Blind A/B comparison
│   └── analyzer.md         ← Post-hoc analysis
└── viewer/
    └── generate_review.py  ← Generate HTML review page
```

## Eval Suite Schema (per skill)

Each `eval/suite/[skill].json` contains:
```json
{
  "skill": "resume-writer",
  "tests": [
    {
      "id": "rw-001",
      "prompt": "Generate a resume for Clio's Revenue Operations Manager role",
      "assertions": [
        { "id": "a1", "type": "contains", "value": "Revenue Operations", "weight": 1 },
        { "id": "a2", "type": "keyword_density", "min": 0.02, "max": 0.04, "weight": 2 },
        { "id": "a3", "type": "not_contains", "value": "work permit|PR|immigration", "weight": 3 },
        { "id": "a4", "type": "length_max", "value": 1, "unit": "page", "weight": 2 },
        { "id": "a5", "type": "contains", "value": "[NAME]|[PHONE]|[EMAIL]|[LINKEDIN]", "weight": 3 }
      ]
    }
  ]
}
```

## How to Run an Eval

1. Write test prompts + assertions in `eval/suite/[skill].json`
2. Run skill on each prompt → get output
3. Run grader agent on each output against assertions → pass/fail per assertion
4. Aggregate: `pass_rate = total_passed / total_assertions`
5. For A/B: run baseline version too, compare pass rates
6. If improvement → keep new version. If regression → revert.

## Grader Agent (agents/grader.md)
Takes: (skill instructions, test prompt, AI output, assertions)
Returns: grading.json with pass/fail per assertion + evidence

## Comparator Agent (agents/comparator.md)
Takes: (same prompt, output_A, output_B)
Returns: blind preference + reasons (without knowing which is which)

## Analyzer Agent (agents/analyzer.md)
Takes: (history of improvements, pass rates deltas)
Returns: patterns — what kinds of changes consistently improve outcomes

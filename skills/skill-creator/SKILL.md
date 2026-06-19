---
name: skill-creator
description: "Triggered when user says 'create a new skill', 'improve this skill', 'test this skill', 'run evals', or wants to iterate on an existing skill. Follows the full skill creation cycle: capture intent → interview → write → test → eval → improve."
---

# SKILL CREATOR — Meta-Skill for Building Skills

## Source Truth Anchors
- Pattern source: anthropics/skills skill-creator

## Creation Cycle

### Phase 1: Capture Intent
1. What should this skill enable?
2. When should it trigger? (user phrases/context)
3. Expected output format?
4. Test case requirements?

### Phase 2: Interview & Research
- Proactively ask about edge cases, input/output formats, success criteria
- Research similar patterns in existing skills
- Check available reference files

### Phase 3: Write SKILL.md
- YAML frontmatter: `name`, `description` (trigger description), `license`
- Body: Overview, Protocol/Steps, Examples, References

### Phase 4: Create Test Prompts
- Write `eval/suite/[skill-name].json` with test prompts + assertions
- Each assertion should be objectively gradable (pass/fail)

### Phase 5: Run Evaluation
- Copy baseline version if exists (for A/B comparison)
- Run with-skill and baseline in parallel (sub-agents)
- Grade assertions against both outputs
- Aggregate pass rates

### Phase 6: Improve
- Based on eval failures → rewrite skill
- Repeat Phase 5-6 until satisfactory

### Phase 7: Package
- Validate SKILL.md frontmatter
- Package as .skill zip if needed
- Register in SKILL_REGISTRY.md

## Eval Suite Commands
- `python3 eval/viewer/generate_review.py` — Launch HTML review viewer
- `run_loop.py` — Full eval + improve loop
- `aggregate_benchmark.py` — Stats across runs
- `quick_validate.py` — Validate SKILL.md frontmatter

## Style Rules for Skills
- Short title + overview sentence at top
- Progressive disclosure (most important info first)
- Show good examples and bad examples
- Reference source files explicitly
- Include "what NOT to do" sections
- Code examples with actual file paths
- Trigger description optimized for accuracy (not length)

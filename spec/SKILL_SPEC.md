# Agent Skills Specification

The canonical specification for the Agent Skills standard is at:
## https://agentskills.io/specification

## Quick Reference

### SKILL.md Frontmatter Fields
| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique kebab-case identifier (e.g., `resume-writer`) |
| `description` | Yes | Trigger description — when and why to load this skill |
| `license` | No | Licensing terms if applicable |

### Skill Structure
A skill is a folder containing at minimum a `SKILL.md` file. Additional files can include:
- `scripts/` — Executable utilities referenced by the skill
- `templates/` — Template files for outputs
- `reference/` — Reference documentation
- `examples/` — Example inputs/outputs
- `agents/` — Sub-agent instructions

### Skill Loading
Skills are loaded dynamically based on trigger matching:
1. User prompt is analyzed for trigger phrases
2. Matching skills are identified from their `description` field
3. Relevant SKILL.md contents are injected into context
4. Multiple skills can be loaded simultaneously (composability)

### Best Practices
- Each skill does ONE thing well (narrow scope)
- Descriptions optimized for trigger accuracy, not length
- Progressive disclosure: important info first
- Show good and bad examples
- Cross-reference source files explicitly

# Skill Authoring Guide

## Minimum files

Each skill should include:

- `SKILL.md`: the required Claude Code skill file

## Required `SKILL.md` format

Use YAML frontmatter at the top of the file:

```md
---
name: my-skill
description: Explain what the skill does and when to use it.
---
```

Only use `name` and `description` in frontmatter.

## Recommended body sections

1. `## Triggers`
2. `## Workflow`
3. `## Rules`
4. `## References`
5. `## Examples`
6. `## Output`

## Naming guidance

- Use lowercase kebab-case for folder names
- Keep names specific to the job the skill performs
- Prefer verbs or clear job titles, such as `release-helper` or `security-auditor`

## Versioning

Skills do not need a separate metadata version file in this repository format.

Track revisions with git history or release tags.

## Validation

- Validate all skills: `python scripts/validate_skill.py skills`
- Validate one skill: `python scripts/validate_skill.py skills/<skill-name>`

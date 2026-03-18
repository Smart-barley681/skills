# Contributing

Thanks for contributing!

## What belongs in this repo

- New skills under `skills/<skill-name>/` (must include `SKILL.md`)
- Improvements to templates in `skills/_template/`
- Documentation in `docs/`
- Utilities in `scripts/` that improve scaffolding/validation

## Skill requirements

- `skills/<skill-name>/SKILL.md` must have YAML frontmatter with only:
  - `name`
  - `description`
- `name` must match the folder name and be lowercase kebab-case
- Keep `SKILL.md` concise and procedural

## Local checks

Validate all skills:

```bash
python scripts/validate_skill.py skills
```

Validate a single skill:

```bash
python scripts/validate_skill.py skills/<skill-name>
```

## Pull requests

- Keep changes focused (one skill / one improvement per PR when possible)
- Update docs when behavior changes
- If you add scripts, prefer standard library only (or document dependencies clearly)

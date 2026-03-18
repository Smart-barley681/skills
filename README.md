# Agent Skills 🧰

English | [中文](README.zh-CN.md)

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

## Available Skills ✨

### random-image-placeholder

Generate stable or random image placeholder URLs (and optionally download them) using [Lorem Picsum](https://picsum.photos/).

**Use when:**

- Building UI mockups / docs / demos that need images without hosting assets
- You need reproducible images for tests/snapshots (use `seed`)
- The user mentions picsum, placeholder images, grayscale, blur, seed, id

**Examples:**

```bash
python skills/random-image-placeholder/scripts/picsum.py url --seed avatar-42 --width 400 --height 400 --grayscale --blur 2
```

```bash
python skills/random-image-placeholder/scripts/picsum.py download --seed avatar-42 --width 120 --height 80 --out ./tmp/picsum_test.jpg
```

Docs:

- `skills/random-image-placeholder/README.md`
- `skills/random-image-placeholder/SKILL.md`

## Installation

This repo supports two common installation paths:

1. **Use directly from source**: clone the repo and use the skill files/scripts under `skills/`
2. **Use packaged `.skill` artifacts**: import a `.skill` file produced under `dist/` (or from your GitHub Releases, if you publish them)

Package a skill locally:

```bash
python scripts/package_skill.py skills/random-image-placeholder
```

## Usage

Skills are automatically available once installed/imported (depending on your editor/agent). If a skill includes helper scripts, run them directly when a deterministic result is needed.

## Skill Structure

Each skill contains:

- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)
- `assets/` - Bundled assets (optional)

## License

MIT. See [LICENSE](LICENSE).

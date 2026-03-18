# Agent Skills 🧰

English | [中文](README.zh-CN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Built for Agents](https://img.shields.io/badge/Built%20for-AI%20Agents-blue)
![Maintained](https://img.shields.io/badge/Maintained-yes-success)
![GitHub stars](https://img.shields.io/github/stars/hicoldcat/skills?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/hicoldcat/skills)

A collection of skills for AI coding agents.

> 🚀 Open source, practical, and easy to extend.

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

## Installation 📦

Clone this repo and use the skill files/scripts directly under `skills/`.

## Usage 🧪

Skills are automatically available once installed/imported (depending on your editor/agent). If a skill includes helper scripts, run them directly when a deterministic result is needed.

## Skill Structure 🗂️

Each skill contains:

- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)
- `assets/` - Bundled assets (optional)

## License 📄

MIT. See [LICENSE](LICENSE).

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def iter_skill_dirs(skills_root: Path) -> list[Path]:
    dirs: list[Path] = []
    for item in sorted(skills_root.iterdir()):
        if not item.is_dir():
            continue
        if item.name == "_template":
            continue
        if (item / "SKILL.md").exists():
            dirs.append(item)
    return dirs


def main() -> int:
    if len(sys.argv) not in {1, 2}:
        print("Usage: python scripts/package_all_skills.py [output-dir]")
        return 1

    repo_root = Path(__file__).resolve().parent.parent
    skills_root = repo_root / "skills"
    output_dir = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else repo_root / "dist"

    if not skills_root.exists():
        print(f"skills/ not found at: {skills_root}")
        return 1

    skill_dirs = iter_skill_dirs(skills_root)
    if not skill_dirs:
        print(f"No skills found under: {skills_root}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    packager = repo_root / "scripts" / "package_skill.py"

    failures: list[str] = []
    for skill_dir in skill_dirs:
        result = subprocess.run([sys.executable, str(packager), str(skill_dir), str(output_dir)])
        if result.returncode != 0:
            failures.append(skill_dir.name)

    if failures:
        print("\nPackaging failed for:\n- " + "\n- ".join(failures))
        return 1

    print(f"\nPackaged {len(skill_dirs)} skill(s) to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


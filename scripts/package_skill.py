from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("Usage: python scripts/package_skill.py <skill-dir> [output-dir]")
        return 1

    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    skill_dir = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else repo_root / "dist"

    if not skill_dir.exists() or not skill_dir.is_dir():
        print(f"Skill directory not found: {skill_dir}")
        return 1

    validator = repo_root / "scripts" / "validate_skill.py"
    result = subprocess.run([sys.executable, str(validator), str(skill_dir)])
    if result.returncode != 0:
        return result.returncode

    output_dir.mkdir(parents=True, exist_ok=True)
    archive_base = output_dir / skill_dir.name
    archive_path = shutil.make_archive(str(archive_base), "zip", root_dir=skill_dir.parent, base_dir=skill_dir.name)
    skill_path = output_dir / f"{skill_dir.name}.skill"

    if skill_path.exists():
        skill_path.unlink()

    Path(archive_path).replace(skill_path)
    print(f"Packaged skill: {skill_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

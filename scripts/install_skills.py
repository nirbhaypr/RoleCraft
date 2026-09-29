#!/usr/bin/env python3
"""Copy selected RoleCraft skills into a local skills directory without overwriting."""

import argparse
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
IGNORED = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
AGENT_DIRECTORIES = {"codex": ".agents", "claude": ".claude"}


def default_destination(agent):
    return Path.home() / AGENT_DIRECTORIES[agent] / "skills"


def available_skills(root=ROOT):
    return {path.parent.name: path.parent for path in sorted(root.glob("*/SKILL.md"))}


def install(names, destination, *, root=ROOT, dry_run=False):
    """Preflight the whole selection, then copy; roll back owned output on failure."""
    available = available_skills(root)
    selected = list(dict.fromkeys(names))
    if not selected:
        raise ValueError("Select at least one skill or use --all")
    unknown = sorted(set(selected) - available.keys())
    if unknown:
        raise ValueError("Unknown skills: " + ", ".join(unknown))
    destination = Path(destination).expanduser().resolve()
    if destination.exists() and not destination.is_dir():
        raise ValueError(f"Destination is not a directory: {destination}")
    license_path = root / "LICENSE"
    if not license_path.is_file():
        raise ValueError("Repository LICENSE is missing")
    targets = []
    for name in selected:
        source = available[name]
        if source.is_symlink() or any(path.is_symlink() for path in source.rglob("*")):
            raise ValueError(f"Refusing a skill containing symlinks: {name}")
        if destination == source.resolve() or source.resolve() in destination.parents:
            raise ValueError("Destination cannot be inside a source skill")
        target = destination / name
        if target.exists() or target.is_symlink():
            raise ValueError(f"Already exists: {target}. Back up and move it before reinstalling.")
        targets.append(target)
    if dry_run:
        return targets

    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        with tempfile.TemporaryDirectory(prefix=".rolecraft-install-", dir=destination) as staging:
            for name in selected:
                staged = Path(staging) / name
                shutil.copytree(available[name], staged, ignore=IGNORED)
                shutil.copy2(license_path, staged / "LICENSE")
            for target in targets:
                target.mkdir()  # Exclusive creation also catches post-preflight collisions.
                created.append(target)
                shutil.copytree(Path(staging) / target.name, target, dirs_exist_ok=True)
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills", nargs="*", help="Skill folder names")
    parser.add_argument("--all", action="store_true", help="Install all skills in this checkout")
    parser.add_argument("--agent", choices=sorted(AGENT_DIRECTORIES), default="codex",
                        help="Personal install location (default: codex)")
    parser.add_argument("--dest", type=Path, help="Explicit directory; overrides --agent for any compatible host")
    parser.add_argument("--dry-run", action="store_true", help="Check and show destinations without writing")
    args = parser.parse_args()
    if args.all and args.skills:
        parser.error("Choose skill names or --all, not both")
    try:
        names = list(available_skills()) if args.all else args.skills
        targets = install(names, args.dest or default_destination(args.agent), dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    for target in targets:
        print(f"{'Would install' if args.dry_run else 'Installed'}: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

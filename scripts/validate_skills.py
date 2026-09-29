#!/usr/bin/env python3
"""Validate skill metadata, discovery prompts, and relative Markdown file links."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def load_yaml(text, label, errors):
    try:
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            raise ValueError("expected a mapping")
        return data
    except (yaml.YAMLError, ValueError) as error:
        errors.append(f"{label}: invalid YAML ({error})")
        return {}


def validate_skill(directory):
    errors = []
    path = directory / "SKILL.md"
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        return [f"{path}: missing YAML frontmatter"]
    metadata = load_yaml(match[1], path, errors)
    portable_fields = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    unsupported = metadata.keys() - portable_fields
    if unsupported:
        errors.append(f"{path}: nonportable frontmatter fields: {', '.join(sorted(unsupported))}")
    name = metadata.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append(f"{path}: name must be lowercase hyphenated text, at most 64 characters")
    elif name != directory.name:
        errors.append(f"{path}: name must match its folder")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(f"{path}: description must contain 1–1024 characters")
    if re.search(r"\[TODO:.*?\]", content):
        errors.append(f"{path}: unfinished scaffold placeholder")

    ui_path = directory / "agents" / "openai.yaml"
    if not ui_path.is_file():
        return errors  # Codex UI metadata is optional; the skill is portable without it.
    ui = load_yaml(ui_path.read_text(encoding="utf-8"), ui_path, errors)
    interface = ui.get("interface", {})
    if not isinstance(interface, dict):
        return errors + [f"{ui_path}: interface must be a mapping"]
    for field in ("display_name", "short_description", "default_prompt"):
        if not isinstance(interface.get(field), str) or not interface[field].strip():
            errors.append(f"{ui_path}: missing or empty {field}")
    short = interface.get("short_description", "")
    if isinstance(short, str) and not 25 <= len(short) <= 64:
        errors.append(f"{ui_path}: short_description must contain 25–64 characters")
    prompt = interface.get("default_prompt", "")
    if isinstance(prompt, str) and re.findall(r"\$([a-z0-9-]+)", prompt) != [name]:
        errors.append(f"{ui_path}: default_prompt must invoke exactly ${name}")
    return errors


def prose_lines(content):
    """Skip fenced code examples when checking Markdown links."""
    fence = None
    for line in content.splitlines():
        marker = re.match(r"\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield line


def validate_links(path, root):
    errors = []
    for line in prose_lines(path.read_text(encoding="utf-8")):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
            target = target.strip().split(' "', 1)[0].strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"{path}: missing or external local link {target}")
    return errors


def validate_repository(root):
    skills = sorted(root.glob("*/SKILL.md"))
    errors = []
    if not skills:
        errors.append(f"{root}: no skills found")
    for skill in skills:
        errors.extend(validate_skill(skill.parent))
    docs = list(root.glob("*.md"))
    for skill in skills:
        docs.extend(skill.parent.rglob("*.md"))
    for folder in ("docs", ".github"):
        docs.extend((root / folder).rglob("*.md"))
    for doc in docs:
        errors.extend(validate_links(doc, root))
    return len(skills), errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    count, errors = validate_repository(args.root.resolve())
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Validated {count} skills: metadata, invocation prompts, and relative file links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

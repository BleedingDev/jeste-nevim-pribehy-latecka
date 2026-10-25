#!/usr/bin/env python3
"""Materialize Obsidian #Text scene transclusions into portable Markdown."""
import argparse
import re
from pathlib import Path

EMBED = re.compile(r"!\[\[([^\]\n]+)\]\]")
FRONT = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)


def without_frontmatter(text):
    return FRONT.sub("", text, count=1)


def scene_text(text, path):
    text = without_frontmatter(text)
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if re.match(r"^## Text\s*$", line.rstrip())]
    if len(starts) != 1:
        raise ValueError(f"{path}: expected exactly one '## Text', found {len(starts)}")
    start = starts[0] + 1
    end = next((i for i in range(start, len(lines)) if re.match(r"^#{1,2}\s+", lines[i])), len(lines))
    return "".join(lines[start:end]).strip("\n")


def resolve_scene(target, manuscript, root):
    if "#" not in target or target.rsplit("#", 1)[1] != "Text":
        raise ValueError(f"unsupported embed: ![[{target}]] (expected #Text)")
    name = target.rsplit("#", 1)[0].split("|", 1)[0]
    if not name or Path(name).is_absolute() or ".." in Path(name).parts:
        raise ValueError(f"unsafe or empty scene path: {name}")
    candidates = []
    for base in (manuscript.parent, root):
        p = base / name
        if p.suffix.lower() != ".md":
            p = p.with_suffix(".md")
        if p.is_file() and p.resolve() not in candidates:
            candidates.append(p.resolve())
    if not candidates and "/" not in name:
        candidates = list(root.rglob(name + ".md"))
    if len(candidates) != 1:
        raise ValueError(f"scene {name!r}: expected one match, found {len(candidates)}")
    if not candidates[0].is_relative_to(root.resolve()):
        raise ValueError(f"scene outside vault: {name}")
    return candidates[0]


def export(manuscript, root):
    source = without_frontmatter(manuscript.read_text(encoding="utf-8"))
    def replace(match):
        path = resolve_scene(match.group(1), manuscript, root)
        return scene_text(path.read_text(encoding="utf-8"), path)
    return EMBED.sub(replace, source).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    try:
        if args.output.resolve() == args.manuscript.resolve():
            raise ValueError("output must not overwrite manuscript")
        result = export(args.manuscript.resolve(), args.root.resolve())
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Export failed: {exc}\n")


if __name__ == "__main__":
    main()

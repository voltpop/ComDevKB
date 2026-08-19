#!/usr/bin/env python3
"""Stamp last_modified: <today> into changed Markdown files' frontmatter.

Only touches files that already have a --- frontmatter block; leaves
compiled: and everything else in the block untouched. Adds
last_modified: if it's missing, updates it in place if it's already
there. Files with no frontmatter (README.md, AGENTS.md, KB-Skills.md)
are left alone entirely.

Usage: update_frontmatter.py <file> [<file> ...]
Prints one line per file actually changed; exits 0 either way.
"""
import re
import sys
from datetime import datetime, timezone

FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)
LAST_MODIFIED_RE = re.compile(r"^last_modified:.*$", re.MULTILINE)


def stamp(path, today):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    match = FRONTMATTER_RE.match(content)
    if not match:
        return False  # no frontmatter block — not one of ours, leave it alone

    fm_body = match.group(1)
    new_line = f"last_modified: {today}"

    if LAST_MODIFIED_RE.search(fm_body):
        new_fm_body = LAST_MODIFIED_RE.sub(new_line, fm_body)
    else:
        new_fm_body = fm_body + new_line + "\n"

    if new_fm_body == fm_body:
        return False  # already stamped with today's date

    new_content = "---\n" + new_fm_body + "---\n" + content[match.end():]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    paths = sys.argv[1:]
    if not paths:
        return
    today = datetime.now(timezone.utc).date().isoformat()
    for path in paths:
        try:
            if stamp(path, today):
                print(f"stamped {path}")
        except FileNotFoundError:
            continue  # file was deleted in this diff


if __name__ == "__main__":
    main()

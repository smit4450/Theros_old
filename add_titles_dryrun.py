"""Dry-run version — reports what would change without writing anything."""

import os
import re

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "content")
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

stats = {"would_update": 0, "skipped_has_title": 0, "skipped_no_heading": 0, "skipped_no_frontmatter": 0}

for root, dirs, files in os.walk(CONTENT_DIR):
    dirs[:] = [d for d in dirs if d != ".obsidian"]
    for fname in files:
        if not fname.endswith(".md"):
            continue
        filepath = os.path.join(root, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.startswith("---"):
            stats["skipped_no_frontmatter"] += 1
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            stats["skipped_no_frontmatter"] += 1
            continue
        frontmatter = parts[1]
        body = parts[2]
        if re.search(r"^title\s*:", frontmatter, re.MULTILINE):
            stats["skipped_has_title"] += 1
            continue
        match = HEADING_RE.search(body)
        if not match:
            stats["skipped_no_heading"] += 1
            continue
        title = match.group(1).strip()
        rel = os.path.relpath(filepath, CONTENT_DIR)
        if stats["would_update"] < 20:
            print(f"  {rel}  ->  title: {title}")
        stats["would_update"] += 1

print(f"\nSummary:")
print(f"  Would update:         {stats['would_update']}")
print(f"  Skipped (has title):  {stats['skipped_has_title']}")
print(f"  Skipped (no heading): {stats['skipped_no_heading']}")
print(f"  Skipped (no frontmatter): {stats['skipped_no_frontmatter']}")

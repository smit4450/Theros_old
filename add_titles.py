"""
Adds a 'title' frontmatter property to every markdown file under content/.
The title is extracted from the first '# ' (h1) heading found in the file body.

- If the file already has a 'title' property, it is skipped.
- If no h1 heading is found, the file is skipped.
- Frontmatter is expected between --- delimiters at the top of the file.
"""

import os
import re

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "content")

HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

stats = {"updated": 0, "skipped_has_title": 0, "skipped_no_heading": 0, "skipped_no_frontmatter": 0}

for root, dirs, files in os.walk(CONTENT_DIR):
    # Skip .obsidian metadata
    dirs[:] = [d for d in dirs if d != ".obsidian"]

    for fname in files:
        if not fname.endswith(".md"):
            continue

        filepath = os.path.join(root, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # Must start with frontmatter
        if not text.startswith("---"):
            stats["skipped_no_frontmatter"] += 1
            continue

        # Split on the closing --- of frontmatter
        parts = text.split("---", 2)
        if len(parts) < 3:
            stats["skipped_no_frontmatter"] += 1
            continue

        frontmatter = parts[1]
        body = parts[2]

        # Check if title already exists in frontmatter
        if re.search(r"^title\s*:", frontmatter, re.MULTILINE):
            stats["skipped_has_title"] += 1
            continue

        # Find the first h1 heading in the body
        match = HEADING_RE.search(body)
        if not match:
            stats["skipped_no_heading"] += 1
            continue

        title = match.group(1).strip()

        # Escape quotes if needed for YAML; wrap in quotes if it contains special chars
        if any(c in title for c in (':', '"', "'", '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', '%', '@', '`')):
            escaped = title.replace('"', '\\"')
            title_line = f'title: "{escaped}"'
        else:
            title_line = f"title: {title}"

        # Insert title as the first property in the frontmatter
        new_frontmatter = "\n" + title_line + frontmatter

        new_text = "---" + new_frontmatter + "---" + body

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_text)

        stats["updated"] += 1

print(f"Done!")
print(f"  Updated:              {stats['updated']}")
print(f"  Skipped (has title):  {stats['skipped_has_title']}")
print(f"  Skipped (no heading): {stats['skipped_no_heading']}")
print(f"  Skipped (no frontmatter): {stats['skipped_no_frontmatter']}")

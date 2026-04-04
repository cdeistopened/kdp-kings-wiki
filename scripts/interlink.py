#!/usr/bin/env python3
"""
Interlink KDP Kings Wiki — add [[wiki-links]] for first occurrence of known entities.

Scans all markdown files in site/content/. For each file, finds mentions of known
page titles (frameworks, skills) and wraps the FIRST unlinked occurrence
in a [[slug|display text]] wiki link.

Rules:
- Only links the first occurrence per page
- Skips text already inside wiki links [[...]]
- Skips text inside markdown links [text](url)
- Skips text inside headings (# lines)
- Skips text inside frontmatter (--- blocks)
- Skips text inside code blocks (``` blocks)
- Skips self-references (don't link a page to itself)
- Longer titles match first (prevents partial matches)
- Frameworks are highest priority (most useful links)
"""

import os
import re
import yaml
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "site" / "content"

# Directories to scan for linkable pages
LINKABLE_DIRS = ["frameworks", "skills"]

# Directories to process (add links into)
PROCESS_DIRS = ["frameworks", "skills"]

def extract_titles(content_dir: Path) -> dict[str, tuple[str, str]]:
    """Build map of display_title -> (slug, folder) for all linkable pages.

    Priority: frameworks > skills (frameworks links are most useful).
    When the same title exists in multiple folders, frameworks/ wins.

    For frameworks/: slug is filename stem (e.g., "30-day-launch-sequence")
    For skills/: slug is directory name (e.g., "launch-sequence")
    """
    titles = {}

    # Process frameworks first (higher priority)
    frameworks_dir = content_dir / "frameworks"
    if frameworks_dir.exists():
        for md_file in frameworks_dir.glob("*.md"):
            slug = md_file.stem

            # Read frontmatter
            text = md_file.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue

            end = text.find("---", 3)
            if end == -1:
                continue

            try:
                fm = yaml.safe_load(text[3:end])
            except yaml.YAMLError:
                continue

            if not fm:
                continue

            # Get title from frontmatter 'name' field
            title = fm.get("name") or fm.get("title")
            if not title:
                continue

            title = title.strip()
            titles[title] = (slug, "frameworks")

            # For long titles with colons, also register the short version
            if ":" in title:
                short = title.split(":")[0].strip()
                if len(short) > 3 and short not in titles:
                    titles[short] = (slug, "frameworks")

    # Process skills next (lower priority, won't overwrite frameworks)
    skills_dir = content_dir / "skills"
    if skills_dir.exists():
        for skill_subdir in sorted(skills_dir.iterdir()):
            if not skill_subdir.is_dir():
                continue

            skill_md = skill_subdir / "SKILL.md"
            if not skill_md.exists():
                continue

            slug = skill_subdir.name

            # Read frontmatter
            text = skill_md.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue

            end = text.find("---", 3)
            if end == -1:
                continue

            try:
                fm = yaml.safe_load(text[3:end])
            except yaml.YAMLError:
                continue

            if not fm:
                continue

            # Get title from frontmatter 'name' field
            title = fm.get("name") or fm.get("title")
            if not title:
                continue

            title = title.strip()
            # Only add if not already claimed by frameworks
            if title not in titles:
                titles[title] = (slug, "skills")

    return titles


def is_in_protected_zone(text: str, match_start: int, match_end: int) -> bool:
    """Check if a match position is inside a protected zone (link, code, etc.)."""

    # Check if inside an existing wiki link [[...]]
    # Find the nearest [[ before the match
    before = text[:match_start]
    open_wiki = before.rfind("[[")
    close_wiki = before.rfind("]]")
    if open_wiki > close_wiki:
        # We're inside an unclosed [[
        return True

    # Check if inside a markdown link [text](url)
    # Look for [ before us that hasn't been closed with ](
    bracket_open = before.rfind("[")
    bracket_close = before.rfind("]")
    if bracket_open > bracket_close and bracket_open >= 0:
        return True

    # Check if inside a markdown link URL part ](url)
    paren_pattern = before.rfind("](")
    paren_close = before.rfind(")")
    if paren_pattern > paren_close and paren_pattern >= 0:
        return True

    # Check if inside inline code `...`
    backtick_count = before.count("`")
    if backtick_count % 2 == 1:
        return True

    return False


def is_heading_line(text: str, match_start: int) -> bool:
    """Check if the match is on a heading line."""
    line_start = text.rfind("\n", 0, match_start) + 1
    line = text[line_start:match_start].lstrip()
    return line.startswith("#")


def add_links(filepath: Path, titles: dict[str, tuple[str, str]], dry_run: bool = False) -> int:
    """Add wiki links to a single file. Returns count of links added."""
    text = filepath.read_text(encoding="utf-8")

    # Extract frontmatter
    if not text.startswith("---"):
        return 0

    fm_end = text.find("---", 3)
    if fm_end == -1:
        return 0

    fm_end += 3  # Include the closing ---
    frontmatter = text[:fm_end]
    body = text[fm_end:]

    # Get this file's own slug to avoid self-linking
    own_slug = filepath.stem

    # Split body into code blocks and non-code blocks
    # We only process non-code blocks
    code_block_pattern = re.compile(r'(```[\s\S]*?```)', re.MULTILINE)

    # Track which titles we've already linked in this file
    linked = set()

    # Sort titles by length (longest first) to prevent partial matches
    sorted_titles = sorted(titles.keys(), key=len, reverse=True)

    links_added = 0

    for title in sorted_titles:
        slug, folder = titles[title]

        # Skip self-references
        if slug == own_slug:
            continue

        # Skip if we already linked this slug
        if slug in linked:
            continue

        # Skip if this title is too short (risk of false positives)
        if len(title) < 4:
            continue

        # Build regex pattern — match whole words, case-sensitive
        # Escape regex special chars in title
        escaped = re.escape(title)
        pattern = re.compile(r'(?<!\[)(?<!\w)' + escaped + r'(?!\w)(?!\])', re.MULTILINE)

        # Find all matches in body
        for match in pattern.finditer(body):
            start = match.start()
            end = match.end()

            # Check protections
            if is_in_protected_zone(body, start, end):
                continue

            if is_heading_line(body, start):
                continue

            # Check if inside code block
            in_code = False
            for cb in code_block_pattern.finditer(body):
                if cb.start() <= start < cb.end():
                    in_code = True
                    break
            if in_code:
                continue

            # Check if the text right before is already a wiki link opener
            before_text = body[max(0, start-2):start]
            if "[[" in before_text:
                continue

            # Build the wiki link
            matched_text = match.group()
            # Use shortest-path resolution (Quartz CrawlLinks setting)
            link = f"[[{slug}|{matched_text}]]"

            # Replace only this first occurrence
            body = body[:start] + link + body[end:]
            linked.add(slug)
            links_added += 1
            break  # Only first occurrence

    if links_added > 0 and not dry_run:
        filepath.write_text(frontmatter + body, encoding="utf-8")

    return links_added


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Interlink KDP Kings Wiki pages")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be linked without changing files")
    parser.add_argument("--verbose", action="store_true", help="Show per-file details")
    args = parser.parse_args()

    print("Building title index...")
    titles = extract_titles(CONTENT_DIR)
    print(f"  Found {len(titles)} linkable titles")

    # Show breakdown
    frameworks = [(t, s) for t, (s, d) in titles.items() if d == "frameworks"]
    skills = [(t, s) for t, (s, d) in titles.items() if d == "skills"]
    print(f"  Frameworks: {len(frameworks)}, Skills: {len(skills)}")

    total_links = 0
    files_modified = 0

    # Process frameworks (flat markdown files)
    frameworks_dir = CONTENT_DIR / "frameworks"
    if frameworks_dir.exists():
        files = sorted(frameworks_dir.glob("*.md"))
        dir_links = 0

        for filepath in files:
            count = add_links(filepath, titles, dry_run=args.dry_run)
            if count > 0:
                dir_links += count
                files_modified += 1
                if args.verbose:
                    print(f"  {filepath.name}: +{count} links")

        total_links += dir_links
        print(f"\nframeworks/: {dir_links} links added across {len(files)} files")

    # Process skills (SKILL.md files in subdirectories)
    skills_dir = CONTENT_DIR / "skills"
    if skills_dir.exists():
        skill_dirs = sorted([d for d in skills_dir.iterdir() if d.is_dir()])
        dir_links = 0

        for skill_subdir in skill_dirs:
            skill_md = skill_subdir / "SKILL.md"
            if skill_md.exists():
                count = add_links(skill_md, titles, dry_run=args.dry_run)
                if count > 0:
                    dir_links += count
                    files_modified += 1
                    if args.verbose:
                        print(f"  {skill_subdir.name}/SKILL.md: +{count} links")

        total_links += dir_links
        print(f"\nskills/: {dir_links} links added across {len(skill_dirs)} skill files")

    mode = "would add" if args.dry_run else "added"
    print(f"\nTotal: {mode} {total_links} links in {files_modified} files")


if __name__ == "__main__":
    main()

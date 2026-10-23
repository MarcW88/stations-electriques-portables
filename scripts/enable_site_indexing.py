#!/usr/bin/env python3
"""Remove noindex from every public HTML page and source generators."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGES = [ROOT / "index.html", *ROOT.glob("*/index.html"), *ROOT.glob("*/*/index.html")]
SOURCE_FILES = [ROOT / name for name in (
    "_generate.py", "_generate_brands.py", "_generate_comparatifs.py",
    "_generate_guides.py", "_validate_brands.py", "_validate_comparatifs.py",
    "_validate_guides.py"
)]
ROBOT_META = re.compile(r"""(<meta\s+[^>]*name=["']robots["'][^>]*content=["'])([^"']+)(["'][^>]*>)""", re.I)
NOINDEX = re.compile(r'\bnoindex\b', re.I)

def update_page(path):
    content = path.read_text(encoding="utf-8")
    def clean(m):
        directives = [part.strip() for part in m.group(2).split(",")]
        directives = [part for part in directives if not NOINDEX.fullmatch(part) and part]
        if not any(part.lower() == "index" for part in directives):
            directives.insert(0, "index")
        if not any(part.lower() == "follow" for part in directives):
            directives.append("follow")
        return m.group(1) + ", ".join(dict.fromkeys(directives)) + m.group(3)
    result = ROBOT_META.sub(clean, content)
    if NOINDEX.search(result):
        raise ValueError(f"Remaining noindex directive in {path}")
    if result != content:
        path.write_text(result, encoding="utf-8")
        return True
    return False

def main():
    changed = []
    for page in sorted(set(PUBLIC_PAGES)):
        if page.is_file() and update_page(page):
            changed.append(str(page.relative_to(ROOT)))
    # Make regeneration and associated quality checks maintain indexability.
    for source in SOURCE_FILES:
        if not source.exists():
            continue
        content = source.read_text(encoding="utf-8")
        revised = content.replace("noindex, follow", "index, follow")
        if revised != content:
            source.write_text(revised, encoding="utf-8")
            changed.append(str(source.relative_to(ROOT)))
    pages = [p for p in set(PUBLIC_PAGES) if p.is_file()]
    failures = [str(p.relative_to(ROOT)) for p in pages if NOINDEX.search(p.read_text(encoding="utf-8"))]
    if failures:
        raise SystemExit("NOINDEX FOUND: " + ", ".join(failures))
    print(f"Checked {len(pages)} published pages; modified {len(changed)} files.")
    for item in changed:
        print("UPDATED", item)

if __name__ == "__main__":
    main()

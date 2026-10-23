#!/usr/bin/env python3
"""Install favicon reference on all public pages and in HTML generators."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK = '<link rel="icon" type="image/svg+xml" href="/favicon.svg">'
pages = sorted([ROOT / "index.html", *ROOT.glob("*/index.html"), *ROOT.glob("*/*/index.html")])
generators = [ROOT / x for x in ("_generate.py", "_generate_guides.py", "_generate_brands.py", "_generate_comparatifs.py")]
updated = []
for path in pages + generators:
    if not path.is_file():
        continue
    old = path.read_text(encoding="utf-8")
    if 'href="/favicon.svg"' in old:
        continue
    # Do not replace other icon declarations; install the site's primary favicon.
    if '<head>' not in old:
        continue
    new = old.replace('<head>', '<head>' + LINK, 1)
    if new != old:
        path.write_text(new, encoding="utf-8")
        updated.append(str(path.relative_to(ROOT)))
for path in pages:
    if path.is_file() and 'href="/favicon.svg"' not in path.read_text(encoding="utf-8"):
        raise SystemExit(f"Missing favicon link: {path.relative_to(ROOT)}")
print(f"Favicon linked: {len(pages)} pages, modified {len(updated)} files")
for name in updated:
    print("UPDATED", name)

#!/usr/bin/env python3
"""Remove the obsolete Accès rapide strip from public pages and generators."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r'<div class="quick-nav">\s*<div class="quick-nav-inner">\s*<span class="qn-label">Accès rapide</span>\s*<div class="qn-links">.*?</div>\s*</div>\s*</div>', re.DOTALL)
files = [p for p in ROOT.rglob('*.html') if '.agents' not in p.parts and '.github' not in p.parts]
files += [p for p in ROOT.glob('*.py')]
changed = []
for p in sorted(set(files)):
    source = p.read_text(encoding='utf-8')
    result, n = PATTERN.subn('', source)
    if n:
        p.write_text(result, encoding='utf-8')
        changed.append((str(p.relative_to(ROOT)), n))
for name, count in changed:
    print(f"UPDATED {name}: {count} quick-nav block(s)")
print(f"Removed {sum(n for _, n in changed)} blocks from {len(changed)} files")
remaining = [str(p.relative_to(ROOT)) for p in files if PATTERN.search(p.read_text(encoding='utf-8'))]
if remaining:
    raise SystemExit("Remaining quick-nav blocks: " + repr(remaining))

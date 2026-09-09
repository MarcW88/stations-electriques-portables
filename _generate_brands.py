#!/usr/bin/env python3
"""Apply researched brand hub content after the global shell generator."""
from pathlib import Path
import html as html_lib
import re

BASE = Path(__file__).resolve().parent
SOURCE_DIR = BASE / ".content" / "brand-pages"
UPDATED = "09/09/2026"

META_RE = re.compile(r"<!--\s*(title|description):\s*(.*?)\s*-->", re.I)
H2_RE = re.compile(r'<h2\s+id="([^"]+)"[^>]*>(.*?)</h2>', re.I | re.S)

def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html_lib.unescape(value)).strip()

def load_source(path: Path):
    raw = path.read_text(encoding="utf-8")
    meta = {k.lower(): v for k, v in META_RE.findall(raw)}
    body = META_RE.sub("", raw).strip()
    if "title" not in meta or "description" not in meta:
        raise ValueError(f"metadata title/description missing in {path}")
    return meta, body

def replace_once(pattern, repl, text, label):
    out, count = re.subn(pattern, repl, text, count=1, flags=re.I | re.S)
    if count != 1:
        raise ValueError(f"{label}: expected one replacement, got {count}")
    return out

def build_toc(body: str) -> str:
    links = []
    for anchor, title in H2_RE.findall(body):
        if "source" in clean_text(title).lower():
            continue
        links.append(f'<a href="#{anchor}">{clean_text(title)}</a>')
    return "".join(links)

def apply(slug: str, source: Path):
    target = BASE / "marques" / slug / "index.html"
    if not target.exists():
        raise FileNotFoundError(target)
    meta, body = load_source(source)
    page = target.read_text(encoding="utf-8")

    page = replace_once(r"<title>.*?</title>", f"<title>{meta['title']}</title>", page, f"{slug} title")
    safe_desc = html_lib.escape(meta["description"], quote=True)
    page = replace_once(r'<meta\s+name="description"\s+content="[^"]*">', f'<meta name="description" content="{safe_desc}">', page, f"{slug} meta")
    page = replace_once(r'(<section class="page-hero">.*?<h1[^>]*>).*?(</h1>)', rf"\g<1>{meta['title']}\2", page, f"{slug} h1")
    page = replace_once(r'(<section class="page-hero">.*?<p class="lead">).*?(</p>)', rf"\g<1>{meta['description']}\2", page, f"{slug} lead")
    page = re.sub(r"Vérifié\s*:\s*MM/AAAA", f"Vérifié : {UPDATED}", page, flags=re.I)
    page = re.sub(r"Vérifié\s*:\s*\d{2}/\d{2}/\d{4}", f"Vérifié : {UPDATED}", page, flags=re.I)

    article = f'<article class="content-main">\n<!-- BRAND_CONTENT_START -->\n{body}\n<!-- BRAND_CONTENT_END -->\n</article>'
    page = replace_once(r'<article class="content-main">.*?</article>', article, page, f"{slug} article")
    page = replace_once(r'(<nav class="toc-list">).*?(</nav>)', rf"\g<1>{build_toc(body)}\2", page, f"{slug} toc")

    if not re.search(r'name="robots"\s+content="noindex,\s*follow"', page, re.I):
        raise ValueError(f"{slug}: noindex, follow must be preserved")
    if "<!-- Contenu à rédiger -->" in page:
        raise ValueError(f"{slug}: placeholder remains")
    target.write_text(page, encoding="utf-8")
    print(f"generated {slug}")

def main():
    sources = sorted(SOURCE_DIR.glob("*.html"))
    if not sources:
        raise SystemExit("no brand content sources found")
    for source in sources:
        apply(source.stem, source)
    print(f"PASS: generated {len(sources)} brand hubs")

if __name__ == "__main__":
    main()

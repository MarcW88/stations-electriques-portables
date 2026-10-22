#!/usr/bin/env python3
"""Static and generated checks for the five reviewed /usages/ pages."""
from pathlib import Path
from html.parser import HTMLParser
import importlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ["camping", "van", "coupure-courant", "chantier", "cpap"]
MODULES = ["usage_camping_content", "usage_van_content",
           "usage_coupure_content", "usage_chantier_content", "usage_cpap_content"]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.toc = []
        self.h2 = []
        self.in_toc = False
        self.in_h2 = False
        self.meta = {}
        self.canonical = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and "name" in a:
            self.meta[a["name"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "nav" and "toc-list" in a.get("class", "").split():
            self.in_toc = True
        if tag == "h2":
            self.in_h2 = True
            self.h2.append(a.get("id"))
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
            if self.in_toc: self.toc.append(a["href"])
    def handle_endtag(self, tag):
        if tag == "nav" and self.in_toc:
            self.in_toc = False
        if tag == "h2":
            self.in_h2 = False

errors = []
for slug, module in zip(SLUGS, MODULES):
    path = ROOT / "usages" / ("station-electrique-" + slug) / "index.html"
    if not path.exists():
        errors.append(f"{slug}: HTML absent")
        continue
    html = path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    if "Contenu à rédiger" in html:
        errors.append(f"{slug}: placeholder")
    if parser.meta.get("robots", "").lower().replace(" ", "") != "noindex,follow":
        errors.append(f"{slug}: robots draft modified")
    expected = f"https://stations-electriques-portables.fr/usages/station-electrique-{slug}/"
    if parser.canonical != expected:
        errors.append(f"{slug}: canonical mismatch")
    if len(parser.meta.get("description", "")) < 70:
        errors.append(f"{slug}: weak meta description")
    if not parser.h2 or any(x is None for x in parser.h2):
        errors.append(f"{slug}: missing H2 anchors")
    if sorted(parser.toc) != sorted("#" + x for x in parser.h2 if x):
        errors.append(f"{slug}: TOC does not match H2 anchors")
    for link in parser.links:
        if link.startswith("#") and link[1:] not in parser.ids:
            errors.append(f"{slug}: broken anchor {link}")
        if link.startswith("/") and not link.startswith("//"):
            target = ROOT / link.lstrip("/")
            if link.endswith("/"): target /= "index.html"
            if not target.exists():
                errors.append(f"{slug}: internal link missing {link}")
    try:
        sys.path.insert(0, str(ROOT))
        editorial = importlib.import_module(module).CONTENT
        if editorial not in html:
            errors.append(f"{slug}: generated article differs from source")
    except Exception as exc:
        errors.append(f"{slug}: source module error: {exc}")
    print(f"{slug}: h2={len(parser.h2)}, TOC={len(parser.toc)}, internal links={sum(x.startswith('/') for x in parser.links)}")

if errors:
    print("FAIL:", *errors, sep="\n - ")
    sys.exit(1)
print("PASS: five usage pages, source parity, TOCs, robots, canonicals and links")

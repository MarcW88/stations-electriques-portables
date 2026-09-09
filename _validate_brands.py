#!/usr/bin/env python3
"""Repo-specific QA for the seven brand hubs."""
from pathlib import Path
import html as html_lib
import json
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
EXPECTED = {
    "aferiy", "allpowers", "anker-solix", "bluetti",
    "ecoflow", "izywatt", "jackery",
}
TAG_RE = re.compile(r"<[^>]+>", re.S)

def clean(raw):
    return re.sub(r"\s+", " ", html_lib.unescape(TAG_RE.sub(" ", raw))).strip()

def article(page):
    m = re.search(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>', page, re.S | re.I)
    return m.group(1) if m else ""

def fail(slug, issue):
    print(f"FAIL {slug}: {issue}")
    return False

def main():
    ok = True
    sources = {p.stem for p in (BASE / ".content" / "brand-pages").glob("*.html")}
    data = {p.stem for p in (BASE / ".content" / "brands").glob("*.yaml")}
    if sources != EXPECTED or data != EXPECTED:
        raise SystemExit(f"brand source/data mismatch: sources={sorted(sources)} data={sorted(data)}")

    for slug in sorted(EXPECTED):
        p = BASE / "marques" / slug / "index.html"
        if not p.exists():
            ok = fail(slug, "rendered page absent") and ok
            continue
        raw = p.read_text(encoding="utf-8")
        body = article(raw)
        text = clean(body).lower()
        words = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", clean(body)))
        h2 = len(re.findall(r"<h2\b", body, re.I))
        internal = re.findall(r'<a\b[^>]*href="(/[^"]+)"', body, re.I)
        sources_n = len(re.findall(r'<a\b[^>]*href="https?://', body, re.I))

        checks = [
            (bool(body), "article.content-main absent"),
            ("<!-- Contenu à rédiger -->" not in body, "placeholder présent"),
            (bool(re.search(r'name="robots"\s+content="noindex,\s*follow"', raw, re.I)), "noindex, follow absent"),
            ("Vérifié : 09/09/2026" in raw, "date de vérification absente"),
            (words >= 1000, f"contenu trop court: {words} mots"),
            (h2 >= 9, f"H2 insuffisants: {h2}"),
            (len(internal) >= 8, f"liens internes insuffisants: {len(internal)}"),
            (len(set(internal)) >= 6, f"cibles internes uniques insuffisantes: {len(set(internal))}"),
            (sources_n >= 3, f"sources externes insuffisantes: {sources_n}"),
            ("analyse documentaire" in text, "niveau de preuve non explicité"),
            (("limites" in text or "points de vigilance" in text), "section limites absente"),
            ("choisissez" in text, "bloc choose absent"),
            ("évitez" in text, "bloc avoid absent"),
            ("/comparatifs/" in body and "/guides/" in body and "/usages/" in body, "maillage comparatifs/guides/usages incomplet"),
            (not any(x in text for x in ["nous avons testé", "lors de notre test", "après plusieurs semaines d'utilisation"]), "langage de faux test détecté"),
        ]
        for cond, issue in checks:
            if not cond:
                ok = fail(slug, issue) and ok

        # Structured entity file: JSON syntax stored in .yaml is valid YAML and dependency-free.
        dpath = BASE / ".content" / "brands" / f"{slug}.yaml"
        try:
            d = json.loads(dpath.read_text(encoding="utf-8"))
        except Exception as e:
            ok = fail(slug, f"données structurées illisibles: {e}") and ok
            continue
        for key in ["brand", "entity_map", "brand_positioning", "product_range", "ecosystem", "evidence", "internal_links"]:
            if key not in d:
                ok = fail(slug, f"clé structurée manquante: {key}") and ok
        if not d.get("product_range"):
            ok = fail(slug, "product_range vide") and ok
        if len(d.get("evidence", [])) < 3:
            ok = fail(slug, "evidence ledger trop court") and ok

        print(f"{slug}: {words} words | {h2} H2 | {len(internal)} internal ({len(set(internal))} unique) | {sources_n} sources")

    if not ok:
        raise SystemExit(1)
    print("PASS: 7 brand hubs validated")

if __name__ == "__main__":
    main()

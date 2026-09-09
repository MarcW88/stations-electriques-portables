#!/usr/bin/env python3
"""Repo-specific floor QA for the seven brand hubs.

This validator intentionally checks hard structural/factual-safety invariants only.
Substantive quality, intent and cross-page structural cloning are handled by
brand-analysis-workflow / PUBLISH_REVIEW rather than by arbitrary quotas.
"""
from pathlib import Path
import html as html_lib
import json
import re

BASE = Path(__file__).resolve().parent
EXPECTED = {
    "aferiy", "allpowers", "anker-solix", "bluetti",
    "ecoflow", "izywatt", "jackery",
}
TAG_RE = re.compile(r"<[^>]+>", re.S)
EDITOR_METADISCOURSE = (
    "objectif seo", "objectif geo", "intention de recherche",
    "maillage interne", "workflow éditorial", "page type",
)
FAKE_TEST_PHRASES = (
    "nous avons testé",
    "lors de notre test",
    "après plusieurs semaines d'utilisation",
    "après plusieurs semaines d’utilisation",
)
LEGACY_ENTITY_KEYS = {"stylus", "notes", "pdf", "ocr"}


def clean(raw):
    return re.sub(r"\s+", " ", html_lib.unescape(TAG_RE.sub(" ", raw))).strip()


def article(page):
    m = re.search(
        r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>',
        page,
        re.S | re.I,
    )
    return m.group(1) if m else ""


def fail(slug, issue):
    print(f"FAIL {slug}: {issue}")
    return False


def warn(slug, issue):
    print(f"WARN {slug}: {issue}")


def main():
    ok = True
    sources = {p.stem for p in (BASE / ".content" / "brand-pages").glob("*.html")}
    data = {p.stem for p in (BASE / ".content" / "brands").glob("*.yaml")}
    if sources != EXPECTED or data != EXPECTED:
        raise SystemExit(
            f"brand source/data mismatch: sources={sorted(sources)} data={sorted(data)}"
        )

    for slug in sorted(EXPECTED):
        p = BASE / "marques" / slug / "index.html"
        if not p.exists():
            ok = fail(slug, "rendered page absent") and ok
            continue

        raw = p.read_text(encoding="utf-8")
        body = article(raw)
        visible = clean(body)
        text = visible.lower()
        internal = re.findall(r'<a\b[^>]*href="(/[^"]+)"', body, re.I)
        external = re.findall(r'<a\b[^>]*href="https?://', body, re.I)
        h2 = len(re.findall(r"<h2\b", body, re.I))
        words = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", visible))

        checks = [
            (bool(body), "article.content-main absent"),
            ("<!-- Contenu à rédiger -->" not in body, "placeholder présent"),
            (
                bool(re.search(r'name="robots"\s+content="noindex,\s*follow"', raw, re.I)),
                "noindex,follow absent",
            ),
            (
                bool(re.search(r"Vérifié\s*:\s*\d{2}/\d{2}/\d{4}", raw, re.I)),
                "date de vérification absente",
            ),
            (bool(external), "aucune source externe dans le contenu"),
            (
                not any(x in text for x in FAKE_TEST_PHRASES),
                "langage de faux test détecté",
            ),
            (
                not any(x in text for x in EDITOR_METADISCOURSE),
                "métadiscours éditeur/SEO détecté dans la prose",
            ),
        ]
        for cond, issue in checks:
            if not cond:
                ok = fail(slug, issue) and ok

        dpath = BASE / ".content" / "brands" / f"{slug}.yaml"
        try:
            d = json.loads(dpath.read_text(encoding="utf-8"))
        except Exception as e:
            ok = fail(slug, f"données structurées illisibles: {e}") and ok
            continue

        for key in [
            "brand", "entity_map", "brand_positioning", "product_range",
            "ecosystem", "evidence", "internal_links",
        ]:
            if key not in d:
                ok = fail(slug, f"clé structurée manquante: {key}") and ok

        if not d.get("product_range"):
            ok = fail(slug, "product_range vide") and ok
        if not d.get("evidence"):
            ok = fail(slug, "evidence ledger vide") and ok

        ecosystem = d.get("ecosystem", {})
        stale = sorted(LEGACY_ENTITY_KEYS.intersection(ecosystem.keys()))
        if stale:
            warn(
                slug,
                "schéma d'écosystème hérité à migrer vers le modèle stations: "
                + ", ".join(stale),
            )

        print(
            f"{slug}: {words} words | {h2} H2 | "
            f"{len(internal)} internal ({len(set(internal))} unique) | "
            f"{len(external)} external sources"
        )

    if not ok:
        raise SystemExit(1)
    print("PASS: hard brand invariants validated; substantive review remains manual/workflow-based")


if __name__ == "__main__":
    main()

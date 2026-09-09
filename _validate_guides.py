#!/usr/bin/env python3
"""Repo-specific QA for the twelve researched guide pages."""
from pathlib import Path
import html as html_lib
import re

BASE = Path(__file__).resolve().parent
SLUGS = [
    "batterie-nomade-ou-station-electrique",
    "calculer-autonomie-station-electrique",
    "calculer-capacite-station-electrique",
    "comment-choisir-station-electrique-portable",
    "duree-vie-cycles-batterie",
    "lifepo4-ou-lithium-ion",
    "onde-sinusoidale-pure",
    "recharge-rapide-station-electrique",
    "recharger-station-electrique-voiture",
    "station-electrique-portable-comment-ca-marche",
    "ups-eps-station-electrique",
    "watt-ou-watt-heure",
]

TAG_RE = re.compile(r"<[^>]+>", re.S)
ARTICLE_RE = re.compile(r'<article\b[^>]*class="[^"]*content-main[^"]*"[^>]*>(.*?)</article>', re.S | re.I)
H2_RE = re.compile(r"<h2\b", re.I)
INTERNAL_RE = re.compile(r'<a\b[^>]*href="(/[^\"]+)"', re.I)
EXTERNAL_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)


def text(raw):
    return re.sub(r"\s+", " ", html_lib.unescape(TAG_RE.sub(" ", raw))).strip()


def words(raw):
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text(raw)))


def main():
    failures = []
    metrics = []
    for slug in SLUGS:
        path = BASE / "guides" / slug / "index.html"
        if not path.exists():
            failures.append(f"{slug}: page absente")
            continue
        page = path.read_text(encoding="utf-8")
        m = ARTICLE_RE.search(page)
        if not m:
            failures.append(f"{slug}: article.content-main absent")
            continue
        article = m.group(1)
        article_text = text(article)
        wc = words(article)
        h2 = len(H2_RE.findall(article))
        internal = INTERNAL_RE.findall(article)
        external = len(EXTERNAL_RE.findall(article))

        checks = [
            ("<!-- Contenu à rédiger -->" not in page, "placeholder présent"),
            ("MM/AAAA" not in page, "MM/AAAA présent"),
            ('name="robots" content="noindex, follow"' in page, "noindex, follow absent"),
            (page.count("<!-- GUIDE_CONTENT_START -->") == 1, "GUIDE_CONTENT_START incorrect"),
            (page.count("<!-- GUIDE_CONTENT_END -->") == 1, "GUIDE_CONTENT_END incorrect"),
            ('class="article-answer"' in article, "article-answer absent"),
            (h2 >= 8, f"H2 insuffisants: {h2}"),
            (wc >= 900, f"contenu trop court: {wc}"),
            (len(internal) >= 5, f"liens internes insuffisants: {len(internal)}"),
            (len(set(internal)) >= 4, f"cibles internes uniques insuffisantes: {len(set(internal))}"),
            (external >= 3, f"sources externes insuffisantes: {external}"),
            ("2025" not in article_text, "mention 2025 obsolète dans le contenu éditorial"),
            (not re.search(r"\bnous (?:avons |l['’]avons )?(?:testé|mesuré|essayé)\b|\bnotre test\b|\blors de nos tests\b", article_text, re.I), "expérience directe non autorisée"),
            (f'<link rel="canonical" href="https://stations-electriques-portables.fr/guides/{slug}/">' in page, "canonical incorrect"),
        ]
        for ok, message in checks:
            if not ok:
                failures.append(f"{slug}: {message}")
        metrics.append((slug, wc, h2, len(internal), len(set(internal)), external))

    for row in metrics:
        print(f"{row[0]}: {row[1]} words | {row[2]} H2 | {row[3]} internal ({row[4]} unique) | {row[5]} sources")
    if failures:
        print("\nFAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print(f"\nPASS: {len(SLUGS)} guide pages validated")


if __name__ == "__main__":
    main()

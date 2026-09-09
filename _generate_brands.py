#!/usr/bin/env python3
"""Apply researched brand content and the brand-only design layer after the global shell generator."""
from pathlib import Path
import html as html_lib
import re

BASE = Path(__file__).resolve().parent
SOURCE_DIR = BASE / ".content" / "brand-pages"
UPDATED = "09/09/2026"

META_RE = re.compile(r"<!--\s*(title|description):\s*(.*?)\s*-->", re.I)
H2_RE = re.compile(r'<h2\s+id="([^"]+)"[^>]*>(.*?)</h2>', re.I | re.S)

TOC_LABELS = {
    "ecoflow": {
        "river-ou-delta": "RIVER ou DELTA",
        "reperes-gamme": "Repères de gamme",
        "recharge-ecosysteme": "Recharge & écosystème",
        "batteries-compatibilite": "Batteries & compatibilité",
        "portabilite": "Portabilité",
        "quel-niveau": "Quel niveau choisir ?",
        "limites-decision": "Quand EcoFlow convient moins",
    },
    "jackery": {
        "v2": "Série v2",
        "plus": "Série Plus & extension",
        "compact": "Branche compacte",
        "solarsaga": "SolarSaga",
        "portabilite": "Portabilité",
        "ancienne-offre": "Anciennes offres",
        "alternatives": "Quand regarder ailleurs",
    },
    "aferiy": {
        "noms": "Nano, Nomad, Haven",
        "fixe-extensible": "Fixe ou extensible",
        "portabilite": "Portabilité",
        "p210-p280-p300-p310": "P210 à P310",
        "ups-app": "UPS & application",
        "choix": "Quel profil choisir ?",
        "alternatives": "Quand regarder ailleurs",
    },
    "allpowers": {
        "versions": "Identifier la bonne version",
        "carte-gamme": "Carte de la gamme",
        "r2500": "R2500 PLUS vs V2",
        "r4000": "R4000 vs V2",
        "serie-s": "Série S",
        "quand-coherent": "Quand ALLPOWERS est cohérent",
        "quand-autre-marque": "Quand regarder ailleurs",
    },
    "anker-solix": {
        "reset-gen2": "Le reset Gen 2",
        "c1000-c2000": "C1000 vs C2000",
        "c1000": "C1000 Gen 2",
        "c2000": "C2000 Gen 2",
        "alternateur": "Recharge alternateur",
        "ancienne-generation": "Ancienne génération",
        "quand-ailleurs": "Quand regarder ailleurs",
    },
    "bluetti": {
        "trois-logiques": "Les 3 logiques BLUETTI",
        "elite": "Famille Elite",
        "elite-100": "Elite 100 V2",
        "apex": "Apex 300",
        "ac-eb": "AC & EB",
        "vehicule-extension": "Véhicule & extension",
        "portable-ou-systeme": "Portable ou système ?",
        "alternatives": "Quand regarder ailleurs",
    },
    "izywatt": {
        "quatre-besoins": "Les 4 niveaux de besoin",
        "mobilite": "800 ou Moov",
        "home-vs-eco": "Home ou Eco",
        "injection": "Injection réseau",
        "extra": "Eco + Extra",
        "solaire": "Recharge solaire",
        "pour-qui": "Pour qui IZYWATT ?",
        "alternatives": "Quand regarder ailleurs",
    },
}

BRAND_CARDS = [
    (
        "EcoFlow",
        "RIVER · DELTA",
        "Du compact réellement nomade aux systèmes extensibles pour van, solaire et secours domestique.",
        "/marques/ecoflow/",
    ),
    (
        "BLUETTI",
        "ELITE · APEX · AC/EB",
        "Une gamme profonde : portable, forte puissance et systèmes de secours extensibles.",
        "/marques/bluetti/",
    ),
    (
        "Jackery",
        "EXPLORER v2 · PLUS",
        "Une lecture assez simple autour du nomade, des kits SolarSaga et de l’extension sur certaines Plus.",
        "/marques/jackery/",
    ),
    (
        "AFERIY",
        "NANO · NOMAD · HAVEN",
        "Beaucoup de capacité et de puissance, avec un vrai arbitrage entre poids, extension et profondeur d’écosystème.",
        "/marques/aferiy/",
    ),
    (
        "Anker SOLIX",
        "C1000 GEN 2 · C2000 GEN 2",
        "Deux cœurs de gamme très lisibles : densité puissance/poids ou système 2–4 kWh avec recharge alternateur.",
        "/marques/anker-solix/",
    ),
    (
        "ALLPOWERS",
        "VOLIX · R · S",
        "Catalogue large où la version exacte compte autant que la capacité : R2500, V2, R4000…",
        "/marques/allpowers/",
    ),
    (
        "IZYWATT",
        "800 · MOOV · HOME · ECO",
        "Une gamme française courte, structurée par usage, du mobile à la gestion d’énergie domestique.",
        "/marques/izywatt/",
    ),
]


def ensure_brand_stylesheet(page: str) -> str:
    """Load the brand-only stylesheet once, after the global design system."""
    if 'href="/brand.css"' in page:
        return page
    return page.replace('</head>', '<link rel="stylesheet" href="/brand.css"></head>', 1)


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


def decorate_body(body: str) -> str:
    """Add brand-only presentation hooks without changing editorial structure."""
    body = body.replace(
        '<div class="table-wrap"><table>',
        '<div class="brand-table-wrap"><table class="brand-table">',
    )
    source_section = re.search(r'(<h2\s+id="sources"[^>]*>.*)$', body, re.I | re.S)
    if source_section:
        body = (
            body[: source_section.start()]
            + '<section class="brand-sources">'
            + source_section.group(1)
            + "</section>"
        )
    return body


def build_toc(body: str, slug: str):
    links = []
    labels = TOC_LABELS.get(slug, {})
    for anchor, title in H2_RE.findall(body):
        if anchor.lower() == "sources" or "source" in clean_text(title).lower():
            continue
        label = labels.get(anchor, clean_text(title))
        links.append(f'<a href="#{anchor}">{label}</a>')
    return "".join(links), len(links)


def build_mobile_toc(toc: str, count: int) -> str:
    return (
        '<!-- BRAND_MOBILE_TOC_START -->'
        '<details class="brand-mobile-toc">'
        f'<summary>Dans cette page <span>{count} sections</span></summary>'
        f'<nav class="brand-mobile-toc-links">{toc}</nav>'
        '</details>'
        '<!-- BRAND_MOBILE_TOC_END -->'
    )


def apply(slug: str, source: Path):
    target = BASE / "marques" / slug / "index.html"
    if not target.exists():
        raise FileNotFoundError(target)
    meta, raw_body = load_source(source)
    body = decorate_body(raw_body)
    toc, toc_count = build_toc(body, slug)
    page = ensure_brand_stylesheet(target.read_text(encoding="utf-8"))

    page = replace_once(
        r'<body(?:\s+class="[^"]*")?>',
        '<body class="brand-page">',
        page,
        f"{slug} body class",
    )
    page = replace_once(
        r"<title>.*?</title>",
        f"<title>{meta['title']}</title>",
        page,
        f"{slug} title",
    )
    safe_desc = html_lib.escape(meta["description"], quote=True)
    page = replace_once(
        r'<meta\s+name="description"\s+content="[^"]*">',
        f'<meta name="description" content="{safe_desc}">',
        page,
        f"{slug} meta",
    )
    page = replace_once(
        r'(<section class="page-hero">.*?<h1[^>]*>).*?(</h1>)',
        rf"\g<1>{meta['title']}\2",
        page,
        f"{slug} h1",
    )
    page = replace_once(
        r'(<section class="page-hero">.*?<p class="lead">).*?(</p>)',
        rf"\g<1>{meta['description']}\2",
        page,
        f"{slug} lead",
    )
    page = re.sub(r"Vérifié\s*:\s*MM/AAAA", f"Vérifié : {UPDATED}", page, flags=re.I)
    page = re.sub(
        r"Vérifié\s*:\s*\d{2}/\d{2}/\d{4}",
        f"Vérifié : {UPDATED}",
        page,
        flags=re.I,
    )
    page = replace_once(
        r'<div class="page-meta">.*?</div>',
        (
            '<div class="page-meta">'
            f'<span class="meta-tag">Vérifié : {UPDATED}</span>'
            '<span class="meta-tag">Analyse documentaire</span>'
            '<a class="meta-tag meta-tag-link" href="/transparence-affiliation/">'
            'Affiliation transparente</a>'
            '</div>'
        ),
        page,
        f"{slug} meta tags",
    )

    article = (
        '<article class="content-main">\n'
        '<!-- BRAND_CONTENT_START -->\n'
        f'{body}\n'
        '<!-- BRAND_CONTENT_END -->\n'
        '</article>'
    )
    page = replace_once(
        r'<article class="content-main">.*?</article>',
        article,
        page,
        f"{slug} article",
    )
    page = replace_once(
        r'(<nav class="toc-list">).*?(</nav>)',
        rf"\g<1>{toc}\2",
        page,
        f"{slug} toc",
    )

    page = re.sub(
        r'<!-- BRAND_MOBILE_TOC_START -->.*?<!-- BRAND_MOBILE_TOC_END -->',
        '',
        page,
        flags=re.I | re.S,
    )
    mobile_toc = build_mobile_toc(toc, toc_count)
    page = replace_once(
        r'(<div class="container">)\s*(<div class="content-layout">)',
        rf"\g<1>{mobile_toc}\2",
        page,
        f"{slug} mobile toc",
    )

    if not re.search(r'name="robots"\s+content="noindex,\s*follow"', page, re.I):
        raise ValueError(f"{slug}: noindex, follow must be preserved")
    if "<!-- Contenu à rédiger -->" in page:
        raise ValueError(f"{slug}: placeholder remains")
    if 'class="table-wrap"' in page:
        raise ValueError(f"{slug}: unstyled table-wrap remains")
    if 'class="brand-page"' not in page:
        raise ValueError(f"{slug}: brand-page design scope missing")

    target.write_text(page, encoding="utf-8")
    print(f"generated {slug}")


def render_brand_hub():
    target = BASE / "marques" / "index.html"
    if not target.exists():
        raise FileNotFoundError(target)
    page = ensure_brand_stylesheet(target.read_text(encoding="utf-8"))

    page = replace_once(
        r'<body(?:\s+class="[^"]*")?>',
        '<body class="brand-hub-page">',
        page,
        "brand hub body class",
    )
    page = replace_once(
        r"<title>.*?</title>",
        '<title>Marques de stations électriques portables — Comparer les gammes</title>',
        page,
        "brand hub title",
    )
    page = replace_once(
        r'<meta\s+name="description"\s+content="[^"]*">',
        (
            '<meta name="description" content="Comparez EcoFlow, BLUETTI, Jackery, '
            'AFERIY, Anker SOLIX, ALLPOWERS et IZYWATT par logique de gamme, usages '
            'et écosystème.">'
        ),
        page,
        "brand hub meta",
    )

    cards = "".join(
        (
            f'<a href="{url}" class="brand-card">'
            f'<div class="brand-tier">{tier}</div>'
            f'<div class="brand-name">{name}</div>'
            f'<p class="brand-desc">{desc}</p>'
            '<span class="brand-card-arrow">Explorer la gamme →</span>'
            '</a>'
        )
        for name, tier, desc, url in BRAND_CARDS
    )
    main = (
        '<main>'
        '<div class="container"><nav class="breadcrumb">'
        '<a href="/">Accueil</a><span class="sep">/</span><span>Marques</span>'
        '</nav></div>'
        '<section class="page-hero brand-hub-hero"><div class="container">'
        '<span class="ctype ctype-marque">Marques</span>'
        '<h1>Comparer les marques de stations électriques portables</h1>'
        '<p class="lead">Toutes les marques ne structurent pas leur gamme de la même façon. '
        'Comparez d’abord leur logique — mobilité, extension, solaire, secours ou recharge '
        'véhicule — avant de descendre au modèle.</p>'
        '</div></section>'
        '<section class="section brand-hub-section"><div class="container">'
        f'<div class="brand-grid brand-grid--hub">{cards}</div>'
        '</div></section>'
        '</main>'
    )
    page = replace_once(r'<main>.*?</main>', main, page, "brand hub main")

    if not re.search(r'name="robots"\s+content="noindex,\s*follow"', page, re.I):
        raise ValueError("brand hub: noindex, follow must be preserved")
    target.write_text(page, encoding="utf-8")
    print("generated brand hub")


def main():
    sources = sorted(SOURCE_DIR.glob("*.html"))
    if not sources:
        raise SystemExit("no brand content sources found")
    for source in sources:
        apply(source.stem, source)
    render_brand_hub()
    print(f"PASS: generated {len(sources)} brand pages + brand hub")


if __name__ == "__main__":
    main()

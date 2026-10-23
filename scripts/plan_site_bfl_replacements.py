#!/usr/bin/env python3
"""Plan safe BFL replacements across all published HTML pages.

Only third-party editorial photography on informational pages and SVG assets
explicitly named editorial-* are candidates. Authentic products, diagrams,
icons, logos and existing BFL assets are untouched.
"""
from pathlib import Path
import hashlib
import html
import json
import re

ROOT = Path(__file__).resolve().parent.parent
REQUESTS = ROOT / ".content/image-requests"
EXCLUDED = {"modeles", "marques", "accessoires", "comparatifs"}
EDITORIAL = {"usages", "guides", "solaire", "puissance-capacite"}
FIGURE = re.compile(r"<figure\\b[^>]*>.*?</figure\\s*>", re.I | re.S)
IMG = re.compile(r"<img\\b[^>]*>", re.I | re.S)
SRC = re.compile(r'\\bsrc\\s*=\\s*["\\']([^"\\']+)["\\']', re.I)
ALT = re.compile(r'\\balt\\s*=\\s*["\\']([^"\\']*)["\\']', re.I)
TITLE = re.compile(r"<h1\\b[^>]*>(.*?)</h1>", re.I | re.S)
TAGS = re.compile(r"<[^>]+>")
GENERATED = re.compile(r"/?assets/generated/", re.I)
STOCK = ("commons.wikimedia.org", "upload.wikimedia.org", "unsplash.com",
         "pexels.com", "pixabay.com", "images.pexels.com")
PRODUCT = ("ecoflow", "bluetti", "jackery", "anker", "aferiy", "allpowers",
           "izywatt", "or ium", "amazon", "cdn.shopify", "shopify.com")
SVG_EDITORIAL = re.compile(r"(?:^|/)editorial-[a-z0-9-]+\\.svg(?:\\?.*)?$", re.I)

def candidate(img, path):
    src_match = SRC.search(img)
    if not src_match:
        return False
    src = html.unescape(src_match.group(1)).lower()
    if GENERATED.search(src) or src.startswith("data:"):
        return False
    if SVG_EDITORIAL.search(src):
        return True
    if path.parts[0] not in EDITORIAL:
        return False
    if src.startswith(("http://", "https://")):
        if any(x in src for x in PRODUCT):
            return False
        return any(x in src for x in STOCK)
    return False

def context_title(page):
    m = TITLE.search(page)
    return TAGS.sub("", m.group(1)).strip() if m else "Station électrique portable"

def replace_once(page, img, marker):
    # Remove the entire enclosing editorial figure if it contains this image,
    # avoiding nested figure markup and abandoned third-party attributions.
    for fm in FIGURE.finditer(page):
        if img in fm.group(0) and len(IMG.findall(fm.group(0))) == 1:
            return page[:fm.start()] + marker + page[fm.end():]
    return page.replace(img, marker, 1)

def main():
    REQUESTS.mkdir(parents=True, exist_ok=True)
    count = 0
    for file in sorted(ROOT.glob("**/index.html")) + [ROOT / "index.html"]:
        if not file.is_file():
            continue
        path = file.relative_to(ROOT)
        if path.parts[0].startswith(".") or path.parts[0] in EXCLUDED:
            continue
        page = file.read_text(encoding="utf-8")
        title = context_title(page)
        matches = [m.group(0) for m in IMG.finditer(page) if candidate(m.group(0), path)]
        for idx, img in enumerate(matches, 1):
            digest = hashlib.sha1((str(path) + img).encode()).hexdigest()[:10]
            rid = f"site-editorial-{digest}"
            destination = REQUESTS / (rid + ".json")
            if destination.exists():
                continue
            marker = f"<!-- EDITORIAL_IMAGE:{rid} -->"
            alt_match = ALT.search(img)
            alt = html.unescape(alt_match.group(1)) if alt_match else ""
            # Require truthful GENERIC editorial representation, not a real product.
            scenario = (alt or title).strip()[:210]
            request = {
                "id": rid, "page": str(path), "slot": "editorial",
                "required": True,
                "reason": "Replace external decorative editorial image or decorative SVG while preserving authentic products and technical diagrams.",
                "allow_ai_generation": True, "truth_risk": "LOW",
                "status": "PENDING", "marker": marker, "placement": "replace",
                "output_path": f"assets/generated/{rid}.webp",
                "prompt": ("Natural, credible premium documentary editorial photograph for a French technical guide about portable power stations. "
                    f"Topic: {title}. Depict this scene: {scenario}. Include a realistic GENERIC unbranded portable electric battery "
                    "only when relevant, physically plausible ports and cables, natural lighting, non-commercial composition, "
                    "no fake claims of product testing, no logo, no text, no watermark, no diagrams, landscape 3:2."),
                "alt": (alt or f"Illustration éditoriale de {title}")[:220],
                "caption": "", "width": 1024, "height": 672,
                "prompt_upsampling": True, "seed": None,
            }
            updated = replace_once(page, img, marker)
            if updated == page:
                continue
            page = updated
            destination.write_text(json.dumps(request, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
            count += 1
        if count and page != file.read_text(encoding="utf-8"):
            file.write_text(page, encoding="utf-8")
    print(f"BFL replacement requests planned: {count}")

if __name__ == "__main__":
    main()

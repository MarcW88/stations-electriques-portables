#!/usr/bin/env python3
"""Repo-specific QA for the seven comparison pages."""
from pathlib import Path
import html as htmlmod
import json
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / ".content" / "comparisons"
EXPECTED = {
    "meilleure-station-electrique-portable",
    "station-electrique-portable-pas-chere",
    "station-electrique-portable-puissante",
    "station-electrique-portable-avec-panneau-solaire",
    "station-electrique-lifepo4",
    "station-electrique-portable-compacte",
    "generateur-solaire",
}
ALLOWED_STATUS = {"ELIGIBLE","CONDITIONALLY_ELIGIBLE","OUTDATED","NOT_COMPARABLE","EXCLUDED"}
ALLOWED_EVIDENCE = {"VERIFIED","SUPPORTED","INFERRED","USER_PATTERN","FIRST_HAND"}

def fail(msg):
    print("FAIL:", msg)
    raise SystemExit(1)

def visible_text(markup):
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", markup, flags=re.I|re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I|re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", htmlmod.unescape(text)).strip()

def internal_links(markup):
    return re.findall(r'href="(/[^"#?]*)"', markup)

files = sorted(DATA_DIR.glob("*.json"))
slugs = {p.stem for p in files}
if slugs != EXPECTED:
    fail(f"comparison data slugs mismatch: {sorted(slugs)}")

for data_file in files:
    data = json.loads(data_file.read_text(encoding="utf-8"))
    slug = data["slug"]
    page = BASE / "comparatifs" / slug / "index.html"
    if not page.exists():
        fail(f"{slug}: missing rendered page")
    s = page.read_text(encoding="utf-8")
    vis = visible_text(s)
    words = len(re.findall(r"\b[\wÀ-ÿ’'-]+\b", vis))
    h2 = len(re.findall(r"<h2\b", s, flags=re.I))
    links = internal_links(s)
    unique_links = set(links)
    sources = set(re.findall(r'href="https?://[^"]+"', s))
    markers = s.count("<!-- COMPARISON_CONTENT_START -->")

    if '<meta name="robots" content="noindex, follow">' not in s:
        fail(f"{slug}: noindex, follow missing")
    if "<!-- Contenu à rédiger -->" in s or "MM/AAAA" in s:
        fail(f"{slug}: placeholder remains")
    if "Comparatif 2025" in vis or "comparatif 2025" in vis:
        fail(f"{slug}: stale 2025 visible")
    if markers != 1 or s.count("<!-- COMPARISON_CONTENT_END -->") != 1:
        fail(f"{slug}: comparison markers invalid")
    if words < 1150:
        fail(f"{slug}: only {words} words")
    if h2 < 8:
        fail(f"{slug}: only {h2} H2")
    if len(links) < 8 or len(unique_links) < 6:
        fail(f"{slug}: insufficient internal linking {len(links)}/{len(unique_links)}")
    if len(sources) < 3:
        fail(f"{slug}: only {len(sources)} external sources")
    for token in ["Méthode", "hard gate", "Limites", "Sources consultées", "desk research"]:
        if token.lower() not in vis.lower():
            fail(f"{slug}: missing editorial token {token}")

    criteria = data.get("criteria", [])
    if sum(c.get("weight", 0) for c in criteria) != 100:
        fail(f"{slug}: weights do not sum to 100")
    if not any(c.get("hard_gate") for c in criteria):
        fail(f"{slug}: no hard gate")
    if data.get("notes", {}).get("affiliate_commission_used_in_ranking") is not False:
        fail(f"{slug}: affiliate commission flag invalid")
    if data.get("notes", {}).get("first_hand_test") is not False:
        fail(f"{slug}: first hand test must be false")
    eligible = [p for p in data["product_universe"] if p["status"] in {"ELIGIBLE","CONDITIONALLY_ELIGIBLE"}]
    if len(eligible) < 3:
        fail(f"{slug}: fewer than 3 eligible candidates")
    evidence = data.get("evidence_ledger", [])
    for p in eligible:
        pe = [e for e in evidence if e.get("product_id") == p["id"]]
        if len(pe) < 4:
            fail(f"{slug}: {p['id']} has fewer than 4 evidence rows")
        if any(e.get("evidence_class") not in ALLOWED_EVIDENCE for e in pe):
            fail(f"{slug}: invalid evidence class")
    ranking = data.get("ranking", [])
    if not ranking or not any(r.get("rank") == 1 for r in ranking):
        fail(f"{slug}: ranking missing")
    if any(r.get("rank") == 1 and r.get("hard_gate_failed") for r in ranking):
        fail(f"{slug}: winner failed hard gate")

    print(f"{slug}: {words} words | {h2} H2 | {len(links)} internal ({len(unique_links)} unique) | {len(sources)} sources")

print("\nPASS: 7 comparison pages validated")

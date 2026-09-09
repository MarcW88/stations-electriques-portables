#!/usr/bin/env python3
"""Render researched comparison pages from .content/comparisons/*.json.

Run after _generate.py. Structured comparison data is the persistent audit trail;
this renderer turns it into the final HTML without changing the underlying shell.
"""
from pathlib import Path
import html
import json
import re

BASE = Path(__file__).resolve().parent
DATA_DIR = BASE / ".content" / "comparisons"
UPDATED = "09/09/2026"

CONFIDENCE = {
    "VERIFIED": 1.00,
    "FIRST_HAND": 1.00,
    "SUPPORTED": 0.95,
    "INFERRED": 0.85,
    "USER_PATTERN": 0.80,
}

def text_only(value):
    return re.sub(r"<[^>]+>", "", value or "")

def recalc_ranking(data):
    criteria = {c["id"]: c for c in data["criteria"]}
    products = {p["id"]: p for p in data["product_universe"]}
    results = []
    for pid, score_map in data["scores"].items():
        product = products[pid]
        if product["status"] not in {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}:
            continue
        raw = 0.0
        adjusted = 0.0
        hard_gate_failed = False
        for cid, criterion in criteria.items():
            entry = score_map[cid]
            score = float(entry["score"])
            weight = float(criterion["weight"])
            factor = CONFIDENCE[entry["evidence_class"]]
            raw += score * weight / 10
            adjusted += score * factor * weight / 10
            if criterion.get("hard_gate") and score < float(criterion.get("hard_gate_min", 5)):
                hard_gate_failed = True
        results.append({
            "product_id": pid,
            "name": product["name"],
            "raw_score": round(raw, 2),
            "confidence_adjusted_score": round(adjusted, 2),
            "hard_gate_failed": hard_gate_failed,
        })
    ranked = sorted(results, key=lambda x: (x["hard_gate_failed"], -x["confidence_adjusted_score"]))
    rank = 1
    for row in ranked:
        if row["hard_gate_failed"]:
            row["rank"] = None
        else:
            row["rank"] = rank
            rank += 1
    return ranked

def product_map(data):
    return {p["id"]: p for p in data["product_universe"]}

def ranking_table(data, ranking):
    products = product_map(data)
    rows = []
    for row in ranking:
        p = products[row["product_id"]]
        rank = f'{row["rank"]}.' if row["rank"] else "Hors classement"
        score = f'{row["confidence_adjusted_score"]:.1f}/100'
        facts = p.get("facts", {})
        cap = facts.get("capacity_wh")
        out = facts.get("output_w")
        if cap and out:
            profile = f"{cap:g} Wh · {out:g} W"
        else:
            profile = p["name"]
        rows.append(
            "<tr>"
            f"<td><strong>{html.escape(rank)} {html.escape(p['name'])}</strong><br><small>{html.escape(profile)}</small></td>"
            f"<td><strong>{score}</strong></td>"
            f"<td>{'Échoue un hard gate' if row['hard_gate_failed'] else 'Éligible au classement'}</td>"
            "</tr>"
        )
    return (
        '<div class="power-table-wrap"><table class="power-table">'
        "<thead><tr><th>Modèle</th><th>Score ajusté</th><th>Statut</th></tr></thead>"
        "<tbody>" + "".join(rows) + "</tbody></table></div>"
    )

def criteria_table(data):
    rows = []
    for c in data["criteria"]:
        gate = " — hard gate" if c.get("hard_gate") else ""
        rows.append(
            f"<tr><td><strong>{html.escape(c['label'])}</strong>{gate}</td>"
            f"<td>{c['weight']} %</td><td>{html.escape(c['basis'])}</td></tr>"
        )
    return (
        '<div class="power-table-wrap"><table class="power-table">'
        "<thead><tr><th>Critère</th><th>Poids</th><th>Ce que nous évaluons</th></tr></thead>"
        "<tbody>" + "".join(rows) + "</tbody></table></div>"
    )

def product_sections(data, ranking):
    products = product_map(data)
    notes = data["page"]["product_notes"]
    out = []
    active = [r for r in ranking if r["rank"] is not None]
    for row in active:
        pid = row["product_id"]
        p = products[pid]
        advantage, limitation, best_for, avoid_if = notes[pid]
        facts = p.get("facts", {})
        source = p.get("source_url")
        internal = p.get("internal_url")
        facts_text = []
        for key, label in [
            ("capacity_wh", "capacité"),
            ("output_w", "puissance nominale"),
            ("weight_kg", "poids"),
            ("station_weight_kg", "poids de la station"),
            ("solar_w", "entrée solaire"),
            ("solar_input_w", "entrée solaire"),
            ("panel_w", "panneau inclus"),
        ]:
            if key in facts:
                unit = " Wh" if "capacity" in key else " W" if key in {"output_w","solar_w","solar_input_w","panel_w"} else " kg"
                facts_text.append(f"{label} {facts[key]:g}{unit}")
        if facts.get("cycles"):
            facts_text.append(f"batterie {facts['cycles']}")
        if facts.get("ups"):
            facts_text.append(f"UPS/ASI {facts['ups']}")
        spec_sentence = ", ".join(facts_text)
        out.append(f"""
<h3>{row['rank']}. {html.escape(p['name'])}</h3>
<p><strong>Pourquoi il est classé ici.</strong> {html.escape(p['name'])} obtient un score ajusté de
<strong>{row['confidence_adjusted_score']:.1f}/100</strong>. Son avantage déterminant est
<strong>{html.escape(advantage)}</strong>. Les données retenues sont issues de la fiche fabricant actuelle :
{html.escape(spec_sentence)}. Nous séparons volontairement ces faits de notre interprétation éditoriale du
meilleur usage.</p>
<p>Le produit convient surtout à <strong>{html.escape(best_for)}</strong>. Sa limite principale est
<strong>{html.escape(limitation)}</strong>. Nous le déconseillons comme premier choix
{html.escape(avoid_if)}. Cette limite compte réellement dans le classement : un bon score global ne transforme
pas une contrainte de poids, de puissance, de recharge ou de disponibilité en détail secondaire.</p>
<p><a href="{html.escape(internal)}">Voir la page liée à {html.escape(p['name'])}</a> ou consulter la
<a href="{html.escape(source)}" rel="nofollow noopener">source fabricant utilisée pour les données</a>.</p>
""")
    return "\n".join(out)

def hard_gate_note(data, ranking):
    products = product_map(data)
    failed = [r for r in ranking if r["hard_gate_failed"]]
    if not failed:
        return ""
    items = []
    for r in failed:
        p = products[r["product_id"]]
        items.append(f"<li><strong>{html.escape(p['name'])}</strong> : conservé pour contexte mais non classé car un hard gate n’est pas satisfait.</li>")
    return "<p>Produits hors classement :</p><ul>" + "".join(items) + "</ul>"

def exclusions(data):
    items = []
    for p in data["product_universe"]:
        if p["status"] in {"OUTDATED","NOT_COMPARABLE","EXCLUDED"}:
            items.append(f"<li><strong>{html.escape(p['name'])}</strong> — {html.escape(p['exclusion_reason'])}</li>")
    return "<ul>" + "".join(items) + "</ul>" if items else ""

def source_list(data):
    seen = {}
    for e in data["evidence_ledger"]:
        seen[e["source"]] = e["product_id"]
    products = product_map(data)
    rows = []
    for url, pid in seen.items():
        name = products.get(pid, {}).get("name", pid)
        rows.append(f'<li><a href="{html.escape(url)}" rel="nofollow noopener">{html.escape(name)} — documentation fabricant</a></li>')
    return "<ul>" + "".join(rows) + "</ul>"

def related_box(data):
    links = "".join(f'<a href="{html.escape(url)}">{html.escape(label)}</a>' for url,label in data["page"]["related"])
    return f'<div class="related-box"><h4>À lire aussi</h4><div class="related-links">{links}</div></div>'

def body_html(data):
    ranking = recalc_ranking(data)
    data["ranking"] = ranking
    page = data["page"]
    winner = next((r for r in ranking if r["rank"] == 1), None)
    criteria_names = ", ".join(c["label"].lower() for c in data["criteria"])
    decision_paragraphs = "\n".join(f"<p>{p}</p>" for p in page["decision_paragraphs"])
    return f"""
<!-- COMPARISON_CONTENT_START -->
<div class="answer-box"><p>{page['answer']}</p></div>

<h2 id="classement">Notre classement 2026</h2>
<p>Le classement est calculé après définition de l’intention, de l’univers produit et des poids. Une commission
d’affiliation n’intervient ni dans l’inclusion, ni dans les notes, ni dans l’ordre final. Le score affiché est
ajusté selon le niveau de confiance de la preuve : les caractéristiques fabricant sont vérifiées, tandis que leur
traduction en note reste une interprétation éditoriale.</p>
{ranking_table(data, ranking)}
{hard_gate_note(data, ranking)}

<h2 id="methode">Méthode : critères avant gagnant</h2>
<p>{page['method_context']}</p>
<p>Nous avons fixé les critères suivants avant de calculer les scores : {html.escape(criteria_names)}.
Les poids totalisent 100 %. Un hard gate est éliminatoire : un produit qui échoue ne peut pas remonter grâce à
une moyenne flatteuse sur les autres critères.</p>
{criteria_table(data)}
<p>Cette page repose sur une <strong>recherche documentaire</strong> datée du {UPDATED}, sans test physique
réalisé par notre rédaction. Les scores synthétisent des données fabricant et des arbitrages d’usage ; ils ne
doivent pas être lus comme une mesure scientifique de performance.</p>

<h2 id="modeles">Les modèles retenus et pourquoi</h2>
{product_sections(data, ranking)}

<h2 id="criteres">Ce qui change réellement la décision</h2>
{decision_paragraphs}
<p>Pour éviter la fausse précision, nous ne récompensons pas mécaniquement la plus grande valeur brute. Une
capacité plus élevée augmente l’autonomie mais aussi le poids ; une puissance élevée élargit la liste d’appareils
compatibles mais ne crée pas d’énergie supplémentaire ; une entrée solaire élevée n’est utile que si les panneaux,
la météo et le mode de voyage permettent de l’exploiter.</p>

<h2 id="cout">Coût total et configuration réellement utilisable</h2>
<p>{page['cost_note']}</p>
<p>Le coût total d’une solution peut inclure le panneau, un câble voiture, une batterie additionnelle ou un
adaptateur. Nous évitons donc de comparer artificiellement un appareil nu à un bundle complet. Lorsqu’un prix est
mentionné, il est daté et ne constitue pas une promesse de prix actuel au moment où vous lirez cette page.</p>

<h2 id="limites">Limites, hard gates et exclusions</h2>
<p>{page['limits_note']}</p>
{exclusions(data)}
<p>Les caractéristiques et disponibilités peuvent évoluer selon le marché et la génération. Une référence qui
change de statut, de prix ou de fiche technique doit être réévaluée avant publication d’un nouveau classement.</p>

<h2 id="choisir">Quel modèle choisir selon votre profil ?</h2>
<p>{page['choose_note']}</p>
<p>Avant achat, vérifiez au minimum la puissance simultanée de vos appareils, l’autonomie nécessaire et vos modes
de recharge. Le <a href="/calculateur-autonomie/">calculateur d’autonomie</a> permet de tester un scénario concret,
tandis que le guide <a href="/guides/comment-choisir-station-electrique-portable/">comment choisir une station
électrique portable</a> explique les critères sans classement commercial.</p>

<h2 id="sources">Sources consultées</h2>
<p>Nous privilégions les pages produit et documents fabricants actuels. Les sources ci-dessous alimentent le
registre de preuves du comparatif ; les interprétations et scores restent ceux de la rédaction.</p>
{source_list(data)}
<p><small>Recherche mise à jour le {UPDATED}. Comparatif réalisé par desk research. Aucun test physique n’est
revendiqué. Les liens affiliés éventuels n’influencent ni le scoring ni le classement.</small></p>
{related_box(data)}
<!-- COMPARISON_CONTENT_END -->
"""

def replace_once(pattern, repl, text, flags=0):
    new, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f"expected one match for {pattern!r}, got {n}")
    return new

def render_one(path, data):
    html_text = path.read_text(encoding="utf-8")
    page = data["page"]

    html_text = replace_once(r"<title>.*?</title>", f"<title>{page['title']}</title>", html_text)
    html_text = replace_once(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(page["description"], quote=True)}">', html_text)
    html_text = replace_once(r'<h1 style="margin-top:10px">.*?</h1>', f'<h1 style="margin-top:10px">{page["title"]}</h1>', html_text)
    html_text = replace_once(r'<p class="lead">.*?</p>', f'<p class="lead">{page["description"]}</p>', html_text)
    html_text = replace_once(r'<span class="meta-tag">Vérifié : .*?</span>', f'<span class="meta-tag">Vérifié : {UPDATED}</span>', html_text)

    article = f'<article class="content-main">{body_html(data)}</article>'
    html_text = replace_once(r'<article class="content-main">.*?</article>', article, html_text, flags=re.S)

    toc = (
        '<nav class="toc-list">'
        '<a href="#classement">Classement</a>'
        '<a href="#methode">Méthode</a>'
        '<a href="#modeles">Modèles</a>'
        '<a href="#criteres">Critères</a>'
        '<a href="#cout">Coût total</a>'
        '<a href="#limites">Limites</a>'
        '<a href="#choisir">Comment choisir</a>'
        '<a href="#sources">Sources</a>'
        '</nav>'
    )
    html_text = replace_once(r'<nav class="toc-list">.*?</nav>', toc, html_text, flags=re.S)
    if '<meta name="robots" content="noindex, follow">' not in html_text:
        raise RuntimeError(f"noindex missing in {path}")
    path.write_text(html_text, encoding="utf-8")
    return data

def main():
    files = sorted(DATA_DIR.glob("*.json"))
    if len(files) != 7:
        raise SystemExit(f"FAIL: expected 7 comparison data files, got {len(files)}")
    for data_file in files:
        data = json.loads(data_file.read_text(encoding="utf-8"))
        slug = data["slug"]
        page_path = BASE / "comparatifs" / slug / "index.html"
        if not page_path.exists():
            raise SystemExit(f"FAIL: missing shell {page_path}")
        data = render_one(page_path, data)
        data_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"generated {slug}")
    print("PASS: generated 7 comparison pages")

if __name__ == "__main__":
    main()

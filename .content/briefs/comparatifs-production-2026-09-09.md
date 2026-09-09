# Brief — Production des comparatifs — 09/09/2026

```yaml
scope: /comparatifs/
mode: NEW_CONTENT
workflow: comparison-content-workflow
research_date: 2026-09-09
source_of_truth: .content/comparisons/*.json
shell_generator: _generate.py
renderer: _generate_comparatifs.py
indexing: noindex, follow
```

## Routing

Les 7 pages enfants `/comparatifs/` étaient encore des shells : réponse courte, date `MM/AAAA`, contenu à rédiger et absence de méthodologie. Le classement pré-existant n'est donc pas considéré comme une source de vérité. Chaque page est reconstruite selon le principe :

**Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.**

## Pages

1. `/comparatifs/meilleure-station-electrique-portable/` — BEST_OVERALL, univers ~1 kWh.
2. `/comparatifs/station-electrique-portable-pas-chere/` — BUDGET, prix fabricant daté et disponibilité comme hard gate.
3. `/comparatifs/station-electrique-portable-puissante/` — FEATURE_SPECIFIC, segment ~2 kWh / 2 kW+.
4. `/comparatifs/station-electrique-portable-avec-panneau-solaire/` — BEST_FOR_USE_CASE, bundles officiels station + panneau.
5. `/comparatifs/station-electrique-lifepo4/` — FEATURE_SPECIFIC, longévité LFP documentée.
6. `/comparatifs/station-electrique-portable-compacte/` — BEST_FOR_USE_CASE, ~250–300 Wh avec vraie sortie AC.
7. `/comparatifs/generateur-solaire/` — BEST_FOR_USE_CASE, autonomie hors réseau avec bundles solaires plus importants.

## Univers et corrections 2026

Le benchmark privilégie des références actuelles et documentées par les fabricants : EcoFlow DELTA 3 Plus / RIVER 3, BLUETTI Elite 30 V2 / Elite 100 V2 / Elite 200 V2, Jackery Explorer 300 Plus / 1000 v2 / 2000 v2 et AFERIY P210.

Corrections par rapport aux placeholders :
- BLUETTI EB3A n'est plus utilisé comme gagnant budget : la gamme actuelle Elite 30 V2 est retenue ; la page EU EB3A signale par ailleurs un statut discontinued.
- EcoFlow DELTA 2 et RIVER 2 ne servent plus de référence principale lorsque les gammes DELTA 3 / RIVER 3 répondent au même segment.
- BLUETTI AC200Max est écarté du comparatif puissant au profit de l'Elite 200 V2 actuelle.
- Le nombre de cycles est relié au seuil résiduel lorsqu'il est publié ; aucune fourchette universelle par chimie n'est inventée.
- La puissance continue est séparée des modes X-Boost / Power Lifting / surge.
- Les prix ne sont utilisés comme critère central que sur la page budget. Ailleurs ils sont datés et contextuels.

## Rankings issus du scoring

- Meilleure station : EcoFlow DELTA 3 Plus > BLUETTI Elite 100 V2 > Jackery Explorer 1000 v2.
- Pas chère : BLUETTI Elite 30 V2 > Jackery Explorer 300 Plus ; EcoFlow RIVER 3 hors classement tant que la disponibilité directe reste insuffisamment stable.
- Puissante : BLUETTI Elite 200 V2 > Jackery Explorer 2000 v2 > AFERIY P210.
- Avec panneau solaire : EcoFlow DELTA 3 Plus + 220 W > Jackery 1000 v2 + 200 W > AFERIY P210 + 400 W.
- LiFePO4 : EcoFlow DELTA 3 Plus > BLUETTI Elite 200 V2 > Jackery Explorer 1000 v2.
- Compacte : BLUETTI Elite 30 V2 > Jackery Explorer 300 Plus ; RIVER 3 hors classement sur disponibilité.
- Générateur solaire : Jackery 2000 v2 + 2×200 W > AFERIY P210 + 400 W > EcoFlow DELTA 3 Plus + 220 W.

## Evidence ledger

Chaque JSON contient :
- intention et contrainte principale ;
- univers et exclusions ;
- critères pondérés (100 %) ;
- au moins un hard gate ;
- evidence ledger basé sur pages fabricants ;
- score 0–10 avec justification et classe de confiance ;
- ranking brut et ajusté ;
- flags affiliation, test physique et validation humaine.

Sources principales : EcoFlow France, BLUETTI France, Jackery France, AFERIY France. Les données instables sont datées au 09/09/2026.

## Maillage

Chaque comparatif relie selon pertinence :
- guides W/Wh, capacité, autonomie, LFP, cycles ;
- usages camping, van, chantier ;
- pages solaire / MPPT ;
- calculateur d'autonomie ;
- autres comparatifs ;
- fiches modèles ou pages marques.

## Publication

Le site reste en `noindex, follow`. Le workflow n'autorise ni merge automatique ni indexation sans validation humaine explicite.

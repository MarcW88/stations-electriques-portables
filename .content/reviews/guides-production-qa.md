# QA — Guides — 09/09/2026

```yaml
scope: /guides/
status: QA_IN_PROGRESS
structural_gate: PENDING_CI
editorial_gate: MANUAL_REVIEW_COMPLETE
indexing_status: noindex
publishable: false
human_validation_required: true
```

## Revue éditoriale

- 12 pages routées en `NEW_CONTENT` car les corps étaient des placeholders.
- Slugs, canonicals, structure du site et `noindex, follow` conservés.
- Source éditoriale : `.content/guides/*.html`, rendue par `_generate_guides.py` après `_generate.py`.
- Intentions séparées : choix, fonctionnement, W/Wh, autonomie, capacité, chimie, cycles, onde, UPS/EPS, recharge rapide, recharge voiture, powerbank vs station.
- Aucun test physique ou prix actuel inventé.

## Fact-check

- Cycles LFP rattachés à des modèles et au seuil de 80 % : `CONFIRMED`.
- Temps de transfert UPS rattachés à Schneider Electric et aux modèles EcoFlow concernés : `CONFIRMED`.
- LFP vs NMC contextualisé via NREL/DOE : `CONFIRMED`.
- Recharge voiture AC180 12/24 V : `CONFIRMED`.
- Coefficient 0,85 dans les calculs : présenté comme hypothèse d’estimation, jamais comme constante fabricant.

## Qualité

- Réponse initiale autonome sur chaque page.
- Minimum visé : 7 H2 substantiels, 5 liens internes, 4 cibles uniques et 3 sources.
- Tableaux introduits et interprétés.
- Maillage vers calculateur, guides, usages, solaire et comparatifs selon le besoin.
- Pas de promesse absolue, faux témoignage, faux test ou urgence artificielle.

## CI attendu

Le workflow doit valider la génération des 12 guides, le quality gate du skill, le QA repo-specific, l’idempotence, le maintien du noindex et `git diff --check`.

## Verdict provisoire

`QA_IN_PROGRESS` jusqu’au premier run GitHub Actions vert. Un CI vert ne déclenche pas de merge automatique : validation humaine requise.

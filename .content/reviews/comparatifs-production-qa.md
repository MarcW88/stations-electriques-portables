# QA — Comparatifs — 09/09/2026

```yaml
scope: /comparatifs/
status: APPROVED_FOR_MERGE
methodology_gate: PASS
editorial_gate: PASS
human_validation: explicit_user_approval_2026-09-09
indexing_status: noindex
publishable_for_indexing: false
human_validation_required: false
workflow_runs:
  - 34323472260
  - 34323632420
```

## Contrôles éditoriaux

- 7 pages routées en `NEW_CONTENT` car les anciennes pages étaient des shells 2025 avec placeholder.
- Critères, poids, univers produit, exclusions et hard gates définis avant le ranking.
- Somme des poids = 100 pour chaque page.
- Au moins un hard gate par comparatif.
- Les commissions d'affiliation ne participent jamais au score.
- Aucun test physique, mesure personnelle ou expérience directe revendiqués.
- Les faits fabricants sont séparés des appréciations éditoriales `INFERRED`.
- Les limites principales sont explicites pour les produits classés.
- Les exclusions sont documentées dans les datasets.
- Le `noindex, follow` est conservé sur les 7 pages.

## Contrôles factuels principaux

- EcoFlow DELTA 3 Plus : 1 024 Wh, 1 800 W, entrée PV 1 000 W, LFP 4 000 cycles à 80 %, ≤12,5 kg.
- BLUETTI Elite 100 V2 : 1 024 Wh, 1 800 W, 11,5 kg, PV 1 000 W, 4 000+ cycles à 80 %, UPS ≤10 ms.
- BLUETTI Elite 30 V2 : 288 Wh, 600 W, 4,3 kg, 3 000+ cycles à 80 %, PV 200 W.
- BLUETTI Elite 200 V2 : 2 073,6 Wh, 2 600 W, env. 24,2 kg, 6 000+ cycles à 80 %, PV 1 000 W.
- Jackery Explorer 1000 v2 : 1 070 Wh, 1 500 W, 11 kg.
- Jackery Explorer 2000 v2 : 2 042 Wh, 2 200 W, 17,5 kg.
- AFERIY P210 : 2 048 Wh, 2 400 W, 22 kg, PV 500 W.
- EcoFlow RIVER 3 : disponibilité directe utilisée comme hard gate sur les comparatifs budget/compact, et non comme simple détail éditorial.

## Rankings finaux

| Comparatif | #1 | #2 | #3 |
|---|---|---|---|
| Meilleure station électrique portable | EcoFlow DELTA 3 Plus | BLUETTI Elite 100 V2 | Jackery Explorer 1000 v2 |
| Station électrique pas chère | BLUETTI Elite 30 V2 | Jackery Explorer 300 Plus | — |
| Station électrique puissante | BLUETTI Elite 200 V2 | Jackery Explorer 2000 v2 | AFERIY P210 |
| Station avec panneau solaire | EcoFlow DELTA 3 Plus + panneau bifacial 220 W | Jackery 1000 v2 + SolarSaga 200 W | AFERIY P210 + panneau 400 W |
| Station LiFePO₄ | EcoFlow DELTA 3 Plus | BLUETTI Elite 200 V2 | Jackery Explorer 1000 v2 |
| Station compacte | BLUETTI Elite 30 V2 | Jackery Explorer 300 Plus | — |
| Générateur solaire | Jackery 2000 v2 + 2×SolarSaga 200 W | AFERIY P210 + panneau 400 W | EcoFlow DELTA 3 Plus + panneau bifacial 220 W |

Sur les comparatifs budget et compact, EcoFlow RIVER 3 reste analysée dans l'univers mais n'est pas classée car son hard gate de disponibilité échoue dans le dataset actuel.

## Métriques finales

| Page | Mots | H2 | Liens internes | Cibles uniques | Sources |
|---|---:|---:|---:|---:|---:|
| generateur-solaire | 1709 | 8 | 62 | 40 | 5 |
| meilleure-station-electrique-portable | 1725 | 8 | 62 | 38 | 5 |
| station-electrique-lifepo4 | 1622 | 8 | 62 | 40 | 5 |
| station-electrique-portable-avec-panneau-solaire | 1693 | 8 | 62 | 40 | 5 |
| station-electrique-portable-compacte | 1449 | 8 | 61 | 37 | 5 |
| station-electrique-portable-pas-chere | 1495 | 8 | 61 | 37 | 5 |
| station-electrique-portable-puissante | 1617 | 8 | 62 | 39 | 5 |

## CI final

Runs permanents `34323472260` et `34323632420` : `PASS`.

Validé :
1. génération du shell avec `_generate.py` ;
2. restauration des 12 guides recherchés ;
3. génération des 7 comparatifs avec `_generate_comparatifs.py` ;
4. validation structurelle des 7 datasets via `validate_comparison_data.py` ;
5. recalcul indépendant des scores via `score_comparison.py` ;
6. QA repo-specific via `_validate_comparatifs.py` ;
7. idempotence des 7 pages ;
8. maintien de `noindex, follow` ;
9. absence de modification parasite des guides ;
10. `git diff --check`.

## Verdict final

`APPROVED_FOR_MERGE`.

Validation humaine explicite reçue le 09/09/2026. Le merge est autorisé. Le passage en index n'est pas autorisé : le `noindex, follow` doit rester en place.

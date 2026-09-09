# QA — Comparatifs — 09/09/2026

```yaml
scope: /comparatifs/
status: QA_IN_PROGRESS
methodology_gate: PENDING_CI
editorial_gate: MANUAL_REVIEW_COMPLETE
indexing_status: noindex
publishable: false
human_validation_required: true
```

## Contrôles éditoriaux

- 7 pages routées en `NEW_CONTENT`.
- Critères et poids définis avant le ranking.
- Somme des poids = 100 pour chaque page.
- Au moins un hard gate par comparatif.
- Aucune commission d'affiliation dans le score.
- Aucun test physique revendiqué.
- Faits fabricants distingués des notes éditoriales `INFERRED`.
- Prix datés lorsqu'ils sont mentionnés.
- Limite principale explicitée pour chaque produit classé.
- Exclusions documentées.

## Contrôles factuels

- DELTA 3 Plus : 1 024 Wh, 1 800 W, entrée PV 1 000 W, LFP 4 000 cycles à 80 %, ≤12,5 kg.
- Elite 100 V2 : 1 024 Wh, 1 800 W, 11,5 kg, PV 1 000 W, 4 000+ cycles à 80 %, UPS ≤10 ms.
- Elite 30 V2 : 288 Wh, 600 W, 4,3 kg, 3 000+ cycles à 80 %, PV 200 W.
- Elite 200 V2 : 2 073,6 Wh, 2 600 W, env. 24,2 kg, 6 000+ cycles à 80 %, PV 1 000 W.
- Jackery 1000 v2 : 1 070 Wh, 1 500 W, 11 kg.
- Jackery 2000 v2 : 2 042 Wh, 2 200 W, 17,5 kg.
- AFERIY P210 : 2 048 Wh, 2 400 W, 22 kg, PV 500 W.
- RIVER 3 : disponibilité directe considérée comme hard gate et non comme simple détail éditorial.

## CI attendu

Le workflow doit :
1. régénérer le shell avec `_generate.py` ;
2. rendre les comparatifs via `_generate_comparatifs.py` ;
3. exécuter `validate_comparison_data.py` sur 7 JSON ;
4. exécuter `score_comparison.py` et vérifier que le ranking stocké correspond ;
5. exécuter `_validate_comparatifs.py` ;
6. vérifier l'idempotence ;
7. préserver `noindex, follow` ;
8. lancer `git diff --check`.

## Verdict provisoire

`QA_IN_PROGRESS` jusqu'au premier run CI vert. Le CI ne merge pas automatiquement.

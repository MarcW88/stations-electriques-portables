# QA — Guides — 09/09/2026

```yaml
scope: /guides/
status: APPROVED_FOR_MERGE
structural_gate: PASS
editorial_gate: PASS
indexing_status: noindex
publishable: false
mergeable: true
human_validation_required: true
human_validation_completed: true
workflow_run: 34319164391
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

## Métriques finales

| Guide | Mots | H2 | Liens internes | Cibles uniques | Sources |
|---|---:|---:|---:|---:|---:|
| batterie-nomade-ou-station-electrique | 975 | 8 | 10 | 8 | 3 |
| calculer-autonomie-station-electrique | 985 | 8 | 8 | 6 | 3 |
| calculer-capacite-station-electrique | 949 | 8 | 11 | 8 | 3 |
| comment-choisir-station-electrique-portable | 1117 | 8 | 15 | 12 | 4 |
| duree-vie-cycles-batterie | 1015 | 8 | 7 | 4 | 3 |
| lifepo4-ou-lithium-ion | 1097 | 8 | 8 | 5 | 4 |
| onde-sinusoidale-pure | 955 | 8 | 8 | 5 | 3 |
| recharge-rapide-station-electrique | 964 | 8 | 8 | 7 | 3 |
| recharger-station-electrique-voiture | 958 | 8 | 7 | 5 | 3 |
| station-electrique-portable-comment-ca-marche | 1030 | 8 | 12 | 10 | 3 |
| ups-eps-station-electrique | 1054 | 8 | 10 | 8 | 3 |
| watt-ou-watt-heure | 1007 | 8 | 9 | 7 | 3 |

## CI final

Run `34319164391` : `PASS`.

Validé :
- génération des 12 guides ;
- quality gate structurel du skill ;
- QA repo-specific ;
- minimum 900 mots ;
- réponse answer-first ;
- au moins 7 H2 substantiels ;
- au moins 5 liens internes vers 4 cibles uniques ;
- au moins 3 sources ;
- idempotence sur les 12 pages ;
- maintien de `noindex, follow` ;
- `git diff --check`.

## Validation humaine

Validation explicite reçue le 09/09/2026 pour finaliser et merger la PR #1.

## Verdict final

`APPROVED_FOR_MERGE`.

Le contenu est validé pour fusion dans `main`. Le `noindex, follow` reste volontairement conservé : la fusion ne constitue pas une demande d’indexation.

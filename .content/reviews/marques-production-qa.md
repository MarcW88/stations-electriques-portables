# QA — Pages marques — 09/09/2026

```yaml
scope: /marques/
status: QA_COMPLETE_AWAITING_HUMAN_VALIDATION
entity_gate: PASS
range_gate: PASS
ecosystem_gate: PASS
editorial_gate: PASS
indexing_status: noindex
publishable: false
human_validation_required: true
workflow_run: 34325946244
```

## Contrôles éditoriaux

- 7 pages routées en `BRAND_HUB` + `NEW_CONTENT` car les anciennes pages étaient des shells sans contenu éditorial.
- Entity map et product range versionnés par marque.
- Générations actuelles, précédentes et disponibilités distinguées lorsqu’elles sont documentées.
- Positionnement de marque basé sur les gammes officielles, sans reprendre les slogans fabricants comme conclusions éditoriales.
- Ecosystem map : station, solaire, batterie additionnelle, application et recharge véhicule lorsque pertinent.
- Bloc forces + limites sur chaque hub.
- Bloc « choisir / éviter » sur chaque hub.
- Maillage vers modèles, comparatifs, guides et usages.
- Analyse documentaire explicitée ; aucun test physique ou mesure personnelle revendiqué.
- Prix promotionnels exclus des faits durables.
- `noindex, follow` maintenu sur les 7 pages.

## Points de vigilance documentés

- EcoFlow : nombreuses générations qui se chevauchent ; RIVER 2 / DELTA 2 distinguées des familles plus récentes.
- BLUETTI : anciennes familles AC/EB distinguées des gammes Elite/Apex.
- Jackery : coexistence des familles v2, Plus et d’anciennes Pro.
- AFERIY : nomenclature actuelle Nano / Nomad / Haven explicitée.
- Anker SOLIX : C300 indisponible lors de la vérification ; C1000 première génération traité comme génération précédente face aux Gen 2.
- ALLPOWERS : familles R/VOLIX actuelles distinguées de S700/S2000 plus anciennes.
- IZYWATT : aucune fiche modèle interne disponible ; aucune URL produit inventée. Les usages d’injection réseau sont présentés comme nécessitant une vérification des conditions électriques et réglementaires applicables.

## Métriques finales

| Marque | Mots | H2 | Liens internes | Cibles uniques | Sources |
|---|---:|---:|---:|---:|---:|
| AFERIY | 1202 | 10 | 22 | 18 | 3 |
| ALLPOWERS | 1222 | 10 | 22 | 18 | 4 |
| Anker SOLIX | 1261 | 10 | 22 | 16 | 3 |
| BLUETTI | 1219 | 10 | 24 | 17 | 3 |
| EcoFlow | 1227 | 10 | 26 | 19 | 3 |
| IZYWATT | 1230 | 10 | 20 | 17 | 4 |
| Jackery | 1251 | 10 | 26 | 18 | 4 |

## CI final

Bootstrap `34325853779` : `PASS`.

Workflow permanent `34325946244` : `PASS`.

Validé :
1. reconstruction du shell via `_generate.py` ;
2. restauration des 12 guides recherchés ;
3. restauration des 7 comparatifs recherchés ;
4. génération des 7 hubs marques via `_generate_brands.py` ;
5. validator générique du `brand-content-workflow` ;
6. QA repo-specific via `_validate_brands.py` ;
7. idempotence des 7 hubs ;
8. maintien de `noindex, follow` ;
9. absence de modification parasite des guides et comparatifs ;
10. `git diff --check`.

## Verdict final

`QA_COMPLETE_AWAITING_HUMAN_VALIDATION`.

Le skill, les datasets de marque, les contenus et le workflow permanent sont prêts pour revue en PR. Un CI vert ne déclenche ni merge ni passage en index : validation humaine explicite requise.

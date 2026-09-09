# QA — Pages marques — 09/09/2026

```yaml
scope: /marques/
status: QA_IN_PROGRESS
entity_gate: PENDING_CI
range_gate: PENDING_CI
ecosystem_gate: PENDING_CI
editorial_gate: MANUAL_REVIEW_COMPLETE
indexing_status: noindex
publishable: false
human_validation_required: true
```

## Contrôles éditoriaux préparés

- 7 pages routées en `BRAND_HUB` + `NEW_CONTENT`.
- Entity map et product range versionnés par marque.
- Générations actuelles / précédentes distinguées.
- Positionnement de marque basé sur les gammes officielles.
- Ecosystem map : station, solaire, batterie additionnelle, application, recharge véhicule lorsque pertinent.
- Bloc forces + limites.
- Bloc « choisir / éviter ».
- Maillage vers modèles, comparatifs, guides et usages.
- Analyse documentaire explicitée ; aucun test physique revendiqué.
- Prix promotionnels exclus des faits durables.
- `noindex, follow` maintenu.

## Points de vigilance

- EcoFlow : nombreuses générations qui se chevauchent.
- BLUETTI : anciennes familles AC/EB encore très visibles.
- Jackery : coexistence v2 / Plus / anciennes Pro.
- AFERIY : changement de nomenclature Nano/Nomad/Haven.
- Anker SOLIX : C300 indisponible lors de la vérification ; anciennes C1000/F2000 à ne pas présenter comme gamme 2026 principale.
- ALLPOWERS : variantes R2500 Plus/V2 et statuts de disponibilité à vérifier.
- IZYWATT : aucune fiche modèle interne ; aucune URL produit interne inventée. Injection réseau traitée comme usage nécessitant vérification des conditions électriques/réglementaires, sans reprendre de promesse juridique simplifiée.

## CI attendu

1. `_generate.py` reconstruit le shell ;
2. `_generate_guides.py` restaure les guides ;
3. `_generate_comparatifs.py` restaure les comparatifs ;
4. `_generate_brands.py` applique les 7 hubs ;
5. le validator générique du skill passe ;
6. `_validate_brands.py` contrôle contenu + données structurées ;
7. idempotence vérifiée ;
8. guides/comparatifs ne changent pas ;
9. `noindex, follow` est conservé ;
10. `git diff --check` passe.

## Verdict provisoire

`QA_IN_PROGRESS` jusqu’au premier run CI vert. Le workflow ne merge pas automatiquement.

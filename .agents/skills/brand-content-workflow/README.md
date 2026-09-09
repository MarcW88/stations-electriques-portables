# Brand workflows — stations-electriques-portables.fr

Le cluster `/marques/` utilise désormais deux workflows complémentaires :

- `brand-analysis-workflow` pour auditer une page ou le cluster et décider `KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE` ou `NOINDEX` ;
- `brand-content-workflow` pour produire ou reconstruire une page lorsqu'une réécriture est justifiée.

## Principe

Le site est traité comme une **base de données indépendante et un comparateur technique**, pas comme un catalogue de marques.

Les plans doivent découler de l'intention et des preuves. Il n'y a plus de minimum obligatoire de mots, H2 ou liens, ni de structure fixe `forces / limites / choisir / éviter`.

Les dimensions spécifiques au marché — W, Wh, poids, batterie, MPPT, solaire, UPS/EPS, recharge, extension et compatibilités — sont utilisées lorsqu'elles changent réellement la décision.

## Données du repo

- contenu éditorial : `.content/brand-pages/`
- données / preuves : `.content/brands/`
- audits : `.content/brand-audits/`
- configuration : `brand-workflow.config.yaml`
- rendu : `_generate_brands.py`
- validation machine : `_validate_brands.py`

## Publication

La validation machine ne prouve pas la qualité éditoriale. Le gate substantiel est :

`brand-analysis-workflow / PUBLISH_REVIEW`

Les pages restent `noindex,follow` jusqu'à validation humaine et instruction explicite d'indexation.

## Legacy

Le script `scripts/validate_brand_quality.py` provient de l'ancien workflow générique à quotas. Il n'est plus utilisé par la CI ni comme gate de publication ; `_validate_brands.py` contrôle uniquement les invariants machine, tandis que `brand-analysis-workflow` porte la QA substantielle et inter-pages.

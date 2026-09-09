# Comparison Content Workflow

Workflow portable pour créer des comparatifs produits SEO/GEO orientés affiliation.

## Ce qu'il ajoute par rapport au workflow Guides

Le cœur n'est plus uniquement éditorial.

Il impose :

1. intention
2. univers produit
3. équivalence
4. evidence ledger
5. critères AVANT gagnant
6. pondération
7. hard gates
8. scoring
9. justification du ranking
10. couche affiliation
11. rédaction
12. QA

## Installation

Copier le dossier dans :

`.agents/skills/comparison-content-workflow/`

Puis copier :

`comparison-workflow.config.example.yaml`

à la racine sous :

`comparison-workflow.config.yaml`

## Fichier obligatoire par comparatif

Créer :

`.content/comparisons/<slug>.yaml`

à partir de :

`references/comparison-data-template.yaml`

## Utilisation recommandée

Exemple :

> Applique `comparison-content-workflow` à `/comparatifs/meilleur-bloc-notes-numerique/`.
> Définis les critères et poids avant de scorer.
> Utilise uniquement des sources vérifiées.
> Ne tiens jamais compte des commissions dans le classement.
> Garde la page noindex jusqu'à validation.

## Scripts

- `scripts/validate_comparison_data.py`
  - vérifie la structure méthodologique.
- `scripts/score_comparison.py`
  - calcule les scores brut et ajusté par confiance.

Les scripts utilisent JSON pour éviter une dépendance obligatoire à PyYAML.
Le template principal reste en YAML pour la lisibilité humaine.

## Important

Un score n'est pas une vérité scientifique.

Le scoring sert à :
- expliciter les arbitrages ;
- rendre le ranking traçable ;
- empêcher les critères de changer après le résultat ;
- documenter l'incertitude.

Il ne remplace jamais le jugement éditorial.

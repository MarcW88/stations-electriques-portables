# Audit global des images — stations-electriques-portables

Date : 2026-10-22 · Inventaire GitHub : branche main

## Portée et réserves

- **82/82 pages HTML recensées**, sans exclusion de section ; arbre GitHub non tronqué.
- **Aucun fichier image du site détecté dans l'arbre** ; deux SVG seulement, internes à des skills.
- Il s'agit d'un **pré-audit éditorial page par page établi à partir de l'inventaire, des intentions par URL et des règles de l'agent**. L'inspection exhaustive des 82 HTML et leur rendu desktop/mobile ne sont **pas encore effectués**. Les recommandations individuelles restent à confirmer sur la page réelle.
- Aucune image générée, aucun prompt PENDING, aucun marqueur ajouté. Respecter 0–1 image IA par page et le refus des fausses photos produit ou faux tests.

## Exécution — 22 octobre 2026

- Illustrations techniques réellement intégrées (HTML et source) : `/solaire/generateur-solaire/`, `/solaire/mppt/`, `/solaire/quel-panneau-solaire-pour-station-electrique/`, `/solaire/recharger-station-electrique-panneau-solaire/`, `/guides/watt-ou-watt-heure/`, `/puissance-capacite/station-electrique-1000wh/`, `/puissance-capacite/station-electrique-2000wh/`.
- Visuels contextuels SVG déjà intégrés : `/usages/station-electrique-camping/` et `/usages/station-electrique-van/`. Ces dessins ne remplissent pas entièrement la recommandation de photographie éditoriale ; **à remplacer par de vraies photos génériques adaptées**, sans prétendre représenter des tests.
- Autres pages : non modifiées par cette passe ; les pages modèles, marques et comparatifs exigent des photographies officielles authentiques. Aucun visuel produit IA inventé.
- Génération/récupération des photos requises, QA visuelle et vérification du domaine public : **non terminées**. Ne pas assimiler les fichiers GitHub à une validation du site en ligne.

## Mise en œuvre complémentaire — 22 octobre 2026

- **Image réelle de produit :** `/modeles/ecoflow-delta-2/` : photographie de l’EcoFlow DELTA 2 depuis EcoFlow.nl, intégrée dans le HTML et dans `_generate.py`. Il s'agit d'une image distante ; droits de réutilisation et pérennité du lien restent à examiner.
- **Diagramme exact W / Wh :** intégré aux quatre pages `/puissance-capacite/station-electrique-{500w,1000w,2000w,3000w}/` et à leurs modules sources.
- **Pages modèles restantes :** sans photographie non vérifiée, conformément au statut `VRAIE_IMAGE`; les images IA et les SVG génériques ne satisfont pas la décision.
- **Pages candidates IA :** créations photographiques non téléversées sur le domaine, donc **non terminées**. **L'ensemble des 82 décisions n'est pas encore implémenté.**

## Synthèse

- VRAIE_IMAGE : 39 pages
- NOT_NEEDED : 4 pages
- REVIEW : 5 pages
- SCHEMA_VERIFIE : 22 pages
- CANDIDAT : 12 pages

## Backlog — toutes les pages

| Page | Image | Type recommandé | Emplacement provisoire | IA | Priorité | Statut |
|---|---|---|---|---|---|---|
| `/a-propos/` | OPTIONNEL | Photo authentique équipe / méthode | Présentation | NON | P2 | VRAIE_IMAGE |
| `/accessoires/batterie-extension/` | OUI | Photo précise du connecteur ou accessoire | Critère de compatibilité | NON | P2 | VRAIE_IMAGE |
| `/accessoires/cables-adaptateurs-solaires/` | OUI | Photo précise du connecteur ou accessoire | Critère de compatibilité | NON | P2 | VRAIE_IMAGE |
| `/accessoires/chargeur-voiture-station-electrique/` | OUI | Photo précise du connecteur ou accessoire | Critère de compatibilité | NON | P2 | VRAIE_IMAGE |
| `/accessoires/` | OUI | Photo précise du connecteur ou accessoire | Critère de compatibilité | NON | P2 | VRAIE_IMAGE |
| `/accessoires/panneau-solaire-portable/` | OUI | Photo précise du connecteur ou accessoire | Critère de compatibilité | NON | P2 | VRAIE_IMAGE |
| `/calculateur-autonomie/` | NON | Aucune image | — | NON | P3 | NOT_NEEDED |
| `/comparatifs/generateur-solaire/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/meilleure-station-electrique-portable/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/station-electrique-lifepo4/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/station-electrique-portable-avec-panneau-solaire/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/station-electrique-portable-compacte/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/station-electrique-portable-pas-chere/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/comparatifs/station-electrique-portable-puissante/` | OUI | Photographies des modèles réellement comparés | Blocs de comparaison | NON | P1 | VRAIE_IMAGE |
| `/contact/` | NON | Aucune image | — | NON | P3 | NOT_NEEDED |
| `/guides/batterie-nomade-ou-station-electrique/` | OPTIONNEL | Scène éditoriale générique à valider | Exemple principal | OUI | P3 | REVIEW |
| `/guides/calculer-autonomie-station-electrique/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/calculer-capacite-station-electrique/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/comment-choisir-station-electrique-portable/` | OPTIONNEL | Scène éditoriale générique à valider | Exemple principal | OUI | P3 | REVIEW |
| `/guides/duree-vie-cycles-batterie/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/` | OPTIONNEL | Scène éditoriale générique à valider | Exemple principal | OUI | P3 | REVIEW |
| `/guides/lifepo4-ou-lithium-ion/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/onde-sinusoidale-pure/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/recharge-rapide-station-electrique/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/recharger-station-electrique-voiture/` | OPTIONNEL | Scène éditoriale générique à valider | Exemple principal | OUI | P3 | REVIEW |
| `/guides/station-electrique-portable-comment-ca-marche/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/ups-eps-station-electrique/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/guides/watt-ou-watt-heure/` | OPTIONNEL | Schéma explicatif factuellement exact | Explication technique | NON | P2 | SCHEMA_VERIFIE |
| `/` | OPTIONNEL | Photographie éditoriale d'un usage réel générique | Introduction | OUI | P2 | REVIEW |
| `/marques/aferiy/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/allpowers/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/anker-solix/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/bluetti/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/ecoflow/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/izywatt/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/marques/jackery/` | OUI | Logo et photo officielle de la marque | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/mentions-legales/` | NON | Aucune image | — | NON | P3 | NOT_NEEDED |
| `/methode-de-test/` | OPTIONNEL | Photo authentique équipe / méthode | Présentation | NON | P2 | VRAIE_IMAGE |
| `/modeles/aferiy-p210/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/allpowers-s700/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/anker-solix-c1000/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/bluetti-ac180/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/bluetti-ac200max/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/bluetti-eb3a/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/bluetti-elite-200-v2/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/ecoflow-delta-2/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/ecoflow-delta-3-plus/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/ecoflow-delta-pro/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/ecoflow-river-2/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/ecoflow-river-3/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/jackery-explorer-1000-v2/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/jackery-explorer-2000-v2/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/modeles/jackery-explorer-3000-pro/` | OUI | Photo officielle du modèle exact | Présentation du produit | NON | P1 | VRAIE_IMAGE |
| `/puissance-capacite/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-1000w/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-1000wh/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-2000w/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-2000wh/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-3000w/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-500w/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/puissance-capacite/station-electrique-500wh/` | OPTIONNEL | Diagramme de puissance / énergie exact | Près du calcul | NON | P2 | SCHEMA_VERIFIE |
| `/solaire/generateur-solaire/` | OUI | Schéma électrique / énergie exact | Section explicative | NON | P1 | SCHEMA_VERIFIE |
| `/solaire/` | OUI | Schéma électrique / énergie exact | Section explicative | NON | P1 | SCHEMA_VERIFIE |
| `/solaire/mppt/` | OUI | Schéma électrique / énergie exact | Section explicative | NON | P1 | SCHEMA_VERIFIE |
| `/solaire/panneau-solaire-portable/` | OUI | Photo éditoriale de panneau générique déployé | Section explicative | OUI | P2 | CANDIDAT |
| `/solaire/quel-panneau-solaire-pour-station-electrique/` | OUI | Schéma électrique / énergie exact | Section explicative | NON | P1 | SCHEMA_VERIFIE |
| `/solaire/recharger-station-electrique-panneau-solaire/` | OUI | Schéma électrique / énergie exact | Section explicative | NON | P1 | SCHEMA_VERIFIE |
| `/transparence-affiliation/` | NON | Aucune image | — | NON | P3 | NOT_NEEDED |
| `/usages/` | OUI | Photographie contextuelle générique de usages | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-camping-car/` | OUI | Photographie contextuelle générique de camping car | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-camping/` | OUI | Photographie contextuelle générique de camping | Après contexte d'usage | OUI | P1 | CANDIDAT |
| `/usages/station-electrique-chantier/` | OUI | Photographie contextuelle générique de chantier | Après contexte d'usage | OUI | P1 | CANDIDAT |
| `/usages/station-electrique-coupure-courant/` | OUI | Photographie contextuelle générique de coupure courant | Après contexte d'usage | OUI | P1 | CANDIDAT |
| `/usages/station-electrique-cpap/` | OUI | Photographie contextuelle générique de cpap | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-glaciere/` | OUI | Photographie contextuelle générique de glaciere | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-maison/` | OUI | Photographie contextuelle générique de maison | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-photo-video/` | OUI | Photographie contextuelle générique de photo video | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-teletravail/` | OUI | Photographie contextuelle générique de teletravail | Après contexte d'usage | OUI | P2 | CANDIDAT |
| `/usages/station-electrique-van/` | OUI | Photographie contextuelle générique de van | Après contexte d'usage | OUI | P1 | CANDIDAT |

## Exécution ultérieure

Valider sur rendu réel si l'image est nécessaire et déjà présente. Pour les scènes IA, créer une requête dédiée d'après le template `.content/image-requests/_template.json`, avec marker dans la source de vérité, validation éditoriale et statut adapté. Pour les marques, modèles et comparatifs, obtenir des médias officiels autorisés. Pour les explications électriques, produire des schémas vérifiables. Aucun changement d'indexation.

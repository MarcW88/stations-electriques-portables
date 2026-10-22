---
name: comparison-content-workflow
description: Workflow générique pour créer, récupérer et valider des comparatifs produits SEO/GEO orientés affiliation. Utiliser pour les pages "meilleur X", "X vs Y", "meilleur X pour Y", "pas cher", "professionnel", "étudiant" et autres pages transactionnelles comparatives. Le workflow impose des critères définis avant le classement, un registre de preuves, un scoring auditable, une justification des recommandations et une QA affiliation/SEO/GEO sans fake test.
---

# Comparison Content Workflow

## Objectif

Produire des comparatifs réellement utiles à la décision d'achat, auditables et compatibles avec un modèle d'affiliation.

Le workflow ne doit jamais commencer par :

> "Quels produits voulons-nous recommander ?"

Il commence par :

> "Quelle décision l'utilisateur essaie-t-il de prendre, quels produits sont réellement éligibles, quels critères changent cette décision, et quelles preuves permettent de les comparer ?"

Principe central :

> **Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.**

---

# 1. Entrées obligatoires

Lire avant toute production :

- instructions du repo (`AGENTS.md`, `README`, etc.) ;
- `comparison-workflow.config.yaml` ;
- page cible existante si elle existe ;
- source de vérité éditoriale ;
- analyse sémantique ;
- pages comparatives voisines ;
- pages marques / produits / usages / guides ;
- données marché ou disponibilités si nécessaires ;
- méthodologie de test du site si elle existe ;
- règles d'affiliation ;
- page de référence qualitative définie par `quality_reference`.

Réutiliser les skills existants lorsqu'ils sont présents :

- `search-intent`
- `affiliate-value`
- `fact-check`
- `content-refresh`
- `internal-linking-audit`
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-technical`
- `seo-best-practices`
- `editorial-qa`

---

# 2. Router le type de comparatif

Choisir un type dominant.

## A. Best overall
Exemple : `meilleur bloc-notes numérique`

Question :
> quel produit offre le meilleur équilibre global pour l'intention cible ?

## B. Best for use case
Exemple : `meilleur bloc-notes numérique étudiant`

Question :
> quel produit est le plus adapté à un job-to-be-done précis ?

## C. Budget
Exemple : `meilleur bloc-notes numérique pas cher`

Question :
> quel produit satisfait le besoin avec le meilleur compromis sous contrainte de budget ?

## D. Feature-specific
Exemple : `meilleur bloc-notes numérique couleur`

Question :
> quel produit répond le mieux à une caractéristique déterminante ?

## E. Head-to-head
Exemple : `Kindle Scribe vs reMarkable`

Question :
> lequel des deux convient le mieux selon les usages ?

Le type de page détermine :
- critères ;
- poids ;
- univers de produits ;
- architecture ;
- niveau de scoring.

---

# 3. Mode RECOVERY ou NEW_CONTENT

## RECOVERY
Si une page existe déjà :
- conserver les passages utiles ;
- conserver les données valides ;
- conserver les liens utiles ;
- conserver le classement uniquement s'il résiste à la nouvelle méthodologie.

Ne jamais préserver un gagnant uniquement parce qu'il était déjà #1.

## NEW_CONTENT
Si la page est vide :
- construire d'abord les données ;
- rédiger ensuite.

---

# 4. Search intent avant sélection produit

Utiliser `search-intent`.

Définir :

- requête principale ;
- variantes ;
- intention dominante ;
- sous-intentions ;
- niveau de maturité ;
- contrainte principale ;
- résultat attendu ;
- risque de cannibalisation.

Exemple :

`meilleur bloc-notes numérique étudiant`

ne doit pas être traité comme :

`meilleur bloc-notes numérique`

avec simplement "étudiant" ajouté dans l'introduction.

Les critères et les poids doivent changer.

---

# 5. Product Universe

Construire la liste des produits éligibles **avant de choisir les gagnants**.

Pour chaque produit :

- marque ;
- modèle ;
- génération ;
- statut actuel ;
- disponibilité ;
- prix actuel si utilisé ;
- stylet inclus ou non ;
- accessoires obligatoires ;
- abonnement éventuel ;
- principales fonctions ;
- sources officielles.

Classer les candidats :

- `ELIGIBLE`
- `CONDITIONALLY_ELIGIBLE`
- `OUTDATED`
- `NOT_COMPARABLE`
- `EXCLUDED`

Documenter toute exclusion.

## Règle
Un produit ne doit pas être ajouté uniquement parce qu'il existe un lien affilié.

---

# 6. Equivalence Engine

Avant de comparer, déterminer si les produits sont réellement comparables.

Évaluer :

- job-to-be-done principal ;
- catégorie fonctionnelle ;
- taille / capacité ;
- workflow ;
- fonctions clés ;
- accessoires nécessaires ;
- logiciel ;
- coûts récurrents ;
- contraintes ;
- public cible.

Attribuer :

- `EXACT`
- `FUNCTIONALLY_COMPARABLE`
- `PARTIALLY_COMPARABLE`
- `NOT_COMPARABLE`

Pour les comparaisons partielles, expliciter les dimensions non comparables.

---

# 7. Evidence Ledger

Aucune note ne doit être attribuée avant création du registre de preuves.

Pour chaque donnée :

| Product | Criterion | Claim | Value | Source | Date | Evidence class |
|---|---|---|---|---|---|---|

Classes :

- `VERIFIED` — source primaire actuelle ;
- `SUPPORTED` — source secondaire crédible ;
- `INFERRED` — conclusion raisonnable depuis plusieurs faits ;
- `USER_PATTERN` — expérience agrégée de plusieurs utilisateurs ;
- `FIRST_HAND` — uniquement si l'utilisateur a fourni un vrai test ;
- `UNKNOWN` — non vérifié ;
- `PROHIBITED` — ne doit pas être publié.

Ne jamais transformer `INFERRED` ou `USER_PATTERN` en expérience directe.

---

# 8. Définir les critères AVANT le classement

Construire les critères depuis :

- intention ;
- JTBD ;
- sous-questions ;
- contraintes ;
- différences réellement décisionnelles.

Exemples possibles :

- qualité d'écriture ;
- annotation PDF ;
- organisation ;
- export ;
- OCR ;
- cloud ;
- applications ;
- taille ;
- couleur ;
- autonomie ;
- lecture ;
- simplicité ;
- coût total ;
- abonnement ;
- accessoires ;
- réparabilité ;
- disponibilité.

Ne pas utiliser systématiquement tous les critères.

## Règle
Un critère doit être :
- pertinent pour l'intention ;
- comparable ;
- mesurable ou analysable ;
- soutenu par des preuves.

---

# 9. Pondération

Définir le poids des critères avant calcul.

La somme des poids = 100.

Exemple :

| Critère | Poids |
|---|---:|
| Écriture | 25 |
| PDF | 20 |
| Organisation | 15 |
| Export/cloud | 15 |
| Coût total | 15 |
| Lecture | 10 |

Documenter pourquoi le poids change selon l'intention.

## Interdit
Modifier les poids après avoir vu quel produit gagne, sauf erreur méthodologique explicitement documentée.

---

# 10. Normalisation et scoring

Utiliser une échelle stable, par exemple 0–10.

Pour chaque score, conserver :

- valeur ;
- justification ;
- evidence class ;
- éventuelle pénalité d'incertitude.

Score brut :

`criterion_score = normalized_score × criterion_weight`

Score total :

`total = Σ criterion_score / 10`

## Confidence factor

Optionnel :

- VERIFIED = 1.00
- SUPPORTED = 0.95
- INFERRED = 0.85
- USER_PATTERN = 0.80
- UNKNOWN = interdit pour un critère important

Score confiance :

`confidence_adjusted = normalized_score × confidence_factor`

Le ranking final doit conserver :
- score brut ;
- score ajusté ;
- niveau de confiance.

---

# 11. Hard Gates

Certains critères sont éliminatoires.

Exemples :

- produit non disponible ;
- fonction indispensable absente ;
- incompatibilité avec le besoin ;
- génération obsolète ;
- données essentielles non vérifiables ;
- prix dépassant une contrainte explicite ;
- abonnement obligatoire incompatible avec l'intention.

Un produit qui échoue un hard gate ne doit pas gagner grâce à un bon score moyen.

---

# 12. Total Solution Cost

Comparer le coût de la configuration réellement utilisable.

Formule générique :

`TSC = appareil + accessoire obligatoire + protection nécessaire + abonnement utile + consommables + autres coûts indispensables`

Éviter de comparer :
- un appareil nu ;
- à un bundle complet.

Les coûts non indispensables ne doivent pas être ajoutés mécaniquement.

---

# 13. Rank Justification

Chaque produit classé doit répondre à :

- pourquoi il est présent ;
- pour qui il est recommandé ;
- pour qui il ne l'est pas ;
- avantage principal ;
- limitation principale ;
- critère qui fait réellement bouger la décision ;
- alternative logique ;
- pourquoi il est classé à cette position.

Pour le #1 :

> expliquer ce qu'il gagne **et ce qu'il ne gagne pas**.

Un "meilleur" absolu sans critères explicites est interdit.

---

# 14. Honest Comparison Standard

Le comparatif doit :

- montrer les désavantages du produit recommandé ;
- éviter le cherry-picking ;
- distinguer différence de spec et différence d'usage ;
- distinguer prix affiché et coût réel ;
- distinguer test réel et desk research ;
- distinguer fait, déduction et opinion ;
- signaler les données instables.

La commission d'affiliation ne peut jamais influencer :
- inclusion ;
- score ;
- classement ;
- formulation des défauts.

---

# 15. Architecture éditoriale

L'ordre exact dépend de l'intention, mais une page "best X" peut contenir :

1. réponse rapide / sélection ;
2. méthodologie ;
3. tableau de comparaison ;
4. critères déterminants ;
5. produits classés ;
6. pour quel profil chaque produit convient ;
7. limites / exclusions ;
8. coût total ;
9. comment choisir ;
10. liens vers guides/usages/marques ;
11. sources / fraîcheur.

Pour `A vs B` :

1. verdict rapide conditionnel ;
2. différences qui comptent ;
3. tableau ;
4. critère 1 ;
5. critère 2 ;
6. critère 3 ;
7. coût total ;
8. pour qui choisir A ;
9. pour qui choisir B ;
10. verdict final ;
11. sources.

---

# 16. Rédaction produit

Chaque bloc produit doit apporter de la décision, pas recopier une fiche constructeur.

Structure possible :

- verdict ;
- pourquoi il se distingue ;
- avantage déterminant ;
- limite déterminante ;
- pour qui ;
- pour qui non ;
- alternative ;
- CTA.

Éviter les fiches symétriques artificielles si les produits nécessitent des explications différentes.

---

# 17. Affiliate Value

Utiliser `affiliate-value`.

Règle :

> la page doit rester utile si tous les liens affiliés disparaissent.

Vérifier :

- commission non prise en compte dans le ranking ;
- défauts visibles ;
- alternatives honnêtes ;
- aucune fausse urgence ;
- aucune fausse disponibilité ;
- prix datés ;
- disclosure claire.

---

# 18. Fact-check obligatoire

Utiliser `fact-check` après la première rédaction.

Vérifier notamment :

- dimensions ;
- écran ;
- autonomie annoncée ;
- formats ;
- compatibilités ;
- cloud ;
- stylet ;
- accessoires ;
- prix ;
- abonnements ;
- génération ;
- disponibilité ;
- comparaisons telles que plus rapide / plus léger / moins cher.

Statuts :

- `CONFIRMED`
- `PARTIAL`
- `UNVERIFIED`
- `CONTRADICTED`
- `OUTDATED`

---

# 19. Search Intent QA

Après rédaction :

- le ranking répond-il réellement à la requête ?
- les poids reflètent-ils l'intention ?
- le #1 est-il cohérent avec les hard gates ?
- une autre page du site répond-elle mieux à l'intention ?
- le contenu est-il devenu trop générique ?

---

# 20. Internal Linking

Utiliser `internal-linking-audit`.

Pour chaque comparatif, prévoir selon pertinence :

- guides explicatifs ;
- usages ;
- marques ;
- fiches modèles ;
- autres comparatifs ;
- prix/budget ;
- abonnements ;
- technologie.

Le comparatif est un hub décisionnel, pas une impasse commerciale.

---

# 21. Finition éditoriale

Exécuter ensuite :

1. `natural-writing`
2. `humanizer`
3. `general-writing`
4. `anti-ai-slop`
5. `seo-drift`

Le `seo-drift` compare aussi :
- critères initiaux ;
- poids ;
- scores ;
- ranking final.

Toute modification du classement sans modification documentée des données ou de la méthode est un blocker.

---

# 22. SEO

Utiliser `seo-best-practices` et `seo-technical`.

Vérifier :

- title ;
- H1 ;
- réponse initiale ;
- sous-intentions ;
- entités ;
- maillage ;
- canonical ;
- robots ;
- données structurées si pertinentes ;
- pagination si applicable ;
- crawlabilité.

---

# 23. GEO

Vérifier :

- verdict autonome ;
- relations explicites produit → usage ;
- critères lisibles ;
- méthodologie résumable ;
- tableaux interprétés ;
- sources identifiables ;
- entités complètes ;
- datation des prix et informations instables.

Éviter les verdicts absolus non contextualisés.

Préférer :

> "Le modèle A est le meilleur choix pour X parce que..."

à :

> "Le modèle A est le meilleur."

---

# 24. Comparison Quality Gate

Le contrôle automatique peut vérifier :

- présence d'une méthodologie ;
- présence d'un fichier de scoring ;
- somme des poids = 100 ;
- produits classés présents dans les données ;
- score justifié ;
- source pour les critères majeurs ;
- hard gates documentés ;
- maillage ;
- sources ;
- tableaux contextualisés ;
- présence des limites ;
- noindex si brouillon.

Il ne doit jamais déclarer automatiquement :

- fact-check PASS ;
- qualité du ranking PASS ;
- Humanizer PASS ;
- GEO PASS ;
- affiliation éthique PASS.

---

# 25. Échecs automatiques

FAIL si :

- gagnant choisi avant critères ;
- poids modifiés pour produire un gagnant ;
- commission dans le scoring ;
- score sans justification ;
- produit obsolète classé sans justification ;
- hard gate ignoré ;
- comparaison de configurations non équivalentes ;
- fake test ;
- avantage comparatif non vérifié ;
- défauts significatifs masqués ;
- données importantes sans date ;
- page marchande déguisée ;
- maillage quasi absent ;
- source de vérité non mise à jour.

---

# 26. Statuts

- `UNIVERSE_READY`
- `EVIDENCE_READY`
- `SCORING_READY`
- `DRAFT_READY`
- `QA_IN_PROGRESS`
- `REVISION_REQUIRED`
- `HUMAN_APPROVED`
- `PUBLISHABLE`

Le ranking peut être `SCORING_READY` avant qu'une ligne éditoriale ne soit écrite.

---

# 27. Publication

Par défaut :

- conserver `noindex` si configuré ;
- ne pas merger ;
- ne pas publier ;
- ne pas déployer.

Autorisation explicite nécessaire.

---

# 28. Fichiers persistants

Pour chaque comparatif :

`.content/comparisons/<slug>.yaml`

doit contenir :

- intent ;
- univers ;
- exclusions ;
- critères ;
- poids ;
- hard gates ;
- evidence ledger ;
- scores ;
- classement ;
- niveau de confiance ;
- date de recherche.

Les briefs et reviews restent séparés.

Le texte final ne doit jamais être la seule source expliquant pourquoi le ranking existe.

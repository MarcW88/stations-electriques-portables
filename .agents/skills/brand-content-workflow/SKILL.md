---
name: brand-content-workflow
description: Workflow générique pour créer, récupérer, structurer et valider des pages marque SEO/GEO à forte valeur éditoriale et commerciale. Utiliser pour les hubs de marque, pages produit, analyses/reviews, services, accessoires et alternatives. Le workflow impose une cartographie d'entités, une gamme actuelle vérifiée, un ecosystem map, un positionnement de marque explicite, un maillage profond et une QA spécifique aux pages commerciales sans inventer de tests ni d'expérience produit.
---

# Brand Content Workflow

## Objectif

Construire des pages marque qui fonctionnent à la fois comme :

- **entity hubs** ;
- **commercial hubs** ;
- **navigation hubs** ;
- **sources de contexte GEO** ;
- **portes d'entrée vers produits, comparatifs, guides et usages**.

Une bonne page marque ne doit pas seulement répondre à :

> "Qu'est-ce que cette marque ?"

Elle doit aussi permettre de comprendre :

> Quels produits sont actuellement dans sa gamme ?  
> Quelle est sa logique d'écosystème ?  
> Quelles différences changent réellement la décision ?  
> Pour quels usages la marque est-elle adaptée ou non ?  
> Vers quelles pages du site faut-il poursuivre ?

Principe central :

> **Entités avant prose. Gamme actuelle avant recommandation. Écosystème avant positionnement. Maillage avant conversion.**

---

# 1. Entrées obligatoires

Lire avant toute production :

- instructions du repo (`AGENTS.md`, `README`, etc.) ;
- `brand-workflow.config.yaml` ;
- page cible existante ;
- source de vérité éditoriale ;
- architecture des pages marque ;
- pages produits associées ;
- pages comparatifs associées ;
- pages guides / usages associées ;
- données sémantiques si disponibles ;
- informations officielles actuelles de la marque ;
- page de référence qualitative définie par `quality_reference`.

Réutiliser les skills existants lorsqu'ils sont présents :

- `search-intent`
- `content-refresh`
- `affiliate-value`
- `fact-check`
- `internal-linking-audit`
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-technical`
- `seo-best-practices`
- `editorial-qa`
- `comparison-content-workflow`
- `guide-content-workflow`

---

# 2. Routing obligatoire

Classer la page avant de rédiger.

## BRAND_HUB

Exemple :

`/marques/remarkable/`

Fonction :
- définir la marque ;
- présenter la gamme actuelle ;
- cartographier l'écosystème ;
- expliquer les grandes forces / limites ;
- router vers produits, comparatifs, guides et usages.

## PRODUCT

Exemple :

`/marques/remarkable/paper-pro/`

Fonction :
- présenter un produit précis ;
- vérifier sa génération et son statut ;
- expliquer ses fonctions ;
- montrer à qui il convient ;
- relier vers comparatifs et alternatives.

## REVIEW

Exemple :

`/marques/remarkable/paper-pro-avis/`

Fonction :
- analyser un produit ;
- distinguer clairement desk research, prise en main et test réel ;
- présenter forces, limites, usages et alternatives.

Si aucun test réel n'existe :
- ne pas utiliser de langage de test ;
- ne pas présenter de scores mesurés ;
- utiliser "analyse", "évaluation documentaire" ou équivalent.

## SERVICE

Exemple :

`/marques/remarkable/connect/`

Fonction :
- expliquer un service, abonnement ou logiciel ;
- détailler ce qui est inclus ou non ;
- expliquer le coût, les limites, l'impact sur le workflow et la dépendance éventuelle.

## ACCESSORY_HUB

Exemple :

`/marques/remarkable/accessoires/`

Fonction :
- expliquer les catégories d'accessoires ;
- distinguer nécessaires / optionnels ;
- relier vers produits compatibles ;
- éviter le catalogue sans contexte.

## ALTERNATIVES

Exemple :

`/marques/remarkable/alternatives/`

Fonction :
- expliquer quand quitter l'écosystème ;
- identifier les alternatives cohérentes ;
- déléguer la comparaison détaillée à `comparison-content-workflow` lorsque pertinent.

---

# 3. Mode RECOVERY ou NEW_CONTENT

## RECOVERY

Si une page existe déjà :

Conserver :
- faits toujours valides ;
- structure utile ;
- liens pertinents ;
- passages différenciants ;
- tableaux exploitables.

Réparer :
- gamme obsolète ;
- entités manquantes ;
- services mal expliqués ;
- positionnement trop vague ;
- maillage pauvre ;
- contenu trop promotionnel ;
- sections trop courtes ;
- liens vers anciens modèles ;
- produits discontinués présentés comme actuels.

## NEW_CONTENT

Si page vide ou inexistante :
- produire d'abord les données structurées ;
- rédiger ensuite.

---

# 4. Entity Map obligatoire

Créer avant rédaction :

```yaml
brand:
products:
services:
software:
technologies:
accessories:
integrations:
formats:
use_cases:
competitors:
```

Pour chaque relation importante, expliciter :

`BRAND -> PRODUCT`  
`PRODUCT -> TECHNOLOGY`  
`PRODUCT -> USE_CASE`  
`BRAND -> SOFTWARE`  
`BRAND -> SERVICE`  
`SERVICE -> FEATURE`  
`BRAND -> INTEGRATION`  
`BRAND -> COMPETITOR`

Exemple :

`reMarkable -> Paper Pro`  
`Paper Pro -> Gallery 3 / Canvas Color`  
`reMarkable -> Connect`  
`Connect -> cloud sync`

La page ne doit pas seulement contenir les mots : elle doit expliquer leurs relations.

---

# 5. Current Product Range

Construire la gamme actuelle.

Statuts possibles :

- `CURRENT`
- `PREVIOUS_GENERATION`
- `DISCONTINUED`
- `ANNOUNCED`
- `REGION_SPECIFIC`
- `UNKNOWN`

Pour chaque produit :

- nom exact ;
- génération ;
- date ou période de lancement si utile ;
- statut ;
- taille ;
- technologie ;
- fonctions principales ;
- compatibilités ;
- accessoires ;
- prix actuel si utilisé ;
- source officielle ;
- date de vérification.

## Règle

Une page hub ne peut pas mélanger générations actuelles et anciennes sans les distinguer.

---

# 6. Brand Proposition

Formuler une proposition claire :

> Quelle est la logique propre de cette marque ?

La proposition doit venir de faits vérifiables.

Exemples de dimensions :

- spécialisation ;
- ouverture logicielle ;
- simplicité ;
- lecture ;
- écriture ;
- organisation ;
- cloud ;
- applications tierces ;
- couleur ;
- accessoires ;
- service.

## Interdit

Écrire :

> "Cette marque est la meilleure pour..."

sans critères ou sans comparaison documentée.

Préférer :

> "La marque privilégie X, ce qui la rend particulièrement cohérente pour Y, mais moins adaptée à Z."

---

# 7. Ecosystem Map

Construire le parcours fonctionnel.

Exemple générique :

```text
Hardware
↓
Stylus
↓
OS
↓
Notes
↓
PDF
↓
OCR
↓
Cloud
↓
Export
↓
Third-party services
```

Pour chaque étape :
- ce qui est natif ;
- ce qui est optionnel ;
- ce qui dépend d'un abonnement ;
- ce qui nécessite un service tiers ;
- ce qui ne fonctionne pas.

Le but est de montrer **comment les données circulent** dans l'écosystème.

---

# 8. Brand Evidence Ledger

Créer :

| Entity | Claim | Source | Date | Status | Freshness |
|---|---|---|---|---|---|

Statuts :

- `VERIFIED`
- `SUPPORTED`
- `INFERRED`
- `UNKNOWN`
- `OUTDATED`
- `CONTRADICTED`

À vérifier en priorité :

- gamme actuelle ;
- services ;
- abonnement ;
- export ;
- cloud ;
- formats ;
- applications ;
- accessoires ;
- compatibilités ;
- prix ;
- disponibilité.

---

# 9. Architecture BRAND_HUB

Architecture recommandée :

1. réponse rapide ;
2. ce qui distingue la marque ;
3. gamme actuelle ;
4. tableau produits ;
5. ecosystem map ;
6. logiciels / services ;
7. forces ;
8. limites ;
9. qui devrait choisir cette marque ;
10. qui devrait éviter cette marque ;
11. alternatives principales ;
12. liens vers comparatifs ;
13. liens vers guides / usages ;
14. sources.

## Tableau gamme

Doit être contextualisé et interprété.

Exemple :

| Modèle | Format | Couleur | Positionnement | Limite |
|---|---|---|---|---|

Le tableau ne doit pas remplacer l'analyse.

---

# 10. Architecture PRODUCT

1. réponse rapide ;
2. statut actuel ;
3. à qui il s'adresse ;
4. caractéristiques décisionnelles ;
5. workflow ;
6. formats / cloud / export ;
7. accessoires ;
8. limites ;
9. alternatives ;
10. comparatifs ;
11. guides utiles ;
12. sources.

Ne pas transformer en fiche constructeur recopiée.

---

# 11. Architecture REVIEW

Si test réel documenté :

- méthodologie ;
- conditions ;
- durée ;
- limites ;
- résultats ;
- observations ;
- verdict.

Sinon :

- mention explicite "analyse documentaire" ;
- aucune formulation du type "nous avons testé" ;
- aucun score simulant une mesure ;
- aucune sensation d'écriture présentée comme vécue ;
- distinguer faits / déductions / retours utilisateurs agrégés.

Structure :

1. verdict ;
2. niveau de preuve ;
3. points forts ;
4. limites ;
5. fonctionnalités ;
6. workflow ;
7. pour qui ;
8. pour qui non ;
9. alternatives ;
10. sources.

---

# 12. Architecture SERVICE

1. ce qu'est le service ;
2. fonctions ;
3. gratuit / payant ;
4. ce qui fonctionne sans ;
5. coût actuel ;
6. impact sur les données ;
7. limites ;
8. alternatives ;
9. décision ;
10. sources.

Toujours distinguer :
- fonction cœur ;
- confort ;
- dépendance ;
- lock-in éventuel.

---

# 13. Architecture ACCESSORY_HUB

Classer :

- `REQUIRED`
- `RECOMMENDED`
- `OPTIONAL`
- `COSMETIC`

Expliquer :
- compatibilité ;
- génération ;
- valeur réelle ;
- coût ;
- alternatives ;
- ce qui peut être acheté en compatible tiers.

Ne pas créer une liste commerciale sans hiérarchie.

---

# 14. Architecture ALTERNATIVES

Utiliser d'abord les raisons de quitter la marque :

- prix ;
- ouverture ;
- lecture ;
- apps ;
- couleur ;
- format ;
- workflow ;
- abonnement ;
- compatibilité.

Puis router les alternatives par besoin.

Pour une vraie comparaison multi-produits :
- déléguer le scoring à `comparison-content-workflow`.

---

# 15. Who should choose / avoid

Obligatoire sur `BRAND_HUB`, `PRODUCT` et `REVIEW`.

## Choose if
Formuler 3 à 5 cas concrets.

## Avoid if
Formuler 2 à 5 situations où une autre marque ou catégorie est plus cohérente.

Le bloc "avoid" ne doit pas être édulcoré pour préserver la conversion.

---

# 16. Internal Linking Architecture

Une page marque doit être un hub profond.

Vérifier selon pertinence :

- modèles actuels ;
- anciens modèles utiles ;
- reviews ;
- comparatifs ;
- alternatives ;
- accessoires ;
- services ;
- guides ;
- usages ;
- bons plans ;
- pages prix.

## Règle

Une page marque presque sans liens internes est incomplète.

---

# 17. Affiliate Value

Utiliser `affiliate-value`.

Vérifier :

- utilité sans CTA ;
- limites visibles ;
- alternatives honnêtes ;
- absence de fausse urgence ;
- prix datés ;
- disponibilité datée ;
- disclosure claire ;
- recommandation indépendante de la commission.

---

# 18. Fact-check

Utiliser `fact-check`.

Vérifier :

- noms ;
- générations ;
- dimensions ;
- technologies ;
- compatibilités ;
- OS ;
- services ;
- cloud ;
- formats ;
- accessoires ;
- prix ;
- abonnements ;
- disponibilité ;
- fin de commercialisation.

---

# 19. GEO Entity Pass

Contrôler explicitement les relations :

- marque → produit ;
- marque → logiciel ;
- marque → service ;
- marque → intégration ;
- produit → technologie ;
- produit → usage ;
- produit → limitation ;
- produit → alternative ;
- marque → concurrent.

La page doit être facilement résumable sous forme de graphe d'entités.

---

# 20. Finition éditoriale

Exécuter :

1. `natural-writing`
2. `humanizer`
3. `general-writing`
4. `anti-ai-slop`
5. `seo-drift`

Le `seo-drift` compare aussi :
- entity map ;
- current range ;
- ecosystem map ;
- proposition de marque ;
- maillage prévu.

---

# 21. SEO

Utiliser `seo-best-practices` et `seo-technical`.

Vérifier :

- title ;
- H1 ;
- intent ;
- entities ;
- canonical ;
- robots ;
- maillage ;
- breadcrumbs ;
- structured data si pertinent ;
- indexation des anciennes générations ;
- cannibalisation.

---

# 22. Brand Quality Gate

Le contrôle automatique peut vérifier :

- entity map existante ;
- gamme actuelle documentée ;
- statuts produits ;
- ecosystem map ;
- page type ;
- preuves ;
- maillage ;
- limites ;
- sources ;
- noindex en brouillon ;
- liens vers au moins une page produit et une page comparative quand pertinent.

Le script ne doit jamais déclarer automatiquement :

- Fact-check PASS ;
- GEO PASS ;
- Humanizer PASS ;
- marque correctement positionnée ;
- review réellement testée.

---

# 23. Échecs automatiques

FAIL si :

- générations anciennes présentées comme actuelles ;
- produit discontinué non signalé ;
- marque décrite uniquement en termes promotionnels ;
- pas de limite réelle ;
- page hub sans profondeur de maillage ;
- service payant présenté comme gratuit ;
- abonnement omis alors qu'il change l'usage ;
- fake test ;
- sensation produit inventée ;
- relation d'entité importante absente ;
- gamme non datée ;
- sources officielles absentes pour claims évolutifs ;
- source de vérité non mise à jour.

---

# 24. Statuts

- `ENTITY_MAP_READY`
- `RANGE_READY`
- `ECOSYSTEM_READY`
- `DRAFT_READY`
- `QA_IN_PROGRESS`
- `REVISION_REQUIRED`
- `HUMAN_APPROVED`
- `PUBLISHABLE`

---

# 25. Publication

Par défaut :

- conserver `noindex` si configuré ;
- ne pas merger ;
- ne pas publier ;
- ne pas déployer.

Autorisation explicite nécessaire.

---

# 26. Fichiers persistants

Pour chaque marque :

`.content/brands/<brand>.yaml`

Contient :

- entity map ;
- product range ;
- ecosystem ;
- evidence ledger ;
- positioning ;
- internal link map ;
- date de recherche.

Pour chaque page :

`.content/briefs/<slug>.md`

et :

`.content/reviews/<slug>.md`

La prose finale ne doit jamais être la seule source expliquant l'écosystème de la marque.

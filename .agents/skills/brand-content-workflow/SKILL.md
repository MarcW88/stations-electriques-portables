---
name: brand-content-workflow
description: Workflow unique de production et de refonte des pages /marques/ de stations-electriques-portables.fr. Orchestre majoritairement des skills existants pour produire des pages d'affiliation techniques, utiles, sourcées, non templatisées et cohérentes avec le ton de comparateur indépendant du site.
metadata:
  adapted_for: stations-electriques-portables.fr
  orchestration_target: ">=80% existing skills"
---

# Brand Content Workflow

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL sous `/marques/`.

Il reprend la logique du workflow de `bloc-notes-numerique`, mais l'adapte au produit et à la mise en avant de stations-electriques-portables.fr : un **comparateur technique indépendant**, orienté décision, qui aide le lecteur à dimensionner son besoin avant de choisir une marque.

Principe central :

> **Pas de plan avant l'intention et les preuves. Pas de claim important sans source. Pas de template éditorial par type de page. Les W, Wh, limites d'usage et compatibilités priment sur la prose marketing.**

Le workflow orchestre des skills spécialisés. Le custom propre à ce repo doit rester limité au contexte des stations électriques portables, à l'architecture éditoriale de l'URL et à la QA du cluster marques.

---

# 1. Entrées obligatoires

Lire avant toute production :

- les instructions du repo lorsqu'elles existent (`AGENTS.md`, README ou équivalent) ;
- `brand-workflow.config.yaml` ;
- l'URL cible et son contenu existant ;
- les pages sœurs `/marques/` pertinentes ;
- `.content/brand-pages/` et `.content/brands/` ;
- `.content/reviews/` lorsqu'une review ou un jugement produit existe ;
- les fiches `/modeles/`, comparatifs, guides, usages, contenus solaires, puissance/capacité et calculateur utiles ;
- les données sémantiques, GSC ou historiques lorsqu'elles existent ;
- les sources actuelles nécessaires à la vérification.

Pour une page existante, commencer obligatoirement par :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `AUDIT`.

Ne pas lancer une réécriture profonde si l'audit conclut `KEEP`, `LIGHT_UPDATE`, `MERGE` ou `NOINDEX` sans raison documentée de changer cette décision.

---

# 2. House style du site

Le site se présente comme une **base de données et un comparateur indépendant**. La rédaction doit donc être :

- technique mais accessible ;
- concise et décisionnelle ;
- explicite sur les unités et les limites ;
- neutre vis-à-vis des marques ;
- plus proche d'un outil d'aide au choix que d'un article lifestyle ;
- utile même sans lien affilié.

## Priorités de lecture

Selon la page, privilégier les dimensions qui changent réellement le choix :

1. usage ou appareils à alimenter ;
2. capacité utile en Wh ;
3. puissance continue en W et éventuels appels de courant ;
4. poids et vraie portabilité ;
5. chimie batterie et durée de vie lorsqu'elle est documentée ;
6. recharge secteur, solaire et véhicule ;
7. entrée solaire, MPPT, tension/courant et compatibilités ;
8. UPS/EPS et temps de transfert lorsque pertinent ;
9. extension de capacité ;
10. application, firmware, accessoires et écosystème ;
11. prix et disponibilité uniquement lorsqu'ils sont datés.

Ne pas reprendre cette liste comme plan automatique.

## Composants éditoriaux du site

- `answer-box` : utile pour une réponse immédiate, mais son texte doit être spécifique à la marque ;
- tableaux : privilégiés quand ils normalisent une comparaison technique ou réduisent une ambiguïté, avec des colonnes choisies selon la marque ;
- calculateur d'autonomie : à lier lorsqu'il répond à une vraie question de dimensionnement ;
- guides W/Wh, LiFePO4, UPS/EPS, solaire, usages et comparatifs : uniquement lorsqu'ils constituent la prochaine étape logique.

La mise en avant visuelle peut rester cohérente entre pages ; **l'architecture éditoriale ne doit pas être clonée**.

---

# 3. Chaîne de production fondée sur les skills existants

## 3.1 Intention — `search-intent`

Avant tout plan, établir :

- requête ou topic principal ;
- intention ;
- décision ou problème concret du lecteur ;
- rôle de l'URL par rapport aux autres pages ;
- prochaine question logique ;
- risque de cannibalisation.

Utiliser les données historiques disponibles avant d'inférer la cible.

## 3.2 Audit/récupération — `content-audit` + `content-refresh`

Pour une page existante :

- utiliser `content-audit` pour décider ce qui mérite d'être conservé ;
- si `UPDATE`, utiliser `content-refresh` pour distinguer correction légère, révision majeure et réécriture complète ;
- préserver les tableaux normalisés, faits vérifiés, limites concrètes et liens réellement utiles ;
- ne pas remplacer une bonne information technique par une prose plus vague.

Pour une nouvelle page, cette étape est `N/A`.

## 3.3 Recherche et evidence brief — `fact-check`

La recherche précède le plan et la rédaction.

Construire un registre des affirmations nécessaires :

| Question / claim | Source | Date | Status | Utilité pour la décision |
|---|---|---|---|---|

Hiérarchie de sources par défaut :

1. fabricant, manuel, support ou documentation officielle ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et médias spécialisés indépendants nommés ;
5. plusieurs sources utilisateurs lorsqu'un pattern d'expérience est réellement étudié.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Règles :

- ne jamais combler `UNKNOWN` avec la mémoire du modèle ;
- ne pas utiliser une autre page affiliée comme source primaire d'une spécification si une source officielle existe ;
- dater les données susceptibles d'évoluer ;
- conserver les contradictions entre sources ;
- distinguer puissance nominale, puissance de crête et modes boost ;
- distinguer capacité nominale et autonomie réelle ;
- ne pas déclarer une compatibilité solaire ou batterie uniquement parce que les connecteurs semblent correspondre.

## 3.4 Reviews et jugements — `evidence-based-reviews`

Obligatoire pour `REVIEW` et dès qu'une page formule un jugement important sur autonomie observée, rendement, bruit, fiabilité, application, charge, ergonomie ou qualité d'usage.

Utiliser les quatre tiers :

- Tier 1 : specs fabricant vérifiées ;
- Tier 2 : synthèse utilisateurs à échelle suffisante ;
- Tier 3 : triangulation de sources expertes ;
- Tier 4 : hands-on uniquement si un vrai test documenté existe.

Une observation issue d'un autre test ne devient jamais une expérience propre au site.

## 3.5 Valeur originale — `affiliate-value`

Avant le plan, identifier la valeur ajoutée par rapport au fabricant et aux marchands.

Exemples adaptés au site :

- expliquer ce qu'une puissance ou une capacité permet réellement d'alimenter ;
- signaler quand le poids contredit le terme « portable » ;
- comparer la logique d'extension de capacité ;
- distinguer vraie compatibilité solaire et simple possibilité de branchement ;
- expliquer les limites d'un UPS/EPS ;
- montrer le coût ou l'encombrement du système complet ;
- distinguer génération actuelle et ancienne ;
- indiquer quand une marque est surdimensionnée ou sous-dimensionnée pour un usage ;
- expliquer les conséquences concrètes d'un écosystème fermé ou d'accessoires propriétaires ;
- proposer une alternative pour une raison précise.

Test obligatoire : **la page reste-t-elle utile si tous les liens affiliés disparaissent ?**

---

# 4. Entités et modèle technique propres aux stations électriques

La cartographie d'entités doit refléter ce marché, pas un autre univers produit.

Selon la page, documenter les relations pertinentes entre :

- marque ;
- station / famille produit ;
- batterie et chimie ;
- onduleur ;
- BMS ;
- sorties AC/DC/USB ;
- solaire / MPPT ;
- batteries additionnelles ;
- panneaux et accessoires ;
- recharge secteur / véhicule / alternateur ;
- UPS/EPS ;
- application / firmware ;
- usages ;
- appareils ou classes de puissance ;
- concurrents / alternatives.

Ne jamais conserver des catégories héritées d'un autre marché (`stylus`, `notes`, `PDF`, `OCR`, etc.) comme schéma de référence pour ce repo.

L'entity map est un support de recherche ; elle ne doit pas imposer des sections si ces entités ne changent pas la décision.

---

# 5. Construction libre mais justifiée du plan

Le plan est construit **après** l'intention, l'evidence brief et `affiliate-value`.

Pour chaque section, pouvoir répondre :

1. quelle question du lecteur résout-elle ?
2. quelles preuves permettent de l'écrire ?
3. quelle décision ou compréhension améliore-t-elle ?
4. pourquoi mérite-t-elle sa propre section ?

Si les réponses sont faibles, supprimer ou fusionner la section.

## Interdiction de template par page type

Il est interdit de définir :

- un nombre fixe de H2/H3 ;
- un ordre standard « positionnement → gamme → écosystème → usages → forces → limites → choisir → éviter → alternatives » ;
- un tableau obligatoire ;
- une FAQ automatique ;
- une conclusion automatique ;
- un minimum de mots ;
- un quota de liens internes ;
- un bloc « choose / avoid » obligatoire lorsque ce n'est pas la meilleure façon de répondre à l'intention.

Deux `BRAND_HUB` doivent pouvoir avoir des architectures très différentes si leurs vraies différences le justifient.

---

# 6. Le type de page comme garde-fou, pas comme squelette

## `BRAND_HUB`

Vérifier la gamme actuelle, les générations, le positionnement technique et l'écosystème **lorsqu'ils changent le choix**. Pour EcoFlow, la logique RIVER/DELTA et l'extension peuvent être centrales ; pour une autre marque, le rapport capacité/puissance, la simplicité ou le solaire peuvent être plus importants.

## `PRODUCT`

Se concentrer sur le modèle : statut, génération, caractéristiques décisionnelles, compatibilités, poids, recharge, limites et coût système. Ne pas dupliquer une review séparée.

## `REVIEW`

Produire un jugement traçable aux preuves. Distinguer clairement desk research, synthèse indépendante et éventuel hands-on réel.

## `SERVICE`

Traiter uniquement ce qui change l'usage : application, abonnement, firmware, monitoring, données, dépendance ou intégrations.

## `ACCESSORY_HUB`

Privilégier compatibilités exactes, tension/courant, génération, utilité réelle et coût système.

## `ALTERNATIVES`

Partir de la raison de quitter la marque ou le produit : poids, puissance, prix, solaire, extension, simplicité, UPS, SAV, application, etc. Les alternatives doivent résoudre cette limite précise.

---

# 7. Rédaction à partir des preuves

Le draft utilise l'evidence brief comme frontière factuelle.

Règles :

- chaque claim important doit être relié à une source ou présenté clairement comme déduction ;
- aucune capacité, puissance, tension, courant, poids, cycle, temps de charge, prix, génération, garantie, compatibilité ou expérience ne peut être inventé ;
- expliquer la conséquence pratique des specs au lieu de recopier la fiche fabricant ;
- afficher les limites aussi clairement que les avantages ;
- éviter les superlatifs non démontrés ;
- ne pas utiliser « meilleure marque » sans critères comparatifs ;
- ne pas simuler de test ;
- ne pas faire varier le verdict selon la commission.

La prose finale ne doit pas parler de SEO, GEO, hub, maillage, intention, workflow, page type ou stratégie éditoriale.

---

# 8. Fact-check post-draft — `fact-check`

Après rédaction :

1. réextraire les claims vérifiables ;
2. comparer avec l'evidence brief ;
3. recontrôler les affirmations ajoutées ou reformulées ;
4. corriger `OUTDATED` et `CONTRADICTED` ;
5. qualifier ou supprimer `UNKNOWN` ;
6. vérifier les unités ;
7. vérifier les compatibilités et générations ;
8. s'assurer qu'aucune synthèse externe n'est devenue une expérience propre.

---

# 9. Finition éditoriale

Utiliser dans cet ordre lorsque les skills sont disponibles :

1. `humanizer` en mode embedded ;
2. `general-writing` comme house-style pass ;
3. `anti-ai-slop` en contrôle final.

La finition peut modifier la structure si elle paraît mécanique, mais ne peut ajouter aucun fait absent des preuves.

À contrôler particulièrement :

- introductions identiques entre marques ;
- paragraphes génériques sur W/Wh, UPS, solaire ou portabilité répétés mot pour mot ;
- même rythme et même nombre de sections ;
- blocs « forces / limites / choisir / éviter » présents par réflexe ;
- alternatives décrites avec la même phrase ;
- tableau identique alors que les critères discriminants changent ;
- surpromesse commerciale.

---

# 10. Maillage — `internal-linking-audit`

Ajouter uniquement les liens qui répondent à une prochaine question logique.

Destinations possibles selon la page :

- `/modeles/` ;
- `/comparatifs/` ;
- `/guides/` ;
- `/usages/` ;
- `/solaire/` ;
- `/puissance-capacite/` ;
- `/calculateur-autonomie/` ;
- autre page marque ou alternative.

Aucun quota de liens ni de destinations. Le calculateur n'est pas un CTA automatique : il doit être proposé lorsqu'un besoin d'autonomie ou de capacité doit réellement être dimensionné.

---

# 11. SEO

Utiliser :

- `seo-technical` pour canonical, robots, indexability, schema, crawlabilité et architecture technique ;
- `seo-best-practices` uniquement pour les règles applicables au HTML statique du site ;
- `seo-drift` seulement si un baseline ou une régression doit être comparé.

Vérifier title, H1, intention, canonical, breadcrumbs, structured data honnête, liens et cannibalisation.

Aucun nombre de mots, headings, tableaux ou liens n'est un KPI de qualité.

---

# 12. QA générique — `editorial-qa`

La page doit passer : intention, valeur originale, factualité, naturel, SEO et utilité sans affiliation.

Un contenu techniquement correct peut encore échouer s'il est générique, marchand ou interchangeable avec une autre marque.

---

# 13. Gate final — `brand-analysis-workflow` / `PUBLISH_REVIEW`

Une fois le draft stable, appeler :

`.agents/skills/brand-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Cette étape :

- exécute `python3 _validate_brands.py` ;
- recontrôle les preuves et l'intention ;
- compare la structure aux pages sœurs ;
- cherche l'industrialisation éditoriale ;
- vérifie les blockers propres au marché des stations électriques.

Résultat attendu avant validation humaine :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

---

# 14. Persistance

Conserver dans les dossiers définis par `brand-workflow.config.yaml` :

- cadrage de l'intention ;
- research/evidence brief ;
- statut des claims ;
- sources et date de vérification ;
- entity map adaptée aux stations électriques ;
- valeur originale recherchée ;
- justification du plan ;
- résultat de l'audit et du `PUBLISH_REVIEW`.

Le HTML final ne doit jamais être l'unique endroit où les preuves sont documentées.

---

# 15. Indexation

Par défaut, conserver `noindex,follow`.

Le workflow n'est jamais autorisé à retirer le `noindex` automatiquement.

Conditions cumulatives avant une future indexation :

1. `_validate_brands.py` sans blocker machine ;
2. `brand-analysis-workflow` / `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 16. Résumé de l'orchestration

```text
PAGE EXISTANTE
  brand-analysis-workflow / AUDIT
        ↓
search-intent
        ↓
content-audit + content-refresh si nécessaire
        ↓
fact-check → evidence brief
        ↓
evidence-based-reviews si jugement/review
        ↓
affiliate-value
        ↓
ENTITY MAP STATION-SPECIFIC
        ↓
PLAN SPÉCIFIQUE À L'URL
        ↓
rédaction depuis les preuves
        ↓
fact-check post-draft
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
internal-linking-audit
        ↓
SEO pertinent
        ↓
editorial-qa
        ↓
brand-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le workflow orchestre ; il ne remplace pas ses skills spécialisés.
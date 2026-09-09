---
name: brand-analysis-workflow
description: Workflow unique d'analyse des pages /marques/ de stations-electriques-portables.fr. Audite une page ou le cluster, compare les architectures, contrôle intention, valeur affiliée, preuves, factualité, AI-slop et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. Le contrôle est adapté à un comparateur technique de stations électriques portables.
metadata:
  adapted_for: stations-electriques-portables.fr
  orchestration_target: ">=80% existing skills"
---

# Brand Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/marques/`.

Il reprend l'orchestration du workflow de `bloc-notes-numerique`, mais adapte les contrôles au marché des stations électriques portables et au ton du site : base de données indépendante, comparateur technique, aide au dimensionnement et à la décision.

Il ne réécrit pas la page par défaut. Il décide quoi conserver, corriger, reconstruire ou fusionner.

Les comparatifs, guides, usages, solaire, puissance/capacité et fiches modèles restent dans leurs workflows respectifs.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante. Retourne une décision et un plan de correction sans produire la nouvelle page.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs `/marques/` ensemble afin de détecter cannibalisation, duplication de rôle, répétition de prose et industrialisation de structure.

## `PUBLISH_REVIEW`

Gate final après rédaction. Il vérifie la page individuellement et dans son cluster, exécute le validateur machine et retourne soit :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex,follow` automatiquement.

---

# 2. Entrées

Lire avant l'audit :

- les instructions du repo lorsqu'elles existent ;
- `brand-workflow.config.yaml` ;
- page cible et pages sœurs pertinentes ;
- `.content/brand-pages/` ;
- `.content/brands/` ;
- `.content/reviews/` si la page contient un jugement produit ;
- pages `/modeles/`, comparatifs, guides, usages, solaire, puissance/capacité et calculateur utiles ;
- données GSC, sémantiques ou historiques lorsqu'elles existent ;
- sources actuelles lorsque les faits peuvent avoir évolué.

Ne jamais inventer une donnée absente pour compléter l'audit.

---

# 3. Chaîne de skills obligatoire

L'analyse repose d'abord sur des skills spécialisés. Ne pas recopier leurs checklists ; les utiliser selon leur rôle lorsque disponibles.

## 3.1 `content-audit`

Décider si l'URL possède encore une fonction autonome et identifier : valeur historique, contenu marchand, obsolescence, faiblesse structurelle, duplication et potentiel de récupération.

Décisions internes possibles : `KEEP`, `UPDATE`, `MERGE`, `REDIRECT`, `REMOVE`.

## 3.2 `search-intent`

Déterminer :

- requête ou topic principal ;
- intention ;
- problème ou décision du lecteur ;
- rôle de l'URL ;
- chevauchements avec les autres URLs ;
- sections qui ne servent pas l'intention.

## 3.3 `content-refresh`

Uniquement lorsque `content-audit` conclut `UPDATE`. Diagnostiquer notamment `Intent drift`, `Thin value`, `Merchant duplication`, `Outdated`, `Weak structure`, `Cannibalization`, `Generic prose` ou `Trust gap`.

## 3.4 `affiliate-value`

Vérifier que la page reste utile si tous les liens affiliés disparaissent. Contrôler en particulier :

- dimensionnement réel ;
- limites et cas de non-achat ;
- poids et portabilité ;
- autonomie vs capacité nominale ;
- compatibilités ;
- coût système ;
- génération actuelle ;
- alternatives pour une raison précise ;
- absence de faux test.

## 3.5 `fact-check`

Extraire les claims vérifiables, appliquer la hiérarchie de sources et classer chaque claim important. Une affirmation plausible mais non sourcée reste non vérifiée.

## 3.6 `evidence-based-reviews`

Obligatoire pour les pages `REVIEW` et toute page contenant un jugement important sur autonomie observée, rendement, bruit, ergonomie, application, fiabilité ou expérience.

## 3.7 `internal-linking-audit`

Vérifier que les liens internes servent une étape logique du parcours : modèle, comparatif, usage, guide, solaire, puissance/capacité, calculateur, accessoire ou alternative. Aucun quota.

## 3.8 `anti-ai-slop`

Utiliser en review/detection. Rechercher les sorties génériques, répétitives, trop symétriques ou applicables à n'importe quelle marque.

## 3.9 SEO

Utiliser `seo-technical` pour indexability, canonical, robots, structured data, crawlabilité et architecture.

Utiliser `seo-best-practices` uniquement pour les règles pertinentes au HTML statique du site.

Utiliser `seo-drift` seulement si un baseline ou une comparaison avant/après existe.

## 3.10 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, SEO et utilité sans affiliation.

---

# 4. Contrôle custom n°1 — adéquation au rôle de page

Le type de page sert de **grille de risque**, jamais de template éditorial.

Types : `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB`, `ALTERNATIVES`.

Vérifier seulement les questions qui changent la décision :

- `BRAND_HUB` : la page explique ce qui distingue réellement la marque et comment lire sa gamme ;
- `PRODUCT` : statut/génération, capacité, puissance, poids, recharge, compatibilités et limites décisionnelles ;
- `REVIEW` : verdict proportionnel aux preuves et distinct d'une fiche produit ;
- `SERVICE` : application, firmware, fonctions, coût, dépendance et fonctionnement sans service ;
- `ACCESSORY_HUB` : compatibilités exactes, tension/courant, générations et utilité ;
- `ALTERNATIVES` : raisons concrètes de changer et alternatives adaptées à ces raisons.

Ne jamais exiger les mêmes headings, le même ordre ou le même nombre de sections entre deux pages du même type.

---

# 5. Contrôle custom n°2 — cohérence avec le ton du site

La page doit rester cohérente avec une **base de données indépendante et un comparateur technique**.

Signaux positifs :

- les W et Wh sont distingués clairement ;
- l'autonomie n'est pas déduite naïvement de la capacité nominale ;
- puissance continue, crête et boost ne sont pas mélangés ;
- le poids est interprété en termes de vraie portabilité ;
- le solaire est traité avec entrée, MPPT et compatibilités lorsque nécessaire ;
- UPS/EPS est décrit avec ses limites ;
- les accessoires ou batteries additionnelles sont vérifiés par génération ;
- les prix sont datés ;
- le calculateur est proposé lorsqu'il aide réellement à dimensionner un besoin ;
- la recommandation peut conclure qu'une marque ou une grosse station est inutile pour le cas étudié.

Signaux négatifs :

- vocabulaire lifestyle ou commercial générique ;
- « meilleure marque », « révolutionnaire », « incontournable » sans preuve ;
- paraphrase de la fiche fabricant ;
- longue introduction sans décision ou information technique ;
- arguments d'écosystème appliqués par réflexe à toutes les marques ;
- CTA affilié avant la compréhension du besoin.

---

# 6. Contrôle custom n°3 — similarité structurelle du cluster

C'est le contrôle principal contre la production industrialisée.

En `AUDIT`, comparer au minimum la page cible avec les pages sœurs les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le cluster pertinent dans son ensemble.

Comparer :

- intitulés et fonctions sémantiques des H2/H3 ;
- ordre des questions traitées ;
- forme des `answer-box` ;
- répétition de blocs « positionnement / gamme / écosystème / usages / forces / limites / choisir / éviter / alternatives » ;
- colonnes de tableaux réutilisées alors que les vrais critères diffèrent ;
- emplacement systématique des tableaux, listes ou CTA ;
- rythme des paragraphes ;
- phrases ou transitions recyclées ;
- alternatives formulées avec les mêmes raisons ;
- paragraphes génériques sur W/Wh, UPS, solaire ou portabilité recopiés entre marques.

## Règle

Une cohérence visuelle ou des composants HTML partagés ne sont pas un problème. Le FAIL intervient lorsque **l'architecture éditoriale ou la prose semble dictée par un squelette réutilisé plutôt que par l'intention, la gamme et les preuves propres à la marque**.

Signaux forts :

- plusieurs pages gardent les mêmes rôles de sections dans le même ordre ;
- une section existe uniquement parce qu'elle existe chez les autres marques ;
- les détails de marque pourraient être permutés sans changer l'argument ;
- les mêmes recommandations « choisir / éviter » se répètent avec changement de nom ;
- le même paragraphe méthodologique est copié dans plusieurs pages ;
- le plan ne peut pas être justifié par le research/evidence brief de la page.

Si le problème est substantiel : `DEEP_REWRITE`.

---

# 7. Contrôle custom n°4 — modèle d'entités adapté au marché

Les données persistées doivent refléter les stations électriques portables.

Vérifier, selon pertinence :

- marque → famille de stations ;
- station → capacité ;
- station → puissance ;
- station → chimie batterie ;
- station → solaire/MPPT ;
- station → batterie additionnelle ;
- station → UPS/EPS ;
- station → recharge véhicule/alternateur ;
- station → application/firmware ;
- station → usage ;
- station → limitation ;
- marque → concurrent/alternative.

Les catégories héritées d'un autre univers produit (`stylus`, `notes`, `PDF`, `OCR`, etc.) ne doivent pas servir de schéma principal. Si elles subsistent sans rôle réel : les signaler comme dette de modèle de données.

---

# 8. Contrôle de preuves

Hiérarchie par défaut :

1. fabricant / documentation / manuel / support officiel ;
2. distributeur officiel ;
3. retailer fiable pour disponibilité ou information commerciale complémentaire ;
4. tests et publications indépendantes nommées ;
5. plusieurs sources utilisateurs pour des patterns d'expérience.

Pour les informations importantes utiliser : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Contrôler en priorité :

- capacité ;
- puissance continue ;
- puissance de crête/boost ;
- poids ;
- chimie ;
- cycles si mentionnés ;
- entrée solaire et limites électriques ;
- temps de charge ;
- UPS/EPS ;
- extension de capacité ;
- compatibilités accessoires ;
- génération ;
- prix et disponibilité.

`UNKNOWN` et `CONTRADICTED` ne peuvent pas être transformés en certitude rédactionnelle.

---

# 9. Décision finale AUDIT / CLUSTER_AUDIT

Mapper les résultats vers cinq statuts :

## `KEEP`

Page forte, actuelle, distincte et utile. Pas de modification substantielle requise.

## `LIGHT_UPDATE`

Corrections ciblées : facts, sources, quelques passages, liens, terminologie ou faiblesse locale. La structure fondamentale reste pertinente.

## `DEEP_REWRITE`

Intent mal servi, valeur faible, architecture générique, contenu marchand, preuves insuffisantes, structure industrialisée, modèle d'entités inadapté ou besoin de reconstruction importante.

## `MERGE`

Une autre URL couvre pratiquement la même intention et la distinction ne justifie pas deux pages.

## `NOINDEX`

La page ne possède pas encore assez de valeur ou de justification pour être indexée. Les recommandations `REDIRECT`/`REMOVE` de `content-audit` peuvent être consignées, sans application automatique.

Pour chaque décision donner :

- confiance ;
- preuves utilisées ;
- unknowns ;
- blockers ;
- valeur déjà présente ;
- actions nécessaires ;
- prochaine étape.

Pour `DEEP_REWRITE`, passer la main à `brand-content-workflow`.

---

# 10. Mode PUBLISH_REVIEW

Exécuter uniquement sur un draft considéré terminé.

## Étape A — validation machine

Exécuter :

```bash
python3 _validate_brands.py
```

Un PASS machine n'est qu'un plancher structurel.

## Étape B — réexécuter les gates substantiels

Vérifier au minimum :

- intention satisfaite ;
- valeur affiliée originale ;
- claims importants sourcés ;
- niveau de preuve honnête ;
- pas de faux test ;
- pas de métadiscours SEO/éditeur dans la prose ;
- pas de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- ton de comparateur technique respecté ;
- W/Wh et limites techniques correctement traités ;
- architecture propre à la page ;
- absence de clonage structurel substantiel avec les pages sœurs ;
- title/H1/canonical/robots cohérents ;
- liens et schema honnêtes ;
- page utile même sans liens affiliés.

## Étape C — résultat

### PASS

Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

Lister les éventuels risques mineurs restants.

### FAIL

Retourner :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou workflow qui doit corriger le problème.

---

# 11. Indexation

Par défaut, toutes les pages travaillées restent `noindex,follow`.

Le workflow n'est jamais autorisé à retirer `noindex` seul. Conditions cumulatives :

1. aucun blocker dans `_validate_brands.py` ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 12. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quotas de mots ;
- quotas de headings ;
- quotas de liens ;
- score artificiel de qualité ;
- template fixe par type de page ;
- obligation systématique de sections « forces / limites / choisir / éviter » ;
- générateur de texte ;
- copie des règles déjà maintenues dans les skills appelés.

Sa valeur est l'orchestration, la décision, le contrôle inter-pages et l'adaptation technique au marché des stations électriques portables.
# Brief de production — Pages marques — 09/09/2026

```yaml
scope: /marques/
routing: BRAND_HUB
mode: NEW_CONTENT
brands: 7
indexing: noindex, follow
workflow: brand-content-workflow
```

## Diagnostic

Les sept pages enfants de `/marques/` étaient des shells générés par `_generate.py` avec le placeholder `<!-- Contenu à rédiger -->`.
Elles sont donc routées en `NEW_CONTENT`.

## Marques

- EcoFlow
- BLUETTI
- Jackery
- AFERIY
- Anker SOLIX
- ALLPOWERS
- IZYWATT

## Principe de production

1. cartographier les entités et la gamme actuelle ;
2. distinguer les générations précédentes des produits actuellement mis en avant ;
3. documenter l’écosystème : solaire, batteries additionnelles, application, recharge véhicule, UPS/EPS ;
4. rédiger le hub à partir des données structurées ;
5. expliciter forces, limites, profils « choisir / éviter » ;
6. mailler vers modèles, comparatifs, guides et usages ;
7. ne jamais revendiquer de test réel lorsque nous avons seulement fait une analyse documentaire ;
8. conserver `noindex, follow` jusqu’à validation humaine.

## Arbitrages de gamme

### EcoFlow
RIVER 3 / RIVER 3 Plus et DELTA 3 / DELTA Pro 3 structurent la gamme actuelle. Les DELTA 2 / RIVER 2 encore visibles sont distinguées comme générations précédentes ou références héritées selon le contexte.

### BLUETTI
Elite 30 V2, Elite 100 V2, Elite 200 V2 et Apex 300 sont les références prioritaires. Les familles EB3A / AC180 / AC200MAX ne sont pas présentées comme équivalentes à la nouvelle génération.

### Jackery
La série Explorer v2 est prioritaire, avec coexistence de la série Plus. Explorer 3000 Pro est traité comme génération précédente face à Explorer 3000 v2.

### AFERIY
La nomenclature 2026 Nano / Nomad / Haven est retenue. P210, P280 et P310 sont contextualisés dans Haven.

### Anker SOLIX
C1000 Gen 2 et C2000 Gen 2 sont les références centrales. C1000 première génération et F2000 sont distinguées comme générations précédentes ; C300 est signalée comme actuellement épuisée sur la boutique FR lors de la vérification.

### ALLPOWERS
La série R récente et VOLIX sont prioritaires. Les variantes R2500 Plus / V2 sont explicitement distinguées. S700 est traité comme ancienne génération interne au site.

### IZYWATT
La gamme Orium 2026 est structurée par usage : 800, Moov, Home, Eco et batterie Extra. Aucune URL de fiche modèle interne n’est inventée : le hub compense avec du maillage vers usages, guides et comparatifs.

## Sources

Priorité aux sources officielles fabricant/Orium, vérifiées le 09/09/2026. Les prix promotionnels ne sont pas utilisés comme faits stables.

## Publication gate

- données structurées présentes ;
- gamme actuelle identifiable ;
- ≥ 9 H2 ;
- ≥ 1 000 mots ;
- ≥ 3 sources officielles ;
- maillage comparatifs / guides / usages ;
- choose / avoid ;
- limites visibles ;
- aucune expérience ou test inventé ;
- `noindex, follow` conservé ;
- validation humaine avant merge.

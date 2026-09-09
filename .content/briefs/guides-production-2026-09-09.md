# Brief de production — Guides — 09/09/2026

```yaml
scope: /guides/
mode: NEW_CONTENT
status: BRIEF_READY
quality_reference: /guides/comment-choisir-station-electrique-portable/
source_of_truth:
  shell: _generate.py
  editorial: .content/guides/*.html
  renderer: _generate_guides.py
robots: noindex, follow
```

## Diagnostic

Les 12 pages guides enfants étaient des shells avec réponse très courte, `Vérifié : MM/AAAA`, sommaire vide et `<!-- Contenu à rédiger -->`. Elles sont donc routées en `NEW_CONTENT` et non en recovery. Les slugs, canonicals, navigation, layout et `noindex, follow` sont conservés ; seul le corps éditorial est entièrement produit.

## Pages

| URL | Intention principale | Angle |
|---|---|---|
| `/guides/comment-choisir-station-electrique-portable/` | Choix | Méthode W + Wh + batterie + recharge + secours |
| `/guides/station-electrique-portable-comment-ca-marche/` | Explication | Chaîne batterie/BMS/onduleur/MPPT |
| `/guides/watt-ou-watt-heure/` | Définition | Puissance instantanée vs énergie stockée |
| `/guides/calculer-autonomie-station-electrique/` | Calcul | Wh utiles ÷ puissance moyenne, hypothèses visibles |
| `/guides/calculer-capacite-station-electrique/` | Calcul | Bilan énergétique + pertes + marge |
| `/guides/lifepo4-ou-lithium-ion/` | Comparaison technique | LFP vs NMC sans caricature |
| `/guides/duree-vie-cycles-batterie/` | Explication | Cycles + seuil de capacité + température + stockage |
| `/guides/onde-sinusoidale-pure/` | Compatibilité | Forme d’onde distincte de puissance et UPS |
| `/guides/ups-eps-station-electrique/` | Secours | Temps de transfert, topologies et limites |
| `/guides/recharge-rapide-station-electrique/` | Recharge | Puissance d’entrée, courbe, thermique, solaire |
| `/guides/recharger-station-electrique-voiture/` | Recharge nomade | 12/24 V, temps, câbles et batterie véhicule |
| `/guides/batterie-nomade-ou-station-electrique/` | Choix de format | Powerbank/USB-C vs station par fonction, pas par seuil arbitraire |

## Registre de preuves

| Claim | Source primaire / autorité | Statut |
|---|---|---|
| EcoFlow DELTA 2 : LFP, >3 000 cycles jusqu’à ~80 % | `https://www.ecoflow.com/fr/delta-2-portable-power-station` | CONFIRMED |
| EcoFlow DELTA 3 Classic : 1 024 Wh, 1 800 W, onde pure, recharge 0–80 % ~45 min, ASI <10 ms | `https://www.ecoflow.com/fr/delta-3-classic-portable-power-station` | CONFIRMED |
| EcoFlow RIVER 3 Plus : UPS <10 ms | `https://www.ecoflow.com/fr/river-3-plus-portable-power-station` | CONFIRMED |
| BLUETTI AC180 : 1 152 Wh, 1 800 W, LiFePO₄, 3 500 cycles à 80 %, 1 440 W CA, 500 W solaire, recharge véhicule 12/24 V | `https://fr.bluettipower.eu/products/bluetti-ac180-station-energie-portable` | CONFIRMED |
| UPS line-interactive : temps de transfert dépend de la sensibilité ; online double conversion : pas de transfert réseau-batterie | `https://www.se.com/us/en/faqs/FAQ000268416/` | CONFIRMED |
| NMC : densité énergétique supérieure au LFP en tendance au niveau matériau | `https://docs.nrel.gov/docs/fy11osti/51474.pdf` | CONFIRMED |
| Froid : mobilité ionique réduite, résistance interne accrue, impact puissance/charge | `https://docs.nrel.gov/docs/fy25osti/92113.pdf` | CONFIRMED |
| LFP plus stable ne signifie pas risque nul | `https://www.energy.gov/sites/default/files/2024-05/EED_2827_FIG_SafetyStrategy%20240505v2.pdf` | CONFIRMED |
| Onduleur Phoenix : sortie sinusoïdale pure | `https://www.victronenergy.com/upload/documents/Manual-Phoenix-Inverter-750-EN.pdf` | CONFIRMED |

## Corrections éditoriales importantes

- Suppression des fourchettes universelles de cycles par chimie : les cycles sont désormais rattachés à des modèles et à un seuil de capacité résiduelle.
- Suppression de la règle générique « PC fixe = <10 ms » : la tolérance dépend de la charge et de son alimentation.
- Le coefficient de rendement 0,85 reste une hypothèse de calcul explicitement présentée comme telle, jamais comme une constante.
- La frontière powerbank/station n’est plus définie par un seuil arbitraire de Wh ; elle est expliquée par les sorties, la puissance, la recharge et l’usage.
- La mention « onde pure » n’est jamais utilisée pour déduire puissance, autonomie ou comportement UPS.
- Aucun prix actuel, test physique ou expérience de première main n’est inventé.

## Architecture commune

Chaque guide comprend :
- une réponse initiale autonome ;
- au moins 7 H2 substantiels ;
- exemples ou mécanismes lorsque nécessaires ;
- limites et erreurs fréquentes ;
- maillage vers guides, usages, solaire, comparatifs ou calculateur ;
- au moins 3 sources externes ;
- une section sources séparée ;
- un bloc de prochaines lectures.

## Maillage prioritaire

- `/calculateur-autonomie/` pour les pages W/Wh, autonomie, capacité et choix.
- `/comparatifs/meilleure-station-electrique-portable/` après les guides de choix.
- `/comparatifs/station-electrique-lifepo4/` depuis LFP/cycles.
- `/usages/station-electrique-coupure-courant/` depuis UPS/capacité/autonomie.
- `/usages/station-electrique-van/` depuis recharge voiture/capacité.
- `/solaire/` et `/solaire/mppt/` depuis recharge et fonctionnement.

## Refresh plan

### Conservé
- slugs et canonicals ;
- shell HTML/navigation/footer ;
- `style.css` ;
- `noindex, follow` ;
- emplacement `/guides/`.

### Supprimé
- `<!-- Contenu à rédiger -->` ;
- micro-descriptions insuffisantes ;
- raccourcis non suffisamment contextualisés ;
- `MM/AAAA` sur les pages rendues.

### Ajouté
- contenu complet ;
- sources primaires ;
- sommaires générés ;
- maillage contextuel ;
- registre de preuves ;
- QA automatisée et repo-specific.

## Publication

Le workflow exige une validation humaine avant publication/merge. Le site reste en `noindex, follow` pendant cette phase.

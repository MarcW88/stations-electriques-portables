# Audit de structure visuelle — ensemble du site

Date : 22 octobre 2026 · Périmètre : 82 pages HTML identifiées dans l'arbre GitHub de main.

## Verdict initial (constats vérifiés dans le dépôt)

Le site possède un design system CSS global structuré (variables `--bg`, `--text`, `--accent`, `--radius-*`, `--shadow-*`) et plusieurs gabarits distincts. L'agent de design était installé, mais son script Playwright original contenait encore des chemins de Bloc-notes numériques et attendait un `package.json` absent du projet. Un adaptateur **en lecture seule** spécifique au site a été publié pour parcourir automatiquement les 82 pages.

**Ne pas confondre l'existence du workflow avec un audit visuel terminé.** Aucune capture Playwright n'a encore été reçue et examinée au moment de ce rapport initial.

## Ce qui fonctionne d'après les fichiers inspectés

1. Palette et espacement CSS centralisés dans `style.css`.
2. Pages guides/usages/comparatifs utilisant des gabarits éditoriaux avec H1, H2 et navigation sommaire.
3. Les six pages représentatives consultées pointent vers la feuille `/style.css`.
4. Les guides W/Wh, MPPT et Camping contiennent des liens de sommaire vers leurs sections ; confirmation des ancrages réels encore nécessaire.
5. Des illustrations existent sur les pages représentatives ; leur **chargement effectif** doit être testé par navigateur.

## Anomalies et risques observés

| Gravité | Emplacement | Preuve vérifiée | Conséquence | Correction recommandée |
| --- | --- | --- | --- | --- |
| Bloquant pour audit complet | `.agents/skills/site-design-review/scripts/run-visual-review.mjs` | Scopes préchargés `remarkable`, `boox`, `bloc-notes-numerique` | Le lancement par scope n'audite pas les vraies URL du site | Adaptateur spécifique **ajouté** : `scripts/site-wide-visual-audit.mjs` |
| Bloquant pour lancement documenté | Références Playwright de l'agent | Instructions `npm run visual:...` et `npm install`, mais pas de `package.json` à la racine | Les commandes citées ne s'exécutent pas telles quelles | Installer Playwright sans modifier le projet dans GitHub Actions **configuré** |
| Majeur à vérifier | Tous les gabarits | CSS partagée `style.css` : une régression affecterait de nombreuses pages | Risque de débordements ou défauts mobile récurrents | Captures de toutes les routes en 1440×1000 et 390×844, avec contrôle d'overflow |
| Majeur à vérifier | Pages éditoriales | Présence de photos externes et d'illustrations ajoutées dans le HTML | Images éventuellement cassées ou dimensions instables | Contrôle `naturalWidth`, alt, ressources en erreur, attribution |
| Majeur à vérifier | Sommaires | Classe réelle `.toc-list` sur les pages inspectées ; ancien script cherchait `.sidebar-toc` | Mesures erronées dans l'ancien rapport | L'adaptateur utilise `.toc-list` et valide les ancres |

## Échantillon de pages source examiné

- `/` : H1, 3 H2, aucune image locale dans la page inspectée.
- `/guides/watt-ou-watt-heure/` : H1, 8 H2, 1 image, sommaire présent.
- `/modeles/bluetti-ac180/` : H1, 2 H2, 1 image.
- `/usages/station-electrique-camping/` : H1, 5 H2, 1 image, sommaire présent.
- `/comparatifs/meilleure-station-electrique-portable/` : H1, 8 H2, 2 images, sommaire présent.
- `/solaire/mppt/` : H1, 6 H2, 1 image, sommaire présent.

Les valeurs précédentes proviennent de la lecture du HTML, **pas d'une inspection de rendu**.

## Exécution de l'audit intégral

- Script : `scripts/site-wide-visual-audit.mjs`
- Workflow : `.github/workflows/site-wide-visual-audit.yml`
- Exécution GitHub : https://github.com/MarcW88/stations-electriques-portables/actions/runs/39838239865
- Statut à la première consultation : **queued**.
- Artéfact attendu : `audit-visuel-global` (capture de chaque URL desktop et mobile, `report.json`, `summary.md`).
- Vérifications automatiques prévues : erreur navigation, console, requêtes échouées, débordement horizontal, image cassée, alt absent, H1/H2, sommaire et ancrages, sidebar, tableaux.
- Limitation : **un PASS automatique ne remplace pas la revue manuelle des captures**, de la qualité esthétique et de l'accessibilité clavier.

## Prochain jalon de clôture

Une fois l'artéfact créé : inspecter `report.json` et les captures des gabarits, qualifier les défauts bloquants/majeurs/mineurs, puis publier la matrice finale des 82 pages. Ce document n'affirme ni exécution réussie ni validation mobile à ce stade.

## Résultats Playwright — exécution RÉUSSIE

Exécution GitHub Actions : https://github.com/MarcW88/stations-electriques-portables/actions/runs/39838239865

- **82 routes × desktop/mobile = 164 contrôles réellement effectués** ; 0 échec de navigation HTTP/Playwright.
- **36 contrôles** (portant sur **24 routes uniques**) rapportent au moins une image non chargée. **22 URL d'images distinctes** apparaissent cassées ; elles sont surtout présentes dans les modèles, comparatifs, marques et accessoires.
- **1 débordement horizontal** : `/marques/ecoflow/` en mobile 390 px, contenu large de 426 px (**+36 px**).
- **2 contrôles** avec ancre de sommaire invalide : `/usages/station-electrique-coupure-courant/`, desktop et mobile ; **1 route unique**.
- 0 page signalée sans attribut `alt` sur les images.
- Les captures de `/comparatifs/` (desktop) confirment visuellement plusieurs **images cassées et leur texte alternatif affiché en plein milieu des cartes**. Problème de qualité perçue et de présentation, pas seulement diagnostic réseau.
- La capture mobile de `/marques/ecoflow/` confirme une mise en page très dense, à revoir au-delà du seul débordement mesuré.
- Les contrôles ont visité le site public ; ils ne garantissent pas le comportement dans tous les navigateurs ou réseaux.

### Corrections prioritaires recommandées (non appliquées dans cet audit de lecture seule)

1. **Majeur — images distantes** : remplacer les URL qui échouent par des ressources autorisées et fiables hébergées avec le site, vérifier chaque visuel produit et les droits de réutilisation ; ne pas réutiliser une illustration approximative. Les erreurs `ERR_BLOCKED_BY_RESPONSE.NotSameOrigin` apparaissent notamment sur des photos tierces.
2. **Majeur — responsive EcoFlow** : identifier dans les styles calculés l'élément largeur 426 px et corriger son `min-width`, `overflow-wrap`, grille ou tableau ; retester en 390 px et à largeur inférieure.
3. **Mineur à majeur — navigation intra-page** : corriger le `href="#…"` ne correspondant à aucun `id` sur Coupure de courant, depuis le fichier de contenu source, pas seulement le HTML.
4. **Qualité éditoriale** : revoir visuellement les templates et l'ergonomie des cartes comparatives lorsque les images sont absentes, et contrôler le reflow à tous les points de rupture.

### Artéfacts disponibles

L'archive `audit-visuel-global` de l'exécution contient `report.json`, `summary.md` et 164 captures. Une revue visuelle ciblée de `/comparatifs/` desktop et `/marques/ecoflow/` mobile a été effectuée ; **l'ensemble des 164 captures n'a pas été examiné manuellement**. Le verdict est donc confirmé sur les anomalies automatiques et ces captures, non sur l'esthétique de chaque page.


## Corrections structurelles supplémentaires — 22 octobre 2026

- Le traitement des images externes en échec est désormais appliqué dans les fichiers HTML des **24 routes identifiées par le premier audit Playwright**. Lors d'un échec réseau, le navigateur masque l'élément image plutôt que d'afficher l'icône brisée et le texte alternatif au milieu des cartes. Les images valides restent affichées ; aucune photographie de marque inventée.
- Le générateur `_generate.py` applique le même garde-fou pour les nouvelles pages régénérées. Les sources externes en échec **ne sont pas réparées**, il s'agit d'un traitement défensif de l'interface.
- L'audit Playwright enrichi identifie désormais les éléments DOM dépassant la fenêtre, pas seulement le scroll global, afin de diagnostiquer précisément le débordement mobile.
- La correction CSS de la table EcoFlow et du sommaire Coupure de courant reste en attente de validation sur une exécution postérieure aux corrections.
- GitHub a démarré plusieurs nouveaux audits automatiques, encore en file d'attente à la dernière consultation ; **aucune réussite n'est revendiquée** pour cette nouvelle passe.

**Dette ouverte :** remplacer les 22 URLs d'images distantes en échec par des sources réelles autorisées et stables ; examiner les captures desktop/mobile post-correction ; vérifier que les pages restent illustrées et accessibles lorsque les photos échouent. Le fallback seul ne suffit pas à clore la qualité des images.

## Validation après corrections — passe de contrôle

- Les exécutions concurrentes avaient créé une file d'attente : `concurrency.cancel-in-progress` ajouté au workflow, afin que seule la version la plus récente de `main` soit auditée.
- Le script Playwright exporte maintenant un fichier `broken-image-inventory.csv` répertoriant chaque image défaillante et toutes ses pages consommatrices ; résultat attendu dans les artéfacts de l'exécution récente.
- Le **premier** rapport confirmé comptait 22 URLs d'images défaillantes sur 24 pages distinctes. Il ne faut pas supposer que masquer les `<img>` en erreur a corrigé ces URLs : les requêtes réseau peuvent continuer d'échouer.
- Nouveau run déclenché : https://github.com/MarcW88/stations-electriques-portables/actions/runs/39844898569 ; en attente au moment de la dernière lecture.
- **Remplacement par des photographies locales : pas réalisé**. Les URL exactes de sources à traiter sont désormais isolées. La récupération automatique des photographies de fabricants/distributeurs exige une source qui réponde effectivement et la vérification des droits ; un fichier distant bloqué ne peut pas devenir une image réelle par un fallback CSS.


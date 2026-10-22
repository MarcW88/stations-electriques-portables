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

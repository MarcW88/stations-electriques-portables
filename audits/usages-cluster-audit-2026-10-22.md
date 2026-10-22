# Audit du cluster /usages/ — 2026-10-22

Périmètre : camping, van, coupure de courant, chantier, CPAP. Lecture du contenu courant et de `_generate.py` via GitHub (branche main). Cette revue n'est ni un test de navigateur ni une certification éditoriale.

## Vérifications statiques réalisées
- 5/5 pages présentes, sans marqueur `Contenu à rédiger`.
- 5/5 pages conservent `noindex, follow`.
- 5/5 ont cinq H2 et des ancres de section.
- 14 destinations internes distinctes vérifiées présentes dans le dépôt.
- 5/5 modules éditoriaux `usage_*_content.py` présents et importés dans `_generate.py`.
- Le générateur construit maintenant les sommaires depuis les H2 et applique des libellés documentaires aux pages d'usage.
- Les meta descriptions courtes des pages coupure, chantier et CPAP ont été améliorées ; descriptions du générateur alignées.

## Diagnostic éditorial
- **Camping** : JOB distinct (durée de séjour et appareils), conseils pratiques et calcul. Revoir preuves des hypothèses de rendement/consommations avant approbation.
- **Van** : distinction utile recharge en route, solaire et batterie auxiliaire. La comparaison avec Camping est pertinente, mais les intentions doivent être corroborées par données de recherche.
- **Coupure de courant** : article beaucoup plus court que les autres ; approfondissement recommandé sur les scénarios de panne, continuité, sécurité et choix des appareils, sans transformer la page en guide technique UPS.
- **Chantier** : valeur ajoutée sur les pointes de démarrage et limites environnementales ; vérification de conformité électrique belge nécessaire avant publication.
- **CPAP** : la compatibilité modèle/alimentation et les conseils de secours médical restent essentiels ; les sources fabricant et l'actualité des recommandations exigent revue humaine.

## Vérifications bloquées ou non exécutées
- `python3 scripts/verify_site_agents.py` : non exécuté.
- `python3 _generate.py` : non exécuté ; impossible de démontrer la parité HTML après régénération.
- `validate_usage_workflow.py` / `usage-workflow.config.yaml` : absents à la racine du dépôt.
- Playwright / responsive / CSS : non exécutés, sans captures.
- GSC, analyse SERP, performances réelles, crawl externe : non examinés.
- `fact-check` complet des assertions et sources, revue humaine, anti-AI-slop détaillé et vérifications SEO rendues : non certifiés.

## Décision de publication
**FAIL — KEEP_NOINDEX** pour les cinq pages, jusqu'au test de génération, à la QA substantielle de chaque page, au rendu navigateur et à la validation humaine explicite. Aucun changement de robots ou d'indexation n'a été effectué.

## Suite d'actions
1. Exécuter les scripts dans un checkout GitHub fiable, puis comparer la sortie générée aux pages actuelles et corriger les écarts.
2. Réaliser la validation des sources, l'analyse d'intention/SERP et la revue comparative du cluster.
3. Effectuer Playwright desktop/mobile et produire des captures.
4. Réexécuter `usage-analysis-workflow / PUBLISH_REVIEW` avec preuves, demander validation humaine avant toute indexation.

## Mise à jour — contrôle exécutable ajouté

- Nouveau script : `scripts/validate_usage_cluster.py`, qui vérifie le contenu, la parité des sources éditoriales, les ancres/TOC, les liens internes, les canonicals, les descriptions et le maintien de `noindex, follow`.
- Nouveau workflow GitHub Actions : `.github/workflows/usage-audit.yml`, censé exécuter l'intégrité des agents, la compilation Python, la génération et les vérifications statiques à chaque modification concernée sur `main`.
- Le clone GitHub depuis l'environnement local a échoué (résolution DNS de github.com), donc aucune exécution locale du build n'a été possible.
- La recherche des exécutions associées au commit de workflow n'a pas retourné de résultat ; ce connecteur ne remonte que les runs déclenchés par une pull request. Par conséquent, **aucune réussite CI n'est attestée**.
- Les corrections structurelles et les contrôles source sont enregistrés sur `main`, mais le gate publication reste **FAIL — KEEP_NOINDEX**.

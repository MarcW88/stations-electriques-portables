# Orchestration éditoriale — stations-electriques-portables

Copie du préparateur de `aspirateurs-chantier`, avec contexte et configuration locaux.

Le préparateur ne lance **aucun modèle IA** : il fabrique une file de pages, des empreintes de fichiers et un handoff pour l'agent du chat. Un statut GitHub Actions vert ne certifie ni audit ni correction.

```bash
python3 scripts/maintenance_orchestrator.py prepare --max-pages 10
python3 scripts/maintenance_orchestrator.py prepare --urls /guides/watt-ou-watt-heure/ --max-pages 1
```

Lire `AGENTS.md`, `.agents/shared-routing.json` et la paire de workflows `analysis/content` correspondante dans `.agents/skills/`. Respecter AUDIT, spécialistes, décision, corrections autorisées, PUBLISH_REVIEW et preuves. L'exécution Playwright est distincte et obligatoire pour une validation visuelle.

Les routes intégrées à `maintenance.config.json` sont les familles disposant de validateurs natifs identifiés. D'autres familles restent disponibles dans le routage partagé et doivent être exécutées manuellement avec leurs propres contrôles tant que les adaptateurs spécifiques ne sont pas intégrés. Ne pas utiliser des validateurs Guides pour prétendre valider la qualité de pages Solaire ou Puissance/capacité ; ils vérifient uniquement leur liste de slugs originelle.

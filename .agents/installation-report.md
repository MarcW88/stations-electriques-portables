# Installation des agents communs — 2026-10-22

Les 15 dépôts cibles ci-dessous ont reçu les 66 fichiers de skills originaux de Bloc-notes numérique, vérifiés octet par octet (SHA-256), leurs dépendances et les workflows complémentaires d’Aspirateurs chantier. Le paquet commun comporte 555 fichiers verrouillés, dont les deux versions sources complètes des workflows/scripts/configurations conservées sous `.agents/reference/`. Les 41 skills actifs communs sont identiques entre les dépôts cibles.

Source canonique : `MarcW88/bloc-notes-numerique@5b798c38648fdc32a9bbb0f2f6742b2dca9b7951`. Compléments : `MarcW88/aspirateurs-chantier@b11401c1e78ec1da7d90238fc1b903b48cca4933`. Les variantes de ces deux sources ne sont pas confondues : la version Bloc-notes est active sur les chemins communs, et tous les originaux Aspirateurs restent accessibles dans reference/. Les anciens fichiers locaux remplacés ont été sauvegardés avec leur empreinte.

Familles installées : guide, comparaison, marque/produit/accessoire, usage, offre, confiance, modèle, récupération de contenu et design/CSS/Playwright. La langue, le sujet et les routes sont adaptés séparément dans `.agents/site-context.shared.md`. AGENTS.md pointe vers les orchestrateurs originaux et leurs spécialistes complets.

| Dépôt | Commit d’installation sur main | Vérification |
|---|---|---|
| Leonardus | [581dd1b](https://github.com/MarcW88/Leonardus/commit/581dd1b0a782cd7b1480b4dfbe87b541922319e2) | [Intégrité GitHub : PASS](https://github.com/MarcW88/Leonardus/actions/runs/39739227749) |
| aspirateurs-chantier | [2385bde](https://github.com/MarcW88/aspirateurs-chantier/commit/2385bde8e1985d88d3f9911b585617d4c06480cf) | [Intégrité GitHub : PASS](https://github.com/MarcW88/aspirateurs-chantier/actions/runs/39739112171) |
| balkon-moestuin | [9a1fe12](https://github.com/MarcW88/balkon-moestuin/commit/9a1fe1231a4247eeadf3cf71f69382c5547bbce1) | [Intégrité GitHub : PASS](https://github.com/MarcW88/balkon-moestuin/actions/runs/39739550989) |
| biologische-hondensnacks | [e192ae5](https://github.com/MarcW88/biologische-hondensnacks/commit/e192ae5fcc8172788b2ba80e415fbbf66b524b4e) | [Intégrité GitHub : PASS](https://github.com/MarcW88/biologische-hondensnacks/actions/runs/39738945595) |
| cafetiere-italienne | [0ac3c23](https://github.com/MarcW88/cafetiere-italienne/commit/0ac3c23bca5e52becdd792f34ca48ca9aaab8c01) | [Intégrité GitHub : PASS](https://github.com/MarcW88/cafetiere-italienne/actions/runs/39739124111) |
| estimation-maison | [15db1b0](https://github.com/MarcW88/estimation-maison/commit/15db1b0ab4e26bcadc245d8a48e366c008e7e058) | [Intégrité GitHub : PASS](https://github.com/MarcW88/estimation-maison/actions/runs/39739544591) |
| freelance_website | [e0ee949](https://github.com/MarcW88/freelance_website/commit/e0ee949cb97ed0b11d82f37640ae0b6c2612df05) | [Intégrité GitHub : PASS](https://github.com/MarcW88/freelance_website/actions/runs/39739236675) |
| haken-breien-shop | [cdff1de](https://github.com/MarcW88/haken-breien-shop/commit/cdff1de18d21fb2b8ffd4f0a0a1be06fba7a01f4) | [Intégrité GitHub : PASS](https://github.com/MarcW88/haken-breien-shop/actions/runs/39739538291) |
| italiaanse-percolator | [0ca0679](https://github.com/MarcW88/italiaanse-percolator/commit/0ca067993c3505754fe71eae4a84ac9e24fd8b73) | [Intégrité GitHub : PASS](https://github.com/MarcW88/italiaanse-percolator/actions/runs/39739531073) |
| italian-moka-pot | [c42d388](https://github.com/MarcW88/italian-moka-pot/commit/c42d388852e822abfd7c7351af475de782d98df9) | [Intégrité GitHub : PASS](https://github.com/MarcW88/italian-moka-pot/actions/runs/39739557376) |
| kastelenbelgie | [82fea95](https://github.com/MarcW88/kastelenbelgie/commit/82fea95118d05a3701bf08ee5d85338d03cabb45) | [Intégrité GitHub : PASS](https://github.com/MarcW88/kastelenbelgie/actions/runs/39738696595) |
| stations-electriques-portables | [b303e13](https://github.com/MarcW88/stations-electriques-portables/commit/b303e13e97098e206e103e5dba7ee28f9b4984eb) | [Intégrité GitHub : PASS](https://github.com/MarcW88/stations-electriques-portables/actions/runs/39739238801) |
| thuisrenovatie-gids | [d55950c](https://github.com/MarcW88/thuisrenovatie-gids/commit/d55950c9dc2b58918a3efde3bb9f8ded838fd0bf) | [Intégrité GitHub : PASS](https://github.com/MarcW88/thuisrenovatie-gids/actions/runs/39739241911) |
| traitement-air | [1c3bae7](https://github.com/MarcW88/traitement-air/commit/1c3bae7b67eab61e8e6ebd41f82c6f8d58748780) | [Intégrité GitHub : PASS](https://github.com/MarcW88/traitement-air/actions/runs/39739233271) |
| visite-musee | [7c30b13](https://github.com/MarcW88/visite-musee/commit/7c30b136a4e069d472282678bed4205fd0f2b972) | [Intégrité GitHub : PASS](https://github.com/MarcW88/visite-musee/actions/runs/39739103902) |

## Vérification et limites

`python3 scripts/verify_site_agents.py` vérifie les fichiers et toutes les familles de workflows ; la même commande est exécutée par `.github/workflows/verify-site-agents.yml`. Les vérifications de provenance et de politique existantes de thuisrenovatie-gids et traitement-air passent avec les nouveaux verrous, sans modifier les skills sources.

Cette installation n’est pas un audit éditorial des pages. Les commandes de validation/génération natives et leurs éventuels adaptateurs sont recensés dans le contexte de chaque site ; une commande manquante doit être signalée BLOCKED. Les générateurs et Actions français originaux sont conservés dans reference/ et ne sont pas activés aveuglément sur d’autres sites. Le PASS d’intégrité ne certifie ni le contenu, ni un rendu Playwright, ni toutes les anciennes Actions CI. Les limites phase 1/audit-only des modèles sont conservées. Aucun contenu de page, URL ou statut d’indexation n’a été modifié par cette installation.

Les 15 contrôles GitHub d’intégrité ci-dessus ont été observés terminés avec succès. Les ajouts de DESIGN.md lient le workflow original au contexte du site sans modifier les SKILL.md.

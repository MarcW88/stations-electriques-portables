# IZYWATT brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/izywatt/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: IZYWATT / Orium portable power stations.

Intent: understand a short French range organised by use case and decide between mobile use, home backup and the more advanced Eco architecture with network injection.

The URL has a valid and potentially very distinctive `BRAND_HUB` role.

Unlike the larger international brands, IZYWATT does not need a generation-heavy catalogue explanation. Its strongest editorial angle is the progression:

- `IZYWATT 800` for compact essential loads;
- `Moov` for mobility;
- `Home` for backup/EPS;
- `Eco` for storage, expansion and controlled grid injection.

That use-case architecture is already visible in Orium's current official positioning and should become the page's editorial backbone.

## 2. Value already present — preserve

- Strong identification of the relationship between IZYWATT and Orium.
- Correct high-level distinction between 800, Moov, Home and Eco.
- Correct official positioning of Eco around adjustable grid injection.
- Correct identification of Home around EPS/backup.
- The page already recognises that IZYWATT is more use-case-led and less catalogue-heavy than EcoFlow/BLUETTI/Jackery.
- The absence of internal IZYWATT product pages is honestly documented.
- Documentary-analysis disclaimer is appropriate.

Current official evidence checked on 2026-09-09:

- https://www.oriumfrance.com/gammes/izywatt/

The official current range page explicitly presents IZYWATT 800, Eco, Home and Moov and describes Eco's adjustable grid injection from 0 to 800 W.

## 3. Blockers

### A. Structural cloning — HIGH

This page has one of the strongest unique brand propositions in the cluster, but still forces it into the same legacy sequence as the other hubs. The result is unnecessary generic content and reduced differentiation.

### B. Generic ecosystem/usages sections obscure the actual range logic — HIGH

The current page repeats the same general paragraphs about stations, solar, camping, CPAP, microwaves and capacity sizing as the other brands. IZYWATT already has a much clearer official use-case architecture, so these generic sections should be substantially reduced or removed.

### C. Grid-injection claim creates a higher evidence burden — HIGH

Eco's adjustable injection is a genuinely differentiating feature, but it is more sensitive than ordinary portable-station use. The rewrite must distinguish:

- what the manufacturer documents technically;
- what connection/accessory setup is required;
- what the site can safely explain without giving unsupported electrical-installation or regulatory claims.

The current caution is directionally correct but too general. Production should use product documentation/manuals for the exact configuration.

### D. Expansion / Extra battery needs direct product-level verification — MEDIUM/HIGH

The structured data states that IZYWATT Extra is a 2,048 Wh battery and that Eco can use up to four modules for a total of 10,240 Wh. This is plausible and already sourced in the repo, but the current main Orium range page does not expose those details in the text retrieved during this audit. Before rewrite, retain the claim only after direct notice/product-page verification.

Status: `SUPPORTED / REVERIFY`.

### E. “French support” should be phrased carefully — MEDIUM

Orium is a French company with a French contact presence. That supports “French brand/company presence”, but not automatically a claim that support quality is better. Avoid upgrading corporate location into an unsupported service-quality judgment.

### F. Independent evidence is thinner — MEDIUM

The current page correctly notes that IZYWATT has less international independent coverage than major global competitors. This creates a trust/evidence constraint: strong experiential claims should be avoided unless independent tests are found.

### G. Data model debt — MEDIUM

The structured ecosystem still contains inherited unrelated keys. Replace them with product/use-case relationships, EPS, solar input, grid injection, Smart Control, expansion battery compatibility and installation/accessory requirements.

## 4. Evidence status

- IZYWATT 800 518 Wh / 800 W: `VERIFIED` on current Orium range page.
- Eco 2,048 Wh and adjustable grid injection 0–800 W: `VERIFIED` on current Orium range page.
- Home positioned for backup with EPS: `VERIFIED`.
- Moov positioned for mobility/outdoor/chantier: `VERIFIED`.
- all stations described by Orium as solar compatible: `VERIFIED` at high level, but electrical input limits remain model-specific.
- Extra battery 2,048 Wh / up to four modules / 10,240 Wh total: `SUPPORTED / REVERIFY` via direct product documentation.
- “better French support”: `UNKNOWN`; do not state as fact.

## 5. Original affiliate value to target

The rewrite should answer:

1. Is my need mobile, backup-oriented or home-energy-oriented?
2. Why would I choose Home instead of Eco, or Eco instead of a conventional 2 kWh portable station?
3. What does grid injection actually add, and what additional setup/constraints come with it?
4. When does Eco's expandability matter?
5. Is IZYWATT attractive because of its short range and local brand context, or would a deeper international ecosystem be more appropriate?

## 6. Bespoke rewrite direction

Likely direction:

- lead with the four-use-case map rather than a generic brand introduction;
- distinguish “portable station” from “home-energy system” before discussing specs;
- make Home vs Eco the central high-capacity decision;
- explain Eco's injection feature carefully from direct documentation;
- keep 800/Moov focused on actual mobility and load range;
- avoid forcing generic “forces / limites / choisir / éviter” sections;
- alternatives should correspond to a specific need: broader model choice, more independent test coverage, >3 kW portable output, deeper expansion ecosystem, etc.

## 7. Unknowns before production

- direct product/manual confirmation for Eco + Extra maximum expansion;
- exact solar input limits for 800, Moov, Home and Eco;
- exact EPS transfer characteristics by model;
- Smart Control capabilities and dependency on app/cloud;
- required official accessories/connection method for grid injection;
- current retail availability by model.

## 8. Required actions

1. Build product-level evidence for Eco/Extra, Home and Moov.
2. Migrate the structured entity model.
3. Preserve the use-case-led brand positioning.
4. Remove generic cluster prose.
5. Rewrite around 800/Moov/Home/Eco decision logic.
6. Treat grid injection as a high-evidence technical claim.
7. Run post-draft fact-check and `PUBLISH_REVIEW`.
8. Keep `noindex,follow` until explicit human approval.

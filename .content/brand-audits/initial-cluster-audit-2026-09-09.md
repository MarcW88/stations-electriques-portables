# Initial brand cluster audit — 2026-09-09

Mode: `CLUSTER_AUDIT`

Scope sampled in detail:

- `/marques/ecoflow/`
- `/marques/jackery/`
- `/marques/aferiy/`

Cluster context: seven brand hubs are generated from `.content/brand-pages/` and structured data in `.content/brands/`.

## Executive decision

**Sampled pages: `DEEP_REWRITE`**

Confidence: **HIGH** for EcoFlow, Jackery and AFERIY.

The recommendation is not caused by weak technical data. The current pages already contain useful researched facts, dated official sources, normalized tables, internal links and an explicit desk-research disclaimer. The blocker is the editorial architecture: the three sampled pages are visibly produced from the same skeleton and reuse several paragraphs almost word for word.

The old config and CI explain part of the problem: they imposed minimum word/H2/link counts and mandatory `choose / avoid` blocks. These gates encouraged pages to converge toward the same shape instead of letting the brand-specific decision problem determine the outline.

## Value already present — preserve during rewrites

- dated official sources;
- explicit `analyse documentaire` language;
- current/previous-generation distinctions;
- capacity and power tables;
- useful links to `/modeles/`, comparatifs, guides, usages and calculator;
- visible limitations rather than conversion-only copy;
- `noindex,follow` preserved during draft production.

This material should be recovered, not discarded.

## Blocker 1 — structural cloning

EcoFlow, Jackery and AFERIY use the same section sequence:

1. answer box;
2. `Ce qui distingue [marque]`;
3. current range;
4. ecosystem;
5. usages;
6. strengths;
7. limitations;
8. who should choose;
9. who should avoid;
10. alternatives;
11. sources.

The problem is not the shared HTML components. It is that the same editorial questions are asked in the same order even though the brands have different reasons to exist in the market.

## Blocker 2 — repeated generic prose

Examples of repeated functions and copy across the three sampled pages:

- the paragraph explaining that readers should compare capacity, continuous power, weight, solar, UPS/EPS and expansion;
- the paragraph introducing current vs previous generations;
- `Une station n’est pas un produit isolé...` ecosystem introduction;
- the generic use-case paragraph covering phones, routers, laptops, fridges, CPAP and appliances;
- the paragraph explaining when expandable batteries or fast UPS matter;
- the generic paragraph after limitations explaining why the site does not use one global score;
- the closing paragraph of the `choose` section;
- the definition of what `avoid` means;
- alternatives described with the same formula about weight, power, solar and expansion.

These passages are individually reasonable, but their repetition makes the cluster look industrialized and reduces brand-specific value.

## Blocker 3 — station-specific entity model is incomplete

The EcoFlow structured data still contains ecosystem keys inherited from another product universe, including:

- `stylus`;
- `notes`;
- `pdf`;
- `ocr`.

For this repo, the primary entity model should instead center on:

- station / product family;
- capacity Wh;
- continuous power W;
- battery chemistry;
- inverter / BMS where decision-relevant;
- AC/DC/USB outputs;
- solar / MPPT;
- extra batteries;
- panels and accessories;
- AC / vehicle / alternator charging;
- UPS/EPS;
- app / firmware;
- use cases and limitations;
- competitors and alternatives.

This is a data-model migration task, not necessarily a visible-page section requirement.

## Brand-specific rewrite direction

### EcoFlow — `DEEP_REWRITE`

Keep the verified range and product links, but rebuild the page around the choice problem that is actually specific to EcoFlow:

- understand RIVER vs DELTA before looking at individual models;
- decide whether expansion and multi-source charging are actually useful;
- show where the ecosystem creates value and where it creates complexity;
- route to capacity/use-case pages only after that decision is clear.

The page should not need a generic `forces → limites → choisir → éviter` sequence if a more direct decision tree or family-based architecture is clearer.

### Jackery — `DEEP_REWRITE`

Rebuild around the questions specific to Jackery:

- how `v2`, `Plus` and older Explorer generations differ;
- when the simpler SolarSaga / generator-kit logic is an advantage;
- where portability and power trade off against competitors;
- which capacity family is coherent for camping, camping-car or backup.

The outline should make Jackery's range logic easier to understand, rather than repeating the EcoFlow page with different model names.

### AFERIY — `DEEP_REWRITE`

Rebuild around AFERIY's real decision tensions:

- high capacity/power for the price;
- the Nano / Nomad / Haven naming transition;
- expandability on some models but not others;
- the point where weight makes a nominally portable station effectively semi-fixed;
- whether the value proposition compensates for a less mature ecosystem or brand environment.

This page should feel materially different from EcoFlow and Jackery.

## Unknowns / next audit work

The four other hubs — ALLPOWERS, Anker SOLIX, BLUETTI and IZYWATT — were not inspected line by line in this first pass. Given the old mandatory structure and validator, cluster-wide cloning risk is high, but each page still needs an individual `AUDIT` before its rewrite decision is finalized.

## Recommended next step

Use **EcoFlow as the pilot rewrite** because it is currently the qualitative reference page and has enough product/evidence depth to test the new workflow properly.

Sequence:

1. `brand-analysis-workflow / AUDIT` on EcoFlow;
2. preserve verified facts and useful table/link assets;
3. rebuild the station-specific entity/evidence brief;
4. produce a bespoke EcoFlow outline;
5. rewrite via `brand-content-workflow`;
6. run `_validate_brands.py`;
7. run `brand-analysis-workflow / PUBLISH_REVIEW` against the cluster;
8. keep `noindex,follow` until explicit human approval.

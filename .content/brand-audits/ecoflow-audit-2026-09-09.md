# EcoFlow — AUDIT + research/evidence brief — 2026-09-09

Target: `/marques/ecoflow/`

Mode: `AUDIT`

## Decision

**DEEP_REWRITE**

Confidence: **HIGH**.

The page already contains a useful factual base, but its editorial architecture is cloned from the other brand hubs. The rewrite must preserve verified facts, useful internal links and the desk-research disclaimer while rebuilding the page around the EcoFlow-specific decision problem.

## Search intent / reader decision

Primary topic: EcoFlow portable power stations / EcoFlow range.

Intent: commercial investigation with technical comparison.

The reader does not mainly need a brand history. The useful decision sequence is:

1. understand whether the need belongs in RIVER or DELTA;
2. size capacity and continuous power;
3. decide whether expansion, solar input and vehicle/alternator charging are genuinely useful;
4. understand the portability penalty as the system grows;
5. only then choose a model or compare EcoFlow with another brand.

Cannibalization boundary: the brand hub should explain the range logic and ecosystem. Detailed model specs belong to `/modeles/`; cross-brand ranking belongs to `/comparatifs/`; autonomy sizing belongs to the calculator/guides.

## Recovery — what to preserve

- current RIVER / DELTA distinction;
- verified capacity and power values;
- explicit distinction between continuous output, peak output and X-Boost;
- current/older-generation context;
- links to EcoFlow model pages already present in the repo;
- links to W/Wh, autonomy, solar, UPS/EPS and usage pages when they answer the next question;
- official sources and verification date;
- `analyse documentaire` language;
- `noindex,follow` during draft state.

## What must change

- remove the inherited `positionnement → gamme → écosystème → usages → forces → limites → choisir → éviter → alternatives` skeleton;
- remove generic paragraphs shared with Jackery/AFERIY;
- make RIVER vs DELTA the first real decision;
- make expansion compatibility a decision topic rather than a generic ecosystem benefit;
- show the weight progression so “portable” is not treated as one category;
- migrate structured data away from inherited `stylus/notes/pdf/ocr` keys;
- represent newer current catalog anchors such as DELTA 3 Classic / DELTA 3 1500 without turning the page into a complete merchant catalog.

## Evidence ledger

| Claim / question | Source | Verified | Status | Decision value |
|---|---|---:|---|---|
| RIVER 3: 245 Wh, 300 W, 3.55 kg, LFP, 110 W solar input | https://fr.ecoflow.com/products/river-3-portable-power-station | 2026-09-09 | VERIFIED | establishes compact/light baseline |
| RIVER 3 Plus: 286 Wh, 600 W, 4.7 kg, 220 W solar, EB300/EB600, up to 858 Wh | https://fr.ecoflow.com/products/river-3-plus-portable-power-station | 2026-09-09 | VERIFIED | shows first meaningful expansion step |
| DELTA 3 / DELTA 3 Plus: 1,024 Wh, 1,800 W; DELTA 3 Plus has 2×500 W MPPT; family can expand from 1 to 5 kWh with listed EcoFlow extra batteries | https://fr.ecoflow.com/collections/1-delta-series-menu/products/delta-3-series-portable-power-station | 2026-09-09 | VERIFIED | defines 1 kWh system tier and multi-source charging value |
| DELTA 3 Max Plus: 2,048 Wh, 3,000 W, ~22.1 kg, 1,000 W solar, LFP, expansion architecture up to 10 kWh in documented configurations | https://fr.ecoflow.com/products/delta-3-max-series-portable-power-station | 2026-09-09 | VERIFIED | shows transition from portable to transportable/high-power |
| Some DELTA 3 Max Plus multi-battery configurations require an expansion adapter; exact accessory availability must be checked | https://fr.ecoflow.com/products/delta-3-max-series-portable-power-station | 2026-09-09 | VERIFIED | prevents overpromising expansion simplicity |
| DELTA Pro 3: 4,096 Wh, 4,000 W, 51.5 kg, 2,600 W solar input, LFP, expandable to 12 kWh | https://fr.ecoflow.com/products/delta-pro-3-portable-power-station | 2026-09-09 | VERIFIED | establishes home-backup tier and portability limit |
| EcoFlow France currently lists newer/current entries including DELTA 3 Classic and DELTA 3 1500 alongside older models still sold | https://fr.ecoflow.com/pages/portable-power-stations | 2026-09-09 | VERIFIED | justifies family-level map instead of pretending one clean generation replaces all older stock |
| Warranty differs by family: DELTA 3/3 Plus listed at 5 years; DELTA 3 Max/Max Plus at 3+2 years with registration; DELTA Pro 3 at 5 years | https://fr.ecoflow.com/pages/warranty-policy | 2026-09-09 | VERIFIED | relevant when comparing system generations |

## Unknowns / deliberately excluded

- real-world autonomy for specific appliances: depends on load, inverter losses, temperature and duty cycle; route to calculator instead of inventing values;
- long-term reliability: no site hands-on evidence sufficient for a brand-level claim;
- app quality / UX superiority: not asserted without independent evidence synthesis;
- current promotional prices: too volatile for durable brand copy;
- blanket compatibility of third-party solar panels: not inferred from connector shape alone.

## Affiliate value / original value

The page should remain useful without any affiliate links by explaining:

- what RIVER vs DELTA changes in practice;
- when expansion is useful versus unnecessary cost/weight;
- why EcoFlow’s compatibility matrix deserves checking before buying an extra battery;
- where “portable” stops being a practical description as weight rises from 3.55 kg to ~22 kg and then 51.5 kg;
- how to choose a model family from a concrete load/usage rather than from brand marketing.

## Bespoke outline justified by evidence

1. `En bref` — one-sentence decision frame: EcoFlow is broad; choose family and system architecture before model.
2. `RIVER ou DELTA : choisissez d’abord le bon niveau` — resolves the first navigation decision.
3. `Cinq repères pour lire la gamme EcoFlow` — normalized technical table of decision anchors, explicitly not a complete catalog.
4. `L’écosystème EcoFlow vaut surtout si vous utilisez plusieurs modes de recharge` — explains where the ecosystem creates real value.
5. `Batteries additionnelles : un vrai avantage, mais pas un Lego universel` — compatibility and expansion caveats.
6. `Portable : 3.55 kg, 12.5 kg, 22.1 kg ou 51.5 kg ne racontent pas la même chose` — makes transportability concrete.
7. `Quel niveau EcoFlow correspond à votre besoin ?` — routes by usage/load without pretending to provide exact runtime.
8. `Quand EcoFlow devient moins rationnel` — situations where the ecosystem is unnecessary or oversized.
9. `Sources et niveau de preuve`.

This outline is deliberately different from the sibling brand pages and is traceable to the EcoFlow evidence brief.

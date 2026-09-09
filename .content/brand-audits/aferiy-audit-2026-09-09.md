# AFERIY brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/aferiy/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: AFERIY portable power stations / Nano, Nomad and Haven ranges.

Intent: understand the brand's current range and decide whether its capacity/power proposition compensates for weight, product-line complexity and a less mature ecosystem than the largest competitors.

The URL has a valid autonomous `BRAND_HUB` role.

The most useful AFERIY-specific decision tensions are:

- high Wh/W for the price vs weight and portability;
- Nano / Nomad / Haven naming vs legacy Pxxx naming;
- fixed-capacity vs expandable models;
- whether the larger P280/P300/P310 systems are still “portable” in practical use;
- whether the ecosystem/SAV/software depth is sufficient for the intended use.

## 2. Value already present — preserve

- Clear distinction between Nano, Nomad and Haven.
- Useful capacity/power data for Nano100, Nomad400 P040, Nomad800 P010, Nomad1800 Pro, P210, P280 and P310.
- Correct identification that P210 is not the same proposition as expandable P280/P310.
- Relevant links toward powerful-station comparisons, LiFePO4, UPS and camping-car/house use cases.
- Explicit documentary-analysis disclaimer.

Current official evidence checked on 2026-09-09:

- https://fr.aferiy.com/pages/compare-aferiy-portable-power-stations
- https://fr.aferiy.com/collections/station-denergie-portable

## 3. Blockers

### A. Structural cloning — HIGH

The page still uses the exact legacy cluster architecture and generic transitional prose used across the other brand hubs.

### B. Current range is incomplete — HIGH

The current official AFERIY comparison page includes at least:

- Haven3000 P300 — 3,000 W / 2,048–10,240 Wh;
- Nomad1800 — 1,800 W / 1,024 Wh;

These are absent from the current brand page while it presents its table as the current 2026 range. The page therefore needs a fresh range model before production.

### C. Naming transition is mentioned but not solved — HIGH

The page notes that Pxxx names coexist with Nano/Nomad/Haven, but does not actually help the reader map old/new naming or understand whether two names represent the same family, a variant, or a distinct generation.

### D. Price/value positioning is insufficiently evidenced — MEDIUM

“Rapport capacité/puissance” is a useful angle, but “tarifs souvent agressifs” is time-sensitive and should be supported by dated price comparisons if retained. Without that, the page risks leaning on a generic merchant/value narrative.

### E. Ecosystem maturity claim needs stronger evidence — MEDIUM

The page implies a less mature software/domotics environment than competitors. That may be directionally fair, but it needs evidence from documented app capabilities, accessory depth and independent sources before becoming a strong comparative claim.

### F. Data model debt — MEDIUM

The structured data still contains inherited keys (`stylus`, `notes`, `pdf`, `ocr`). The model should instead persist expansion batteries, charging inputs, solar limits, UPS/EPS, app support, weight, generations and compatibility.

## 4. Evidence status

- Nano100 / Nomad400 / Nomad800 / Nomad1800 / Nomad1800 Pro: `VERIFIED` as current families/products on the official comparison page.
- Haven P210 / P280 / P300 / P310: `VERIFIED` as current products on the official comparison page.
- P280 2,048–10,240 Wh and P310 3,840–11,520 Wh: `VERIFIED`.
- “AFERIY is cheaper / better value than competitors”: `UNKNOWN` without a dated benchmark.
- “Less mature ecosystem/software”: `INFERRED`; requires comparative evidence before strong wording.

## 5. Original affiliate value to target

The rewrite should answer:

1. Which AFERIY family actually fits the need: Nano, Nomad or Haven?
2. Which models are expandable and how far?
3. At what weight/capacity does a Haven become semi-fixed rather than genuinely portable?
4. Is the extra capacity worth choosing AFERIY over a competitor with a stronger ecosystem or simpler generation structure?
5. Which current product replaces or overlaps the legacy Pxxx model the reader may have found elsewhere?

## 6. Bespoke rewrite direction

Likely editorial direction:

- lead with the naming map: Nano / Nomad / Haven and legacy Pxxx references;
- separate “portable” from “transportable” using actual weight and capacity thresholds;
- compare fixed vs expandable AFERIY architectures;
- explain why P210, P280, P300 and P310 should not be treated as a simple linear ladder;
- only use price/value claims when dated and benchmarked;
- position alternatives by ecosystem maturity, portability or expansion architecture rather than generic brand substitution.

## 7. Unknowns before production

- current exact weights of all retained models;
- model-by-model expansion-battery compatibility;
- exact UPS transfer values by model;
- current app support by model;
- dated France/EU price positioning vs comparable BLUETTI/EcoFlow/ALLPOWERS products.

## 8. Required actions

1. Refresh the product-range ledger to include P300 and Nomad1800 where relevant.
2. Build a naming/generation map.
3. Migrate structured entities.
4. Replace generic cluster prose with AFERIY-specific decision logic.
5. Fact-check weights, expandability, UPS and app support.
6. Rewrite through `brand-content-workflow`.
7. Run `PUBLISH_REVIEW` and keep `noindex,follow` pending human validation.

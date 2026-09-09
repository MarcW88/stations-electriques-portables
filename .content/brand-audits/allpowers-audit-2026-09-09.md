# ALLPOWERS brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/allpowers/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: ALLPOWERS portable power stations / R, VOLIX and legacy S ranges.

Intent: understand a broad, sometimes confusing catalogue and identify the correct generation/version before comparing capacity, power, solar input, expansion and availability.

This is a valid `BRAND_HUB`, but its strongest role should be “decode the ALLPOWERS catalogue”, not repeat generic power-station buying advice.

## 2. Value already present — preserve

- The page correctly identifies catalogue complexity as the main buyer risk.
- Useful capacity/power anchors are already present for VOLIX P300, R600, R1500 Lite, R2500, R3500 and R4000 Lite.
- It correctly warns that R2500 variants need exact-version verification.
- Solar input, UPS and expandability are relevant brand-specific dimensions.
- Documentary-analysis disclaimer and useful internal links should be retained.

Current official evidence checked on 2026-09-09:

- https://iallpowers.com/collections/portable-power-stations

The official collection currently shows VOLIX P300, R600, R1500 Lite, R2500, R2500 v2, R3500, R4000/R4000 Lite and several S-series products.

## 3. Blockers

### A. Structural cloning — HIGH

The page uses the legacy cluster skeleton and multiple generic paragraphs identical in function and wording to the other brand hubs.

### B. Product lifecycle/status contradiction — HIGH

The page classifies `S700` as `Génération précédente`. The current official ALLPOWERS portable-power-station collection still lists S700/S-series products among active products. This does not prove every S product is strategically current, but the current page's categorical lifecycle label is not sufficiently supported.

Status: `CONTRADICTED / NEEDS_RECLASSIFICATION`.

### C. R4000 naming/version ambiguity — HIGH

Official ALLPOWERS navigation references `R4000` as a 4,000 W product, while the collection body also presents `R4000 Lite` at 3,600 W / 3,456 Wh. The current page only presents `R4000 Lite` and calls it the top of the collection. The rewrite must explicitly separate these variants rather than treat “R4000” as one stable specification.

### D. The range selection is too editorially compressed — MEDIUM/HIGH

The official collection also surfaces S2000 Pro, S300 Plus/S200 and P1800. A brand hub need not list every SKU, but if it claims to explain the current range, it needs a defensible family map showing why some products are included and others omitted.

### E. Source localisation / commercial state — MEDIUM

The evidence currently relies heavily on the global/US ALLPOWERS site even though France/Europe storefronts exist. Availability, warranty, stock and exact variants should be checked against the relevant European/French storefront before strong commercial claims.

### F. Generic “value” claims — MEDIUM

“Rapport capacité/puissance agressif” may be true, but it is a comparative claim. It should be supported by a dated benchmark or softened to a factual description of the specs.

### G. Data model debt — MEDIUM

The structured ecosystem contains inherited unrelated keys. It should instead model exact variants, LFP vs older chemistry, solar-input limits, expansion batteries B1000/B3000, app support, UPS transfer, stock/region and generation/version status.

## 4. Evidence status

- VOLIX P300 256 Wh / 300 W: `VERIFIED`.
- R600 299 Wh / 600 W: `VERIFIED`.
- R1500 Lite 1,056 Wh / 1,600 W and 15 ms UPS: `VERIFIED` on official collection.
- R2500 2,016 Wh / 2,500 W: `VERIFIED`.
- R2500 v2 1,920 Wh / 2,500 W: `VERIFIED` as a distinct current listing.
- R3500 3,168 Wh / 3,200 W: `VERIFIED`.
- R4000 Lite 3,456 Wh / 3,600 W: `VERIFIED` in collection body.
- “S700 = previous generation”: `CONTRADICTED / UNKNOWN`.
- exact relationship between R4000 and R4000 Lite: `UNKNOWN` until product-level research.

## 5. Original affiliate value to target

The rewrite should primarily solve version confusion:

1. Which ALLPOWERS family/version am I actually looking at?
2. Is it R2500, R2500 v2 or another similarly named variant?
3. Does that exact version use LFP, support UPS, accept an expansion battery, and at what solar input?
4. Is an older S-series deal still rational or merely hard to compare with newer R/VOLIX products?
5. Does the European/French stock actually match the global catalogue?

## 6. Bespoke rewrite direction

Recommended direction:

- open with a “decode the catalogue before buying” framing;
- group products by version/family rather than a simple capacity ladder;
- make R2500 and R4000 naming ambiguity a central buyer-safety section;
- separate current technical relevance from current stock/region availability;
- compare legacy S products only when they remain purchasable and technically competitive;
- alternatives should solve a specific issue such as catalogue clarity, ecosystem coherence, service/distribution or expansion compatibility.

## 7. Unknowns before production

- exact current France/EU lineup and stock;
- exact R4000 vs R4000 Lite relationship;
- current lifecycle status of S700/S2000 Pro/S300 Plus;
- expansion compatibility by R-series model;
- app/UPS/solar-input differences by exact variant.

## 8. Required actions

1. Rebuild product/version ledger from France/EU sources plus manuals.
2. Correct lifecycle statuses.
3. Split ambiguous variants into separate entities.
4. Migrate the data model.
5. Remove generic cluster structure and prose.
6. Rewrite around catalogue/version decoding.
7. Run post-draft fact-check and `PUBLISH_REVIEW`.
8. Keep `noindex,follow` pending explicit human approval.

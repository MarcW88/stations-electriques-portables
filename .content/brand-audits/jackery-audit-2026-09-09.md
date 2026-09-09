# Jackery brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/jackery/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: Jackery portable power stations / Jackery Explorer range.

Intent: understand the current Jackery range, distinguish generations, and decide which capacity/family fits camping, campervan or backup use.

The page has a valid autonomous role as a `BRAND_HUB`. It should not become a generic “is Jackery good?” review or duplicate individual Explorer model pages.

The most useful Jackery-specific decision problem is not “strengths vs weaknesses”; it is:

- how the current `v2` line differs from `Plus` and older `Pro` products;
- whether Jackery's relatively simple Explorer + SolarSaga logic is an advantage for the reader;
- what portability is gained or lost as capacity rises from 256 Wh to 3,072 Wh;
- when expansion matters and when a fixed-capacity v2 station is enough.

## 2. Value already present — preserve

- The current v2 range is correctly represented at a high level: Explorer 240 v2, 500 v2, 1000 v2, 2000 v2 and 3000 v2.
- Capacity and continuous-power values are useful and consistent with the current official v2 collection.
- The page distinguishes current and older product generations instead of treating every Explorer as equivalent.
- SolarSaga is correctly identified as a meaningful part of the brand ecosystem.
- The page explicitly states that it is a documentary analysis rather than a hands-on test.
- Internal links to Explorer model pages, camping/campervan content and the autonomy calculator are relevant assets.

Current official evidence checked on 2026-09-09:

- https://fr.jackery.com/collections/serie-v2-station-electrique-portable
- https://fr.jackery.com/products/explorer-1000-v2-portable-power-station
- https://fr.jackery.com/collections/serie-v2-generateur-solaire

## 3. Blockers

### A. Structural cloning — HIGH

The page still follows the legacy cluster skeleton:

`positionnement → gamme → écosystème → usages → forces → limites → choisir → éviter → alternatives → sources`

Several paragraphs are functionally identical to AFERIY, ALLPOWERS, BLUETTI, Anker SOLIX and IZYWATT. This is a substantive `anti-ai-slop` / industrialisation signal, not merely shared styling.

### B. The real v2 / Plus decision is underdeveloped — HIGH

The current page says that v2 and Plus coexist, but the distinction is not used to structure the user's decision. A reader should understand why a Plus model may still be relevant, particularly when extension is important, rather than seeing Plus as one more row in a catalogue.

### C. Generic use-case prose dilutes brand-specific value — MEDIUM

The paragraph covering phones, routers, laptops, fridges, CPAP, microwaves and heaters could apply to any brand. It should be replaced by Jackery-specific capacity/weight trade-offs and then route to the site's generic dimensioning guides.

### D. Alternatives are generic — HIGH

EcoFlow, BLUETTI and Anker SOLIX are listed for the same generic reasons used elsewhere in the cluster. Alternatives need to be tied to a reason for leaving Jackery: e.g. more expandable architecture, different power density, deeper home-backup ecosystem, or another solar/vehicle-charging strategy.

### E. Data model debt — MEDIUM

The structured `ecosystem` still contains inherited keys such as `stylus`, `notes`, `pdf` and `ocr`. Replace them with station-specific relationships: product family, battery chemistry, continuous power, solar input, compatible SolarSaga panels, expansion capability, UPS, application, vehicle charging and generation status.

## 4. Evidence status

- Current v2 lineup: `VERIFIED`.
- Explorer 1000 v2 1,070 Wh / 1,500 W: `VERIFIED`.
- LFP and UPS ≤20 ms on Explorer 1000 v2: `VERIFIED`.
- v2 solar-generator kits across 240/500/1000/2000/3000 v2: `VERIFIED`.
- Exact ongoing status and positioning of every `Plus` product in France: `SUPPORTED`, but should be rechecked model by model before rewrite.
- Claim that Jackery is categorically “simpler” than competitors: `INFERRED`; usable only as a qualified editorial interpretation.

## 5. Original affiliate value to target

The rewrite should help the user answer:

1. Do I need a current v2 or does a Plus model make more sense because I need expansion?
2. At what capacity does Jackery stop being genuinely easy to carry for my use?
3. When does buying a SolarSaga kit simplify the system, and when should solar compatibility be checked more carefully?
4. Which Explorer capacity is coherent for camping, campervan or home backup without oversizing?

The page must remain useful with every affiliate link removed.

## 6. Bespoke rewrite direction

Recommended architecture should be built around the Jackery range logic rather than the cluster template. A likely direction:

- start with the current `v2` spine and explain what changed;
- isolate the `Plus` branch only where expandability changes the decision;
- compare capacity families using weight / power / practical mobility rather than a generic strengths list;
- treat SolarSaga as a “system simplicity vs compatibility” decision;
- explain when an older Pro/Plus offer is still rational if price and warranty are favorable;
- alternatives only after a concrete reason to leave Jackery is identified.

Do not copy this outline mechanically during production; the final plan must be rebuilt from the evidence brief.

## 7. Unknowns before production

- exact current French availability of the remaining Plus line;
- model-specific expansion compatibility across Plus products;
- model-specific solar input and connector constraints for the products actually retained in the rewrite;
- whether any older Explorer pages should be treated as current discounted stock vs previous generation.

## 8. Required actions

1. Rebuild Jackery evidence ledger around current v2 + decision-relevant Plus products.
2. Migrate the structured entity model.
3. Preserve verified product facts and useful internal links.
4. Remove generic cluster prose.
5. Produce a brand-specific outline via `brand-content-workflow`.
6. Run post-draft fact-check and `PUBLISH_REVIEW`.
7. Keep `noindex,follow` until explicit human approval.

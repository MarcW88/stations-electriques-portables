# BLUETTI brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/bluetti/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: BLUETTI portable power stations / Elite, Apex and older AC/EB families.

Intent: understand the current BLUETTI generation structure and choose between compact portable models, 1–2 kWh stations and more expandable backup-oriented systems.

The URL has a valid autonomous `BRAND_HUB` role.

The most useful BLUETTI-specific problem is generation/family decoding: `Elite` now structures the mainstream portable line, `Apex` moves toward larger expandable backup systems, while older `AC`/`EB` references remain highly visible in search, retailers and existing content.

## 2. Value already present — preserve

- Correct focus on current Elite and Apex families.
- Useful current anchors: Elite 30 V2, Elite 100 V2, Elite 200 V2 and Apex 300.
- Correct recognition that older AC/EB products still matter for users comparing historical reviews and discounted stock.
- Capacity/power data are useful and aligned with the current official portable-station page for the main Elite/Apex products.
- UPS, expansion and vehicle charging are correctly identified as decision-relevant.
- Existing model links to Elite 200 V2 and AC180 are useful assets.
- Documentary-analysis disclaimer should remain.

Current official evidence checked on 2026-09-09:

- https://fr.bluettipower.eu/pages/station-de-energie-portative
- https://fr.bluettipower.eu/products/elite-200-v2

The current official selection prominently surfaces Elite 100 V2, Elite 200 V2, Apex 300 and Elite 30 V2.

## 3. Blockers

### A. Structural cloning — HIGH

The page follows the same legacy cluster skeleton and repeats the same generic explanations about W/Wh, ecosystem, use cases, strengths, limits, choosing, avoiding and alternatives.

### B. The generation map is identified but not actually solved — HIGH

The page says users should distinguish Elite/Apex from AC/EB, yet it still presents the range as a conventional table. A better brand hub should explicitly explain what has replaced what, what remains current, and when an older AC-series product can still make sense.

### C. AC70 lifecycle status needs re-verification — MEDIUM/HIGH

The current page labels AC70 as `CURRENT`. The current official portable-station selection page prominently pushes Elite/Apex and does not surface AC70 in its main current-choice block. That does not prove AC70 is discontinued, but its status should be rechecked against the store/product page before the rewrite.

Status: `UNKNOWN / NEEDS_RECHECK`.

### D. Marketing longevity claims need careful handling — MEDIUM

The official site uses marketing language such as “17-Year Lifespan” for Elite 200 V2. The brand hub should not repeat lifespan claims without tying them to documented cycle methodology and retention thresholds.

### E. Expansion architecture is too generic — HIGH

Apex 300 plus B500K / charging accessories is a materially different architecture from an Elite 30/100/200. The current “ecosystem” section flattens these distinctions.

### F. Alternatives are generic — HIGH

The alternatives section uses the same formula as other brands. Alternatives should answer a specific BLUETTI limitation: simpler nomenclature, lower weight, different expansion system, more streamlined camping kit or another vehicle-charging approach.

### G. Data model debt — MEDIUM

The structured ecosystem still includes unrelated inherited keys. The data should instead represent family/generation, power, capacity, weight, UPS transfer, expansion compatibility, Charger 2/vehicle charging, solar input, battery modules and current/legacy status.

## 4. Evidence status

- Elite 30 V2 288 Wh / 600 W / LiFePO4 / UPS ≤10 ms: `VERIFIED`.
- Elite 100 V2 1,024 Wh / 1,800 W / LiFePO4: `VERIFIED`.
- Elite 200 V2 2,073.6 Wh / 2,600 W / LiFePO4: `VERIFIED`.
- Apex 300 2,764.8 Wh / 3,840 W / LiFePO4: `VERIFIED`.
- Apex 300 + B500K / Charger 2 as current system configurations: `VERIFIED` on the official selection page.
- AC70 current lifecycle status: `UNKNOWN` pending product/store verification.
- older AC180 / AC200MAX / EB3A as “previous generation” collectively: `SUPPORTED` as an editorial grouping, but should be verified individually.

## 5. Original affiliate value to target

The rewrite should answer:

1. What is the practical difference between Elite and Apex?
2. Which older AC/EB models remain rational if found at a good price?
3. When does BLUETTI's expansion ecosystem become useful rather than unnecessary complexity?
4. Is the reader buying a portable station or gradually building a backup system?
5. Which charging/vehicle accessories are actually compatible with the chosen family?

## 6. Bespoke rewrite direction

Likely editorial direction:

- start with the generation map: Elite vs Apex vs legacy AC/EB;
- use portability and system growth as the main fork in the decision;
- treat Elite 30/100/200 as distinct portability/capacity steps rather than generic “strengths”;
- treat Apex as a different architecture, not simply the largest BLUETTI;
- include a “when an older AC model still makes sense” section only if current evidence supports it;
- alternatives based on nomenclature simplicity, weight, system expansion or charging ecosystem.

## 7. Unknowns before production

- exact current status of AC70, AC180, AC200MAX and EB3A in France;
- exact expansion-battery compatibility by Elite/Apex model;
- Charger 2 compatibility and limits by model;
- current product weights for all retained comparison anchors;
- cycle/longevity claims and exact retention thresholds for any longevity comparison.

## 8. Required actions

1. Build a current-vs-legacy BLUETTI generation ledger.
2. Verify AC70 and older AC/EB status individually.
3. Migrate the structured entity model.
4. Preserve verified Elite/Apex technical data and useful model links.
5. Replace generic cluster prose with generation/system architecture logic.
6. Run fact-check after drafting.
7. Run `PUBLISH_REVIEW` and preserve `noindex,follow` pending explicit approval.

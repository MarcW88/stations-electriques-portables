# Anker SOLIX brand audit — 2026-09-09

Mode: `AUDIT`
URL: `/marques/anker-solix/`
Decision: **`DEEP_REWRITE`**
Confidence: **HIGH**

## 1. Search intent and page role

Primary topic: Anker SOLIX portable power stations / C-series.

Intent: understand the current Gen 2 portable lineup, how it differs from the sold-out first generation, and whether compactness, power density, charging speed, UPS and vehicle charging justify choosing SOLIX.

The page has a valid `BRAND_HUB` role.

The strongest Anker-specific decision problem is the generational reset around C1000 Gen 2 / C2000 Gen 2 rather than a generic overview of capacity, solar and use cases.

## 2. Value already present — preserve

- Correct identification of C1000 Gen 2 and C2000 Gen 2 as the current core of the French portable range.
- Useful distinction between current Gen 2 and sold-out C1000/F2000 first-generation products.
- C1000 Gen 2 1,024 Wh / 2,000 W / 11.3 kg is a strong, decision-relevant technical anchor.
- C2000 Gen 2 2,048 Wh / 2,400 W, 18.9 kg, expansion to 4 kWh and 800 W alternator charging are highly relevant differentiators.
- UPS transfer and application features are directly relevant to the site positioning.
- Documentary-analysis disclaimer and current internal links can be reused.

Current official evidence checked on 2026-09-09:

- https://www.ankersolix.com/fr/collections/portable-power-stations
- https://www.ankersolix.com/fr/products/c1000-gen2
- https://www.ankersolix.com/fr/c2000-gen2

## 3. Blockers

### A. Structural cloning — HIGH

Despite relatively good facts, the page still follows the same legacy sequence as the other hubs. The structure therefore undersells what is actually distinctive about Anker SOLIX.

### B. Gen 2 transition should be the core story — HIGH

The current page mentions the generational change, but then falls back into generic ecosystem/usages/strengths/limits sections. The reader would benefit more from a direct comparison of what Gen 2 changes in power density, charging, expansion and vehicle integration.

### C. C300 availability should not drive evergreen architecture — MEDIUM

The French collection currently marks C300 as sold out. This is useful as a dated availability note, but should not become a permanent structural pillar. The hub should distinguish current strategic lineup from temporary stock state.

### D. C2000 Gen 2 deserves a separate “vehicle/off-grid architecture” treatment — HIGH

The 800 W alternator charger and expansion battery create a materially different use case from C1000 Gen 2. The current generic ecosystem section does not explain that system-level difference clearly enough.

### E. Alternatives are generic — HIGH

The current alternative blurbs repeat the cluster formula. They should be tied to concrete reasons: need more than 4 kWh expansion, different solar architecture, lower entry price, simpler camping-kit ecosystem, etc.

### F. Data model debt — MEDIUM

The structured ecosystem still contains unrelated legacy keys. It should persist Gen 1 vs Gen 2, weight, power density, solar input, alternator charging, BP2000 Gen 2 compatibility, UPS, app connectivity and availability status.

## 4. Evidence status

- C1000 Gen 2: 1,024 Wh / 2,000 W / 11.3 kg / 600 W solar / 10 ms UPS: `VERIFIED`.
- C2000 Gen 2: 2,048 Wh / 2,400 W / 18.9 kg / 800 W solar / 10 ms transfer / expansion to 4 kWh: `VERIFIED`.
- 800 W alternator charging on C2000 Gen 2: `VERIFIED`.
- C300 sold out on French collection: `VERIFIED` as of 2026-09-09.
- first-generation C1000 and F2000 sold out on French collection: `VERIFIED` as of 2026-09-09.
- “more coherent than before”: `INFERRED`; acceptable only as qualified editorial analysis.

## 5. Original affiliate value to target

The rewrite should help answer:

1. What does Gen 2 materially improve over first-generation C1000/F2000?
2. Is C1000 Gen 2 unusually attractive because of power/weight density for a 1 kWh station?
3. When does C2000 Gen 2 become the more logical choice because of alternator charging and expansion?
4. Is a 4 kWh ceiling sufficient for the user's backup need, or should another ecosystem be considered?
5. Which older SOLIX deals are still worth considering if heavily discounted?

## 6. Bespoke rewrite direction

Likely direction:

- lead with the Gen 2 reset and current French lineup;
- compare C1000 Gen 2 vs C2000 Gen 2 on weight, power, charging and system growth;
- isolate vehicle charging as a specific C2000 Gen 2 advantage;
- treat sold-out Gen 1 models as context, not as equal current choices;
- route users to compact/van/UPS content only where it follows from the chosen model;
- alternatives based on expansion ceiling, solar architecture, price or portability.

## 7. Unknowns before production

- whether C300 returns to French stock or is being phased out;
- exact compatibility of all current SOLIX panels/accessories across C300/C1000 Gen 2/C2000 Gen 2;
- current pricing needed for any value claim;
- whether upcoming SOLIX portable products announced elsewhere should alter the French current-range framing.

## 8. Required actions

1. Rebuild the range around current Gen 2 products.
2. Migrate structured entities.
3. Preserve verified weight/power/charging facts.
4. Remove generic cluster prose.
5. Rewrite around Gen 2 power density and C2000 system architecture.
6. Run post-draft fact-check and `PUBLISH_REVIEW`.
7. Keep `noindex,follow` until human validation and explicit indexation instruction.

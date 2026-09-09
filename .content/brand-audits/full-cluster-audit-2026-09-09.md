# Full brand cluster audit — 2026-09-09

Mode: `CLUSTER_AUDIT`

Scope:

- `/marques/ecoflow/`
- `/marques/jackery/`
- `/marques/aferiy/`
- `/marques/allpowers/`
- `/marques/anker-solix/`
- `/marques/bluetti/`
- `/marques/izywatt/`

Inputs:

- seven individual brand audits;
- current brand source pages in `.content/brand-pages/`;
- structured brand data in `.content/brands/`;
- EcoFlow pilot rewrite and its `PUBLISH_REVIEW`;
- `brand-analysis-workflow` and `brand-content-workflow` adapted for stations-electriques-portables.fr.

## Executive decision

### Cluster status

**The cluster requires structural diversification.**

Current page-level state:

| Brand | Current decision / state | Confidence | Cluster action |
|---|---|---|---|
| EcoFlow | pilot rewritten; `PUBLISH_REVIEW` passed | HIGH | use as proof that a bespoke hub can work, not as a template |
| Jackery | `DEEP_REWRITE` | HIGH | rewrite |
| AFERIY | `DEEP_REWRITE` | HIGH | rewrite + refresh range ledger |
| ALLPOWERS | `DEEP_REWRITE` | HIGH | rewrite + resolve factual/version blockers first |
| Anker SOLIX | `DEEP_REWRITE` | HIGH | rewrite around Gen 2 |
| BLUETTI | `DEEP_REWRITE` | HIGH | rewrite + resolve generation/lifecycle map |
| IZYWATT | `DEEP_REWRITE` | HIGH | rewrite around use-case architecture + high-evidence grid-injection treatment |

There is no recommendation to merge or remove any of the seven brand hubs. Each has a distinct autonomous search intent and enough brand-specific material to justify its own URL.

The main cluster problem is not URL-level cannibalisation between brand names. It is **functional and editorial cannibalisation**: six legacy hubs still answer the same generic power-station questions with nearly the same architecture and prose, instead of concentrating on the decision problem unique to the brand.

---

# 1. Cluster-wide blocker — structural cloning

Before the EcoFlow pilot rewrite, the hubs were built from the same sequence:

`answer box → positionnement → gamme → écosystème → usages → forces → limites → choisir → éviter → alternatives → sources`

Jackery, AFERIY, ALLPOWERS, Anker SOLIX, BLUETTI and IZYWATT still substantially retain this architecture.

This is a `HIGH` blocker under the current workflow because the repeated structure is editorial, not merely visual.

Shared HTML components, tables and visual styles are acceptable. Repeating the same editorial questions in the same order is not, especially when the brands have materially different range logic.

## Repeated prose functions detected across the legacy hubs

The six remaining pages repeatedly contain equivalent or near-identical passages for:

- the generic instruction to compare Wh, continuous W, weight, solar, UPS/EPS and expansion;
- the explanation that a station is not an isolated product and that ecosystem/recharge/accessories matter;
- generic device examples such as phone, router, laptop, fridge, CPAP, microwave and heater;
- the instruction to use the autonomy calculator before choosing capacity;
- the statement that expansion only matters if the user expects to grow the system;
- the justification for not converting limitations into one global score;
- the generic definition of what “éviter” means;
- alternatives described with the same reasons: weight, power, solar or expansion.

These functions are individually valid. The problem is that the same explanatory burden is repeated on every brand hub even when generic guides already exist for W/Wh, capacity, autonomy, UPS/EPS, LiFePO4 and solar.

### Cluster decision

Generic education belongs primarily in shared guides and calculators. A brand hub should only re-explain a generic concept when a brand-specific implementation changes the decision.

Examples:

- EcoFlow: expansion compatibility is worth explaining because the ecosystem is central and non-universal.
- Jackery: SolarSaga is worth explaining as part of system simplicity and kit logic.
- Anker SOLIX: alternator charging is worth explaining because it materially separates C2000 Gen 2 from C1000 Gen 2.
- IZYWATT: grid injection is worth explaining because Eco is no longer just a conventional portable station.

---

# 2. Functional cannibalisation with generic site content

The legacy brand pages repeatedly cover subjects that already have dedicated destinations:

- `/guides/watt-ou-watt-heure/`;
- capacity/autonomy guides;
- `/calculateur-autonomie/`;
- UPS/EPS guides;
- LiFePO4/cycle guides;
- solar charging content;
- generic usage pages for camping, van, campervan, house, backup and chantier;
- cross-brand comparisons.

This creates a cluster-level role problem: the hubs spend too much space teaching “how to choose a power station” and too little explaining “how to understand this brand”.

## Recommended role boundary

### Brand hubs own

- current family/generation map;
- exact brand-specific product architecture;
- brand-specific compatibility and expansion logic;
- brand-specific charging/ecosystem decisions;
- lifecycle/version confusion;
- portability consequences within that brand;
- reasons to choose another brand for a specific limitation.

### Generic guides/comparisons own

- what Wh means;
- how to calculate runtime;
- what LiFePO4 means generally;
- what UPS/EPS means generally;
- generic solar sizing;
- generic camping/van/home load requirements;
- ranking brands/models against each other.

Brand hubs should route to those pages instead of duplicating them.

---

# 3. Distinct editorial territory required for each brand

The cluster can become strongly differentiated because the seven brands do not present the same decision problem.

## EcoFlow — family + system architecture

Core territory:

- `RIVER vs DELTA` first;
- expansion and compatibility;
- multi-source charging;
- transition from genuinely portable to transportable/home-backup;
- ecosystem value vs ecosystem complexity.

EcoFlow has already been rewritten around this logic and passed `PUBLISH_REVIEW`.

**Do not use EcoFlow's new section sequence as a cluster template.** Its value is the methodology, not the outline.

## Jackery — generation simplicity vs expandability

Core territory:

- current `v2` spine;
- `Plus` when expansion changes the decision;
- SolarSaga / solar-generator kit logic;
- capacity versus practical portability;
- when an older Plus/Pro offer can still be rational.

Jackery should feel simpler and more linear than EcoFlow/BLUETTI, provided this interpretation remains evidence-qualified.

## AFERIY — naming transition + capacity/power + weight

Core territory:

- Nano / Nomad / Haven map versus Pxxx references;
- current-range completeness;
- fixed versus expandable products;
- high Wh/W proposition only when factually or commercially benchmarked;
- point at which large Haven units become semi-fixed rather than practically portable.

The naming problem should be solved for the reader, not merely mentioned.

## ALLPOWERS — version decoding and buyer safety

Core territory:

- decode R / VOLIX / S families;
- split similarly named variants such as R2500 vs R2500 v2;
- resolve R4000 vs R4000 Lite;
- distinguish technical relevance, generation status and actual France/EU availability;
- avoid categorical lifecycle labels without regional evidence.

This hub should be the most “catalogue decoder” of the cluster.

## Anker SOLIX — Gen 2 reset + power density + vehicle architecture

Core territory:

- current C1000 Gen 2 / C2000 Gen 2 spine;
- what Gen 2 materially changes from the first generation;
- power/weight density;
- C2000 Gen 2 expansion and 800 W alternator charging;
- 4 kWh expansion ceiling as a decision threshold.

Sold-out products should provide context, not dominate evergreen structure.

## BLUETTI — generation map + portable vs expandable system

Core territory:

- `Elite vs Apex vs legacy AC/EB`;
- what is genuinely current versus merely still visible in search/retail;
- portability and growth as the main fork;
- Apex as a system architecture, not simply “the biggest BLUETTI”;
- exact battery/vehicle-charger compatibility.

This hub must solve the generation map more explicitly than the current table does.

## IZYWATT — use-case architecture + transition to home energy

Core territory:

- `800 → Moov → Home → Eco` by use case;
- compact/mobile versus backup versus home-energy system;
- `Home vs Eco` as the central high-capacity decision;
- grid injection as a high-evidence technical feature;
- Eco + Extra expansion only after direct product/manual verification;
- limited independent evidence acknowledged honestly.

IZYWATT should probably become the least catalogue-like hub in the cluster.

---

# 4. Cross-brand overlap matrix

The same technical dimension can appear on several pages, but each page must use it for a different decision.

| Dimension | EcoFlow | Jackery | AFERIY | ALLPOWERS | Anker SOLIX | BLUETTI | IZYWATT |
|---|---|---|---|---|---|---|---|
| Family/generation map | RIVER/DELTA | v2/Plus/Pro | Nano/Nomad/Haven + Pxxx | VOLIX/R/S + variants | Gen 2 vs Gen 1 | Elite/Apex/AC/EB | 800/Moov/Home/Eco |
| Expansion | ecosystem compatibility | Plus-specific need | fixed vs expandable | variant-specific | C2000 Gen 2 to 4 kWh | Apex/system growth | Eco + Extra |
| Portability | 3.55 → 51.5 kg continuum | capacity/weight ladder | large Haven penalty | secondary to version clarity | power density | Elite vs Apex fork | 800/Moov vs Home/Eco |
| Vehicle charging | ecosystem/multi-source | secondary | model-specific | model-specific | core C2000 Gen 2 feature | Charger 2/system feature | secondary |
| Solar | multi-source system value | SolarSaga kit logic | model/price dependent | variant-specific | architecture criterion | family/accessory compatibility | model-specific limits |
| Backup/home | DELTA/Pro architecture | larger v2/Pro context | Haven high-capacity | R3500/R4000 context | C2000 Gen 2 | Apex | Home/Eco central |
| Main editorial risk | ecosystem complexity | genericising simplicity | unsupported value claim | version confusion | underusing Gen 2 story | generation confusion | unsafe/overbroad injection claims |

This matrix should guide production, but it is not a template. If evidence changes, page structure should change with it.

---

# 5. Alternatives and internal linking — cluster correction

The current legacy pages repeatedly link EcoFlow, BLUETTI, Jackery, Anker SOLIX, AFERIY or ALLPOWERS with almost identical wording.

This creates weak circular linking rather than decision support.

## New cluster rule

An alternative brand should only be linked when the current page has first established a concrete reason to leave the target brand.

Examples:

- leave EcoFlow because the expansion ecosystem is unnecessary → compare a simpler fixed-capacity option;
- leave Jackery because deep expansion matters → compare a brand with stronger system growth;
- leave AFERIY because weight/service/ecosystem depth matters more than capacity → compare accordingly;
- leave ALLPOWERS because version ambiguity or regional availability is unacceptable → compare a clearer catalogue;
- leave Anker SOLIX because >4 kWh expansion is needed → compare a deeper backup ecosystem;
- leave BLUETTI because nomenclature/system complexity is excessive → compare a simpler range;
- leave IZYWATT because broader independent coverage or >3 kW portable output is required → compare an international alternative.

No alternative section is mandatory. Contextual links can appear inside the decision section that creates the need for the alternative.

---

# 6. Structured entity model — cluster migration

The six unreworked data files still use inherited ecosystem keys from another product universe, notably `stylus`, `notes`, `pdf` and `ocr`.

EcoFlow has already been migrated during the pilot.

The remaining six should move to brand-specific station relations, using only relevant fields such as:

- product/family;
- current/legacy/unknown lifecycle;
- capacity Wh;
- continuous output W;
- battery chemistry;
- weight;
- solar input / MPPT;
- UPS/EPS;
- expansion battery compatibility;
- vehicle/alternator charging;
- app/firmware;
- accessories;
- limitations;
- use-case fit;
- evidence status;
- availability region/date when material.

Do not require every brand to populate every field.

---

# 7. Evidence asymmetry across the cluster

The cluster should not pretend all brands have the same evidence depth.

## Stronger current official product evidence

- EcoFlow;
- Jackery;
- Anker SOLIX;
- BLUETTI.

These still need careful generation and compatibility checks, but the current official ecosystems are relatively well documented.

## Higher evidence/reconciliation burden

### AFERIY

- current range changed enough that the existing page is incomplete;
- value/price positioning requires dated benchmarking;
- ecosystem maturity should remain qualified unless independently evidenced.

### ALLPOWERS

- regional catalogue and variant naming need reconciliation;
- lifecycle labels are currently unsafe in at least one case;
- R4000 / R4000 Lite and R2500 variants require product-level evidence.

### IZYWATT

- grid injection is a higher-sensitivity technical feature;
- expansion claims require direct product/manual verification;
- independent experiential evidence is thinner.

The absence of equal evidence depth is not a reason to drop these URLs. It is a reason to calibrate the confidence and claims differently.

---

# 8. Cluster-level cannibalisation assessment

## Brand-to-brand cannibalisation

**LOW.**

The seven pages target different branded queries. No pair currently justifies `MERGE` based on intent.

## Functional duplication inside the cluster

**HIGH.**

The repeated generic buyer education and section architecture make the pages interchangeable in function.

## Cannibalisation with guides/comparisons

**MEDIUM/HIGH.**

Generic W/Wh, capacity, device-load, UPS/EPS, solar and use-case education is overrepresented in brand pages. Those topics should be summarized only when needed and routed to the dedicated generic pages.

## Cannibalisation with model pages

**MEDIUM.**

Brand hubs should not become complete spec catalogs. Use model anchors to explain the family/generation logic, then route model-level detail to `/modeles/`.

---

# 9. Recommended rewrite priority

Priority is based on factual risk first, then structural opportunity.

## Priority 1 — ALLPOWERS

Why first:

- current lifecycle contradiction around S700;
- unresolved R4000/R4000 Lite relationship;
- multiple similarly named current variants;
- global versus France/EU catalogue differences.

This is the highest factual buyer-safety risk in the six legacy pages.

## Priority 2 — AFERIY

Why:

- current range is incomplete;
- naming transition remains unresolved;
- value/price and ecosystem maturity claims require stronger evidence;
- strong opportunity to differentiate by fixed/expandable and portability thresholds.

## Priority 3 — IZYWATT

Why:

- very strong unique editorial role;
- Eco grid injection needs high-evidence treatment;
- Home vs Eco can produce a genuinely distinctive hub;
- direct evidence should be strengthened before wording grows.

## Priority 4 — BLUETTI

Why:

- generation map is central but currently unresolved;
- AC70/older AC/EB lifecycle needs individual verification;
- Apex deserves system-level treatment.

## Priority 5 — Anker SOLIX

Why:

- facts are relatively strong already;
- structure is the main weakness;
- clear Gen 2 architecture makes production comparatively straightforward.

## Priority 6 — Jackery

Why:

- current v2 evidence is relatively coherent;
- main work is editorial separation of v2/Plus/Pro and SolarSaga logic;
- lower factual urgency than ALLPOWERS/AFERIY/BLUETTI/IZYWATT.

This priority order is operational, not a judgment of commercial importance.

---

# 10. Rewrite acceptance criteria at cluster level

After the six rewrites, a new `CLUSTER_AUDIT` should only pass when all of the following are true:

1. no two brand pages rely on the same section-role sequence as their main architecture;
2. generic W/Wh/autonomy/UPS/solar explanations are not repeated verbatim across hubs;
3. each page can be summarised by a different decision problem in one sentence;
4. alternative links are triggered by explicit brand-specific limitations;
5. entity data no longer carries unrelated inherited schema keys;
6. product lifecycle/generation labels are evidence-backed or explicitly marked uncertain;
7. detailed model specs are not duplicated unnecessarily from `/modeles/`;
8. generic dimensioning remains primarily in guides/calculator/comparisons;
9. no page simulates hands-on experience;
10. every page remains useful without affiliate links;
11. each finished page passes its own `PUBLISH_REVIEW`;
12. `noindex,follow` remains until explicit human validation and indexation instruction.

---

# 11. Cluster conclusion

The seven URLs are justified and should remain separate.

The current weakness is not the subject selection but the original production system: mandatory headings, quotas and repeated prose caused six of the hubs to converge toward an interchangeable affiliate-page skeleton.

The EcoFlow pilot demonstrates the desired correction: keep the shared visual language and technical rigor while letting the brand's actual product architecture determine the content architecture.

The remaining production sequence should therefore be:

1. ALLPOWERS rewrite + `PUBLISH_REVIEW`;
2. AFERIY rewrite + `PUBLISH_REVIEW`;
3. IZYWATT rewrite + `PUBLISH_REVIEW`;
4. BLUETTI rewrite + `PUBLISH_REVIEW`;
5. Anker SOLIX rewrite + `PUBLISH_REVIEW`;
6. Jackery rewrite + `PUBLISH_REVIEW`;
7. final seven-page `CLUSTER_AUDIT`;
8. human validation;
9. indexation only on explicit instruction.

Until step 8, keep the cluster `noindex,follow`.

# EcoFlow — PUBLISH_REVIEW — 2026-09-09

Target: `/marques/ecoflow/`

Workflow: `.agents/skills/brand-analysis-workflow/SKILL.md`

## Machine validation

GitHub Actions run `Generate brand content` #16 completed successfully after the EcoFlow source/data rewrite.

Validated by CI:

- global shell generation;
- researched guides/comparisons restoration;
- seven brand hubs generation;
- repo-specific hard brand invariants;
- generation idempotence;
- `noindex,follow` preservation;
- guides/comparisons unchanged;
- whitespace check.

## Substantive gates

### Intent

PASS.

The page now answers the EcoFlow-specific choice problem in a direct sequence: RIVER vs DELTA → technical range anchors → recharge ecosystem → battery compatibility → portability → use-case sizing → situations where EcoFlow is less rational.

### Original affiliate value

PASS.

The page remains useful without affiliate CTAs because it explains:

- how to choose the family before the model;
- why continuous W and Wh should not be confused with peak/X-Boost;
- when expansion is valuable;
- why the battery compatibility matrix matters;
- how weight changes the meaning of “portable” across the range;
- why the calculator should be used for real autonomy rather than invented runtime promises.

### Evidence / factuality

PASS with normal freshness risk.

Key capacity, continuous power, weight, solar input, battery chemistry and expansion claims are traceable to EcoFlow France sources verified on 2026-09-09. Unknowns are left unknown rather than completed from model memory. Volatile promotional prices are excluded from durable copy.

### Review / hands-on honesty

PASS.

The page explicitly states that it is documentary analysis and does not claim physical testing. No first-person test language or simulated measured result is used.

### Merchant rewrite risk

PASS.

The page does not follow the manufacturer’s sales sequence. Specs are interpreted through decision consequences: sizing, portability, charging architecture and compatibility.

### Internal linking

PASS.

Links are contextual and route to model pages, W/Wh guidance, solar guidance, use cases, autonomy calculator and the cross-brand comparison only when they answer the next question.

### SEO / technical

PASS at draft level.

The generator consumes the new title/description and CI confirms the brand generation pipeline remains valid. `noindex,follow` is preserved pending human validation.

### AI-slop / generic prose

PASS.

The main repeated generic paragraphs from the previous EcoFlow/Jackery/AFERIY skeleton were removed. The copy is built around EcoFlow-specific facts such as RIVER vs DELTA, EB300/EB600, DELTA battery cross-compatibility, MPPT scaling and the 3.55 kg → 12.5 kg → 22.1 kg → 51.5 kg portability gradient.

### Cluster structural cloning

PASS for the EcoFlow pilot.

The new EcoFlow outline is materially different from the current Jackery and AFERIY sibling pages. Shared visual components remain acceptable, but the editorial question order is no longer the old common skeleton.

## Remaining minor risks

- EcoFlow’s catalog changes quickly and currently mixes new, older-still-sold and adjacent residential lines; range status should be refreshed before eventual indexation if publication is delayed.
- Battery compatibility is complex enough that future changes to adapters or extra batteries should trigger a targeted fact-check.
- No claim is made about long-term reliability or comparative app quality because the current evidence brief does not support those conclusions.

## Result

**PASS — READY_FOR_HUMAN_VALIDATION**

The page must remain `noindex,follow` until explicit human validation and an explicit instruction to make it indexable.

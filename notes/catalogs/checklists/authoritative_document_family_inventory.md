# Authoritative Document Family Inventory

## Purpose

Identify which document families are treated as authoritative implementation assets.

## Starter Families

| Family | Why it matters | Expected test coverage |
| --- | --- | --- |
| lifecycle notes | govern stage-specific behavior | document-structure checks |
| task plans | govern meaningful work | plan-schema checks |
| development logs | reconstruct work and proof | log-schema checks |
| operational-state checklist | records maturity truthfully | checklist-structure checks |
| rigid feature definitions | define which governed files, proof assets, and snapshot baselines belong to a real feature | schema, mapping, and snapshot-consistency checks |
| feature snapshot baselines | record the approved content-hash baseline for governed files | snapshot-integrity and change-detection checks |
| feature checklists | track implementation and proof status | checklist-schema checks and milestone-gate consistency checks |
| verification command catalog | defines canonical proving commands | doc-consistency checks |
| flow inventory | tracks relevant flows and E2E mapping | mapping, status-consistency, and milestone-gate checks |
| product-definition specs | define feature contracts, domain terms, processing contracts, and operator surfaces before setup | lifecycle, note-family, and documentation-claim-boundary checks |
| user documentation docs | define user-facing guidance, operator guidance, references, and runbooks that must track real behavior | doc-structure, alignment, and warning-oriented readiness checks |

## Rule

If a new document family becomes authoritative, add it here and add or update the relevant consistency tests in the same change.

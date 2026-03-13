# Feature Delivery Map

## Purpose

Map the starter features into an intended delivery order so implementation work can start from deliberate slices instead of rediscovering dependencies feature by feature.

## Product Feature Delivery Rule

Once product features have been identified, this map must include their delivery order explicitly.

Do not keep this file limited to governance-stage starter features after real product features are known.

Each product feature should appear here with:

- the first delivery slice
- why that slice proves meaningful user value
- which requested capability it serves
- which flows and proofs it depends on

## Starter Table

| Feature ID | First slice | Depends on | Delivery notes | Documentation surfaces | Bounded proof | Real E2E target |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | bootstrap governance starter | none | Establish the governing surfaces and bounded checks first. | `docs/README.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` | planned |
| F02 | architecture boundary notes | F01 | Define system ownership and stack direction before product-level slicing. | not_applicable | bounded document review | not_applicable |
| F03 | product-definition contract package | F02 | Deliver flow inventory, contract notes, domain model, operator surfaces, user-documentation contract, and implementation slicing before setup. | `docs/README.md`, `docs/user/README.md`, `docs/operator/README.md`, `docs/reference/README.md`, `docs/runbooks/README.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` | planned |
| F04 | first real runtime narrative | F03 | Select one live user or operator narrative from the defined flow inventory and drive it to real E2E. | flow-specific user, operator, reference, and runbook docs selected from the contract | bounded narrative readiness review | `tests/e2e/test_e2e_first_flow.py` |

## Rule

If delivery order changes materially, update this note, the feature inventory, and the governing task plans together.

Feature delivery should also keep the maintenance loop explicit during implementation:

- update notes when implementation reveals new constraints or invariants
- update docs when supported behavior, commands, setup steps, or operator expectations change
- update checklists when status or proof posture changes
- update bounded-test and E2E expectations when proving changes

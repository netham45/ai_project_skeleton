# Feature Delivery Map

## Purpose

Map the starter features into an intended delivery order so implementation work can start from deliberate slices instead of rediscovering dependencies feature by feature.

## Starter Table

| Feature ID | First slice | Depends on | Delivery notes | Bounded proof | Real E2E target |
| --- | --- | --- | --- | --- | --- |
| F01 | bootstrap governance starter | none | Establish the governing surfaces and bounded checks first. | `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q` | planned |
| F02 | architecture boundary notes | F01 | Define system ownership and stack direction before product-level slicing. | bounded document review | not_applicable |
| F03 | product-definition contract package | F02 | Deliver flow inventory, contract notes, domain model, operator surfaces, and implementation slicing before setup. | `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q` | planned |
| F04 | first real runtime narrative | F03 | Select one live user or operator narrative from the defined flow inventory and drive it to real E2E. | bounded narrative readiness review | `tests/e2e/test_e2e_first_flow.py` |

## Rule

If delivery order changes materially, update this note, the feature inventory, and the governing task plans together.

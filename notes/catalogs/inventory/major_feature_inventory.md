# Major Feature Inventory

## Purpose

Track both:

- skeleton-governance features used to stand up the repository discipline
- real product features derived from the user's original vision

Once a concrete project vision exists, user-requested product features must not be omitted from this inventory.

## Required Rules

When the repository is still a pure starter template, governance-only starter rows are acceptable.

Once a concrete project vision exists, add one row per meaningful user-requested product feature.

Do not collapse multiple independently valuable user-visible capabilities into one generic feature row such as "core workflow" or "main app behavior".

Every product-feature row must include:

- a stable feature ID
- the source vision reference
- governing flow IDs
- a rigid feature definition file once the feature is real
- affected systems
- documentation surfaces
- bounded proof target
- real E2E target or explicit not-applicable reason
- checklist file reference once feature checklists exist

## Starter Rows

| Feature ID | Feature kind | Name | Source vision reference | Status | Governing flows | Feature definition | Systems | Dependencies | Initial slice | Documentation surfaces | Checklist | Bounded proof | Real E2E target | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | governance | Bootstrap governance | not_applicable | planned | FLOW01 | not_applicable | notes, plans, checklists, tests, user_docs | none | lifecycle, checklist, and bounded-test starter surfaces | `docs/README.md` | not_applicable | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` | planned | Establish the repository's first governed scaffold and bounded verification surface. |
| F02 | governance | Primary architecture boundaries | not_applicable | planned | FLOW00 | not_applicable | database, cli, daemon, config, prompts, website_ui, notes | F01 | authority, durability, and stack boundary notes | not_applicable | not_applicable | bounded document review | not_applicable | Define durable-state, authority, code-vs-config, and stack boundaries explicitly. |
| F03 | governance | Product definition contracts | not_applicable | planned | FLOW03, FLOW04 | not_applicable | database, cli, daemon, config, prompts, website_ui, user_docs, notes | F02 | flow inventory, contract notes, domain model, operator surface map, user-documentation contract, and implementation slicing guide | `docs/README.md`, `docs/user/README.md`, `docs/operator/README.md`, `docs/reference/README.md`, `docs/runbooks/README.md` | not_applicable | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` | planned | Define major flows, feature contracts, operator surfaces, domain model, user-documentation expectations, implementation slices, and proof targets before setup. |
| F04 | governance | First real runtime flow | not_applicable | planned | FLOW02 | not_applicable | all applicable systems, including user_docs when the flow is documented for real operators or users | F03 | first live narrative selected from the product-definition flow inventory | flow-specific docs chosen from the user-documentation contract | not_applicable | bounded narrative readiness review | `tests/e2e/test_e2e_first_flow.py` | Define and prove the first real end-to-end narrative. |
| PF01 | product_example | Example user-requested capability | `notes/explorations/original_concept.md#capability-1` | planned | FLOW10 | `plan/features/PF01_example_capability.yaml` | cli, daemon, website_ui, user_docs, notes | none | minimal end-to-end usable slice | `docs/user/example.md`, `docs/operator/example.md` | `plan/checklists/PF01_example_capability.md` | `python3 -m pytest tests/unit/test_product_feature_traceability_docs.py -q` | `python3 -m pytest tests/e2e/test_e2e_example_capability.py -q` | Replace this row with a real user-requested feature before setup hardens implementation. |

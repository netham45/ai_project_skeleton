# Major Feature Inventory

## Purpose

Track the repository's meaningful feature families at a level above individual task plans.

## Starter Rows

| Feature ID | Name | Status | Governing flows | Systems | Dependencies | Initial slice | Proof target | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | Bootstrap governance | planned | FLOW01 | notes, plans, checklists, tests | none | lifecycle, checklist, and bounded-test starter surfaces | `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q` | Establish the repository's first governed scaffold and bounded verification surface. |
| F02 | Primary architecture boundaries | planned | FLOW00 | database, cli, daemon, config, prompts, website_ui, notes | F01 | authority, durability, and stack boundary notes | bounded document review | Define durable-state, authority, code-vs-config, and stack boundaries explicitly. |
| F03 | Product definition contracts | planned | FLOW03, FLOW04 | database, cli, daemon, config, prompts, website_ui, notes | F02 | flow inventory, contract notes, domain model, operator surface map, and implementation slicing guide | `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q` | Define major flows, feature contracts, operator surfaces, domain model, implementation slices, and proof targets before setup. |
| F04 | First real runtime flow | planned | FLOW02 | all applicable systems | F03 | first live narrative selected from the product-definition flow inventory | `tests/e2e/test_e2e_first_flow.py` | Define and prove the first real end-to-end narrative. |

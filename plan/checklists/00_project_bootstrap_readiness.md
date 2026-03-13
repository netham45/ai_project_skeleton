# Project Bootstrap Readiness

## Goal

Track the minimum artifacts needed before the repository can honestly move from genesis through architecture and product definition into setup work.

## Status Table

| Area | Status | Notes |
| --- | --- | --- |
| Mission note | planned | Create `notes/explorations/original_concept.md`. |
| System inventory | planned | Create `notes/catalogs/inventory/system_inventory.md`. |
| Stack decision record | planned | Create `notes/specs/architecture/stack_decision_record.md` and either mark the stack undecided or record the first proposals. |
| First architecture boundary note | planned | Start `notes/specs/architecture/code_vs_config_delineation.md`. |
| Original vision decomposition | planned | Convert the original concept into explicit product-feature rows before setup begins. |
| Major user flow inventory | planned | Define the starter operator and user flows in `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`. |
| Major feature inventory | planned | Expand `notes/catalogs/inventory/major_feature_inventory.md` with stable starter features and proof targets. |
| Feature-to-flow mapping | planned | Ensure each product feature is covered by one or more relevant flows. |
| Feature checklist surface | planned | Add per-feature checklist files once product features are identified. |
| Feature-to-proof mapping | planned | Ensure each product feature names bounded proof and real E2E targets or an explicit not-applicable reason. |
| Product contract notes | planned | Add starter product-definition notes under `notes/specs/product/`. |
| Domain model and vocabulary | planned | Define starter entities, state language, and durable-record terms before setup begins. |
| User documentation contract | planned | Add `notes/specs/product/user_documentation_contract.md` and define required `docs/` families before setup begins. |
| Implementation slicing guide | planned | Define the first delivery slices and dependency order for starter features under `notes/specs/product/`. |
| Traceability matrix | planned | Map mission, flows, features, and proof targets in `notes/catalogs/traceability/spec_traceability_matrix.md`. |
| Verification command catalog | planned | Seed at least one bounded proof command and one doc-consistency command. |
| Starter user-docs tree | planned | Add `docs/README.md` plus starter `user/`, `operator/`, `reference/`, and `runbooks/` subtrees. |
| Documentation consistency command | planned | Add and run `python3 -m pytest tests/unit/test_user_documentation_docs.py -q`. |
| Bootstrap task plan | implemented | Starter governing task plan exists. |
| Bootstrap development log | implemented | Starter setup log exists. |
| Lifecycle note set | implemented | Starter lifecycle note family exists. |
| Operational-state checklist | implemented | Current stage rollup surface exists. |
| First real E2E target named | planned | Add explicit runtime-flow target before stronger claims. |

## Exit Condition

This checklist can move to `verified` for bootstrap readiness only when the planned artifact surfaces above exist, the original vision has been decomposed into explicit product features, those features are mapped to flows and proof targets, product definition is no longer implicit, the starter documentation surface exists, and the starter bounded commands actually pass.

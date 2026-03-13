# Spec Traceability Matrix

## Purpose

Track which major repository goals map to which notes, plans, tests, and E2E targets.

## Starter Matrix

| Goal ID | Goal | Governing notes | Governing plans | Documentation surfaces | Proof surface |
| --- | --- | --- | --- | --- |
| G01 | Repository purpose is explicit | `notes/explorations/original_concept.md` | bootstrap task plan | `docs/README.md` | artifact review |
| G02 | System boundaries are explicit | architecture notes | architecture or bootstrap plan | not_applicable | bounded document checks |
| G03 | Product definition is explicit before setup | `notes/lifecycle/03_stage_02_product_definition.md`, `notes/specs/product/domain_model_outline.md`, `notes/specs/product/processing_system_contracts.md`, `notes/specs/product/user_documentation_contract.md` | `plan/tasks/2026-03-12_product_definition_stage.md` | `docs/README.md`, `docs/user/README.md`, `docs/operator/README.md`, `docs/reference/README.md`, `docs/runbooks/README.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G04 | Major flows and feature contracts are traceable | `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`, `notes/catalogs/inventory/major_feature_inventory.md`, `notes/catalogs/traceability/spec_traceability_matrix.md` | `plan/tasks/2026-03-12_product_definition_stage.md` | `docs/README.md` plus flow-specific docs selected from the documentation contract | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G05 | Product definition is implementation-ready | `notes/specs/product/implementation_slicing_guide.md`, `notes/specs/product/feature_delivery_map.md`, `notes/catalogs/inventory/major_feature_inventory.md` | `plan/tasks/2026-03-12_product_definition_implementation_guides.md` | documentation surfaces are named for each starter feature slice | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G06 | User documentation is first-class and explicitly linked to work | `notes/specs/product/user_documentation_contract.md`, `notes/catalogs/checklists/feature_checklist_standard.md`, `notes/catalogs/checklists/verification_command_catalog.md` | `plan/tasks/2026-03-13_user_documentation_system.md` | `docs/README.md`, `docs/user/README.md`, `docs/operator/README.md`, `docs/reference/README.md`, `docs/runbooks/README.md` | `python3 -m pytest tests/unit/test_user_documentation_docs.py -q` |
| G07 | First runtime narrative is named and mapped | flow inventory, E2E policy | feature or E2E plan | flow-specific docs selected from the documentation contract | real E2E command |
| G08 | User-requested product features are explicitly decomposed and traceable | `notes/explorations/original_concept.md`, `notes/catalogs/inventory/major_feature_inventory.md`, `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`, `notes/catalogs/checklists/feature_checklist_standard.md` | product-definition task plan and future feature plans | feature-specific docs chosen from the documentation contract | document-consistency tests that enforce feature-to-flow-to-proof linkage |

# Spec Traceability Matrix

## Purpose

Track which major repository goals map to which notes, plans, tests, and E2E targets.

## Starter Matrix

| Goal ID | Goal | Governing notes | Governing plans | Proof surface |
| --- | --- | --- | --- | --- |
| G01 | Repository purpose is explicit | `notes/explorations/original_concept.md` | bootstrap task plan | artifact review |
| G02 | System boundaries are explicit | architecture notes | architecture or bootstrap plan | bounded document checks |
| G03 | Product definition is explicit before setup | `notes/lifecycle/03_stage_02_product_definition.md`, `notes/specs/product/domain_model_outline.md`, `notes/specs/product/processing_system_contracts.md` | `plan/tasks/2026-03-12_product_definition_stage.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G04 | Major flows and feature contracts are traceable | `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`, `notes/catalogs/inventory/major_feature_inventory.md`, `notes/catalogs/traceability/spec_traceability_matrix.md` | `plan/tasks/2026-03-12_product_definition_stage.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G05 | Product definition is implementation-ready | `notes/specs/product/implementation_slicing_guide.md`, `notes/specs/product/feature_delivery_map.md`, `notes/catalogs/inventory/major_feature_inventory.md` | `plan/tasks/2026-03-12_product_definition_implementation_guides.md` | `python3 -m pytest tests/unit/test_lifecycle_docs.py -q` |
| G06 | First runtime narrative is named and mapped | flow inventory, E2E policy | feature or E2E plan | real E2E command |

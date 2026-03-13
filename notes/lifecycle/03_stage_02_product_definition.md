# Stage 02: Product Definition

## Purpose

Product definition turns architecture boundaries into concrete product contracts before scaffolding and implementation begin.

## Required Outcomes

- major user and operator flows are defined
- the original vision is decomposed into explicit product features before setup begins
- major features have stable IDs, scope, and dependencies
- feature contracts exist for the first meaningful capability slices
- processing-system contracts are written for background or runtime coordination paths
- domain model and durable-state outline are explicit
- operator surfaces are mapped for CLI and website UI scope where applicable
- user-documentation contracts and ownership boundaries are explicit
- implementation slices are defined for the starter features
- per-feature delivery guidance exists so setup and feature work can proceed in a deliberate order
- canonical vocabulary and traceability exist across goals, flows, features, and proof targets
- bounded-proof and real-E2E targets are named for the intended starter scope

## Required Artifacts

- `notes/catalogs/inventory/major_feature_inventory.md`
- `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`
- `notes/catalogs/traceability/spec_traceability_matrix.md`
- `notes/specs/product/canonical_vocabulary.md`
- `notes/specs/product/domain_model_outline.md`
- `notes/specs/product/feature_contract_template.md`
- `notes/specs/product/feature_delivery_map.md`
- `notes/specs/product/implementation_slicing_guide.md`
- `notes/specs/product/operator_surface_map.md`
- `notes/specs/product/processing_system_contracts.md`
- `notes/specs/product/user_documentation_contract.md`

## Original Vision Decomposition Rule

Product definition is not complete until the repository's original user vision has been decomposed into explicit product features.

The original vision may begin as freeform notes, but before setup begins it must be transformed into a durable feature inventory that:

- assigns stable feature IDs
- preserves the user-visible intent of each requested capability
- records affected systems explicitly
- maps each feature to one or more relevant user or operator flows
- names bounded proof targets
- names a real E2E target or an explicit not-applicable reason
- records required documentation surfaces or an explicit no-change rationale

Do not treat a broad product paragraph as sufficient decomposition once implementation planning begins.

If the original vision contains multiple distinct capabilities, those capabilities must not remain bundled into one vague feature row.

## Common Failure Modes

- jumping from boundary notes to repo scaffolding without defining what the product actually does
- treating feature names as enough without actor, trigger, input, output, failure, and proof contracts
- leaving flow definitions implicit in chat or task plans
- defining UI or CLI surfaces without stating their daemon, persistence, or prompt contract dependencies
- treating user or operator documentation as cleanup work instead of part of the product contract
- stopping at feature names and contracts without deciding the first implementation slices or delivery order
- naming E2E targets before the flows and invariants they are supposed to prove are written down

## Exit Condition

This stage is complete enough to exit when setup and early feature work can proceed without contributors having to guess the original requested capabilities, major flows, feature boundaries, implementation slice order, processing contracts, documentation surfaces, or proof targets.

Before exit:

- the original vision has been decomposed into explicit product features
- every product feature is mapped to flows, documentation surfaces, and proof targets
- no user-provided feature remains implicit in prose-only form

# Project Operational State

## Goal

Track the repository's current operational maturity honestly.

Use this checklist to:

- record the current lifecycle stage
- record which sub-steps are complete
- record what stronger claims are blocked
- record what must pass before the repository advances

## Current State

- Active stage: `genesis`
- Current maturity status: `genesis_in_progress`
- Next target stage: `architecture_defined`
- Stronger claims currently blocked: `verified`, `flow_complete`, `release_ready`
- Governing references:
  - `notes/lifecycle/00_project_lifecycle_overview.md`
  - `notes/lifecycle/01_stage_00_genesis.md`
  - `notes/catalogs/checklists/verification_command_catalog.md`

## State Table

| State | Status | Current stage? | Acceptance summary | Proof summary | Blocked stronger claims | Advance when |
| --- | --- | --- | --- | --- | --- | --- |
| `genesis` | in_progress | yes | Mission, systems, initial invariants, and bootstrap governance are being established. | Artifact creation and early document checks are expected first. | `verified`, `flow_complete`, `release_ready` | Architecture inputs are explicit and governed. |
| `architecture_defined` | planned | no | Boundaries, durable state, code-vs-config lines, and command surfaces are documented. | Architecture notes and command catalog exist. | `flow_complete`, `release_ready` | Product-definition work can begin without guessing system boundaries. |
| `product_defined` | planned | no | Major flows, feature outlines, system contracts, and proof targets are documented. | Product-definition notes, inventories, and traceability surfaces exist. | `flow_complete`, `release_ready` | Setup can begin without inventing the product shape ad hoc. |
| `setup_bootstrapped` | planned | no | Scaffold, starter tests, governing artifacts, and bounded proof exist. | Bounded commands pass from a clean shell. | `flow_complete`, `release_ready` | Feature work can proceed without ad hoc process invention. |
| `feature_delivery_ready` | planned | no | Task plans, logs, checklists, and note maintenance operate reliably for feature work. | A real feature slice is governed and bounded-tested. | `flow_complete`, `release_ready` | Features can ship under consistent doctrine. |
| `bounded_verified` | blocked | no | Bounded proof discipline exists across the active scope. | Current bounded commands and doc checks pass. | `flow_complete`, `release_ready` | Active features are honestly proven at the bounded layer. |
| `e2e_ready` | blocked | no | Real E2E targets and mapping exist for intended runtime behavior. | E2E execution policy and traceability docs agree. | `release_ready` | The next runtime narrative is concrete enough to test. |
| `flow_complete` | blocked | no | A declared runtime narrative passes end to end for the stated scope. | The real E2E command has passed. | N/A | A named real flow is proven and documented. |
| `release_ready` | blocked | no | Release-scope proof, readiness docs, and risk treatment are complete. | Required bounded, E2E, resilience, and audit surfaces pass. | N/A | The declared release scope is honestly proven. |

## Active Stage Sub-Steps

### `genesis.capture_mission`

- Status: `planned`
- Required artifacts:
  - `notes/explorations/original_concept.md`
- Advance when:
  - the repo mission is durable and specific

### `genesis.define_system_inventory`

- Status: `planned`
- Required artifacts:
  - `notes/catalogs/inventory/system_inventory.md`
- Advance when:
  - the primary systems are explicit

### `genesis.record_invariants_and_unknowns`

- Status: `planned`
- Required artifacts:
  - `notes/explorations/initial_risks_and_unknowns.md`
  - `notes/specs/architecture/authority_and_api_model.md`
- Advance when:
  - first invariants and unknowns are written down

### `genesis.record_stack_direction`

- Status: `planned`
- Required artifacts:
  - `notes/specs/architecture/stack_decision_record.md`
- Advance when:
  - stack choices are either explicitly undecided or explicitly proposed without being implied silently

### `genesis.seed_bootstrap_governance`

- Status: `planned`
- Required artifacts:
  - `plan/tasks/2026-03-12_project_bootstrap.md`
  - `notes/logs/setup/2026-03-12_project_bootstrap.md`
- Advance when:
  - the first work is plan-governed and logged

### `genesis.initialize_operational_state`

- Status: `complete`
- Required artifacts:
  - this file
- Advance when:
  - the repo has a durable stage rollup surface

## Upcoming Stage Sub-Steps

### `product_definition.define_major_user_flows`

- Status: `planned`
- Required artifacts:
  - `notes/catalogs/traceability/relevant_user_flow_inventory.yaml`
- Advance when:
  - the major operator and user flows are explicit, scoped, and mapped to systems

### `product_definition.define_major_features`

- Status: `planned`
- Required artifacts:
  - `notes/catalogs/inventory/major_feature_inventory.md`
- Advance when:
  - the starter feature set has stable IDs, summaries, dependencies, and proof targets

### `product_definition.decompose_original_vision_into_features`

- Status: `planned`
- Required artifacts:
  - `notes/explorations/original_concept.md`
  - `notes/catalogs/inventory/major_feature_inventory.md`
- Advance when:
  - every meaningful user-requested capability has a stable feature row, affected systems, and proof posture

### `product_definition.define_feature_contracts`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/feature_contract_template.md`
- Advance when:
  - the starter contract model covers triggers, inputs, outputs, failures, and proof surfaces

### `product_definition.define_processing_system_contracts`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/processing_system_contracts.md`
- Advance when:
  - background processing, retries, idempotency, and ownership boundaries are outlined explicitly

### `product_definition.define_domain_model`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/domain_model_outline.md`
  - `notes/specs/product/canonical_vocabulary.md`
- Advance when:
  - the starter entities, state language, and durable records are defined consistently

### `product_definition.define_operator_surfaces`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/operator_surface_map.md`
- Advance when:
  - the CLI and website UI surfaces are outlined for the intended scope, or marked not applicable explicitly

### `product_definition.define_user_documentation_contracts`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/user_documentation_contract.md`
  - `docs/README.md`
- Advance when:
  - documentation audiences, ownership boundaries, and required starter documentation surfaces are explicit

### `product_definition.define_implementation_slices`

- Status: `planned`
- Required artifacts:
  - `notes/specs/product/implementation_slicing_guide.md`
  - `notes/specs/product/feature_delivery_map.md`
- Advance when:
  - each starter feature has an initial implementation slice, dependency order, and intended delivery posture

### `product_definition.establish_traceability_and_proof_targets`

- Status: `planned`
- Required artifacts:
  - `notes/catalogs/traceability/spec_traceability_matrix.md`
  - `notes/catalogs/checklists/verification_command_catalog.md`
- Advance when:
  - goals, flows, features, and proof targets are linked without implicit gaps

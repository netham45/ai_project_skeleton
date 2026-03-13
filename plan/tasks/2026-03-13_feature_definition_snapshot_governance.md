# Task: Add Feature Definition And Snapshot Governance

## Goal

Add a lightweight feature-governance model to the skeleton that explicitly maps each real feature to its governed docs, notes, checklists, logs, tests, and E2E target, then verifies those declared surfaces changed against a persisted baseline without requiring git.

## Scope

- Database: not applicable for this slice; no runtime persistence layer is added beyond repo-local governance artifacts.
- CLI: define the canonical snapshot-refresh command surface as documentation only; do not add a product CLI.
- Daemon or backend: not applicable for this slice.
- Website UI: not applicable for this slice.
- Config or YAML: add a rigid feature-definition YAML family for the skeleton's planning surface.
- Prompts: not applicable for this slice.
- User documentation: document the new feature-definition and snapshot model where it affects operator-facing governance expectations.
- Notes: update the rulebook, policy, README, feature-contract guidance, checklist guidance, and log guidance to describe the new model.
- Tests: add bounded document and snapshot-consistency tests plus shared helpers.

## Documentation Impact

- Status: required_update
- Required documentation changes:
  - `README.md`
  - `notes/catalogs/checklists/document_schema_rulebook.md`
  - `notes/catalogs/checklists/document_schema_test_policy.md`
  - `notes/catalogs/checklists/verification_command_catalog.md`
  - `notes/specs/product/feature_contract_template.md`
  - `notes/specs/product/user_documentation_contract.md`
- Rationale: the feature-definition and snapshot model becomes part of the starter repository contract.

## Documentation Verification

- `python3 -m pytest tests/unit/test_milestone_gate_docs.py tests/unit/test_user_documentation_docs.py -q`

## Notes Impact

- Status: required_update
- Required notes changes:
  - checklist policy and rulebook notes
  - feature-definition guidance
  - development-log guidance
- Rationale: the skeleton's authoritative governance notes must describe the new rigid feature family and snapshot behavior.

## Checklist Impact

- Status: required_update
- Required checklist changes:
  - `plan/checklists/PF01_example_capability.md`
- Rationale: the example feature checklist should reflect the new feature-definition and snapshot fields.

## Test Impact

- Status: required_update
- Required test changes:
  - new feature-definition schema tests
  - new snapshot-integrity and feature-snapshot comparison tests
  - helper updates to load feature definitions and snapshot files
- Rationale: the new authoritative document family and baseline model must be validated immediately.

## Canonical Verification

- `python3 -m pytest tests/unit/test_milestone_gate_docs.py tests/unit/test_user_documentation_docs.py tests/unit/test_feature_definition_docs.py tests/unit/test_feature_completion_snapshot.py -q`

## Exit Criteria

- The skeleton contains a rigid per-feature definition file family with an example asset.
- The example feature checklist and inventory surfaces reference the rigid feature definition and per-feature snapshot baseline.
- The rulebook, policy, command catalog, and product guidance distinguish E2E target definition from actual E2E proof.
- Snapshot comparison tests are read-only and do not rewrite the prior baseline on failure.
- A separate documented snapshot-refresh command exists and is described as the only supported way to update baselines.

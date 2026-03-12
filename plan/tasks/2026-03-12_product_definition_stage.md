# Task: Add Product Definition Stage

## Goal

Insert a product-definition lifecycle stage between architecture and setup so the skeleton requires major flows, feature outlines, contracts, and proof targets before scaffolding begins.

## Scope

- Database: document the durable-state outline and contract expectations that must be defined before setup, but do not add runtime schema or migrations.
- CLI: document the operator and AI command-surface expectations that must be outlined during product definition, but do not add active commands.
- Daemon or backend: document the runtime authority and processing-system contracts that must be defined before setup, but do not add active runtime behavior.
- Website UI: document the operator-surface map expectations that must be outlined during product definition when a browser surface is in scope.
- Config or YAML: document the declarative contract surfaces and traceability expectations that must be defined before setup, but do not add active schemas.
- Prompts: document the prompt-contract expectations that must be outlined during product definition when AI behavior is in scope.
- Notes: update lifecycle, checklist, inventory, traceability, and starter spec notes so the new stage is explicit and governed.
- Tests: add and run bounded document checks for the new lifecycle stage and starter product-definition note family.

## Canonical Verification

- `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q`

## Exit Criteria

- The lifecycle overview and stage notes include a product-definition stage between architecture and setup.
- The operational-state and bootstrap-readiness checklists treat product definition as a real maturity gate.
- The skeleton includes starter product-definition notes for feature contracts, processing-system contracts, operator surfaces, domain model outline, and canonical vocabulary.
- The feature inventory, relevant-flow inventory, traceability matrix, README, and verification-command catalog align with the new stage.
- The governing development log records the actual commands and results honestly.
- The bounded document test for the new stage passes.

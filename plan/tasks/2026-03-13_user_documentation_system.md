# Task: Add User Documentation As A First-Class System

## Goal

Make user documentation a first-class governed system in the skeleton so plans, features, flows, checklists, traceability, and bounded document tests all account for it explicitly.

## Scope

- Database: document how durable-state behavior that is exposed to users or operators must be reflected in reference or runbook material, but do not add runtime schema or migrations.
- CLI: document how supported commands, flags, and examples must map to authoritative user or operator docs, but do not add active commands.
- Daemon or backend: document how runtime behavior, failure handling, and recovery guidance map to runbooks, but do not add active runtime behavior.
- Website UI: document how browser-visible workflows and deep-linked help surfaces relate to authoritative documentation, but do not add active routes or pages.
- Config or YAML: document how supported configuration and environment requirements map to reference docs, but do not add active schemas.
- Prompts: document how prompt-backed workflows reference authoritative user or operator guidance where applicable.
- User documentation: add a starter `docs/` tree, a product-level documentation contract, and explicit plan, checklist, feature, and flow linkage rules.
- Notes: update lifecycle, inventories, traceability, schema rules, and README surfaces so user documentation is governed explicitly.
- Tests: add and run bounded document checks for the new documentation system and task-plan documentation fields.

## Documentation Impact

- Status: required_update
- Required documentation changes:
  - `docs/README.md`
  - `docs/user/README.md`
  - `docs/operator/README.md`
  - `docs/reference/README.md`
  - `docs/runbooks/README.md`
  - `notes/specs/product/user_documentation_contract.md`
- Rationale: this task creates the starter user-documentation system itself

## Documentation Verification

- `python3 -m pytest tests/unit/test_user_documentation_docs.py -q`

## Canonical Verification

- `python3 -m pytest tests/unit/test_lifecycle_docs.py -q`
- `python3 -m pytest tests/unit/test_user_documentation_docs.py -q`

## Exit Criteria

- `AGENTS.md` and the system inventory treat user documentation as a declared primary system.
- The skeleton contains a starter `docs/` tree with explicit audience-oriented subdirectories.
- Product definition requires a user-documentation contract before setup.
- Task plans require a documentation-impact section and documentation verification commands.
- Feature, flow, checklist, and traceability surfaces explicitly link work to documentation surfaces.
- The authoritative document-family inventory and schema rules treat user docs as a governed family.
- The bounded documentation tests pass and the development log records the real command results honestly.

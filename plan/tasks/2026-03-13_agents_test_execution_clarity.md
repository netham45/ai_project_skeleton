# Task: Clarify Test Execution Expectations In AGENTS

## Goal

Make `AGENTS.md` state more explicitly which tests must be run, when they must be run, and how the verification-command catalog controls that decision.

## Scope

- Database: not applicable for this doc-only clarification.
- CLI: not applicable for this doc-only clarification.
- Daemon or backend: not applicable for this doc-only clarification.
- Website UI: not applicable for this doc-only clarification.
- Config or YAML: document when config or feature-definition changes require their relevant tests.
- Prompts: not applicable for this doc-only clarification.
- User documentation: clarify how documentation changes trigger document-consistency tests.
- Notes: update the always-on doctrine in `AGENTS.md` and any enforcing doc tests.
- Tests: update the document-consistency test that validates `AGENTS.md`.

## Documentation Impact

- Status: required_update
- Required documentation changes:
  - `AGENTS.md`
- Rationale: the repository doctrine should state verification timing and scope explicitly rather than leaving it implied.

## Documentation Verification

- `python3 -m pytest tests/unit/test_lifecycle_docs.py -q`

## Notes Impact

- Status: reviewed_no_change
- Required notes changes:
  - none beyond `AGENTS.md`
- Rationale: the command catalog and test policy already define the command surfaces; this task clarifies the always-on doctrine that points contributors to them.

## Checklist Impact

- Status: not_applicable
- Required checklist changes:
  - none
- Rationale: this is a doctrine clarification, not a feature-status change.

## Test Impact

- Status: required_update
- Required test changes:
  - `tests/unit/test_lifecycle_docs.py`
- Rationale: the new `AGENTS.md` language should be enforced by the existing lifecycle/doctrine doc test.

## Canonical Verification

- `python3 -m pytest tests/unit/test_lifecycle_docs.py -q`

## Exit Criteria

- `AGENTS.md` tells contributors to use the verification-command catalog for changed scope rather than guessing.
- `AGENTS.md` states that item-level verification must run before claiming completion for that item.
- `AGENTS.md` states when broader test layers must run for stronger claims.
- The enforcing lifecycle doc test passes.

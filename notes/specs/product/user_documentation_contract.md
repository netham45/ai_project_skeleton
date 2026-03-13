# User Documentation Contract

## Purpose

Define the user-facing and operator-facing documentation surfaces that the product requires before setup and feature work begin to harden implementation choices.

## Required Audiences

Record which audiences exist for the real project:

- end users
- operators
- administrators
- integrators
- developers consuming supported interfaces

## Required Documentation Families

At minimum, decide whether the project needs:

- `docs/user/` guides
- `docs/operator/` guides
- `docs/reference/` reference material
- `docs/runbooks/` troubleshooting and recovery procedures

If a family is not applicable, say so explicitly rather than omitting it silently.

## Ownership Boundaries

- `notes/` own governance, lifecycle, planning, traceability, and internal design.
- `docs/` own user-facing and operator-facing guidance.
- CLI help, website UI text, and generated reference output must agree with the authoritative `docs/` surfaces when those are in scope.

## Required Plan And Checklist Linkage

Every meaningful task plan should record:

- documentation impact
- required documentation changes or an explicit no-change rationale
- documentation verification commands

Every meaningful feature checklist should record:

- user documentation status
- documentation surfaces affected

## Documentation Triggers

Documentation review is required when work changes:

- setup steps
- commands, flags, or examples shown to users
- configuration or environment requirements
- user-visible workflows
- operator-visible workflows
- supported failure handling
- troubleshooting or recovery guidance
- limits, compatibility, or prerequisites

## Documentation Invariants

- user-facing instructions must not claim unsupported behavior
- reference docs must not disagree with supported commands or configuration
- runbooks must not describe recovery steps the system does not actually support
- plans, checklists, and traceability assets must record whether documentation changed, did not change, or was not applicable

## Proof Surface

- Bounded proof: `python3 -m pytest tests/unit/test_user_documentation_docs.py -q`
- Real E2E target: documentation alignment should be exercised by the real feature or flow E2E that the docs describe; documentation-only changes do not replace runtime E2E

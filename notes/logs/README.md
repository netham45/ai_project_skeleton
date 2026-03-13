# Development Logs

This folder records meaningful AI-assisted or human-driven development work so plans, notes, code changes, tests, and status claims remain reconstructible.

## Required Family Mapping

Meaningful work should leave logs in the family that matches the work being performed:

- `setup/` for repository bootstrap and environment setup
- `features/` for feature implementation, hardening, or feature-slice remediation
- `e2e/` for end-to-end proving work
- `doc_updates/` for documentation-governance or documentation-family changes
- `reviews/` for review and audit passes

## Milestone Gate Rule

Milestone-gate tests should reject active feature work that is only logged under setup once the repository has moved beyond `template_only`.

Active task plans should be traceable to logs through task IDs, task titles, or clearly corresponding log entries. A repository should not be able to enter feature delivery with meaningful tasks that have no durable log coverage.

## Warning-Oriented Heuristics

Milestone-gate tests may warn when:

- one broad log entry appears to cover many unrelated active tasks
- commands or tests run are omitted from otherwise mature status claims
- completion entries exist without clearly naming remaining gaps or next steps

## Stop-Point Quality Rule

Implementation-stage stop points should be reconstructible without rereading the full diff.

Feature-delivery logs should record:

- what code or behavior changed
- what docs, notes, checklists, or contracts changed
- which governed files changed according to the latest snapshot comparison when that model is in use
- what tests or commands were run
- what passed or failed
- what still remains before a stronger status claim is honest

# Stage 03: Setup

## Purpose

Setup creates the first runnable repository skeleton and bounded-proof surface from the already-defined product contracts.

## Required Outcomes

- scaffold directories exist
- starter governance docs exist
- lifecycle governance is active
- bounded verification command exists and passes
- at least one future real E2E target is named
- the scaffold reflects the defined major flows, feature outlines, and contract notes instead of inventing them ad hoc

## Entry Gate

Setup should not begin merely because a repository has one concept note and one broad task file.

Setup entry requires product-definition evidence that is proportionate to the product's apparent complexity. Milestone-gate tests should consider:

- whether real product features have been decomposed explicitly
- whether those features are mapped to flows and proof targets
- whether the product-definition task surface is specific enough for the number of meaningful capabilities in scope
- whether documentation and operator surfaces have been identified before scaffolding hardens implementation choices

Thin but technically valid product-definition work may warn. Missing prerequisite evidence should fail setup entry outright.

## Required Artifacts

- `plan/tasks/2026-03-12_project_bootstrap.md`
- `notes/logs/setup/2026-03-12_project_bootstrap.md`
- `plan/checklists/00_project_bootstrap_readiness.md`
- starter tests under `tests/`

## Common Failure Modes

- creating folders without explaining why they exist
- allowing setup to make product-scope decisions that product definition was supposed to settle
- shipping placeholder docs that do not state what is missing
- treating setup as complete without any real proof command
- treating bounded setup checks as final runtime proof

## Exit Condition

This stage is complete enough to exit when the repository has a real scaffold, a real bounded command, and honest documentation about what stronger proof is still missing for the defined starter scope.

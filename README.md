# AI Project Skeleton

This folder is a released starter repository for teams that want to begin a new AI-assisted project under the governance model used by this repo.

It is a project skeleton, not a finished application template.

Its purpose is to provide a concrete starting shape for:

- lifecycle-driven planning
- notes-as-implementation discipline
- checklist and log requirements
- traceability and verification command tracking
- bounded-test and later E2E-proof expectations

The skeleton is intentionally stack-agnostic at release time.

It ships the operating model, repository shape, and governance artifacts first. The cloned project is expected to record its real stack choices during genesis and architecture instead of inheriting them silently.

This released skeleton also serves as the concrete reference target for the future project-skeleton generator work under `plan/future_plans/project_skeleton_generator/`. That future-plan material is still non-authoritative planning; this folder is the consumable starter artifact.

Start with these files:

- `AGENTS.md`
- `notes/lifecycle/00_project_lifecycle_overview.md`
- `plan/checklists/00_project_operational_state.md`
- `notes/specs/architecture/stack_decision_record.md`
- `notes/catalogs/checklists/verification_command_catalog.md`
- `notes/catalogs/inventory/system_inventory.md`

Repository layout:

- `notes/`: lifecycle, architecture, inventories, checklists, traceability, and development logs
- `plan/`: setup, task, feature, checklist, and future-plan surfaces
- `code/`: product implementation area
- `simulations/`: bounded-proof fixtures and harness artifacts
- `tests/`: unit, integration, and E2E proving surfaces

What this skeleton does not claim:

- a chosen application stack
- completed runtime behavior
- a generated repository pipeline
- release-ready proof for any specific product

Use it when you want the repository discipline already in place before substantive implementation begins.

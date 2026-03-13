# AI Project Skeleton

This folder is a released starter repository for teams that want to begin a new AI-assisted project under the governance model used by this repo.

It is a project skeleton, not a finished application template.

Its purpose is to provide a concrete starting shape for:

- lifecycle-driven planning
- notes-as-implementation discipline
- first-class user-documentation governance
- checklist and log requirements
- traceability and verification command tracking
- bounded-test and later E2E-proof expectations

The skeleton is intentionally stack-agnostic at release time.

It ships the operating model, repository shape, and governance artifacts first. The cloned project is expected to record its real stack choices during genesis and architecture instead of inheriting them silently.

It also expects a product-definition pass before setup. Major flows, feature outlines, domain terms, operator surfaces, user-documentation contracts, processing contracts, and implementation slices should be written down before the starter scaffold begins to harden implementation choices.

This released skeleton also serves as the concrete reference target for the future project-skeleton generator work under `plan/future_plans/project_skeleton_generator/`. That future-plan material is still non-authoritative planning; this folder is the consumable starter artifact.

Start with these files:

- `AGENTS.md`
- `notes/lifecycle/00_project_lifecycle_overview.md`
- `plan/checklists/00_project_operational_state.md`
- `notes/specs/architecture/stack_decision_record.md`
- `notes/lifecycle/03_stage_02_product_definition.md`
- `docs/README.md`
- `notes/specs/product/domain_model_outline.md`
- `notes/specs/product/user_documentation_contract.md`
- `notes/specs/product/implementation_slicing_guide.md`
- `notes/catalogs/checklists/verification_command_catalog.md`
- `notes/catalogs/inventory/system_inventory.md`

Repository layout:

- `notes/`: lifecycle, architecture, inventories, checklists, traceability, and development logs
- `docs/`: user guides, operator guides, references, and runbooks that must track real product behavior
- `notes/specs/product/`: starter product-definition notes for flows, contracts, vocabulary, and operator surfaces
- `plan/`: setup, task, feature, checklist, and future-plan surfaces
- `code/`: product implementation area
- `simulations/`: bounded-proof fixtures and harness artifacts
- `tests/`: unit, integration, and E2E proving surfaces

Documentation boundary:

- `notes/` are governance, planning, traceability, lifecycle, and design artifacts.
- `docs/` are consumer-facing user and operator documentation artifacts.

What this skeleton does not claim:

- a chosen application stack
- completed user or operator documentation for any specific product
- completed runtime behavior
- a generated repository pipeline
- release-ready proof for any specific product

Use it when you want the repository discipline already in place before substantive implementation begins.

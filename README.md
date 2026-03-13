# AI Project Skeleton

This folder is a released starter repository for teams that want to begin a new AI-assisted project under the governance model used by this repo.

It is a project skeleton, not a finished application template.

Its purpose is to provide a concrete starting shape for:

- lifecycle-driven planning
- notes-as-implementation discipline
- first-class user-documentation governance
- rigid per-feature definition files
- lightweight repo-local change snapshots for governed files
- checklist and log requirements
- traceability and verification command tracking
- bounded-test and later E2E-proof expectations

The skeleton is intentionally stack-agnostic at release time.

It ships the operating model, repository shape, and governance artifacts first. The cloned project is expected to record its real stack choices during genesis and architecture instead of inheriting them silently.

It also expects a product-definition pass before setup. Major flows, feature outlines, domain terms, operator surfaces, user-documentation contracts, processing contracts, and implementation slices should be written down before the starter scaffold begins to harden implementation choices.

## Milestone Gate Model

The starter repository uses milestone-gate validation rather than a single loose documentation-quality check.

Repository state progresses through:

- `template_only`: starter examples and placeholder feature artifacts are still allowed
- `product_defined`: real product features exist and placeholder feature artifacts must be retired
- `implementation_started`: setup or feature work has begun and milestone-entry, consistency, log, and proof rules all apply

The inherited template tests are expected to enforce three rule classes:

- `schema`: required files, headings, fields, statuses, and references exist
- `consistency`: plans, checklists, inventories, flows, docs, and logs do not contradict one another
- `readiness`: milestone-entry and milestone-exit gates can emit warnings for thin planning and errors for insufficient prerequisite evidence

Severity model:

- `error`: the repository is not allowed to claim the current milestone or proving posture
- `warn`: the repository can proceed, but the planning or documentation surface is unusually thin and should be expanded before the next stage hardens

Examples of milestone-gate enforcement:

- setup must not begin until product definition is decomposed enough for the product's apparent complexity
- real `PFxx` feature rows require real per-feature checklists
- real `PFxx` feature rows should also define a rigid feature-definition asset that names their governed docs, notes, checklists, logs, tests, and E2E target
- placeholder example checklist text must not survive once real product features exist
- runtime or E2E claims must not exceed the recorded proof posture
- feature snapshot tests should report created, modified, deleted, and unchanged governed files without requiring git
- failing snapshot-comparison tests must not rewrite the prior approved baseline
- warning-emitting tests should surface scant planning, scant documentation, or coarse grouping before that thinness turns into drift

## Feature Definition And Snapshot Model

Once the repository moves beyond pure template use, each real `PFxx` product feature should have:

- a rigid feature-definition file under `plan/features/`
- a matching feature checklist under `plan/checklists/`
- a per-feature snapshot baseline under `notes/catalogs/verification/`

The rigid feature-definition file is the source of truth for:

- which docs, notes, checklists, logs, and tests belong to the feature
- which files are expected to change versus only be reviewed
- which files count as key milestone-gating evidence
- which E2E asset and E2E command satisfy the feature's planning requirement

The per-feature snapshot baseline exists to support a repo-local, git-free comparison of governed files.

Snapshot comparison should:

- hash only the files declared for the feature
- report `created`, `modified`, `deleted`, and `unchanged`
- remain read-only during normal test runs
- only be refreshed through an explicit snapshot-update command

Defining a real E2E command satisfies the feature's E2E-target requirement. It does not satisfy actual E2E proof by itself.

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

# Feature Checklist Standard

## Purpose

Define the minimum fields every feature checklist should carry once real product features exist.

## Required Fields

- feature name
- feature ID
- affected systems
- database status
- CLI status
- daemon or backend status
- website UI status
- config or YAML status
- prompt status
- user documentation status
- documentation surfaces
- notes status
- bounded test status
- E2E status
- E2E asset
- rigid feature definition file
- feature snapshot baseline
- last snapshot update command
- last snapshot result
- last E2E command run
- last E2E result
- known limitations
- overall status

## Required Traceability Fields

Every product-feature checklist should also record:

- feature ID
- source vision reference
- governing flow IDs
- rigid feature definition file
- bounded proof command
- real E2E command or explicit not-applicable reason
- checklist file path should align with the feature ID

## Checklist-Per-Feature Rule

Template example checklist files are allowed only while the repository remains `template_only`.

Once one or more real `PFxx` product rows exist in `notes/catalogs/inventory/major_feature_inventory.md`:

- every real `PFxx` row must have exactly one real checklist file
- the template example checklist must be removed or clearly remain outside the active feature set
- active product checklists must not retain placeholder prose such as "replace this file" or "example capability"

## Coverage Rule

A product feature is not adequately tracked if its checklist cannot be traced back to a user-requested capability.

Checklist existence alone is insufficient. The checklist must preserve the linkage from user request to feature to flow to proof.

## Consistency Rules

- checklist overall status must not be stronger than the weakest required affected-system status
- checklist proof posture must not be stronger than the recorded E2E status and last E2E result
- checklist snapshot posture must not imply that required governed files changed unless the latest snapshot result records that evidence
- checklist documentation surfaces should agree with the feature inventory and governing flow docs
- checklist feature ID, source vision reference, governing flow IDs, and rigid feature definition file should agree with the feature inventory and flow inventory

## Warning-Oriented Readiness Heuristics

Milestone-gate tests may warn when a checklist is technically valid but unusually thin. Examples include:

- empty or nearly empty known-limitation sections for nontrivial features
- E2E fields present but still uninformative for a feature nearing stronger completion claims
- documentation surfaces named only generically when the feature touches multiple operator or user surfaces
- grouped feature planning that remains too coarse relative to the number of independently useful capabilities
- setup or later stages advancing without changes to the checklist's declared key files

## Delivery Loop Alignment

During active implementation, checklist maintenance should stay aligned with the governing task plan and the latest development-log stop point.

Tests may reject or warn on:

- implementation tasks that do not declare checklist impact at all
- feature work whose logs mention code changes but do not mention checklist, doc, note, or test synchronization
- stale checklist proof posture after a task records newly run commands or stronger completion claims

## Status Vocabulary

Per-system status values:

- `not_applicable`
- `planned`
- `in_progress`
- `implemented`
- `verified`
- `partial`
- `blocked`
- `deferred`

E2E status values:

- `not_started`
- `planned`
- `blocked`
- `failing`
- `passed`

Overall feature status values:

- `planned`
- `in_progress`
- `implemented`
- `partial`
- `verified`
- `flow_complete`
- `release_ready`
- `blocked`
- `deferred`

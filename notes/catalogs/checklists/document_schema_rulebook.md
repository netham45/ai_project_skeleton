# Document Schema Rulebook

## Purpose

Define the structural rules authoritative document families are expected to follow.

## Starter Rules

- required headings should exist for each family
- allowed status vocabularies should be enforced
- required references should be present where the family depends on them
- command surfaces should be consistent across plans, checklists, and command catalogs
- cross-document mappings should not drift silently
- lifecycle stage sequences should agree with operational-state and README guidance
- flow inventory, feature inventory, and traceability notes should agree on the product-definition stage
- product-definition spec notes should exist when the lifecycle claims that stage is required
- real product features should have rigid feature-definition files once the skeleton stops being template-only
- feature snapshot baselines should be read-only during normal verification and refreshed only by an explicit update command
- task plans should record documentation impact explicitly
- user-documentation contract and starter `docs/` surfaces should exist when the skeleton claims user documentation is first-class

## Repository State Model

Milestone-gate tests should classify the repository into one of these states:

- `template_only`: only starter governance rows and template example product rows exist
- `product_defined`: one or more real `PFxx` product rows exist, but setup may not yet have started
- `implementation_started`: setup or later work is active, so milestone-entry, milestone-exit, and stronger consistency checks apply

Starter example artifacts are only allowed while the repository remains `template_only`.

Once the repository becomes `product_defined`, tests should reject placeholder feature artifacts that were only meant to demonstrate starter shape.

## Rule Classes

Document-family tests should be grouped conceptually into:

- `schema` rules for required structure, required fields, and allowed vocabularies
- `consistency` rules for cross-document agreement between plans, checklists, flows, inventories, logs, and commands
- `readiness` rules for milestone-entry and milestone-exit sufficiency

## Severity Model

Document-family tests should use two machine severities:

- `error`: fail the test because the repository is structurally invalid, contradictory, or claiming a stronger posture than the evidence supports
- `warn`: emit a warning because the repository is technically valid but thin, coarse, or likely to drift if the next milestone hardens without more detail

Warnings are appropriate for scant but non-contradictory planning. Errors are required when milestone prerequisites are actually missing.

## Milestone Gate Families

The starter test suite should validate milestone gates for:

- genesis
- architecture
- product definition
- setup
- feature delivery
- hardening and E2E
- release readiness when the cloned project later adopts that scope

Each milestone gate should be able to express:

- entry errors
- entry warnings
- exit errors
- exit warnings

## Required Enforcement Areas

Milestone-gate tests should eventually enforce at least the following:

- real `PFxx` feature rows require real per-feature checklist files
- feature inventories, feature checklists, flow inventories, and task plans must not drift in status claims
- rigid feature-definition assets must agree with feature inventories, feature checklists, governed docs, and snapshot baselines
- active work must have development logs in the correct family rather than only in a generic setup log
- E2E target paths are not a substitute for explicit E2E proof status
- defining a real E2E command satisfies target-definition requirements, but not actual E2E proof status
- docs must not claim supported behavior beyond the current feature contract or documented limitation posture
- setup-entry readiness should consider the product's apparent complexity rather than relying only on raw artifact counts
- warning-emitting checks should flag suspiciously sparse task decomposition, documentation coverage, or checklist detail before later stages harden those gaps into errors
- active implementation tasks should continuously declare documentation, notes, checklist, and test impact rather than relying only on the original planning pass
- feature-delivery logs should preserve stop-point quality well enough to explain what changed, what was verified, and what remains
- milestone gates may warn when later stages advance without changes to declared key files

## Anti-Goals

These tests should not freeze exact prose wording unless wording itself is part of the contract.

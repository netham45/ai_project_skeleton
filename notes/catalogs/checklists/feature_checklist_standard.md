# Feature Checklist Standard

## Purpose

Define the minimum fields every feature checklist should carry.

## Required Fields

- feature name
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
- known limitations
- overall status

## Required Traceability Fields

Every product-feature checklist should also record:

- feature ID
- source vision reference
- governing flow IDs
- bounded proof command
- real E2E command or explicit not-applicable reason

## Coverage Rule

A product feature is not adequately tracked if its checklist cannot be traced back to a user-requested capability.

Checklist existence alone is insufficient. The checklist must preserve the linkage from user request to feature to flow to proof.

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

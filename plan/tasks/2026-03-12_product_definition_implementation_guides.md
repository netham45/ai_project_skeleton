# Task: Extend Product Definition With Implementation Guides

## Goal

Strengthen the product-definition stage so it ends with implementation-ready slicing and per-feature delivery guidance rather than only high-level contracts.

## Scope

- Database: document how feature slices should account for durable-state concerns and dependency order, but do not add runtime schema or migrations.
- CLI: document how feature slices should account for command-surface delivery order and operator dependencies, but do not add active commands.
- Daemon or backend: document how feature slices should account for runtime and processing dependencies, but do not add active runtime behavior.
- Website UI: document how feature slices should account for browser-surface sequencing and daemon-backed authority, but do not add active routes or pages.
- Config or YAML: document how feature slices should account for config or policy dependencies, but do not add active schemas.
- Prompts: document how feature slices should account for prompt dependencies and delivery order when AI behavior is in scope.
- Notes: update the lifecycle, checklist, inventory, and starter product-definition notes so implementation slicing and feature-delivery mapping are explicit requirements.
- Tests: update and run the bounded skeleton lifecycle-document test for the strengthened product-definition stage.

## Canonical Verification

- `python3 -m pytest ai_project_skeleton/tests/unit/test_lifecycle_docs.py -q`

## Exit Criteria

- The product-definition stage note requires implementation slicing and feature-delivery guidance explicitly.
- The operational-state and bootstrap-readiness checklists treat implementation slicing as part of the pre-setup gate.
- The skeleton includes starter notes for implementation slicing and feature-delivery mapping.
- The feature inventory and traceability surfaces point to the new implementation-guide artifacts.
- The bounded document test passes and the development log records the real command result.

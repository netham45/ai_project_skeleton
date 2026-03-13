# Verification Command Catalog

## Purpose

Define the canonical verification command surface for the starter repository.

These commands are examples to be replaced or refined by the real project, but they should not stay implicit.

## Bootstrap Commands

Use these during early setup:

```bash
python3 -m pytest tests/unit/test_lifecycle_docs.py -q
```

## Product Definition Commands

Use these when product-definition notes, inventories, or lifecycle assets change:

```bash
python3 -m pytest tests/unit/test_lifecycle_docs.py -q
python3 -m pytest tests/unit/test_user_documentation_docs.py -q
```

## Documentation Consistency Commands

Use these when `docs/`, documentation contracts, task-plan documentation fields, or documentation traceability assets change:

```bash
python3 -m pytest tests/unit/test_user_documentation_docs.py -q
```

## Product Feature Traceability Commands

Use these when original-concept notes, product-feature inventory rows, flow mappings, or feature checklists change:

```bash
python3 -m pytest tests/unit/test_lifecycle_docs.py -q
python3 -m pytest tests/unit/test_user_documentation_docs.py -q
python3 -m pytest tests/unit/test_product_feature_traceability_docs.py -q
```

## Feature Definition And Snapshot Commands

Use these when feature-definition YAML, feature snapshot baselines, or governed-file mapping rules change:

```bash
python3 -m pytest tests/unit/test_feature_definition_docs.py -q
python3 -m pytest tests/unit/test_feature_completion_snapshot.py -q
python3 scripts/update_feature_snapshot.py --feature PF01
```

The snapshot update command is a maintenance command, not proof by itself. It should refuse to update a baseline if the relevant verification tests are failing.

## Milestone Gate Commands

Use these when changing milestone-entry rules, checklist standards, log rules, or warning-versus-error validation behavior:

```bash
python3 -m pytest tests/unit/test_milestone_gate_docs.py -q
python3 -m pytest tests/unit/test_first_product_slice_governance_gate.py -q
python3 -m pytest tests/unit/test_feature_delivery_sync_docs.py -q
python3 -m pytest tests/unit/test_feature_completion_snapshot.py -q
```

## Integration Command Placeholder

Replace this once the real integration surface exists:

```bash
python3 -m pytest tests/integration -q
```

## E2E Command Placeholder

Replace this once the first real runtime narrative exists:

```bash
python3 -m pytest tests/e2e/test_e2e_first_flow.py -q
```

## Rule

If a plan, note, or checklist claims something is verified, it must cite the documented command that actually passed.

Commands that remain explicit placeholders should be marked as placeholders honestly rather than being described as runnable completion proof.

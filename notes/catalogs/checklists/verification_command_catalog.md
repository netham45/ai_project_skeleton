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

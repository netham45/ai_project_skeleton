# Document Schema Test Policy

## Purpose

Explain how and when authoritative document-family tests must run.

## Policy

- if an authoritative document changes, run the relevant document tests afterward
- if a new required field or status value is introduced, update the tests in the same change
- documentation work is not complete unless the relevant document-family tests exist and pass for the changed scope

## Milestone Gate Policy

Milestone-gate validation should combine:

- schema checks
- consistency checks
- readiness checks

Readiness checks may emit warnings when a repository is technically valid but unusually thin for its current milestone.

Warnings should not replace hard failures when the repository lacks required prerequisite evidence for entering or exiting a stage.

Milestone-entry examples:

- entering setup without sufficiently decomposed product-definition evidence should fail
- entering setup with barely enough but unusually coarse planning may warn
- entering feature delivery with empty limitation sections or unusually sparse operator docs may warn before later gates promote that thinness into an error

Implementation-loop examples:

- an active coding task that omits notes impact, checklist impact, or test impact should fail
- a feature log that records code work but omits commands run or remaining gaps should fail
- sparse stop-point summaries or unusually skeletal synced docs may warn before stronger completion claims are allowed
- a rigid feature-definition file may satisfy the requirement that a feature has an E2E target by defining a real E2E command and asset
- a passing E2E target-definition check must not be treated as proof that the E2E command actually passed
- feature snapshot-comparison tests must remain read-only and must not rewrite the prior baseline on failure
- milestone key-file drift checks may warn when setup or later stages advance without changes to the declared key files for an active feature

## Starter Command Placeholder

```bash
python3 -m pytest tests/unit/test_lifecycle_docs.py -q
python3 -m pytest tests/unit/test_user_documentation_docs.py -q
python3 -m pytest tests/unit/test_product_feature_traceability_docs.py -q
python3 -m pytest tests/unit/test_milestone_gate_docs.py -q
python3 -m pytest tests/unit/test_first_product_slice_governance_gate.py -q
python3 -m pytest tests/unit/test_feature_delivery_sync_docs.py -q
python3 -m pytest tests/unit/test_feature_definition_docs.py -q
python3 -m pytest tests/unit/test_feature_completion_snapshot.py -q
```

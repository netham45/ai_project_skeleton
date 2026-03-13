from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_readme_and_rulebook_define_milestone_gate_model() -> None:
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    rulebook_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_rulebook.md"
    ).read_text(encoding="utf-8")

    assert "## Milestone Gate Model" in readme_text
    assert "`template_only`" in readme_text
    assert "`product_defined`" in readme_text
    assert "`implementation_started`" in readme_text
    assert "`schema`" in readme_text
    assert "`consistency`" in readme_text
    assert "`readiness`" in readme_text
    assert "## Feature Definition And Snapshot Model" in readme_text

    assert "## Repository State Model" in rulebook_text
    assert "## Rule Classes" in rulebook_text
    assert "## Severity Model" in rulebook_text
    assert "## Milestone Gate Families" in rulebook_text
    assert "entry errors" in rulebook_text
    assert "exit warnings" in rulebook_text
    assert "rigid feature-definition files" in rulebook_text
    assert "read-only during normal verification" in rulebook_text


def test_policy_and_command_catalog_require_milestone_gate_tests() -> None:
    policy_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_test_policy.md"
    ).read_text(encoding="utf-8")
    commands_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "verification_command_catalog.md"
    ).read_text(encoding="utf-8")

    assert "## Milestone Gate Policy" in policy_text
    assert "Readiness checks may emit warnings" in policy_text
    assert "entering setup without sufficiently decomposed product-definition evidence should fail" in policy_text
    assert "tests/unit/test_milestone_gate_docs.py" in policy_text
    assert "tests/unit/test_first_product_slice_governance_gate.py" in policy_text
    assert "tests/unit/test_feature_definition_docs.py" in policy_text
    assert "tests/unit/test_feature_completion_snapshot.py" in policy_text

    assert "## Milestone Gate Commands" in commands_text
    assert "test_milestone_gate_docs.py" in commands_text
    assert "test_first_product_slice_governance_gate.py" in commands_text
    assert "test_feature_completion_snapshot.py" in commands_text


def test_checklist_log_and_feature_contract_docs_capture_new_rules() -> None:
    checklist_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "feature_checklist_standard.md"
    ).read_text(encoding="utf-8")
    log_text = (REPO_ROOT / "notes" / "logs" / "README.md").read_text(encoding="utf-8")
    contract_text = (
        REPO_ROOT / "notes" / "specs" / "product" / "feature_contract_template.md"
    ).read_text(encoding="utf-8")
    docs_contract_text = (
        REPO_ROOT / "notes" / "specs" / "product" / "user_documentation_contract.md"
    ).read_text(encoding="utf-8")
    setup_text = (REPO_ROOT / "notes" / "lifecycle" / "04_stage_03_setup.md").read_text(encoding="utf-8")

    assert "## Checklist-Per-Feature Rule" in checklist_text
    assert "## Consistency Rules" in checklist_text
    assert "## Warning-Oriented Readiness Heuristics" in checklist_text
    assert "E2E asset" in checklist_text
    assert "rigid feature definition file" in checklist_text
    assert "feature snapshot baseline" in checklist_text
    assert "last E2E command run" in checklist_text
    assert "E2E status values" in checklist_text

    assert "## Required Family Mapping" in log_text
    assert "## Milestone Gate Rule" in log_text
    assert "Active task plans should be traceable to logs" in log_text
    assert "latest snapshot comparison" in log_text

    assert "### Supported Behaviors" in contract_text
    assert "### Known Unsupported Cases" in contract_text
    assert "### Failure Handling Actually Implemented" in contract_text
    assert "### Documentation Claim Boundary" in contract_text
    assert "E2E readiness status" in contract_text
    assert "Required E2E command" in contract_text
    assert "Rigid feature definition file" in contract_text

    assert "## Feature Contract Alignment" in docs_contract_text
    assert "supported behaviors" in docs_contract_text
    assert "failure handling actually implemented" in docs_contract_text
    assert "## Snapshot Rule" in docs_contract_text

    assert "## Entry Gate" in setup_text
    assert "Setup should not begin merely because a repository has one concept note and one broad task file." in setup_text

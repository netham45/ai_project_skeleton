from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = REPO_ROOT / "docs"
TASK_PLANS_DIR = REPO_ROOT / "plan" / "tasks"


def test_user_documentation_is_declared_primary_system() -> None:
    agents_text = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    inventory_text = (
        REPO_ROOT / "notes" / "catalogs" / "inventory" / "system_inventory.md"
    ).read_text(encoding="utf-8")

    assert "### 7. User Documentation" in agents_text
    assert "User documentation is the user-facing and operator-facing guidance surface" in agents_text
    assert "`notes/` are governance and design artifacts." in agents_text
    assert "`docs/` are consumer-facing documentation artifacts." in agents_text
    assert "User documentation:" in inventory_text


def test_user_documentation_contract_and_docs_tree_exist() -> None:
    contract_text = (
        REPO_ROOT / "notes" / "specs" / "product" / "user_documentation_contract.md"
    ).read_text(encoding="utf-8")
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "## Required Plan And Checklist Linkage" in contract_text
    assert "documentation impact" in contract_text
    assert "documentation verification commands" in contract_text
    assert "`docs/`" in readme_text
    assert "Documentation boundary:" in readme_text

    for path in [
        DOCS_DIR / "README.md",
        DOCS_DIR / "user" / "README.md",
        DOCS_DIR / "operator" / "README.md",
        DOCS_DIR / "reference" / "README.md",
        DOCS_DIR / "runbooks" / "README.md",
    ]:
        assert path.exists(), f"Missing documentation surface: {path}"


def test_task_plan_schema_requires_documentation_sections() -> None:
    task_readme_text = (TASK_PLANS_DIR / "README.md").read_text(encoding="utf-8")

    assert "documentation impact" in task_readme_text
    assert "documentation verification commands" in task_readme_text

    for path in TASK_PLANS_DIR.glob("*.md"):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        assert "## Documentation Impact" in text, f"Missing documentation impact section in {path.name}"
        assert "## Documentation Verification" in text, f"Missing documentation verification section in {path.name}"


def test_checklist_traceability_and_command_catalog_reference_docs() -> None:
    checklist_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "feature_checklist_standard.md"
    ).read_text(encoding="utf-8")
    flow_text = (
        REPO_ROOT / "notes" / "catalogs" / "traceability" / "relevant_user_flow_inventory.yaml"
    ).read_text(encoding="utf-8")
    feature_text = (
        REPO_ROOT / "notes" / "catalogs" / "inventory" / "major_feature_inventory.md"
    ).read_text(encoding="utf-8")
    traceability_text = (
        REPO_ROOT / "notes" / "catalogs" / "traceability" / "spec_traceability_matrix.md"
    ).read_text(encoding="utf-8")
    commands_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "verification_command_catalog.md"
    ).read_text(encoding="utf-8")

    assert "user documentation status" in checklist_text
    assert "documentation surfaces" in checklist_text
    assert "documentation_required: true" in flow_text
    assert "documentation_surfaces:" in flow_text
    assert "covers_feature_ids" in flow_text
    assert "user_docs" in feature_text
    assert "Source vision reference" in feature_text
    assert "G06 | User documentation is first-class and explicitly linked to work" in traceability_text
    assert "## Documentation Consistency Commands" in commands_text
    assert "tests/unit/test_user_documentation_docs.py" in commands_text


def test_feature_inventory_and_traceability_require_documentation_decisions_for_product_features() -> None:
    feature_text = (
        REPO_ROOT / "notes" / "catalogs" / "inventory" / "major_feature_inventory.md"
    ).read_text(encoding="utf-8")
    flow_text = (
        REPO_ROOT / "notes" / "catalogs" / "traceability" / "relevant_user_flow_inventory.yaml"
    ).read_text(encoding="utf-8")

    assert "Documentation surfaces" in feature_text
    assert "Source vision reference" in feature_text
    assert "covers_feature_ids" in flow_text
    assert "source_vision_refs" in flow_text


def test_user_documentation_family_is_authoritative() -> None:
    family_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "authoritative_document_family_inventory.md"
    ).read_text(encoding="utf-8")
    rulebook_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_rulebook.md"
    ).read_text(encoding="utf-8")
    policy_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_test_policy.md"
    ).read_text(encoding="utf-8")

    assert "user documentation docs" in family_text
    assert "task plans should record documentation impact explicitly" in rulebook_text
    assert "starter `docs/` surfaces should exist" in rulebook_text
    assert "tests/unit/test_user_documentation_docs.py" in policy_text

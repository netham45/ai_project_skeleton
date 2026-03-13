from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
LIFECYCLE_DIR = REPO_ROOT / "notes" / "lifecycle"
PRODUCT_SPECS_DIR = REPO_ROOT / "notes" / "specs" / "product"


def test_agents_doc_defines_lifecycle_progression_model() -> None:
    text = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "## Lifecycle Governance Rule" in text
    assert "## Lifecycle Progression Rule" in text
    assert "## Lifecycle Maturity Ladder" in text
    assert "`AGENTS.md` defines the always-on doctrine" in text
    assert "`notes/lifecycle/*.md` define the stage-specific standards" in text
    assert "`plan/checklists/00_project_operational_state.md` records which stage" in text
    assert "`plan/tasks/*.md` define the concrete work package" in text
    for stage_name in [
        "`genesis`",
        "`architecture`",
        "`product definition`",
        "`setup`",
        "`feature delivery`",
        "`hardening and end-to-end proof`",
        "`post-v1 evolution`",
    ]:
        assert stage_name in text


def test_lifecycle_overview_lists_product_definition_stage() -> None:
    text = (LIFECYCLE_DIR / "00_project_lifecycle_overview.md").read_text(encoding="utf-8")

    assert "3. product definition" in text
    assert "`03_stage_02_product_definition.md`" in text
    assert "`04_stage_03_setup.md`" in text
    assert "`05_stage_04_feature_delivery.md`" in text
    assert "`06_stage_05_hardening_and_e2e.md`" in text
    assert "`07_stage_06_post_v1_evolution.md`" in text
    assert "Product definition turns those boundaries into major flows" in text


def test_product_definition_stage_note_references_required_artifacts() -> None:
    text = (LIFECYCLE_DIR / "03_stage_02_product_definition.md").read_text(encoding="utf-8")

    for required_ref in [
        "notes/catalogs/inventory/major_feature_inventory.md",
        "notes/catalogs/traceability/relevant_user_flow_inventory.yaml",
        "notes/catalogs/traceability/spec_traceability_matrix.md",
        "notes/specs/product/canonical_vocabulary.md",
        "notes/specs/product/domain_model_outline.md",
        "notes/specs/product/feature_contract_template.md",
        "notes/specs/product/feature_delivery_map.md",
        "notes/specs/product/implementation_slicing_guide.md",
        "notes/specs/product/operator_surface_map.md",
        "notes/specs/product/processing_system_contracts.md",
    ]:
        assert required_ref in text


def test_operational_state_and_bootstrap_readiness_require_product_definition() -> None:
    operational_text = (REPO_ROOT / "plan" / "checklists" / "00_project_operational_state.md").read_text(
        encoding="utf-8"
    )
    bootstrap_text = (REPO_ROOT / "plan" / "checklists" / "00_project_bootstrap_readiness.md").read_text(
        encoding="utf-8"
    )

    assert "`product_defined`" in operational_text
    for substep in [
        "product_definition.define_major_user_flows",
        "product_definition.define_major_features",
        "product_definition.define_feature_contracts",
        "product_definition.define_processing_system_contracts",
        "product_definition.define_domain_model",
        "product_definition.define_operator_surfaces",
        "product_definition.define_implementation_slices",
        "product_definition.establish_traceability_and_proof_targets",
    ]:
        assert substep in operational_text

    for row in [
        "Major user flow inventory",
        "Major feature inventory",
        "Product contract notes",
        "Domain model and vocabulary",
        "Implementation slicing guide",
        "Traceability matrix",
    ]:
        assert row in bootstrap_text


def test_product_definition_spec_family_exists() -> None:
    inventory_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "authoritative_document_family_inventory.md"
    ).read_text(encoding="utf-8")
    rulebook_text = (REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_rulebook.md").read_text(
        encoding="utf-8"
    )
    policy_text = (REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_test_policy.md").read_text(
        encoding="utf-8"
    )

    assert "product-definition specs" in inventory_text
    assert "product-definition spec notes should exist" in rulebook_text
    assert "tests/unit/test_lifecycle_docs.py" in policy_text

    for path in [
        PRODUCT_SPECS_DIR / "README.md",
        PRODUCT_SPECS_DIR / "canonical_vocabulary.md",
        PRODUCT_SPECS_DIR / "domain_model_outline.md",
        PRODUCT_SPECS_DIR / "feature_contract_template.md",
        PRODUCT_SPECS_DIR / "feature_delivery_map.md",
        PRODUCT_SPECS_DIR / "implementation_slicing_guide.md",
        PRODUCT_SPECS_DIR / "operator_surface_map.md",
        PRODUCT_SPECS_DIR / "processing_system_contracts.md",
    ]:
        assert path.exists(), f"Missing required product-definition note: {path.name}"


def test_flow_feature_traceability_assets_reference_product_definition() -> None:
    flow_text = (REPO_ROOT / "notes" / "catalogs" / "traceability" / "relevant_user_flow_inventory.yaml").read_text(
        encoding="utf-8"
    )
    feature_text = (REPO_ROOT / "notes" / "catalogs" / "inventory" / "major_feature_inventory.md").read_text(
        encoding="utf-8"
    )
    traceability_text = (
        REPO_ROOT / "notes" / "catalogs" / "traceability" / "spec_traceability_matrix.md"
    ).read_text(encoding="utf-8")
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    commands_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "verification_command_catalog.md"
    ).read_text(encoding="utf-8")

    assert "FLOW03" in flow_text
    assert "FLOW04" in flow_text
    assert "notes/lifecycle/03_stage_02_product_definition.md" in flow_text
    assert "F03 | Product definition contracts" in feature_text
    assert "G03 | Product definition is explicit before setup" in traceability_text
    assert "G05 | Product definition is implementation-ready" in traceability_text
    assert "product-definition pass before setup" in readme_text
    assert "## Product Definition Commands" in commands_text

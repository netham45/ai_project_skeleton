from doc_validation_helpers import (
    REPO_ROOT,
    get_repo_state,
    iter_feature_definition_docs,
    load_feature_snapshot,
    parse_feature_inventory,
)


def test_feature_definition_family_is_documented() -> None:
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    family_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "authoritative_document_family_inventory.md"
    ).read_text(encoding="utf-8")
    policy_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_test_policy.md"
    ).read_text(encoding="utf-8")
    commands_text = (
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "verification_command_catalog.md"
    ).read_text(encoding="utf-8")
    plan_text = (REPO_ROOT / "plan" / "features" / "README.md").read_text(encoding="utf-8")

    assert "## Feature Definition And Snapshot Model" in readme_text
    assert "rigid feature definitions" in family_text
    assert "feature snapshot baselines" in family_text
    assert "test_feature_definition_docs.py" in policy_text
    assert "test_feature_completion_snapshot.py" in policy_text
    assert "## Feature Definition And Snapshot Commands" in commands_text
    assert "rigid feature-definition file per feature" in plan_text


def test_feature_inventory_rows_reference_feature_definition_files() -> None:
    rows = parse_feature_inventory(REPO_ROOT)

    for row in rows:
        if not row.feature_id.startswith("PF"):
            continue
        assert row.feature_definition.strip(), f"{row.feature_id} must name a feature-definition file."
        path = REPO_ROOT / row.feature_definition
        assert path.exists(), f"{row.feature_id} feature definition is missing: {row.feature_definition}"


def test_feature_definition_files_have_required_fields_and_linked_snapshots() -> None:
    definitions = iter_feature_definition_docs(REPO_ROOT)
    assert definitions, "The skeleton should ship at least one example feature-definition file."

    for definition in definitions:
        data = definition.data
        assert data.get("feature_id"), f"{definition.path.name} must declare feature_id."
        assert data.get("name"), f"{definition.path.name} must declare name."
        assert isinstance(data.get("traceability"), dict), f"{definition.path.name} must declare traceability."
        assert isinstance(data.get("governed_files"), dict), f"{definition.path.name} must declare governed_files."
        assert isinstance(data.get("proof"), dict), f"{definition.path.name} must declare proof."
        assert isinstance(data.get("snapshot"), dict), f"{definition.path.name} must declare snapshot."

        proof = data["proof"]
        assert proof.get("required_e2e_command"), f"{definition.path.name} must define required_e2e_command."
        assert proof.get("e2e_asset"), f"{definition.path.name} must define e2e_asset."
        assert proof["e2e_asset"] in proof["required_e2e_command"], (
            f"{definition.path.name} should have an E2E command that references the declared E2E asset."
        )

        snapshot_path = REPO_ROOT / data["snapshot"]["baseline_file"]
        assert snapshot_path.exists(), f"{definition.path.name} snapshot baseline is missing."

        snapshot = load_feature_snapshot(snapshot_path)
        assert snapshot.data.get("feature_id") == data["feature_id"], (
            f"{snapshot.path.name} must point at feature {data['feature_id']}."
        )
        assert snapshot.data.get("based_on_definition") == definition.path.relative_to(REPO_ROOT).as_posix(), (
            f"{snapshot.path.name} must cite its defining feature asset."
        )


def test_template_state_still_ships_example_feature_definition() -> None:
    if get_repo_state(REPO_ROOT) != "template_only":
        return

    definitions = iter_feature_definition_docs(REPO_ROOT)
    feature_ids = {definition.data["feature_id"] for definition in definitions}
    assert "PF01" in feature_ids

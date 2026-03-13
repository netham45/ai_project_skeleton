from doc_validation_helpers import (
    LATE_STAGE_NAMES,
    REPO_ROOT,
    collect_feature_paths,
    compare_feature_snapshot,
    emit_warning,
    get_active_stage,
    get_repo_state,
    iter_feature_definition_docs,
    load_feature_snapshot,
    read_text,
)


def test_snapshot_family_is_documented_as_read_only_during_verification() -> None:
    readme_text = read_text(REPO_ROOT / "notes" / "catalogs" / "verification" / "README.md")
    contract_text = read_text(REPO_ROOT / "notes" / "specs" / "product" / "user_documentation_contract.md")

    assert "remain read-only during normal test runs" in readme_text
    assert "must not rewrite the prior approved baseline on failure" in contract_text


def test_feature_snapshots_cover_declared_governed_files_without_mutating_baselines() -> None:
    for definition in iter_feature_definition_docs(REPO_ROOT):
        snapshot_path = REPO_ROOT / definition.data["snapshot"]["baseline_file"]
        before_text = read_text(snapshot_path)
        snapshot = load_feature_snapshot(snapshot_path)
        declared_paths = set(collect_feature_paths(definition))
        snapshot_paths = set(snapshot.data.get("files", {}).keys())

        assert declared_paths == snapshot_paths, (
            f"{definition.path.name} and {snapshot.path.name} disagree on the tracked governed files."
        )

        report = compare_feature_snapshot(definition, snapshot, REPO_ROOT)
        assert set(report) == {"created", "modified", "deleted", "unchanged"}

        after_text = read_text(snapshot_path)
        assert before_text == after_text, f"{snapshot.path.name} changed during a read-only comparison test."


def test_required_update_files_must_change_when_snapshot_policy_requires_it() -> None:
    repo_state = get_repo_state(REPO_ROOT)

    for definition in iter_feature_definition_docs(REPO_ROOT):
        snapshot = load_feature_snapshot(REPO_ROOT / definition.data["snapshot"]["baseline_file"])
        report = compare_feature_snapshot(definition, snapshot, REPO_ROOT)
        required_update = definition.data["governed_files"]["documentation"]["required_update"]
        required_update += definition.data["governed_files"]["notes"]["required_update"]
        required_update += definition.data["governed_files"]["checklists"]["required_update"]
        required_update += definition.data["governed_files"]["logs"]["required_update"]

        if not definition.data["snapshot"].get("require_changes_since_last"):
            continue
        if repo_state == "template_only":
            continue

        changed = set(report["created"] + report["modified"] + report["deleted"])
        unchanged_required = sorted(path for path in required_update if path not in changed)
        assert not unchanged_required, (
            f"{definition.data['feature_id']} has required_update files that did not change since the last snapshot: "
            + ", ".join(unchanged_required)
        )


def test_late_stage_repositories_warn_when_key_files_do_not_change() -> None:
    active_stage = get_active_stage(REPO_ROOT)
    if active_stage not in LATE_STAGE_NAMES:
        return

    for definition in iter_feature_definition_docs(REPO_ROOT):
        snapshot = load_feature_snapshot(REPO_ROOT / definition.data["snapshot"]["baseline_file"])
        report = compare_feature_snapshot(definition, snapshot, REPO_ROOT)
        changed = set(report["created"] + report["modified"] + report["deleted"])
        unchanged_key_files = sorted(path for path in definition.data.get("key_files", []) if path not in changed)
        if len(unchanged_key_files) == len(definition.data.get("key_files", [])):
            emit_warning(
                "FEATURE_SNAPSHOT_WARN_001",
                f"{definition.data['feature_id']} advanced to {active_stage} without changes to any declared key files.",
            )

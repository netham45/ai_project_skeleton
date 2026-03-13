import re

from doc_validation_helpers import (
    LATE_STAGE_NAMES,
    REPO_ROOT,
    emit_warning,
    find_matching_logs,
    get_active_stage,
    get_real_product_rows,
    get_repo_state,
    parse_task_docs,
    read_text,
)


def _assert_required_task_sections(text: str, path_name: str) -> None:
    for heading in [
        "## Documentation Impact",
        "## Documentation Verification",
        "## Notes Impact",
        "## Checklist Impact",
        "## Test Impact",
    ]:
        assert heading in text, f"{path_name} is missing required task-plan section {heading!r}."


def test_feature_delivery_docs_define_delivery_loop_requirements() -> None:
    lifecycle_text = read_text(REPO_ROOT / "notes" / "lifecycle" / "05_stage_04_feature_delivery.md")
    task_readme_text = read_text(REPO_ROOT / "plan" / "tasks" / "README.md")
    logs_text = read_text(REPO_ROOT / "notes" / "logs" / "README.md")
    policy_text = read_text(
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "document_schema_test_policy.md"
    )
    commands_text = read_text(
        REPO_ROOT / "notes" / "catalogs" / "checklists" / "verification_command_catalog.md"
    )

    assert "## Delivery Loop Rule" in lifecycle_text
    assert "active implementation tasks keep docs, notes, checklists, and test impact synchronized" in lifecycle_text
    assert "notes impact" in task_readme_text
    assert "checklist impact" in task_readme_text
    assert "test impact" in task_readme_text
    assert "## Stop-Point Quality Rule" in logs_text
    assert "Implementation-loop examples:" in policy_text
    assert "test_feature_delivery_sync_docs.py" in commands_text


def test_all_template_task_plans_follow_delivery_loop_schema() -> None:
    for task in parse_task_docs(REPO_ROOT):
        _assert_required_task_sections(task.text, task.path.name)


def test_active_feature_tasks_require_maintenance_impact_fields_and_logs() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    active_stage = get_active_stage(REPO_ROOT)
    real_rows = get_real_product_rows(REPO_ROOT)
    if active_stage not in LATE_STAGE_NAMES or not real_rows:
        return

    feature_ids = {row.feature_id for row in real_rows}
    active_feature_tasks = [
        task
        for task in parse_task_docs(REPO_ROOT)
        if any(feature_id in task.text for feature_id in feature_ids)
    ]

    if active_stage in {"feature_delivery_ready", "bounded_verified", "e2e_ready", "flow_complete", "release_ready"}:
        assert active_feature_tasks, (
            "Feature-delivery-or-later repositories must have at least one task plan that names real feature IDs."
        )

    for task in active_feature_tasks:
        _assert_required_task_sections(task.text, task.path.name)
        for label in ["Status: required_update", "Status: reviewed_no_change", "Status: not_applicable"]:
            if label in task.text:
                break
        else:
            raise AssertionError(
                f"{task.path.name} must use explicit impact-status values in its maintenance sections."
            )

        matching_logs = find_matching_logs(task.task_id, REPO_ROOT)
        assert matching_logs, f"{task.path.name} must have a matching development log."

        combined_log_text = "\n".join(path.read_text(encoding="utf-8") for path in matching_logs)
        assert "Commands and tests run:" in combined_log_text, (
            f"Logs for {task.path.name} must record commands and tests run."
        )
        assert "Result:" in combined_log_text, f"Logs for {task.path.name} must record a result."
        assert "Next step:" in combined_log_text, f"Logs for {task.path.name} must record the next step."

        lowered = combined_log_text.lower()
        surface_terms = ["docs", "documentation", "notes", "checklist", "test"]
        if not any(term in lowered for term in surface_terms):
            emit_warning(
                "FEATURE_SYNC_WARN_001",
                f"Logs for {task.path.name} record work and commands but do not obviously mention doc/note/checklist/test sync.",
            )


def test_feature_delivery_logs_warn_when_stop_points_are_too_sparse() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    active_stage = get_active_stage(REPO_ROOT)
    if active_stage not in {"feature_delivery_ready", "bounded_verified", "e2e_ready", "flow_complete", "release_ready"}:
        return

    sparse_logs: list[str] = []
    for task in parse_task_docs(REPO_ROOT):
        matches = find_matching_logs(task.task_id, REPO_ROOT)
        if not matches:
            continue
        combined_text = "\n".join(path.read_text(encoding="utf-8") for path in matches)
        result_match = re.search(r"Result:\s*(.+)", combined_text)
        next_step_match = re.search(r"Next step:\s*(.+)", combined_text)
        if result_match and len(result_match.group(1).strip()) < 40:
            sparse_logs.append(task.path.name)
            continue
        if next_step_match and len(next_step_match.group(1).strip()) < 30:
            sparse_logs.append(task.path.name)

    if sparse_logs:
        emit_warning(
            "FEATURE_SYNC_WARN_002",
            "Some feature-delivery stop points are unusually terse and may be hard to reconstruct later: "
            + ", ".join(sorted(set(sparse_logs))),
        )

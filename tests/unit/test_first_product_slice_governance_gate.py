import re
from pathlib import Path

from doc_validation_helpers import (
    LATE_STAGE_NAMES,
    REPO_ROOT,
    emit_warning,
    feature_has_flow_coverage,
    find_matching_logs,
    get_active_stage,
    get_real_product_rows,
    get_repo_state,
    get_template_example_rows,
    parse_checklist_docs,
    parse_task_docs,
    require_no_placeholder_phrases,
)


def test_template_state_or_real_product_state_is_unambiguous() -> None:
    repo_state = get_repo_state(REPO_ROOT)

    if repo_state == "template_only":
        assert get_template_example_rows(REPO_ROOT), "Template-only state should still include starter example feature rows."
        return

    assert get_real_product_rows(REPO_ROOT), "Non-template repositories must have at least one real product feature row."


def test_real_product_features_require_real_checklists_and_flow_coverage() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    real_rows = get_real_product_rows(REPO_ROOT)
    checklists = parse_checklist_docs(REPO_ROOT)
    checklist_ids = [checklist.feature_id for checklist in checklists if checklist.feature_id]

    for row in real_rows:
        assert row.checklist not in {"", "planned", "not_applicable"}, (
            f"Real product feature {row.feature_id} must cite a real checklist path instead of {row.checklist!r}."
        )
        assert checklist_ids.count(row.feature_id) == 1, (
            f"Real product feature {row.feature_id} must have exactly one checklist file with a matching feature ID."
        )
        assert feature_has_flow_coverage(row.feature_id, REPO_ROOT), (
            f"Real product feature {row.feature_id} must be covered by at least one relevant flow."
        )
        assert row.bounded_proof.strip(), f"Real product feature {row.feature_id} must name a bounded proof target."
        assert row.real_e2e_target.strip(), f"Real product feature {row.feature_id} must name a real E2E target."

    for checklist in checklists:
        require_no_placeholder_phrases(checklist.text, str(checklist.path.relative_to(REPO_ROOT)))
        assert "E2E asset" in checklist.text, f"{checklist.path.name} must record an explicit E2E asset field."
        assert "last E2E command run" in checklist.text, f"{checklist.path.name} must record the last E2E command run."
        assert "last E2E result" in checklist.text, f"{checklist.path.name} must record the last E2E result."


def test_active_tasks_require_matching_logs_once_real_product_work_exists() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    tasks = parse_task_docs(REPO_ROOT)
    assert tasks, "Real product repositories should have task plans."

    for task in tasks:
        matches = find_matching_logs(task.task_id, REPO_ROOT)
        assert matches, f"Task plan {task.path.name} must have a matching development log entry."


def test_setup_entry_requires_product_definition_evidence_proportionate_to_complexity() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    active_stage = get_active_stage(REPO_ROOT)
    real_rows = get_real_product_rows(REPO_ROOT)
    if active_stage not in LATE_STAGE_NAMES or len(real_rows) < 3:
        return

    tasks = parse_task_docs(REPO_ROOT)
    product_definition_tasks = [
        task
        for task in tasks
        if "product definition" in task.text.lower() or "product_definition" in task.path.stem
    ]
    covering_tasks = [
        task for task in product_definition_tasks if any(row.feature_id in task.text for row in real_rows)
    ]

    assert covering_tasks, (
        "Entering setup or later with a nontrivial product requires at least one product-definition task "
        "that names real feature IDs explicitly."
    )

    all_feature_ids = {row.feature_id for row in real_rows}
    covered_feature_ids = {
        row.feature_id for row in real_rows for task in covering_tasks if row.feature_id in task.text
    }

    assert covered_feature_ids == all_feature_ids, (
        "Product-definition task coverage is too thin for setup-or-later work: not every real feature ID is named "
        "in the surviving product-definition task surface."
    )

    if len(covering_tasks) == 1:
        emit_warning(
            "SETUP_ENTRY_WARN_001",
            "A nontrivial product is entering setup or later with only one product-definition task carrying the full "
            "feature decomposition. This can be valid, but it is unusually coarse and should be reviewed.",
        )


def test_setup_or_later_warns_when_docs_are_present_but_skeletal() -> None:
    if get_repo_state(REPO_ROOT) == "template_only":
        return

    active_stage = get_active_stage(REPO_ROOT)
    if active_stage not in LATE_STAGE_NAMES:
        return

    doc_paths = [
        REPO_ROOT / "docs" / "README.md",
        REPO_ROOT / "docs" / "user" / "README.md",
        REPO_ROOT / "docs" / "operator" / "README.md",
        REPO_ROOT / "docs" / "reference" / "README.md",
        REPO_ROOT / "docs" / "runbooks" / "README.md",
    ]

    skeletal_docs: list[Path] = []
    for path in doc_paths:
        text = path.read_text(encoding="utf-8")
        content_lines = [
            line
            for line in text.splitlines()
            if line.strip() and not line.strip().startswith("#") and not re.fullmatch(r"[-*]\s*", line.strip())
        ]
        if len(content_lines) < 3:
            skeletal_docs.append(path)

    if skeletal_docs:
        emit_warning(
            "DOC_WARN_001",
            "Some required docs surfaces are still skeletal for a setup-or-later repository: "
            + ", ".join(path.relative_to(REPO_ROOT).as_posix() for path in skeletal_docs),
        )

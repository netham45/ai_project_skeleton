"""
Bounded document-consistency checks for the rule that user-requested product features
must be decomposed and linked to flows, checklists, documentation, and proof targets.
"""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_original_concept_note_requires_feature_decomposition_follow_on() -> None:
    text = (REPO_ROOT / "notes" / "explorations" / "original_concept.md").read_text(encoding="utf-8")

    assert "## Candidate User-Visible Capabilities" in text
    assert "## Required Follow-On" in text
    assert "Freeform concept text is not a substitute" in text


def test_major_feature_inventory_defines_product_feature_traceability_fields() -> None:
    text = (REPO_ROOT / "notes" / "catalogs" / "inventory" / "major_feature_inventory.md").read_text(
        encoding="utf-8"
    )

    assert "Feature kind" in text
    assert "Source vision reference" in text
    assert "Checklist" in text
    assert "Bounded proof" in text
    assert "Real E2E target" in text
    assert "Every product-feature row must include:" in text
    assert "PF01 | product_example | Example user-requested capability" in text


def test_flow_inventory_requires_feature_coverage_fields() -> None:
    text = (REPO_ROOT / "notes" / "catalogs" / "traceability" / "relevant_user_flow_inventory.yaml").read_text(
        encoding="utf-8"
    )

    assert "invariants:" in text
    assert "covers_feature_ids" in text
    assert "source_vision_refs" in text
    assert "every product feature must be covered by at least one relevant flow" in text
    assert "FLOW10" in text


def test_feature_checklist_standard_requires_user_request_traceability() -> None:
    text = (REPO_ROOT / "notes" / "catalogs" / "checklists" / "feature_checklist_standard.md").read_text(
        encoding="utf-8"
    )

    assert "## Required Traceability Fields" in text
    assert "source vision reference" in text
    assert "governing flow IDs" in text
    assert "real E2E command or explicit not-applicable reason" in text
    assert "The checklist must preserve the linkage from user request to feature to flow to proof." in text

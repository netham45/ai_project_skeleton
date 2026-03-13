from __future__ import annotations

import hashlib
import json
import re
import warnings
from dataclasses import dataclass
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]

LATE_STAGE_NAMES = {
    "setup_bootstrapped",
    "feature_delivery_ready",
    "bounded_verified",
    "e2e_ready",
    "flow_complete",
    "release_ready",
}

BANNED_PLACEHOLDER_PHRASES = (
    "example per-feature checklist",
    "replace this file",
    "placeholder",
    "once the product feature is known",
)


@dataclass(frozen=True)
class FeatureRow:
    feature_id: str
    feature_kind: str
    name: str
    status: str
    source_vision_reference: str
    governing_flows: str
    feature_definition: str
    checklist: str
    bounded_proof: str
    real_e2e_target: str


@dataclass(frozen=True)
class ChecklistDoc:
    path: Path
    feature_id: str
    text: str


@dataclass(frozen=True)
class TaskDoc:
    path: Path
    task_id: str
    text: str


@dataclass(frozen=True)
class FeatureDefinition:
    path: Path
    data: dict


@dataclass(frozen=True)
class FeatureSnapshot:
    path: Path
    data: dict


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _parse_markdown_table(text: str) -> list[dict[str, str]]:
    lines = [line.rstrip() for line in text.splitlines()]
    rows: list[dict[str, str]] = []
    header: list[str] | None = None
    collecting = False

    for line in lines:
        if not line.startswith("|"):
            if collecting and rows:
                break
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            collecting = True
            continue
        if set("".join(cells)) <= {"-", " "}:
            continue
        rows.append({header[index]: cells[index] for index in range(min(len(header), len(cells)))})

    return rows


def parse_feature_inventory(repo_root: Path = REPO_ROOT) -> list[FeatureRow]:
    text = read_text(repo_root / "notes" / "catalogs" / "inventory" / "major_feature_inventory.md")
    rows = _parse_markdown_table(text)
    result: list[FeatureRow] = []
    for row in rows:
        feature_id = row.get("Feature ID", "")
        if not feature_id:
            continue
        result.append(
            FeatureRow(
                feature_id=feature_id,
                feature_kind=row.get("Feature kind", ""),
                name=row.get("Name", ""),
                status=row.get("Status", ""),
                source_vision_reference=row.get("Source vision reference", ""),
                governing_flows=row.get("Governing flows", ""),
                feature_definition=row.get("Feature definition", ""),
                checklist=row.get("Checklist", ""),
                bounded_proof=row.get("Bounded proof", ""),
                real_e2e_target=row.get("Real E2E target", ""),
            )
        )
    return result


def get_real_product_rows(repo_root: Path = REPO_ROOT) -> list[FeatureRow]:
    return [
        row
        for row in parse_feature_inventory(repo_root)
        if row.feature_id.startswith("PF") and row.feature_kind != "product_example"
    ]


def get_template_example_rows(repo_root: Path = REPO_ROOT) -> list[FeatureRow]:
    return [
        row
        for row in parse_feature_inventory(repo_root)
        if row.feature_id.startswith("PF") and row.feature_kind == "product_example"
    ]


def get_active_stage(repo_root: Path = REPO_ROOT) -> str:
    text = read_text(repo_root / "plan" / "checklists" / "00_project_operational_state.md")
    match = re.search(r"Active stage: `([^`]+)`", text)
    assert match, "Operational-state checklist must name the active stage."
    return match.group(1)


def get_repo_state(repo_root: Path = REPO_ROOT) -> str:
    real_product_rows = get_real_product_rows(repo_root)
    if not real_product_rows:
        return "template_only"
    active_stage = get_active_stage(repo_root)
    if active_stage in LATE_STAGE_NAMES:
        return "implementation_started"
    return "product_defined"


def parse_checklist_docs(repo_root: Path = REPO_ROOT) -> list[ChecklistDoc]:
    result: list[ChecklistDoc] = []
    for path in sorted((repo_root / "plan" / "checklists").glob("PF*.md")):
        if path.name == "README.md":
            continue
        text = read_text(path)
        match = re.search(r"Feature ID:\s*`?(PF\d+)`?", text)
        feature_id = match.group(1) if match else ""
        result.append(ChecklistDoc(path=path, feature_id=feature_id, text=text))
    return result


def parse_task_docs(repo_root: Path = REPO_ROOT) -> list[TaskDoc]:
    result: list[TaskDoc] = []
    for path in sorted((repo_root / "plan" / "tasks").glob("*.md")):
        if path.name == "README.md":
            continue
        text = read_text(path)
        task_id = re.sub(r"^\d{4}-\d{2}-\d{2}_", "", path.stem)
        result.append(TaskDoc(path=path, task_id=task_id, text=text))
    return result


def parse_log_texts(repo_root: Path = REPO_ROOT) -> list[tuple[Path, str]]:
    result: list[tuple[Path, str]] = []
    for path in sorted((repo_root / "notes" / "logs").glob("*/*.md")):
        if path.name == "README.md":
            continue
        result.append((path, read_text(path)))
    return result


def find_matching_logs(task_id: str, repo_root: Path = REPO_ROOT) -> list[Path]:
    matches: list[Path] = []
    pattern = re.compile(rf"Task ID:\s*`?{re.escape(task_id)}`?")
    for path, text in parse_log_texts(repo_root):
        if pattern.search(text):
            matches.append(path)
    return matches


def parse_flow_blocks(repo_root: Path = REPO_ROOT) -> list[str]:
    text = read_text(repo_root / "notes" / "catalogs" / "traceability" / "relevant_user_flow_inventory.yaml")
    blocks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if re.match(r"^\s*- flow_id:", line):
            if current:
                blocks.append("\n".join(current))
            current = [line]
            continue
        if current:
            current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def feature_has_flow_coverage(feature_id: str, repo_root: Path = REPO_ROOT) -> bool:
    for block in parse_flow_blocks(repo_root):
        if re.search(rf"^\s+-\s+{re.escape(feature_id)}\s*$", block, re.MULTILINE):
            return True
    return False


def emit_warning(rule_id: str, message: str) -> None:
    warnings.warn(f"{rule_id}: {message}", UserWarning, stacklevel=2)


def require_no_placeholder_phrases(text: str, context: str) -> None:
    lowered = text.lower()
    for phrase in BANNED_PLACEHOLDER_PHRASES:
        assert phrase not in lowered, f"{context} still contains template placeholder phrase: {phrase!r}"


def iter_feature_definition_docs(repo_root: Path = REPO_ROOT) -> list[FeatureDefinition]:
    result: list[FeatureDefinition] = []
    for path in sorted((repo_root / "plan" / "features").glob("PF*.yaml")):
        data = yaml.safe_load(read_text(path))
        assert isinstance(data, dict), f"{path.name} must parse to a mapping."
        result.append(FeatureDefinition(path=path, data=data))
    return result


def load_feature_definition(path: Path) -> FeatureDefinition:
    data = yaml.safe_load(read_text(path))
    assert isinstance(data, dict), f"{path.name} must parse to a mapping."
    return FeatureDefinition(path=path, data=data)


def load_feature_snapshot(path: Path) -> FeatureSnapshot:
    data = json.loads(read_text(path))
    assert isinstance(data, dict), f"{path.name} must parse to an object."
    return FeatureSnapshot(path=path, data=data)


def compute_hash_for_relative_path(relative_path: str, repo_root: Path = REPO_ROOT) -> str:
    path = repo_root / relative_path
    if not path.exists():
        return "missing"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def collect_feature_paths(definition: FeatureDefinition) -> list[str]:
    governed_files = definition.data.get("governed_files", {})
    collected: list[str] = []

    for surface in governed_files.values():
        if not isinstance(surface, dict):
            continue
        for value in surface.values():
            if isinstance(value, list):
                collected.extend(item for item in value if isinstance(item, str))

    proof = definition.data.get("proof", {})
    e2e_asset = proof.get("e2e_asset")
    if isinstance(e2e_asset, str):
        collected.append(e2e_asset)

    snapshot = definition.data.get("snapshot", {})
    baseline_file = snapshot.get("baseline_file")
    if isinstance(baseline_file, str):
        pass

    seen: set[str] = set()
    ordered: list[str] = []
    for item in collected:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return ordered


def compare_feature_snapshot(definition: FeatureDefinition, snapshot: FeatureSnapshot, repo_root: Path = REPO_ROOT) -> dict[str, list[str]]:
    snapshot_files = snapshot.data.get("files", {})
    assert isinstance(snapshot_files, dict), f"{snapshot.path.name} must contain a files object."

    report = {"created": [], "modified": [], "deleted": [], "unchanged": []}
    for relative_path in sorted(snapshot_files):
        previous_hash = snapshot_files[relative_path]
        current_hash = compute_hash_for_relative_path(relative_path, repo_root)
        if previous_hash == "missing" and current_hash != "missing":
            report["created"].append(relative_path)
        elif previous_hash != "missing" and current_hash == "missing":
            report["deleted"].append(relative_path)
        elif previous_hash == current_hash:
            report["unchanged"].append(relative_path)
        else:
            report["modified"].append(relative_path)
    return report

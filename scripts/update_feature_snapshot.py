#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]


def _compute_hash(relative_path: str) -> str:
    path = REPO_ROOT / relative_path
    if not path.exists():
        return "missing"
    import hashlib

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def _load_definition(feature_id: str) -> tuple[Path, dict]:
    for path in sorted((REPO_ROOT / "plan" / "features").glob("PF*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("feature_id") == feature_id:
            return path, data
    raise SystemExit(f"Unknown feature id: {feature_id}")


def _collect_paths(data: dict) -> list[str]:
    governed_files = data.get("governed_files", {})
    collected: list[str] = []
    for surface in governed_files.values():
        if not isinstance(surface, dict):
            continue
        for value in surface.values():
            if isinstance(value, list):
                collected.extend(item for item in value if isinstance(item, str))
    proof = data.get("proof", {})
    if isinstance(proof.get("e2e_asset"), str):
        collected.append(proof["e2e_asset"])
    return sorted(dict.fromkeys(collected))


def _run_verification(feature_id: str) -> None:
    commands = [
        [sys.executable, "-m", "pytest", "tests/unit/test_feature_definition_docs.py", "-q"],
        [sys.executable, "-m", "pytest", "tests/unit/test_feature_completion_snapshot.py", "-q"],
    ]
    for command in commands:
        completed = subprocess.run(command, cwd=REPO_ROOT)
        if completed.returncode != 0:
            raise SystemExit(
                f"Refusing to update snapshot for {feature_id}: verification failed for {' '.join(command)}"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature", required=True, help="Feature ID such as PF01")
    args = parser.parse_args()

    definition_path, data = _load_definition(args.feature)
    _run_verification(args.feature)

    snapshot_path = REPO_ROOT / data["snapshot"]["baseline_file"]
    snapshot_payload = {
        "feature_id": data["feature_id"],
        "snapshot_id": datetime.now(timezone.utc).isoformat(),
        "based_on_definition": definition_path.relative_to(REPO_ROOT).as_posix(),
        "files": {path: _compute_hash(path) for path in _collect_paths(data)},
    }
    snapshot_path.write_text(json.dumps(snapshot_payload, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

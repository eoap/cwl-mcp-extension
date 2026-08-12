#!/usr/bin/env python3
"""Validate CWL documents plus repository-level cwlmcp:Tool conventions."""

from __future__ import annotations

import argparse
import sys
from io import StringIO
from pathlib import Path
from typing import Any

from cwltool.main import main as cwltool_main
from ruamel.yaml import YAML

ALLOWED_MCP_TOOL_FIELDS = {
    "name": (str, type(None)),
    "title": (str, type(None)),
    "description": (str, type(None)),
    "aliases": list,
    "useWhen": (str, type(None)),
    "doNotUseWhen": (str, type(None)),
    "annotations": (dict, type(None)),
}

ALLOWED_ANNOTATION_FIELDS = {
    "title": (str, type(None)),
    "readOnlyHint": (bool, type(None)),
    "destructiveHint": (bool, type(None)),
    "idempotentHint": (bool, type(None)),
    "openWorldHint": (bool, type(None)),
}

PROCESS_CLASSES = {"Workflow", "CommandLineTool", "ExpressionTool"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate CWL files with cwltool and check cwlmcp:Tool metadata."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="CWL files to validate. Defaults to examples/*.cwl.",
    )
    return parser.parse_args()


def default_paths() -> list[Path]:
    return sorted(Path("examples").glob("*.cwl"))


def run_cwltool_validate(path: Path) -> list[str]:
    stdout = StringIO()
    stderr = StringIO()
    result = cwltool_main(
        argsl=["--validate", "--non-strict", str(path)],
        stdin=StringIO(""),
        stdout=stdout,
        stderr=stderr,
    )
    if result == 0:
        return []
    details = stderr.getvalue().strip() or stdout.getvalue().strip()
    return [f"{path}: cwltool validation failed\n{details or 'cwltool validation failed'}"]


def load_yaml(path: Path) -> Any:
    yaml = YAML(typ="safe")
    with path.open("r", encoding="utf-8") as stream:
        return yaml.load(stream)


def iter_processes(document: Any) -> list[dict[str, Any]]:
    if isinstance(document, dict):
        if document.get("class") in PROCESS_CLASSES:
            return [document]
        graph = document.get("$graph")
        if isinstance(graph, list):
            return [
                item
                for item in graph
                if isinstance(item, dict) and item.get("class") in PROCESS_CLASSES
            ]
    if isinstance(document, list):
        return [
            item
            for item in document
            if isinstance(item, dict) and item.get("class") in PROCESS_CLASSES
        ]
    return []


def extract_mcp_tool(hints: Any) -> Any:
    if isinstance(hints, dict):
        return hints.get("cwlmcp:Tool")
    if isinstance(hints, list):
        for item in hints:
            if isinstance(item, dict) and "cwlmcp:Tool" in item:
                return item["cwlmcp:Tool"]
    return None


def validate_aliases(value: Any, prefix: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        return [f"{prefix}.aliases must be an array of strings"]
    errors: list[str] = []
    for index, alias in enumerate(value):
        if not isinstance(alias, str):
            errors.append(f"{prefix}.aliases[{index}] must be a string")
    return errors


def validate_annotations(value: Any, prefix: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, dict):
        return [f"{prefix}.annotations must be an object"]
    errors: list[str] = []
    for key in value:
        if key not in ALLOWED_ANNOTATION_FIELDS:
            errors.append(f"{prefix}.annotations contains unknown field '{key}'")
    for key, allowed_types in ALLOWED_ANNOTATION_FIELDS.items():
        if key in value and not isinstance(value[key], allowed_types):
            if key == "title":
                errors.append(f"{prefix}.annotations.title must be string or null")
            else:
                errors.append(f"{prefix}.annotations.{key} must be boolean or null")
    return errors


def validate_mcp_tool(value: Any, prefix: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    for forbidden in ("inputs", "outputs"):
        if forbidden in value:
            errors.append(
                f"{prefix} must not duplicate CWL {forbidden} definitions"
            )

    for key in value:
        if key not in ALLOWED_MCP_TOOL_FIELDS and key not in {"inputs", "outputs"}:
            errors.append(f"{prefix} contains unknown field '{key}'")

    for key, allowed_types in ALLOWED_MCP_TOOL_FIELDS.items():
        if key not in value:
            continue
        if key == "aliases":
            errors.extend(validate_aliases(value[key], prefix))
            continue
        if key == "annotations":
            errors.extend(validate_annotations(value[key], prefix))
            continue
        if not isinstance(value[key], allowed_types):
            errors.append(f"{prefix}.{key} has the wrong type")

    return errors


def validate_extension_metadata(path: Path) -> list[str]:
    document = load_yaml(path)
    processes = iter_processes(document)
    if not processes:
        return [f"{path}: no CWL process found"]

    errors: list[str] = []
    for process in processes:
        process_id = process.get("id", "<anonymous>")
        mcp_tool = extract_mcp_tool(process.get("hints"))
        if mcp_tool is None:
            continue
        prefix = f"{path} [{process_id}] cwlmcp:Tool"
        errors.extend(validate_mcp_tool(mcp_tool, prefix))
    return errors


def main() -> int:
    args = parse_args()
    paths = [Path(path) for path in args.paths] if args.paths else default_paths()
    if not paths:
        print("No CWL files found to validate.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for path in paths:
        all_errors.extend(run_cwltool_validate(path))
        all_errors.extend(validate_extension_metadata(path))

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    for path in paths:
        print(f"validated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

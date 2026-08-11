# CWL MCP Extension Specification

## Overview

This extension introduces two records:

- `mcp:Tool`
- `mcp:ToolAnnotations`

These records are intended for use in CWL metadata, typically under `hints`, to provide agent-facing guidance for deriving an MCP Tool from a CWL `Process`.

## Canonical Schema

The canonical schema entrypoint is `schema/mcp-extension.yml`.

Implementations should load that file rather than importing individual record files directly.

## Normative Constraints

- Standard CWL remains authoritative for process execution and structural semantics.
- `mcp:Tool` must not duplicate CWL inputs or outputs.
- `mcp:ToolAnnotations` values are hints only.
- `aliases` may be preserved as extension metadata but are not a standard top-level MCP Tool field.

## Recommended Derivation Rules

### Name

Precedence:

1. `mcp:Tool.name`
2. normalized CWL `id`

### Title

Precedence:

1. `mcp:Tool.title`
2. CWL `label`
3. normalized CWL `id`

### Description

Precedence:

1. `mcp:Tool.description`
2. composed text from CWL `doc`, `useWhen`, and `doNotUseWhen`

### Annotations

If present, `mcp:Tool.annotations` should map mechanically into MCP Tool annotations without reinterpretation.

## Validation With `cwltool`

For this repository, `cwltool` is used to validate the underlying CWL document,
while `scripts/validate_with_mcp_schema.py` adds repository-level checks for the
`mcp:Tool` metadata structure.

This keeps standard CWL validation delegated to `cwltool` and leaves the MCP
extension constraints explicit and easy to evolve within this repository.

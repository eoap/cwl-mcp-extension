# CWL MCP Extension Specification

## Overview

This extension introduces two records:

- `mcp:Tool`
- `mcp:ToolAnnotations`

These records are intended for use in CWL metadata, typically under `hints`, to provide agent-facing guidance for deriving an MCP Tool from a CWL `Process`.

## Related MCP References

This extension is intended to map onto the MCP Tool model documented in the official Model Context Protocol specification dated July 28, 2026:

- MCP specification: <https://modelcontextprotocol.io/specification/2026-07-28>
- MCP Tools section: <https://modelcontextprotocol.io/specification/2026-07-28/server/tools>

For non-normative background on the intent and limits of MCP tool annotations, see:

- Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do: <https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/>

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

The aligned MCP 2026-07-28 annotation fields are:

- `title`
- `readOnlyHint`
- `destructiveHint`
- `idempotentHint`
- `openWorldHint`

The MCP defaults are intentionally conservative when these hints are absent:

- `readOnlyHint`: `false`
- `destructiveHint`: `true`
- `idempotentHint`: `false`
- `openWorldHint`: `true`

## Validation With `cwltool`

For this repository, `cwltool` is used to validate the underlying CWL document,
while `scripts/validate_with_mcp_schema.py` adds repository-level checks for the
`mcp:Tool` metadata structure.

This keeps standard CWL validation delegated to `cwltool` and leaves the MCP
extension constraints explicit and easy to evolve within this repository.

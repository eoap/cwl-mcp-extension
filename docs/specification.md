# CWL MCP Extension Specification

## Overview

This extension introduces two records:

- `cwlmcp:Tool`
- `cwlmcp:ToolAnnotations`

These records are intended for use in CWL metadata, typically under `hints`, to provide agent-facing guidance for deriving an MCP Tool from a CWL `Process`.

## Namespace

The canonical namespace URI for this extension is `https://eoap.github.io/cwl-mcp-extension#`.

- `cwlmcp` is the recommended prefix.
- Prefixes are aliases; the namespace URI is the actual identifier.
- EOAP hosts the namespace because EOAP currently maintains this extension.
- The project intentionally does not claim an unregistered `w3id.org` namespace at this stage.
- A neutral persistent identifier such as `w3id.org` may be considered later if the extension becomes community-maintained or moves toward standardization.

## Related MCP References

This extension is intended to map onto the MCP Tool model documented in the official Model Context Protocol specification dated July 28, 2026:

- MCP specification: <https://modelcontextprotocol.io/specification/2026-07-28>
- MCP Tools section: <https://modelcontextprotocol.io/specification/2026-07-28/server/tools>

For non-normative background on the intent and limits of MCP tool annotations, see:

- Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do: <https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/>

## Canonical Schema

The canonical schema entrypoint is `schema/cwlmcp-extension.yml`.

Implementations should load that file rather than importing individual record files directly.

## Normative Constraints

- Standard CWL remains authoritative for process execution and structural semantics.
- `cwlmcp:Tool` must not duplicate CWL inputs or outputs.
- `cwlmcp:ToolAnnotations` values are hints only.
- `aliases` may be preserved as extension metadata but are not a standard top-level MCP Tool field.

## Recommended Derivation Rules

### Name

Precedence:

1. `cwlmcp:Tool.name`
2. normalized CWL `id`

### Title

Precedence:

1. `cwlmcp:Tool.title`
2. CWL `label`
3. normalized CWL `id`

### Description

Precedence:

1. `cwlmcp:Tool.description`
2. composed text from CWL `doc`, `useWhen`, and `doNotUseWhen`

### Annotations

If present, `cwlmcp:Tool.annotations` should map mechanically into MCP Tool annotations without reinterpretation.

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
`cwlmcp:Tool` metadata structure.

This keeps standard CWL validation delegated to `cwltool` and leaves the MCP
extension constraints explicit and easy to evolve within this repository.

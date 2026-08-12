# Authoring Guide

## Minimal Pattern

Attach `cwlmcp:Tool` metadata under `hints`:

```yaml
$namespaces:
  cwlmcp: https://eoap.github.io/cwl-mcp-extension#

hints:
  cwlmcp:Tool:
    annotations:
      readOnlyHint: true
```

## Authoring Tips

- Set `name` only when the default normalized CWL `id` is not good enough.
- Reuse CWL `label` and `doc` unless you need MCP-specific presentation text.
- Keep `useWhen` and `doNotUseWhen` concise and action-oriented.
- Treat `aliases` as discovery aids, not as alternate identifiers.
- Avoid restating CWL `inputs` or `outputs` inside `cwlmcp:Tool`.

## Example

```yaml
$namespaces:
  cwlmcp: https://eoap.github.io/cwl-mcp-extension#

hints:
  cwlmcp:Tool:
    name: buffer_geometry
    aliases:
      - buffer a geometry
      - expand an area of interest
    useWhen: |
      Use when the user needs to expand a point or polygon into a buffered area.
    doNotUseWhen: |
      Do not use when exact geometry preservation is required.
    annotations:
      readOnlyHint: true
      destructiveHint: false
      idempotentHint: true
      openWorldHint: false
```

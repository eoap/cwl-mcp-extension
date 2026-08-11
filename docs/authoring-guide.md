# Authoring Guide

## Minimal Pattern

Attach `mcp:Tool` metadata under `hints`:

```yaml
hints:
  mcp:Tool:
    annotations:
      readOnlyHint: true
```

## Authoring Tips

- Set `name` only when the default normalized CWL `id` is not good enough.
- Reuse CWL `label` and `doc` unless you need MCP-specific presentation text.
- Keep `useWhen` and `doNotUseWhen` concise and action-oriented.
- Treat `aliases` as discovery aids, not as alternate identifiers.
- Avoid restating CWL `inputs` or `outputs` inside `mcp:Tool`.

## Example

```yaml
hints:
  mcp:Tool:
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

# CWL MCP Extension

`cwl-mcp-extension` defines a small CWL extension for attaching MCP tool metadata to a CWL `Process` without duplicating standard CWL execution semantics.

This repository is a work in progress. Contributions, feedback, and discussion are welcome.

## Scope

The extension introduces two records:

- `cwlmcp:Tool`
- `cwlmcp:ToolAnnotations`

These records are intended for use in CWL metadata, typically under `hints`, to provide agent-facing guidance for deriving an MCP Tool from a CWL `Process`.

## Namespace

The canonical namespace URI for this extension is `https://eoap.github.io/cwl-mcp-extension#`.

- `cwlmcp` is the recommended prefix.
- Prefixes are aliases; the namespace URI is the actual identifier.
- EOAP currently hosts the namespace because EOAP maintains this extension.
- The project intentionally does not claim an unregistered `w3id.org` namespace at this stage.
- A neutral persistent namespace may be adopted later if the extension moves toward broader CWL community standardization.

## Canonical Example

```yaml
cwlVersion: v1.2
class: Workflow

$namespaces:
  cwlmcp: https://eoap.github.io/cwl-mcp-extension#

hints:
  cwlmcp:Tool:
    annotations:
      readOnlyHint: false
      destructiveHint: false
      idempotentHint: false
      openWorldHint: true
```

## References

- MCP specification (2026-07-28): <https://modelcontextprotocol.io/specification/2026-07-28>
- MCP Tools section: <https://modelcontextprotocol.io/specification/2026-07-28/server/tools>
- Tool annotations background: <https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/>

## Next Reading

- [Specification](specification.md)
- [CWL to MCP Crosswalk](crosswalk-cwl-mcp.md)
- [Authoring Guide](authoring-guide.md)
- [Design Principles](design-principles.md)

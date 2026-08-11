# CWL to MCP Crosswalk

| CWL source | Extension role | MCP target |
| --- | --- | --- |
| `id` | default tool identity | `name` |
| `label` | default presentation title | `title` |
| `doc` | base descriptive text | `description` |
| `inputs` | authoritative input model | `inputSchema` |
| `outputs` | authoritative output model | `outputSchema` |
| `mcp:Tool.name` | explicit override | `name` |
| `mcp:Tool.title` | explicit override | `title` |
| `mcp:Tool.description` | explicit override | `description` |
| `mcp:Tool.useWhen` | usage guidance | composed into `description` or metadata |
| `mcp:Tool.doNotUseWhen` | avoidance guidance | composed into `description` or metadata |
| `mcp:Tool.aliases` | discovery metadata | `_meta` or generator-only data |
| `mcp:Tool.annotations.title` | display fallback hint | `annotations.title` |
| `mcp:Tool.annotations.*` | direct hint mapping | `annotations.*` |

## Notes

- The extension is additive, not substitutive.
- CWL remains the source of truth for input/output typing.
- MCP display precedence is `title`, then `annotations.title`, then `name`.
- Generators may keep richer provenance metadata than is emitted into the MCP Tool object.

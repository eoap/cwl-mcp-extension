# CWL to MCP Crosswalk

| CWL source | Extension role | MCP target |
| --- | --- | --- |
| `id` | default tool identity | `name` |
| `label` | default presentation title | `title` |
| `doc` | base descriptive text | `description` |
| `inputs` | authoritative input model | `inputSchema` |
| `outputs` | authoritative output model | `outputSchema` |
| `cwlmcp:Tool.name` | explicit override | `name` |
| `cwlmcp:Tool.title` | explicit override | `title` |
| `cwlmcp:Tool.description` | explicit override | `description` |
| `cwlmcp:Tool.useWhen` | usage guidance | composed into `description` or metadata |
| `cwlmcp:Tool.doNotUseWhen` | avoidance guidance | composed into `description` or metadata |
| `cwlmcp:Tool.aliases` | discovery metadata | `_meta` or generator-only data |
| `cwlmcp:Tool.annotations.title` | display fallback hint | `annotations.title` |
| `cwlmcp:Tool.annotations.*` | direct hint mapping | `annotations.*` |

## Notes

- The extension is additive, not substitutive.
- CWL remains the source of truth for input/output typing.
- MCP display precedence is `title`, then `annotations.title`, then `name`.
- Generators may keep richer provenance metadata than is emitted into the MCP Tool object.

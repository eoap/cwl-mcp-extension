# cwl-mcp-extension

`cwl-mcp-extension` defines a small CWL extension for attaching MCP tool metadata to a CWL `Process` without duplicating standard CWL execution semantics.

**This repository is a work in progress. Contributions, feedback, and discussion are welcome.**

The canonical schema entrypoint is [schema/mcp-extension.yml](schema/mcp-extension.yml). It aggregates the two records currently defined by the extension:

- `mcp:Tool`
- `mcp:ToolAnnotations`

This extension targets the MCP Tool model described in the official Model Context Protocol specification:

- MCP specification (2026-07-28): <https://modelcontextprotocol.io/specification/2026-07-28>
- MCP Tools section: <https://modelcontextprotocol.io/specification/2026-07-28/server/tools>
- Background on tool annotations: <https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/>

## Goals

- Keep standard CWL authoritative for execution, inputs, outputs, and workflow structure.
- Add only the agent-facing metadata needed to derive an MCP Tool.
- Make the extension easy to validate, document, and map into generated MCP JSON.

## Repository Layout

```text
cwl-mcp-extension/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── schema/
│   ├── mcp-tool.yml
│   ├── mcp-tool-annotations.yml
│   └── mcp-extension.yml
├── vocab/
│   ├── mcp.ttl
│   └── context.jsonld
├── docs/
│   ├── specification.md
│   ├── crosswalk-cwl-mcp.md
│   ├── authoring-guide.md
│   └── design-principles.md
├── examples/
│   ├── minimal-tool.cwl
│   ├── buffer.cwl
│   └── expected/
│       ├── minimal-tool.mcp.json
│       └── buffer.mcp.json
├── tests/
│   ├── valid/
│   ├── invalid/
│   └── expected/
└── fixtures/
    └── mcp-tool.schema.json
```

## Status

This repository currently provides:

- the extension schema draft
- vocabulary/context scaffolding
- specification and guidance documents
- example CWL documents and expected MCP projections
- seed validation fixtures and negative test cases

## Validation

Use the repository validation helper to run `cwltool` validation and check the
`mcp:Tool` metadata shape expected by this extension:

```bash
/home/fbrito/.local/share/hatch/env/virtual/cwl-mcp-extension/jLCmTDeX/cwl-mcp-extension/bin/python \
  scripts/validate_with_mcp_schema.py examples/*.cwl
```

The GitHub Actions workflow at `.github/workflows/validate-examples.yml` runs the
same validation in CI for the files under `examples/`.

The same workflow also validates `examples/expected/*.json` against the official
MCP `Tool` TypeScript schema for the 2026-07-28 specification revision.

## Scope

`mcp:Tool` is descriptive metadata only. It does not redefine CWL process behavior and it must not be interpreted as authorization or security policy.

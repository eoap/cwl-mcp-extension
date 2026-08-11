# cwl-mcp-extension

`cwl-mcp-extension` defines a small CWL extension for attaching MCP tool metadata to a CWL `Process` without duplicating standard CWL execution semantics.

The canonical schema entrypoint is [schema/mcp-extension.yml](/data/work/github/eoap/cwl-mcp-extension/schema/mcp-extension.yml). It aggregates the two records currently defined by the extension:

- `mcp:Tool`
- `mcp:ToolAnnotations`

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

## Scope

`mcp:Tool` is descriptive metadata only. It does not redefine CWL process behavior and it must not be interpreted as authorization or security policy.

# Design Principles

## Minimal Surface Area

The extension should remain intentionally small and should only model metadata that standard CWL does not already express.

## Clear Precedence

Explicit `mcp:Tool` values override derived values, but only for MCP-facing presentation and discovery behavior.

## No Semantic Duplication

Inputs, outputs, execution requirements, and workflow topology belong to CWL and should not be mirrored inside the extension.

## Safe Interpretation

Annotation fields are hints. They do not grant permission, replace policy, or guarantee runtime behavior.

## Canonical Aggregation

The extension should have one stable entrypoint so validators, generators, and downstream tooling can resolve the record set consistently.

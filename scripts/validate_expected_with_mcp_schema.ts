import bufferTool from "../examples/expected/buffer.mcp.json" with { type: "json" };
import minimalTool from "../examples/expected/minimal-tool.mcp.json" with { type: "json" };
import type { Tool } from "../vendor/modelcontextprotocol/2026-07-28/schema.js";

function requireObjectType<T extends "object">(value: T): T {
  return value;
}

function validateToolShape(
  tool: Omit<Tool, "inputSchema"> & { inputSchema: Record<string, unknown> },
): Tool {
  return {
    ...tool,
    inputSchema: {
      ...tool.inputSchema,
      type: requireObjectType(tool.inputSchema.type as "object"),
    },
  };
}

const tools: Tool[] = [
  validateToolShape(bufferTool),
  validateToolShape(minimalTool),
];

void tools;

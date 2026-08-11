import bufferTool from "../examples/expected/buffer.mcp.json";
import minimalTool from "../examples/expected/minimal-tool.mcp.json";
import type { Tool } from "../vendor/modelcontextprotocol/2026-07-28/schema";

const tools: Tool[] = [bufferTool, minimalTool];

void tools;

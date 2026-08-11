cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  mcp: https://w3id.org/terradue/mcp#

id: invalid_tool

hints:
  mcp:Tool:
    inputs:
      region:
        type: string

baseCommand: [echo]
inputs:
  region:
    type: string
outputs: {}

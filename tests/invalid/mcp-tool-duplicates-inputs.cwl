cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  mcp: https://eoap.github.io/cwl-mcp-extension#

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

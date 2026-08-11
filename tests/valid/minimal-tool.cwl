cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  mcp: https://w3id.org/terradue/mcp#

id: list_catalog

hints:
  mcp:Tool:
    name: list_catalog
    annotations:
      readOnlyHint: true

baseCommand: [echo]
inputs: {}
outputs: {}

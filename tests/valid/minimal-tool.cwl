cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  cwlmcp: https://eoap.github.io/cwl-mcp-extension#

id: list_catalog

hints:
  cwlmcp:Tool:
    name: list_catalog
    annotations:
      readOnlyHint: true

baseCommand: [echo]
inputs: {}
outputs: {}

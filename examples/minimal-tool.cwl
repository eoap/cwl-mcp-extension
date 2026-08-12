cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  cwlmcp: https://eoap.github.io/cwl-mcp-extension#

id: echo-region
label: Echo region identifier
doc: Returns the region identifier provided by the caller.

hints:
  cwlmcp:Tool:
    annotations:
      readOnlyHint: true
      destructiveHint: false
      idempotentHint: true
      openWorldHint: false

baseCommand: [bash, -lc]
arguments:
  - valueFrom: echo $(inputs.region)

inputs:
  region:
    type: string
    label: Region
    doc: Region identifier to echo.

outputs: {}

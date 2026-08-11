cwlVersion: v1.2
class: CommandLineTool

$namespaces:
  mcp: https://w3id.org/terradue/mcp#

id: echo-region
label: Echo region identifier
doc: Returns the region identifier provided by the caller.

hints:
  mcp:Tool:
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

cwlVersion: v1.2
class: Workflow

$namespaces:
  mcp: https://w3id.org/terradue/mcp#

id: buffer
label: Buffer
doc: |
  Create a buffered geometry from an input GeoJSON point or polygon.
  Use this workflow when an LLM needs to transform a point into an area of
  interest or expand an existing polygon before calling another spatial tool.
  The buffer distance is expressed in the same coordinate units as the input
  geometry.

hints:
  mcp:Tool:
    name: buffer_geometry
    aliases:
      - buffer a geometry
      - expand an area of interest
      - grow a polygon around a point
    useWhen: |
      Use when the user needs to expand a GeoJSON point or polygon into
      a buffered geometry for downstream spatial processing.
    doNotUseWhen: |
      Do not use when the user needs exact geometry preservation or expects
      the distance to be interpreted in meters for longitude and latitude
      coordinates.
    annotations:
      readOnlyHint: true
      destructiveHint: false
      idempotentHint: true
      openWorldHint: false

inputs:
  geometry:
    type: string
    label: Geometry To Buffer
    doc: |
      GeoJSON geometry to buffer. Use a point to create an area of interest
      around a location, or a polygon to expand an existing area.
  distance:
    type: float
    label: Buffer Distance
    doc: |
      Buffer distance expressed in the coordinate units of the input geometry.

outputs:
  geometry_buffered:
    type: string
    label: Buffered AOI Geometry
    doc: |
      Buffered geometry that can be passed to downstream spatial workflows.

steps: {}

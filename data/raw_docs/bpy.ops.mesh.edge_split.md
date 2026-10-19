# bpy.ops.mesh.edge_split

## Signature
```python
bpy.ops.mesh.edge_split(*, type='EDGE')Â
Description
Split selected edges so that each neighbor face gets its own copy
Parameters:
type (Literal['EDGE', 'VERT']) â Type, Method to use for splitting (optional)
EDGE
Faces by Edges â Split faces along selected edges.
VERT
Faces & Edges by Vertices â Split faces and edges connected to selected vertices.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

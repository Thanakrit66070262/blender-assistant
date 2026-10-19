# bpy.ops.mesh.edgering_select

## Signature
```python
bpy.ops.mesh.edgering_select(*, delimit_edge_ring={'NGONS'}, extend=False, deselect=False, toggle=False, object_index=-1, edge_index=-1, vert_index=-1, face_index=-1)Â
Description
Select an edge ring
Parameters:
delimit_edge_ring (set[Literal[Mesh Walk Delimit Edge Ring Items]]) â Edge Ring Delimit, Delimit edge ring selection (optional)
extend (bool) â Extend Select, Extend the selection (optional)
deselect (bool) â Deselect, Remove from the selection (optional)
toggle (bool) â Toggle Select, Toggle the selection (optional)
object_index (int) â (in [-1, inf], optional)
edge_index (int) â (in [-1, inf], optional)
vert_index (int) â (in [-1, inf], optional)
face_index (int) â (in [-1, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

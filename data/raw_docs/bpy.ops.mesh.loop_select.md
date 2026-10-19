# bpy.ops.mesh.loop_select

## Signature
```python
bpy.ops.mesh.loop_select(*, delimit_edge_loop={'NGONS', 'OUTER_CORNERS'}, delimit_face_loop=set(), extend=False, deselect=False, toggle=False, object_index=-1, edge_index=-1, vert_index=-1, face_index=-1)Â
Description
Select a loop of connected edges
Parameters:
delimit_edge_loop (set[Literal[Mesh Walk Delimit Edge Loop Items]]) â Delimit, Delimit edge loop selection (optional)
delimit_face_loop (set[Literal[Mesh Walk Delimit Face Loop Items]]) â Face Loop Delimit, Delimit face loop selection (optional)
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

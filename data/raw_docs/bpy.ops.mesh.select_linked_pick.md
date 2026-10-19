# bpy.ops.mesh.select_linked_pick

## Signature
```python
bpy.ops.mesh.select_linked_pick(*, deselect=False, delimit={'SEAM'}, object_index=-1, index=-1)Â
Description
(De)select all vertices linked to the edge under the mouse cursor
Parameters:
deselect (bool) â Deselect, (optional)
delimit (set[Literal[Mesh Delimit Mode Items]]) â Delimit, Delimit selected region (optional)
object_index (int) â (in [-1, inf], optional)
index (int) â (in [-1, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

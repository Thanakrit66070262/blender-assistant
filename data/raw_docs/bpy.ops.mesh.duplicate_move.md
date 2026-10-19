# bpy.ops.mesh.duplicate_move

## Signature
```python
bpy.ops.mesh.duplicate_move(*, MESH_OT_duplicate={}, TRANSFORM_OT_translate={})Â
Description
Duplicate mesh and move
Parameters:
MESH_OT_duplicate (dict[str, Any]) â Duplicate, Duplicate selected vertices, edges or faces (optional, bpy.ops.mesh.duplicate() keyword arguments)
TRANSFORM_OT_translate (dict[str, Any]) â Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

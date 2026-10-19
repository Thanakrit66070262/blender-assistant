# bpy.ops.mesh.rip_move

## Signature
```python
bpy.ops.mesh.rip_move(*, MESH_OT_rip={}, TRANSFORM_OT_translate={})Â
Description
Rip polygons and move the result
Parameters:
MESH_OT_rip (dict[str, Any]) â Rip, Disconnect vertices or edges from connected geometry (optional, bpy.ops.mesh.rip() keyword arguments)
TRANSFORM_OT_translate (dict[str, Any]) â Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.rip_edge_move

## Signature
```python
bpy.ops.mesh.rip_edge_move(*, MESH_OT_rip_edge={}, TRANSFORM_OT_translate={})Â
Description
Extend vertices and move the result
Parameters:
MESH_OT_rip_edge (dict[str, Any]) â Extend Vertices, Extend vertices along the edge closest to the cursor (optional, bpy.ops.mesh.rip_edge() keyword arguments)
TRANSFORM_OT_translate (dict[str, Any]) â Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

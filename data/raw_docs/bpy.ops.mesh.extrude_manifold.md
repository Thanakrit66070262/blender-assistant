# bpy.ops.mesh.extrude_manifold

## Signature
```python
bpy.ops.mesh.extrude_manifold(*, MESH_OT_extrude_region={}, TRANSFORM_OT_translate={})Â
Description
Extrude, dissolves edges whose faces form a flat surface and intersect new edges
Parameters:
MESH_OT_extrude_region (dict[str, Any]) â Extrude Region, Extrude region of faces (optional, bpy.ops.mesh.extrude_region() keyword arguments)
TRANSFORM_OT_translate (dict[str, Any]) â Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

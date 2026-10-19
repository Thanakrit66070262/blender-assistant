# bpy.ops.mesh.extrude_region_shrink_fatten

## Signature
```python
bpy.ops.mesh.extrude_region_shrink_fatten(*, MESH_OT_extrude_region={}, TRANSFORM_OT_shrink_fatten={})Â
Description
Extrude region together along local normals
Parameters:
MESH_OT_extrude_region (dict[str, Any]) â Extrude Region, Extrude region of faces (optional, bpy.ops.mesh.extrude_region() keyword arguments)
TRANSFORM_OT_shrink_fatten (dict[str, Any]) â Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, bpy.ops.transform.shrink_fatten() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.extrude_faces_move

## Signature
```python
bpy.ops.mesh.extrude_faces_move(*, MESH_OT_extrude_faces_indiv={}, TRANSFORM_OT_shrink_fatten={})Â
Description
Extrude each individual face separately along local normals
Parameters:
MESH_OT_extrude_faces_indiv (dict[str, Any]) â Extrude Individual Faces, Extrude individual faces only (optional, bpy.ops.mesh.extrude_faces_indiv() keyword arguments)
TRANSFORM_OT_shrink_fatten (dict[str, Any]) â Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, bpy.ops.transform.shrink_fatten() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

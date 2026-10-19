# bpy.ops.mesh.smooth_normals

## Signature
```python
bpy.ops.mesh.smooth_normals(*, factor=0.5)Â
Description
Smooth custom normals based on adjacent vertex normals
Parameters:
factor (float) â Factor, Specifies weight of smooth vs original normal (in [0, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

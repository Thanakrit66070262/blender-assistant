# bpy.ops.mesh.blend_from_shape

## Signature
```python
bpy.ops.mesh.blend_from_shape(*, shape='', blend=1.0, add=True)Â
Description
Blend in shape from a shape key
Parameters:
shape (str) â Shape, Shape key to use for blending (optional)
blend (float) â Blend, Blending factor (in [-1000, 1000], optional)
add (bool) â Add, Add rather than blend between shapes (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

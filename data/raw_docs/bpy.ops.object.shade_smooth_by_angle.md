# bpy.ops.object.shade_smooth_by_angle

## Signature
```python
bpy.ops.object.shade_smooth_by_angle(*, angle=0.523599, keep_sharp_edges=True)Â
Description
Set the sharpness of mesh edges based on the angle between the neighboring faces
Parameters:
angle (float) â Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
keep_sharp_edges (bool) â Keep Sharp Edges, Only add sharp edges instead of clearing existing tags first (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

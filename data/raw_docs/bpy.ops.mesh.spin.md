# bpy.ops.mesh.spin

## Signature
```python
bpy.ops.mesh.spin(*, steps=12, dupli=False, angle=1.5708, use_auto_merge=True, use_normal_flip=False, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))Â
Description
Extrude selected vertices in a circle around the cursor in indicated viewport
Parameters:
steps (int) â Steps, Steps (in [0, 1000000], optional)
dupli (bool) â Use Duplicates, (optional)
angle (float) â Angle, Rotation for each step (in [-inf, inf], optional)
use_auto_merge (bool) â Auto Merge, Merge first/last when the angle is a full revolution (optional)
use_normal_flip (bool) â Flip Normals, (optional)
center (mathutils.Vector | Sequence[float]) â Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
axis (mathutils.Vector | Sequence[float]) â Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

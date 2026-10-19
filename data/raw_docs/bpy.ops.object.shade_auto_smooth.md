# bpy.ops.object.shade_auto_smooth

## Signature
```python
bpy.ops.object.shade_auto_smooth(*, use_auto_smooth=True, angle=0.523599)Â
Description
Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces
Parameters:
use_auto_smooth (bool) â Auto Smooth, Add modifier to set edge sharpness automatically (optional)
angle (float) â Angle, Maximum angle between face normals that will be considered as smooth (in [0, 3.14159], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

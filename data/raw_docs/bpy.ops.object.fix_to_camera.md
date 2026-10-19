# bpy.ops.object.fix_to_camera

## Signature
```python
bpy.ops.object.fix_to_camera(*, use_location=True, use_rotation=True, use_scale=True)Â
Description
Generate new keys to fix the selected object/bone to the camera on unkeyed frames
Parameters:
use_location (bool) â Location, Create Location keys when fixing to the scene camera (optional)
use_rotation (bool) â Rotation, Create Rotation keys when fixing to the scene camera (optional)
use_scale (bool) â Scale, Create Scale keys when fixing to the scene camera (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/copy_global_transform.py:639

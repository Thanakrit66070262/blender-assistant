# bpy.ops.mesh.average_normals

## Signature
```python
bpy.ops.mesh.average_normals(*, average_type='CUSTOM_NORMAL', weight=50, threshold=0.01)Â
Description
Average custom normals of selected vertices
Parameters:
average_type (Literal['CUSTOM_NORMAL', 'FACE_AREA', 'CORNER_ANGLE']) â Type, Averaging method (optional)
CUSTOM_NORMAL
Custom Normal â Take average of vertex normals.
FACE_AREA
Face Area â Set all vertex normals by face area.
CORNER_ANGLE
Corner Angle â Set all vertex normals by corner angle.
weight (int) â Weight, Weight applied per face (in [1, 100], optional)
threshold (float) â Threshold, Threshold value for different weights to be considered equal (in [0, 10], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

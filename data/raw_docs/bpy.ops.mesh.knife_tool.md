# bpy.ops.mesh.knife_tool

## Signature
```python
bpy.ops.mesh.knife_tool(*, use_occlude_geometry=True, only_selected=False, xray=True, visible_measurements='NONE', angle_snapping='NONE', angle_snapping_increment=0.523599, wait_for_input=True)Â
Description
Cut new topology
Parameters:
use_occlude_geometry (bool) â Occlude Geometry, Only cut the front most geometry (optional)
only_selected (bool) â Only Selected, Only cut selected geometry (optional)
xray (bool) â X-Ray, Show cuts hidden by geometry (optional)
visible_measurements (Literal['NONE', 'BOTH', 'DISTANCE', 'ANGLE']) â Measurements, Visible distance and angle measurements (optional)
NONE
None â Show no measurements.
BOTH
Both â Show both distances and angles.
DISTANCE
Distance â Show just distance measurements.
ANGLE
Angle â Show just angle measurements.
angle_snapping (Literal['NONE', 'SCREEN', 'RELATIVE']) â Angle Snapping, Angle snapping mode (optional)
NONE
None â No angle snapping.
SCREEN
Screen â Screen space angle snapping.
RELATIVE
Relative â Angle snapping relative to the previous cut edge.
angle_snapping_increment (float) â Angle Snap Increment, The angle snap increment used when in constrained angle mode (in [0, 3.14159], optional)
wait_for_input (bool) â Wait for Input, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

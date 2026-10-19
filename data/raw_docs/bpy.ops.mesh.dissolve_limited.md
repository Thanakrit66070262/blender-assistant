# bpy.ops.mesh.dissolve_limited

## Signature
```python
bpy.ops.mesh.dissolve_limited(*, angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'})Â
Description
Dissolve selected edges and vertices, limited by the angle of surrounding geometry
Parameters:
angle_limit (float) â Max Angle, Angle limit (in [0, 3.14159], optional)
use_dissolve_boundaries (bool) â All Boundaries, Dissolve all vertices in between face boundaries (optional)
delimit (set[Literal[Mesh Delimit Mode Items]]) â Delimit, Delimit dissolve operation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.bisect

## Signature
```python
bpy.ops.mesh.bisect(*, plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)Â
Description
Cut geometry along a plane (click-drag to define plane)
Parameters:
plane_co (mathutils.Vector | Sequence[float]) â Plane Point, A point on the plane (array of 3 items, in [-inf, inf], optional)
plane_no (mathutils.Vector | Sequence[float]) â Plane Normal, The direction the plane points (array of 3 items, in [-1, 1], optional)
use_fill (bool) â Fill, Fill in the cut (optional)
clear_inner (bool) â Clear Inner, Remove geometry behind the plane (optional)
clear_outer (bool) â Clear Outer, Remove geometry in front of the plane (optional)
threshold (float) â Axis Threshold, Preserves the existing geometry along the cut plane (in [0, 10], optional)
xstart (int) â X Start, (in [-inf, inf], optional)
xend (int) â X End, (in [-inf, inf], optional)
ystart (int) â Y Start, (in [-inf, inf], optional)
yend (int) â Y End, (in [-inf, inf], optional)
flip (bool) â Flip, (optional)
cursor (int) â Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

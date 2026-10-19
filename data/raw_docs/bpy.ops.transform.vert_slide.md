# bpy.ops.transform.vert_slide

## Signature
```python
bpy.ops.transform.vert_slide(*, value=0.0, use_even=False, flipped=False, use_clamp=True, direction=(0.0, 0.0, 0.0), mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), correct_uv=True, release_confirm=False, use_accurate=False)Â
Description
Slide a vertex along a mesh
Parameters:
value (float) â Factor, (in [-10, 10], optional)
use_even (bool) â Even, Make the edge loop match the shape of the adjacent edge loop (optional)
flipped (bool) â Flipped, When Even mode is active, flips between the two adjacent edge loops (optional)
use_clamp (bool) â Clamp, Clamp within the edge extents (optional)
direction (mathutils.Vector | Sequence[float]) â Slide Direction, World-space direction (array of 3 items, in [-inf, inf], optional)
mirror (bool) â Mirror Editing, (optional)
snap (bool) â Use Snapping Options, (optional)
snap_elements (set[Literal[Snap Element Items]]) â Snap to Elements, (optional)
use_snap_project (bool) â Project Individual Elements, (optional)
snap_target (Literal[Snap Source Items]) â Snap Base, Point on source that will snap to target (optional)
use_snap_self (bool) â Target: Include Active, (optional)
use_snap_edit (bool) â Target: Include Edit, (optional)
use_snap_nonedit (bool) â Target: Include Non-Edited, (optional)
use_snap_selectable (bool) â Target: Exclude Non-Selectable, (optional)
snap_point (mathutils.Vector | Sequence[float]) â Point, (array of 3 items, in [-inf, inf], optional)
correct_uv (bool) â Correct UVs, Correct UV coordinates when transforming (optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

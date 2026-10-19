# bpy.ops.mesh.symmetry_snap

## Signature
```python
bpy.ops.mesh.symmetry_snap(*, direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True, use_topology=False)Â
Description
Snap vertex pairs to their mirrored locations
Parameters:
direction (Literal[Symmetrize Direction Items]) â Direction, Which sides to copy from and to (optional)
threshold (float) â Threshold, Distance within which matching vertices are searched (in [0, 10], optional)
factor (float) â Factor, Mix factor of the locations of the vertices (in [0, 1], optional)
use_center (bool) â Center, Snap middle vertices to the axis center (optional)
use_topology (bool) â Topology Mirror, Use topology to find mirrored vertices instead of spatial proximity (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

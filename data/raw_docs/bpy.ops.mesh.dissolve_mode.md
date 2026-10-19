# bpy.ops.mesh.dissolve_mode

## Signature
```python
bpy.ops.mesh.dissolve_mode(*, use_verts=False, angle_threshold=3.14159, use_preserve_quads=True, use_face_split=False, use_boundary_tear=False)Â
Description
Dissolve geometry based on the selection mode
Parameters:
use_verts (bool) â Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)
angle_threshold (float) â Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)
use_preserve_quads (bool) â Preserve Quads, When dissolving the edge between two triangles, donât dissolve vertices (optional)
use_face_split (bool) â Face Split, Split off face corners to maintain surrounding geometry (optional)
use_boundary_tear (bool) â Tear Boundary, Split off face corners instead of merging faces (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

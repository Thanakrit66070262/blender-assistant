# bpy.ops.mesh.shortest_path_select

## Signature
```python
bpy.ops.mesh.shortest_path_select(*, edge_mode='SELECT', use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0)Â
Description
Select shortest path between two vertices/edges/faces
Parameters:
edge_mode (Literal['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE']) â Edge Tag, The edge flag to tag when selecting the shortest path (optional)
use_face_step (bool) â Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)
use_topology_distance (bool) â Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)
use_fill (bool) â Fill Region, Select all paths between the source/destination elements (optional)
skip (int) â Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)
nth (int) â Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
offset (int) â Offset, Offset from the starting point (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

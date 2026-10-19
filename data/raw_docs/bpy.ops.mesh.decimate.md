# bpy.ops.mesh.decimate

## Signature
```python
bpy.ops.mesh.decimate(*, ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y')Â
Description
Simplify geometry by collapsing edges
Parameters:
ratio (float) â Ratio, (in [0, 1], optional)
use_vertex_group (bool) â Vertex Group, Use active vertex group as an influence (optional)
vertex_group_factor (float) â Weight, Vertex group strength (in [0, 1000], optional)
invert_vertex_group (bool) â Invert, Invert vertex group influence (optional)
use_symmetry (bool) â Symmetry, Maintain symmetry on an axis (optional)
symmetry_axis (Literal[Axis Xyz Items]) â Axis, Axis of symmetry (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

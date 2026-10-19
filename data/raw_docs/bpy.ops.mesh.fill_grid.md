# bpy.ops.mesh.fill_grid

## Signature
```python
bpy.ops.mesh.fill_grid(*, span=1, offset=0, use_interp_simple=False)Â
Description
Fill grid from two loops
Parameters:
span (int) â Span, Number of grid columns (in [1, 1000], optional)
offset (int) â Offset, Vertex that is the corner of the grid (in [-1000, 1000], optional)
use_interp_simple (bool) â Simple Blending, Use simple interpolation of grid vertices (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

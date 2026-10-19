# bpy.ops.mesh.inset

## Signature
```python
bpy.ops.mesh.inset(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.0, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True, release_confirm=False)Â
Description
Inset new faces into selected faces
Parameters:
use_boundary (bool) â Boundary, Inset face boundaries (optional)
use_even_offset (bool) â Offset Even, Scale the offset to give more even thickness (optional)
use_relative_offset (bool) â Offset Relative, Scale the offset by surrounding geometry (optional)
use_edge_rail (bool) â Edge Rail, Inset the region along existing edges (optional)
thickness (float) â Thickness, (in [0, inf], optional)
depth (float) â Depth, (in [-inf, inf], optional)
use_outset (bool) â Outset, Outset rather than inset (optional)
use_select_inset (bool) â Select Outer, Select the new inset faces (optional)
use_individual (bool) â Individual, Individual face inset (optional)
use_interpolate (bool) â Interpolate, Blend face data across the inset (optional)
release_confirm (bool) â Confirm on Release, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

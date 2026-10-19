# bpy.ops.mesh.wireframe

## Signature
```python
bpy.ops.mesh.wireframe(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01)Â
Description
Create a solid wireframe from faces
Parameters:
use_boundary (bool) â Boundary, Inset face boundaries (optional)
use_even_offset (bool) â Offset Even, Scale the offset to give more even thickness (optional)
use_relative_offset (bool) â Offset Relative, Scale the offset by surrounding geometry (optional)
use_replace (bool) â Replace, Remove original faces (optional)
thickness (float) â Thickness, (in [0, 10000], optional)
offset (float) â Offset, (in [0, 10000], optional)
use_crease (bool) â Crease, Crease hub edges for an improved subdivision surface (optional)
crease_weight (float) â Crease Weight, (in [0, 1000], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.poke

## Signature
```python
bpy.ops.mesh.poke(*, offset=0.0, use_relative_offset=False, center_mode='MEDIAN_WEIGHTED')Â
Description
Split a face into a fan
Parameters:
offset (float) â Poke Offset, Poke Offset (in [-1000, 1000], optional)
use_relative_offset (bool) â Offset Relative, Scale the offset by surrounding geometry (optional)
center_mode (Literal['MEDIAN_WEIGHTED', 'MEDIAN', 'BOUNDS']) â Poke Center, Poke face center calculation (optional)
MEDIAN_WEIGHTED
Weighted Median â Weighted median face center.
MEDIAN
Median â Median face center.
BOUNDS
Bounds â Face bounds center.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.transform.shrink_fatten

## Signature
```python
bpy.ops.transform.shrink_fatten(*, value=0.0, use_even_offset=False, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, release_confirm=False, use_accurate=False)Â
Description
Shrink/fatten selected vertices along normals
Parameters:
value (float) â Offset, (in [-inf, inf], optional)
use_even_offset (bool) â Offset Even, Scale the offset to give more even thickness (optional)
mirror (bool) â Mirror Editing, (optional)
use_proportional_edit (bool) â Proportional Editing, (optional)
proportional_edit_falloff (Literal[Proportional Falloff Items]) â Proportional Falloff, Falloff type for proportional editing mode (optional)
proportional_size (float) â Proportional Size, (in [1e-06, inf], optional)
use_proportional_connected (bool) â Connected, (optional)
use_proportional_projected (bool) â Projected (2D), (optional)
snap (bool) â Use Snapping Options, (optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

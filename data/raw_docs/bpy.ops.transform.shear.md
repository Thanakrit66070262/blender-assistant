# bpy.ops.transform.shear

## Signature
```python
bpy.ops.transform.shear(*, angle=0.0, orient_axis='Z', orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, gpencil_strokes=False, release_confirm=False, use_accurate=False)Â
Description
Shear selected items along the given axis
Parameters:
angle (float) â Angle, (in [-inf, inf], optional)
orient_axis (Literal[Axis Xyz Items]) â Axis, (optional)
orient_axis_ortho (Literal[Axis Xyz Items]) â Axis Ortho, (optional)
orient_type (str) â Orientation, Transformation orientation (optional)
orient_matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)
orient_matrix_type (str) â Matrix Orientation, (optional)
mirror (bool) â Mirror Editing, (optional)
use_proportional_edit (bool) â Proportional Editing, (optional)
proportional_edit_falloff (Literal[Proportional Falloff Items]) â Proportional Falloff, Falloff type for proportional editing mode (optional)
proportional_size (float) â Proportional Size, (in [1e-06, inf], optional)
use_proportional_connected (bool) â Connected, (optional)
use_proportional_projected (bool) â Projected (2D), (optional)
snap (bool) â Use Snapping Options, (optional)
gpencil_strokes (bool) â Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

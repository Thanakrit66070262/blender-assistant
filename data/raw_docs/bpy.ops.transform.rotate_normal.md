# bpy.ops.transform.rotate_normal

## Signature
```python
bpy.ops.transform.rotate_normal(*, value=0.0, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, release_confirm=False, use_accurate=False)Â
Description
Rotate custom normal of selected items
Parameters:
value (float) â Angle, (in [-inf, inf], optional)
orient_axis (Literal[Axis Xyz Items]) â Axis, (optional)
orient_type (str) â Orientation, Transformation orientation (optional)
orient_matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)
orient_matrix_type (str) â Matrix Orientation, (optional)
constraint_axis (Sequence[bool]) â Constraint Axis, (array of 3 items, optional)
mirror (bool) â Mirror Editing, (optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

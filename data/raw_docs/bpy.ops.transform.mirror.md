# bpy.ops.transform.mirror

## Signature
```python
bpy.ops.transform.mirror(*, orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)Â
Description
Mirror selected items around one or more axes
Parameters:
orient_type (str) â Orientation, Transformation orientation (optional)
orient_matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)
orient_matrix_type (str) â Matrix Orientation, (optional)
constraint_axis (Sequence[bool]) â Constraint Axis, (array of 3 items, optional)
gpencil_strokes (bool) â Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)
center_override (mathutils.Vector | Sequence[float]) â Center Override, Force using this center value (when set) (array of 3 items, in [-inf, inf], optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

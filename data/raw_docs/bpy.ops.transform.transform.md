# bpy.ops.transform.transform

## Signature
```python
bpy.ops.transform.transform(*, mode='TRANSLATION', value=(0.0, 0.0, 0.0, 0.0), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, use_duplicated_keyframes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False, use_automerge_and_split=False)Â
Description
Transform selected items by mode type
Parameters:
mode (Literal[Transform Mode Type Items]) â Mode, (optional)
value (mathutils.Vector | Sequence[float]) â Values, (array of 4 items, in [-inf, inf], optional)
orient_axis (Literal[Axis Xyz Items]) â Axis, (optional)
orient_type (Literal[Transform Orientation Items]) â Orientation, Transformation orientation (optional)
orient_matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)
orient_matrix_type (Literal[Transform Orientation Items]) â Matrix Orientation, (optional)
constraint_axis (Sequence[bool]) â Constraint Axis, (array of 3 items, optional)
mirror (bool) â Mirror Editing, (optional)
use_proportional_edit (bool) â Proportional Editing, (optional)
proportional_edit_falloff (Literal[Proportional Falloff Items]) â Proportional Falloff, Falloff type for proportional editing mode (optional)
proportional_size (float) â Proportional Size, (in [1e-06, inf], optional)
use_proportional_connected (bool) â Connected, (optional)
use_proportional_projected (bool) â Projected (2D), (optional)
snap (bool) â Use Snapping Options, (optional)
snap_elements (set[Literal[Snap Element Items]]) â Snap to Elements, (optional)
use_snap_project (bool) â Project Individual Elements, (optional)
snap_target (Literal[Snap Source Items]) â Snap Base, Point on source that will snap to target (optional)
use_snap_self (bool) â Target: Include Active, (optional)
use_snap_edit (bool) â Target: Include Edit, (optional)
use_snap_nonedit (bool) â Target: Include Non-Edited, (optional)
use_snap_selectable (bool) â Target: Exclude Non-Selectable, (optional)
snap_point (mathutils.Vector | Sequence[float]) â Point, (array of 3 items, in [-inf, inf], optional)
snap_align (bool) â Align with Point Normal, (optional)
snap_normal (mathutils.Vector | Sequence[float]) â Normal, (array of 3 items, in [-inf, inf], optional)
gpencil_strokes (bool) â Edit Grease Pencil, Edit selected Grease Pencil strokes (optional)
texture_space (bool) â Edit Texture Space, Edit object data texture space (optional)
remove_on_cancel (bool) â Remove on Cancel, Remove elements on cancel (optional)
use_duplicated_keyframes (bool) â Duplicated Keyframes, Transform duplicated keyframes (optional)
center_override (mathutils.Vector | Sequence[float]) â Center Override, Force using this center value (when set) (array of 3 items, in [-inf, inf], optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
use_automerge_and_split (bool) â Auto Merge & Split, Forces the use of Auto Merge and Split (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

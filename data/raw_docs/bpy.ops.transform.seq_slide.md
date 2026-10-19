# bpy.ops.transform.seq_slide

## Signature
```python
bpy.ops.transform.seq_slide(*, value=(0.0, 0.0), use_restore_handle_selection=False, snap=False, texture_space=False, remove_on_cancel=False, use_duplicated_keyframes=False, view2d_edge_pan=False, release_confirm=False, use_accurate=False)Â
Description
Slide a sequence strip in time
Parameters:
value (mathutils.Vector | Sequence[float]) â Offset, (array of 2 items, in [-inf, inf], optional)
use_restore_handle_selection (bool) â Restore Handle Selection, Restore handle selection after tweaking (optional)
snap (bool) â Use Snapping Options, (optional)
texture_space (bool) â Edit Texture Space, Edit object data texture space (optional)
remove_on_cancel (bool) â Remove on Cancel, Remove elements on cancel (optional)
use_duplicated_keyframes (bool) â Duplicated Keyframes, Transform duplicated keyframes (optional)
view2d_edge_pan (bool) â Edge Pan, Enable edge panning in 2D view (optional)
release_confirm (bool) â Confirm on Release, Always confirm operation when releasing button (optional)
use_accurate (bool) â Accurate, Use accurate transformation (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

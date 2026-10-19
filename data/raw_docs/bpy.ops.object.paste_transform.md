# bpy.ops.object.paste_transform

## Signature
```python
bpy.ops.object.paste_transform(*, method='CURRENT', bake_step=0, use_mirror=False, mirror_axis_loc='x', mirror_axis_rot='z', use_relative=False)Â
Description
Pastes the matrix from the clipboard to the currently active pose bone or object. Uses world-space matrices
Parameters:
method (Literal['CURRENT', 'EXISTING_KEYS', 'BAKE']) â Paste Method, Update the current transform, selected keyframes, or even create new keys (optional)
CURRENT
Current Transform â Paste onto the current values only, only manipulating the animation data if auto-keying is enabled.
EXISTING_KEYS
Selected Keys â Paste onto frames that have a selected key, potentially creating new keys on those frames.
BAKE
Bake on Key Range â Paste onto all frames between the first and last selected key, creating new keyframes if necessary.
bake_step (int) â Frame Step, Only used for baking. Step=1 creates a key on every frame, step=2 bakes on 2s, etc (in [1, inf], optional)
use_mirror (bool) â Mirror Transform, When pasting, mirror the transform relative to a specific object or bone (optional)
mirror_axis_loc (Literal['x', 'y', 'z']) â Location Axis, Coordinate axis used to mirror the location part of the transform (optional)
mirror_axis_rot (Literal['x', 'y', 'z']) â Rotation Axis, Coordinate axis used to mirror the rotation part of the transform (optional)
use_relative (bool) â Use Relative Paste, When pasting, assume the pasted matrix is relative to another object (set in the user interface) (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/copy_global_transform.py:325

# bpy.ops.object.transform_to_mouse

## Signature
```python
bpy.ops.object.transform_to_mouse(*, name='', session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)Â
Description
Snap selected item(s) to the mouse location
Parameters:
name (str) â Name, Object name to place (uses the active object when this and âsession_uidâ are unset) (optional, never None)
session_uid (int) â Session UUID, Session UUID of the object to place (uses the active object when this and ânameâ are unset) (in [-inf, inf], optional)
matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
drop_x (int) â Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
drop_y (int) â Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

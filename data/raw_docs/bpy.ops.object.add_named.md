# bpy.ops.object.add_named

## Signature
```python
bpy.ops.object.add_named(*, linked=False, name='', session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0)Â
Description
Add named object
Parameters:
linked (bool) â Linked, Duplicate object but not object data, linking to the original data (optional)
name (str) â Name, Name of the data-block to use by the operator (optional, never None)
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
matrix (mathutils.Matrix | Sequence[Sequence[float]]) â Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
drop_x (int) â Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
drop_y (int) â Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

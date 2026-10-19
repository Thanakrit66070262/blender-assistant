# bpy.ops.object.transforms_to_deltas

## Signature
```python
bpy.ops.object.transforms_to_deltas(*, mode='ALL', reset_values=True)Â
Description
Convert normal object transforms to delta transforms, any existing delta transforms will be included as well
Parameters:
mode (Literal['ALL', 'LOC', 'ROT', 'SCALE']) â Mode, Which transforms to transfer (optional)
ALL
All Transforms â Transfer location, rotation, and scale transforms.
LOC
Location â Transfer location transforms only.
ROT
Rotation â Transfer rotation transforms only.
SCALE
Scale â Transfer scale transforms only.
reset_values (bool) â Reset Values, Clear transform values after transferring to deltas (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:777

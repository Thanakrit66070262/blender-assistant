# bpy.ops.object.select_hierarchy

## Signature
```python
bpy.ops.object.select_hierarchy(*, direction='PARENT', extend=False)Â
Description
Select object relative to the active objectâs position in the hierarchy
Parameters:
direction (Literal['PARENT', 'CHILD']) â Direction, Direction to select in the hierarchy (optional)
extend (bool) â Extend, Extend the existing selection (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:174

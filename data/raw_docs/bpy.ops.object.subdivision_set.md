# bpy.ops.object.subdivision_set

## Signature
```python
bpy.ops.object.subdivision_set(*, level=1, relative=False, ensure_modifier=True)Â
Description
Sets a Subdivision Surface level (1 to 5)
Parameters:
level (int) â Level, (in [-100, 100], optional)
relative (bool) â Relative, Apply the subdivision surface level as an offset relative to the current level (optional)
ensure_modifier (bool) â Ensure Modifier, Create the corresponding modifier if it does not exist (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:242

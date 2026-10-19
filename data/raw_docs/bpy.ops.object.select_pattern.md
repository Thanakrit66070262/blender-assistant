# bpy.ops.object.select_pattern

## Signature
```python
bpy.ops.object.select_pattern(*, pattern='*', case_sensitive=False, extend=True)Â
Description
Select objects matching a naming pattern
Parameters:
pattern (str) â Pattern, Name filter using â*â, â?â and â[abc]â unix style wildcards (optional, never None)
case_sensitive (bool) â Case Sensitive, Do a case sensitive compare (optional)
extend (bool) â Extend, Extend the existing selection (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:45

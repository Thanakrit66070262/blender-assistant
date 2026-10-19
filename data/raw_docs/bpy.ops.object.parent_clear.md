# bpy.ops.object.parent_clear

## Signature
```python
bpy.ops.object.parent_clear(*, type='CLEAR')Â
Description
Clear the objectâs parenting
Parameters:
type (Literal['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE']) â Type, (optional)
CLEAR
Clear Parent â Completely clear the parenting relationship, including involved modifiers if any.
CLEAR_KEEP_TRANSFORM
Clear and Keep Transformation â As âClear Parentâ, but keep the current visual transformations of the object.
CLEAR_INVERSE
Clear Parent Inverse â Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

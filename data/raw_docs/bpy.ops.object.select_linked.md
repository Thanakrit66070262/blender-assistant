# bpy.ops.object.select_linked

## Signature
```python
bpy.ops.object.select_linked(*, extend=False, type='OBDATA')Â
Description
Select all visible objects that are linked
Parameters:
extend (bool) â Extend, Extend selection instead of deselecting everything first (optional)
type (Literal['OBDATA', 'MATERIAL', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA']) â Type, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

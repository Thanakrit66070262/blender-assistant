# bpy.ops.object.modifier_apply_as_shapekey

## Signature
```python
bpy.ops.object.modifier_apply_as_shapekey(*, keep_modifier=False, modifier='', report=False, use_selected_objects=False)Â
Description
Apply modifier as a new shape key and remove from the stack
Parameters:
keep_modifier (bool) â Keep Modifier, Do not remove the modifier from stack (optional)
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
report (bool) â Report, Create a notification after the operation (optional)
use_selected_objects (bool) â Selected Objects, Affect all selected objects instead of just the active object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

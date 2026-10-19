# bpy.ops.object.modifier_remove

## Signature
```python
bpy.ops.object.modifier_remove(*, modifier='', report=False, use_selected_objects=False)Â
Description
Remove a modifier from the active object
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
report (bool) â Report, Create a notification after the operation (optional)
use_selected_objects (bool) â Selected Objects, Affect all selected objects instead of just the active object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

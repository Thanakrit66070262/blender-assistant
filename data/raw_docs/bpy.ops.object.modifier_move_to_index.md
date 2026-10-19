# bpy.ops.object.modifier_move_to_index

## Signature
```python
bpy.ops.object.modifier_move_to_index(*, modifier='', index=0, use_selected_objects=False)Â
Description
Change the modifierâs index in the stack so it evaluates after the set number of others
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
index (int) â Index, The index to move the modifier to (in [0, inf], optional)
use_selected_objects (bool) â Selected Objects, Affect all selected objects instead of just the active object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

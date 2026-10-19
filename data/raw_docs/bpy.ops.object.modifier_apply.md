# bpy.ops.object.modifier_apply

## Signature
```python
bpy.ops.object.modifier_apply(*, modifier='', report=False, merge_customdata=True, single_user=False, all_keyframes=False, use_selected_objects=False)Â
Description
Apply modifier and remove from the stack
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
report (bool) â Report, Create a notification after the operation (optional)
merge_customdata (bool) â Merge UVs, For mesh objects, merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
single_user (bool) â Make Data Single User, Make the objectâs data single user if needed (optional)
all_keyframes (bool) â Apply to all keyframes, For Grease Pencil objects, apply the modifier to all the keyframes (optional)
use_selected_objects (bool) â Selected Objects, Affect all selected objects instead of just the active object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

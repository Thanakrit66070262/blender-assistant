# bpy.ops.object.modifier_add_node_group

## Signature
```python
bpy.ops.object.modifier_add_node_group(*, asset_library_type='LOCAL', asset_library_identifier='', relative_asset_identifier='', session_uid=0, use_selected_objects=False)Â
Description
Add a procedural operation/effect to the active object
Parameters:
asset_library_type (Literal[Asset Library Type Items]) â Asset Library Type, (optional)
asset_library_identifier (str) â Asset Library Identifier, (optional, never None)
relative_asset_identifier (str) â Relative Asset Identifier, (optional, never None)
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
use_selected_objects (bool) â Selected Objects, Affect all selected objects instead of just the active object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

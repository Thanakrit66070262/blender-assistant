# bpy.ops.object.geometry_node_bake_unpack_single

## Signature
```python
bpy.ops.object.geometry_node_bake_unpack_single(*, session_uid=0, modifier_name='', bake_id=0, method='USE_LOCAL')Â
Description
Unpack baked data from the .blend file to disk
Parameters:
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
modifier_name (str) â Modifier Name, Name of the modifier that contains the node (optional, never None)
bake_id (int) â Bake ID, Nested node id of the node (in [0, inf], optional)
method (Literal['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL']) â Method, How to unpack (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

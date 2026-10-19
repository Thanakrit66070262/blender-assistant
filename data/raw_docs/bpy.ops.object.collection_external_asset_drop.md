# bpy.ops.object.collection_external_asset_drop

## Signature
```python
bpy.ops.object.collection_external_asset_drop(*, session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), use_instance=True, drop_x=0, drop_y=0, collection='')Â
Description
Add the dragged collection to the scene
Parameters:
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
align (Literal['WORLD', 'VIEW', 'CURSOR']) â Align, The alignment of the new object (optional)
WORLD
World â Align the new object to the world.
VIEW
View â Align the new object to the view.
CURSOR
3D Cursor â Use the 3D cursor orientation for the new object.
location (mathutils.Vector | Sequence[float]) â Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
rotation (mathutils.Euler | Sequence[float]) â Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
scale (mathutils.Vector | Sequence[float]) â Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
use_instance (bool) â Instance, Add the dropped collection as collection instance (optional)
drop_x (int) â Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
drop_y (int) â Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
collection (str) â Collection, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

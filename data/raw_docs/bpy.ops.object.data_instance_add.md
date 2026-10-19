# bpy.ops.object.data_instance_add

## Signature
```python
bpy.ops.object.data_instance_add(*, name='', session_uid=0, type='ACTION', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), drop_x=0, drop_y=0)Â
Description
Add an object data instance
Parameters:
name (str) â Name, Name of the data-block to use by the operator (optional, never None)
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
type (Literal[Id Type Items]) â Type, (optional)
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
drop_x (int) â Drop X, X-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
drop_y (int) â Drop Y, Y-coordinate (screen space) to place the new object under (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.object.make_single_user

## Signature
```python
bpy.ops.object.make_single_user(*, type='SELECTED_OBJECTS', object=False, obdata=False, material=False, animation=False, obdata_animation=False)Â
Description
Make linked data local to each object
Parameters:
type (Literal['SELECTED_OBJECTS', 'ALL']) â Type, (optional)
object (bool) â Object, Make single user objects (optional)
obdata (bool) â Object Data, Make single user object data (optional)
material (bool) â Materials, Make materials local to each data-block (optional)
animation (bool) â Object Animation, Make object animation data local to each object (optional)
obdata_animation (bool) â Object Data Animation, Make object data (mesh, curve etc.) animation data local to each object (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

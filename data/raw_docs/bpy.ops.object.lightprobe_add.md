# bpy.ops.object.lightprobe_add

## Signature
```python
bpy.ops.object.lightprobe_add(*, type='SPHERE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))Â
Description
Add a light probe object
Parameters:
type (Literal['SPHERE', 'PLANE', 'VOLUME']) â Type, (optional)
SPHERE
Sphere â Light probe that captures precise lighting from all directions at a single point in space.
PLANE
Plane â Light probe that captures incoming light from a single direction on a plane.
VOLUME
Volume â Light probe that captures low frequency lighting inside a volume.
radius (float) â Radius, (in [0, inf], optional)
enter_editmode (bool) â Enter Edit Mode, Enter edit mode when adding this object (optional)
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
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

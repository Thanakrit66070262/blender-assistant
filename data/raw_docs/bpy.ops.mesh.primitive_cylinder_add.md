# bpy.ops.mesh.primitive_cylinder_add

## Signature
```python
bpy.ops.mesh.primitive_cylinder_add(*, vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))Â
Description
Construct a cylinder mesh
Parameters:
vertices (int) â Vertices, (in [3, 10000000], optional)
radius (float) â Radius, (in [0, inf], optional)
depth (float) â Depth, (in [0, inf], optional)
end_fill_type (Literal['NOTHING', 'NGON', 'TRIFAN']) â Cap Fill Type, (optional)
NOTHING
Nothing â Donât fill at all.
NGON
N-Gon â Use n-gons.
TRIFAN
Triangle Fan â Use triangle fans.
calc_uvs (bool) â Generate UVs, Generate a default UV map (optional)
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

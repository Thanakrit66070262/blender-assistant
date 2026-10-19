# bpy.ops.mesh.primitive_torus_add

## Signature
```python
bpy.ops.mesh.primitive_torus_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs=True)Â
Description
Construct a torus mesh
Parameters:
align (Literal['WORLD', 'VIEW', 'CURSOR']) â Align, (optional)
WORLD
World â Align the new object to the world.
VIEW
View â Align the new object to the view.
CURSOR
3D Cursor â Use the 3D cursor orientation for the new object.
location (mathutils.Vector | Sequence[float]) â Location, (array of 3 items, in [-inf, inf], optional)
rotation (mathutils.Euler | Sequence[float]) â Rotation, (array of 3 items, in [-inf, inf], optional)
major_segments (int) â Major Segments, Number of segments for the main ring of the torus (in [3, 256], optional)
minor_segments (int) â Minor Segments, Number of segments for the minor ring of the torus (in [3, 256], optional)
mode (Literal['MAJOR_MINOR', 'EXT_INT']) â Dimensions Mode, (optional)
MAJOR_MINOR
Major/Minor â Use the major/minor radii for torus dimensions.
EXT_INT
Exterior/Interior â Use the exterior/interior radii for torus dimensions.
major_radius (float) â Major Radius, Radius from the origin to the center of the cross sections (in [0, 10000], optional)
minor_radius (float) â Minor Radius, Radius of the torusâs cross section (in [0, 10000], optional)
abso_major_rad (float) â Exterior Radius, Total Exterior Radius of the torus (in [0, 10000], optional)
abso_minor_rad (float) â Interior Radius, Total Interior Radius of the torus (in [0, 10000], optional)
generate_uvs (bool) â Generate UVs, Generate a default UV map (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/add_mesh_torus.py:222

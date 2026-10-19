# bpy.ops.object.origin_set

## Signature
```python
bpy.ops.object.origin_set(*, type='GEOMETRY_ORIGIN', center='MEDIAN')Â
Description
Set the objectâs origin, by either moving the data, or set to center of data, or use 3D cursor
Parameters:
type (Literal['GEOMETRY_ORIGIN', 'ORIGIN_GEOMETRY', 'ORIGIN_CURSOR', 'ORIGIN_CENTER_OF_MASS', 'ORIGIN_CENTER_OF_VOLUME']) â Type, (optional)
GEOMETRY_ORIGIN
Geometry to Origin â Move object geometry to object origin.
ORIGIN_GEOMETRY
Origin to Geometry â Calculate the center of geometry based on the current pivot point (median, otherwise bounding box).
ORIGIN_CURSOR
Origin to 3D Cursor â Move object origin to position of the 3D cursor.
ORIGIN_CENTER_OF_MASS
Origin to Center of Mass (Surface) â Calculate the center of mass from the surface area.
ORIGIN_CENTER_OF_VOLUME
Origin to Center of Mass (Volume) â Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
center (Literal['MEDIAN', 'BOUNDS']) â Center, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

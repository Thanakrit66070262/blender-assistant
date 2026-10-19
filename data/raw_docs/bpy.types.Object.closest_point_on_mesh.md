# bpy.types.Object.closest_point_on_mesh

## Signature
```python
closest_point_on_mesh(origin, *, distance=1.84467e+19, depsgraph=None)Â
Description
Find the nearest point on evaluated geometry, in object space (using contextâs or provided depsgraph to get evaluated mesh if needed)
Parameters:
origin (mathutils.Vector | Sequence[float]) â Point to find closest geometry from (in object space) (array of 3 items, in [-inf, inf])
distance (float) â Maximum distance (in [0, inf], optional)
depsgraph (Depsgraph | None) â Depsgraph to use to get evaluated data, when called from original object (only needed if current Contextâs depsgraph is not suitable) (optional)
Returns:
result, Whether closest point on geometry was found, bool
location, The location on the object closest to the point, mathutils.Vector
normal, The face normal at the closest point, mathutils.Vector
index, The face index, -1 when original data isnât available, int
Return type:
tuple[bool, mathutils.Vector, mathutils.Vector, int]

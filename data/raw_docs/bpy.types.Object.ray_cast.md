# bpy.types.Object.ray_cast

## Signature
```python
ray_cast(origin, direction, *, distance=1.70141e+38, depsgraph=None)Â
Description
Cast a ray onto evaluated geometry, in object space (using contextâs or provided depsgraph to get evaluated mesh if needed)
Parameters:
origin (mathutils.Vector | Sequence[float]) â Origin of the ray, in object space (array of 3 items, in [-inf, inf])
direction (mathutils.Vector | Sequence[float]) â Direction of the ray, in object space (array of 3 items, in [-inf, inf])
distance (float) â Maximum distance (in [0, inf], optional)
depsgraph (Depsgraph | None) â Depsgraph to use to get evaluated data, when called from original object (only needed if current Contextâs depsgraph is not suitable) (optional)
Returns:
result, Whether the ray successfully hit the geometry, bool
location, The hit location of this ray cast, mathutils.Vector
normal, The face normal at the ray cast hit location, mathutils.Vector
index, The face index, -1 when original data isnât available, int
Return type:
tuple[bool, mathutils.Vector, mathutils.Vector, int]

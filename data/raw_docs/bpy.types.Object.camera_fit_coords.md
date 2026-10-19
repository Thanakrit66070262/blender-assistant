# bpy.types.Object.camera_fit_coords

## Signature
```python
camera_fit_coords(depsgraph, coordinates)Â
Description
Compute the coordinate (and scale for ortho cameras) given object should be to âseeâ all given coordinates
Parameters:
depsgraph (Depsgraph | None) â Depsgraph to get evaluated data from
coordinates (Sequence[float]) â Coordinates to fit in (array of 1 items, in [-inf, inf], never None)
Returns:
co_return, The location to aim to be able to see all given points, mathutils.Vector
scale_return, The ortho scale to aim to be able to see all given points (if relevant), float
Return type:
tuple[mathutils.Vector, float]

# bpy.ops.mesh.circularize

## Signature
```python
bpy.ops.mesh.circularize(*, factor=1.0, fit_method='LEAST_SQUARE', angle=0.0, use_custom_radius=False, custom_radius=1.0, regular=True, flatten=1.0, lock=(False, False, False))Â
Description
Shape selected geometry into a circle
Parameters:
factor (float) â Factor, Circularization factor (in [0, 1], optional)
fit_method (Literal['LEAST_SQUARE', 'CONTRACT']) â Method, Method used for fitting a circle to the vertices (optional)
LEAST_SQUARE
Best Fit â Calculate a best-fit circle using non-linear least squares.
CONTRACT
Interior Fit â Only move vertices towards the center.
angle (float) â Rotation, Rotate the circle (in [-6.28319, 6.28319], optional)
use_custom_radius (bool) â Use Custom Radius, Enable custom radius (optional)
custom_radius (float) â Radius, Radius of the circle (in [0, inf], optional)
regular (bool) â Space Evenly, Distribute vertices at constant distances along the circle, otherwise preserves original spacing (optional)
flatten (float) â Flatten, Flatten the circle, instead of projecting it on the mesh (in [0, 1], optional)
lock (Sequence[bool]) â Lock, Lock editing of the axis (array of 3 items, optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.point_normals

## Signature
```python
bpy.ops.mesh.point_normals(*, mode='COORDINATES', invert=False, align=False, target_location=(0.0, 0.0, 0.0), spherize=False, spherize_strength=0.1)Â
Description
Point selected custom normals to specified Target
Parameters:
mode (Literal['COORDINATES', 'MOUSE']) â Mode, How to define coordinates to point custom normals to (optional)
COORDINATES
Coordinates â Use static coordinates (defined by various means).
MOUSE
Mouse â Follow mouse cursor.
invert (bool) â Invert, Invert affected normals (optional)
align (bool) â Align, Make all affected normals parallel (optional)
target_location (mathutils.Vector | Sequence[float]) â Target, Target location to which normals will point (array of 3 items, in [-inf, inf], optional)
spherize (bool) â Spherize, Interpolate between original and new normals (optional)
spherize_strength (float) â Spherize Strength, Ratio of spherized normal to original normal (in [0, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

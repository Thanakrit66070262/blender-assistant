# bpy.ops.mesh.flatten

## Signature
```python
bpy.ops.mesh.flatten(*, factor=1.0, method='BEST_FIT', lock=(False, False, False))Â
Description
Flatten vertices on a best-fitting plane
Parameters:
factor (float) â Factor, Flattening factor (in [0, 1], optional)
method (Literal['BEST_FIT', 'NORMAL', 'VIEW']) â Method, Plane on which vertices are flattened (optional)
BEST_FIT
Best Fit â Calculate a best fitting plane.
NORMAL
Normal â Derive plane by averaging face normals.
VIEW
View â Flatten on a plane perpendicular to the viewing angle.
lock (Sequence[bool]) â Lock, Lock editing of the axis (array of 3 items, optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

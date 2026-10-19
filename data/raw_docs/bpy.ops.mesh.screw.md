# bpy.ops.mesh.screw

## Signature
```python
bpy.ops.mesh.screw(*, steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))Â
Description
Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport
Parameters:
steps (int) â Steps, Steps (in [1, 100000], optional)
turns (int) â Turns, Turns (in [1, 100000], optional)
center (mathutils.Vector | Sequence[float]) â Center, Center in global view space (array of 3 items, in [-inf, inf], optional)
axis (mathutils.Vector | Sequence[float]) â Axis, Axis in global view space (array of 3 items, in [-1, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

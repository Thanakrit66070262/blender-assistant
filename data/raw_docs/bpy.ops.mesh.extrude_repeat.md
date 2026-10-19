# bpy.ops.mesh.extrude_repeat

## Signature
```python
bpy.ops.mesh.extrude_repeat(*, steps=10, offset=(0.0, 0.0, 0.0), scale_offset=1.0)Â
Description
Extrude selected vertices, edges or faces repeatedly
Parameters:
steps (int) â Steps, (in [0, 1000000], optional)
offset (mathutils.Vector | Sequence[float]) â Offset, Offset vector (array of 3 items, in [-100000, 100000], optional)
scale_offset (float) â Scale Offset, (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.symmetrize

## Signature
```python
bpy.ops.mesh.symmetrize(*, direction='NEGATIVE_X', threshold=0.0001)Â
Description
Enforce symmetry (both form and topological) across an axis
Parameters:
direction (Literal[Symmetrize Direction Items]) â Direction, Which sides to copy from and to (optional)
threshold (float) â Threshold, Limit for snap middle vertices to the axis center (in [0, 10], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

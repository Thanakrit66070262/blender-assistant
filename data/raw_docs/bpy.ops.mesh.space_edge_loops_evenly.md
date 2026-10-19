# bpy.ops.mesh.space_edge_loops_evenly

## Signature
```python
bpy.ops.mesh.space_edge_loops_evenly(*, factor=1.0, interpolation='CUBIC', lock=(False, False, False))Â
Description
Space the vertices in a regular distribution on the loop
Parameters:
factor (float) â Factor, Spacing effect factor (in [0, 1], optional)
interpolation (Literal['CUBIC', 'LINEAR']) â Interpolation, Algorithm used for interpolation (optional)
CUBIC
Cubic â Natural cubic spline, smooth results.
LINEAR
Linear â Vertices are projected on existing edges.
lock (Sequence[bool]) â Lock, Lock editing of the axis (array of 3 items, optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

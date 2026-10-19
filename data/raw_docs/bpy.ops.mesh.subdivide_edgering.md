# bpy.ops.mesh.subdivide_edgering

## Signature
```python
bpy.ops.mesh.subdivide_edgering(*, number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')Â
Description
Subdivide perpendicular edges to the selected edge-ring
Parameters:
number_cuts (int) â Number of Cuts, (in [0, 1000], optional)
interpolation (Literal['LINEAR', 'PATH', 'SURFACE']) â Interpolation, Interpolation method (optional)
smoothness (float) â Smoothness, Smoothness factor (in [0, 1000], optional)
profile_shape_factor (float) â Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
profile_shape (Literal[Proportional Falloff Curve Only Items]) â Profile Shape, Shape of the profile (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

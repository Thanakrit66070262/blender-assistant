# bpy.ops.mesh.bridge_edge_loops

## Signature
```python
bpy.ops.mesh.bridge_edge_loops(*, type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')Â
Description
Create a bridge of faces between two or more selected edge loops
Parameters:
type (Literal['SINGLE', 'CLOSED', 'PAIRS']) â Connect Loops, Method of bridging multiple loops (optional)
use_merge (bool) â Merge, Merge rather than creating faces (optional)
merge_factor (float) â Merge Factor, (in [0, 1], optional)
twist_offset (int) â Twist, Twist offset for closed loops (in [-1000, 1000], optional)
number_cuts (int) â Number of Cuts, (in [0, 1000], optional)
interpolation (Literal['LINEAR', 'PATH', 'SURFACE']) â Interpolation, Interpolation method (optional)
smoothness (float) â Smoothness, Smoothness factor (in [0, 1000], optional)
profile_shape_factor (float) â Profile Factor, How much intermediary new edges are shrunk/expanded (in [-1000, 1000], optional)
profile_shape (Literal[Proportional Falloff Curve Only Items]) â Profile Shape, Shape of the profile (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

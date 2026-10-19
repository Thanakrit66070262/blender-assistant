# bpy.ops.mesh.loopcut

## Signature
```python
bpy.ops.mesh.loopcut(*, number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', object_index=-1, edge_index=-1, mesh_select_mode_init=(False, False, False))Â
Description
Add a new loop between existing loops
Parameters:
number_cuts (int) â Number of Cuts, (in [1, 1000000], optional)
smoothness (float) â Smoothness, Smoothness factor (in [-1000, 1000], optional)
falloff (Literal[Proportional Falloff Curve Only Items]) â Falloff, Falloff type of the feather (optional)
object_index (int) â Object Index, (in [-1, inf], optional)
edge_index (int) â Edge Index, (in [-1, inf], optional)
mesh_select_mode_init (Sequence[bool]) â (array of 3 items, optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

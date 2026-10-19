# bpy.ops.object.vertex_group_smooth

## Signature
```python
bpy.ops.object.vertex_group_smooth(*, group_select_mode='', factor=0.5, repeat=1, expand=0.0)Â
Description
Smooth weights for selected vertices
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
factor (float) â Factor, (in [0, 1], optional)
repeat (int) â Iterations, (in [1, 10000], optional)
expand (float) â Expand/Contract, Expand/contract weights (in [-1, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

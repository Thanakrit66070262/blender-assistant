# bpy.ops.object.vertex_group_levels

## Signature
```python
bpy.ops.object.vertex_group_levels(*, group_select_mode='', offset=0.0, gain=1.0)Â
Description
Add some offset and multiply with some gain the weights of the active vertex group
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
offset (float) â Offset, Value to add to weights (in [-1, 1], optional)
gain (float) â Gain, Value to multiply weights by (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

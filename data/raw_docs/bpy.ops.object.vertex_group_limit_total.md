# bpy.ops.object.vertex_group_limit_total

## Signature
```python
bpy.ops.object.vertex_group_limit_total(*, group_select_mode='', limit=4)Â
Description
Limit deform weights associated with a vertex to a specified number by removing lowest weights
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
limit (int) â Limit, Maximum number of deform weights (in [1, 32], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

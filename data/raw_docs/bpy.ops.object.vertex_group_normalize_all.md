# bpy.ops.object.vertex_group_normalize_all

## Signature
```python
bpy.ops.object.vertex_group_normalize_all(*, group_select_mode='', lock_active=True)Â
Description
Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
lock_active (bool) â Lock Active, Keep the values of the active group while normalizing others (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

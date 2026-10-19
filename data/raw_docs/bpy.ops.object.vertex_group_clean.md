# bpy.ops.object.vertex_group_clean

## Signature
```python
bpy.ops.object.vertex_group_clean(*, group_select_mode='', limit=0.0, keep_single=False)Â
Description
Remove vertex group assignments which are not required
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
limit (float) â Limit, Remove vertices which weight is below or equal to this limit (in [0, 1], optional)
keep_single (bool) â Keep Single, Keep verts assigned to at least one group when cleaning (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

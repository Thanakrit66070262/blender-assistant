# bpy.ops.object.vertex_group_invert

## Signature
```python
bpy.ops.object.vertex_group_invert(*, group_select_mode='', auto_assign=True, auto_remove=True)Â
Description
Invert active vertex groupâs weights
Parameters:
group_select_mode (str) â Subset, Define which subset of groups shall be used (optional)
auto_assign (bool) â Add Weights, Add vertices from groups that have zero weight before inverting (optional)
auto_remove (bool) â Remove Weights, Remove vertices from groups that have zero weight after inverting (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

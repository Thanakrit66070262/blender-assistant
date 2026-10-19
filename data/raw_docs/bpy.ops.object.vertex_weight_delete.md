# bpy.ops.object.vertex_weight_delete

## Signature
```python
bpy.ops.object.vertex_weight_delete(*, weight_group=-1)Â
Description
Delete this weight from the vertex (disabled if vertex group is locked)
Parameters:
weight_group (int) â Weight Index, Index of source weight in active vertex group (in [-1, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

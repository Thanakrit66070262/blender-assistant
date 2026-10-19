# bpy.ops.object.multires_base_apply

## Signature
```python
bpy.ops.object.multires_base_apply(*, modifier='', apply_heuristic=True)Â
Description
Modify the base mesh to conform to the displaced mesh
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
apply_heuristic (bool) â Apply Subdivision Heuristic, Whether or not the final base mesh positions will be slightly altered to account for a new subdivision modifier being added (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

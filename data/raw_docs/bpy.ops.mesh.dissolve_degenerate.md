# bpy.ops.mesh.dissolve_degenerate

## Signature
```python
bpy.ops.mesh.dissolve_degenerate(*, threshold=0.0001)Â
Description
Dissolve zero area faces and zero length edges
Parameters:
threshold (float) â Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

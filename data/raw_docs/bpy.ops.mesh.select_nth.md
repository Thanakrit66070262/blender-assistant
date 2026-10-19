# bpy.ops.mesh.select_nth

## Signature
```python
bpy.ops.mesh.select_nth(*, skip=1, nth=1, offset=0)Â
Description
Deselect every Nth element starting from the active vertex, edge or face
Parameters:
skip (int) â Deselected, Number of deselected elements in the repetitive sequence (in [1, inf], optional)
nth (int) â Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)
offset (int) â Offset, Offset from the starting point (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.select_by_pole_count

## Signature
```python
bpy.ops.mesh.select_by_pole_count(*, pole_count=4, type='NOTEQUAL', extend=False, exclude_nonmanifold=True)Â
Description
Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected
Parameters:
pole_count (int) â Pole Count, (in [0, inf], optional)
type (Literal['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL']) â Type, Type of comparison to make (optional)
extend (bool) â Extend, Extend the selection (optional)
exclude_nonmanifold (bool) â Exclude Non Manifold, Exclude non-manifold poles (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

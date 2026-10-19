# bpy.ops.mesh.select_face_by_sides

## Signature
```python
bpy.ops.mesh.select_face_by_sides(*, number=4, type='EQUAL', extend=True)Â
Description
Select vertices or faces by the number of face sides
Parameters:
number (int) â Number of Vertices, (in [3, inf], optional)
type (Literal['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL']) â Type, Type of comparison to make (optional)
extend (bool) â Extend, Extend the selection (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

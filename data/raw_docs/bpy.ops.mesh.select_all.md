# bpy.ops.mesh.select_all

## Signature
```python
bpy.ops.mesh.select_all(*, action='TOGGLE')Â
Description
(De)select all vertices, edges or faces
Parameters:
action (Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']) â Action, Selection action to execute (optional)
TOGGLE
Toggle â Toggle selection for all elements.
SELECT
Select â Select all elements.
DESELECT
Deselect â Deselect all elements.
INVERT
Invert â Invert selection of all elements.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

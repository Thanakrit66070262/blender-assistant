# bpy.ops.object.select_all

## Signature
```python
bpy.ops.object.select_all(*, action='TOGGLE')Â
Description
Change selection of all visible objects in scene
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

# bpy.ops.object.make_override_library

## Signature
```python
bpy.ops.object.make_override_library(*, collection=0)Â
Description
Create a local override of the selected linked objects, and their hierarchy of dependencies
Parameters:
collection (int) â Override Collection, Session UID of the directly linked collection containing the selected object, to make an override from (in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

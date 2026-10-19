# bpy.ops.transform.create_orientation

## Signature
```python
bpy.ops.transform.create_orientation(*, name='', use_view=False, use=False, overwrite=False)Â
Description
Create transformation orientation from selection
Parameters:
name (str) â Name, Name of the new custom orientation (optional, never None)
use_view (bool) â Use View, Use the current view instead of the active object to create the new orientation (optional)
use (bool) â Use After Creation, Select orientation after its creation (optional)
overwrite (bool) â Overwrite Previous, Overwrite previously created orientation with same name (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

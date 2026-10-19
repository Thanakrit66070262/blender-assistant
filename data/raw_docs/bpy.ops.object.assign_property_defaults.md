# bpy.ops.object.assign_property_defaults

## Signature
```python
bpy.ops.object.assign_property_defaults(*, process_data=True, process_bones=True)Â
Description
Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing
Parameters:
process_data (bool) â Process data properties, (optional)
process_bones (bool) â Process bone properties, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:1001

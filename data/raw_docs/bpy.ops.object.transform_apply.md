# bpy.ops.object.transform_apply

## Signature
```python
bpy.ops.object.transform_apply(*, location=True, rotation=True, scale=True, properties=True, corrective_flip_normals=True, isolate_users=False)Â
Description
Apply the objectâs transformation to its data
Parameters:
location (bool) â Location, (optional)
rotation (bool) â Rotation, (optional)
scale (bool) â Scale, (optional)
properties (bool) â Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope (optional)
corrective_flip_normals (bool) â Corrective Flip Normals, Invert normals for negative scaled objects. (optional)
isolate_users (bool) â Isolate Multi User Data, Create new object-data users if needed (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

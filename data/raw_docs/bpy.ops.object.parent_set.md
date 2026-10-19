# bpy.ops.object.parent_set

## Signature
```python
bpy.ops.object.parent_set(*, type='OBJECT', xmirror=False, keep_transform=False)Â
Description
Set the objectâs parenting
Parameters:
type (Literal['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI']) â Type, (optional)
xmirror (bool) â X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation (optional)
keep_transform (bool) â Keep Transform, Apply transformation before parenting (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

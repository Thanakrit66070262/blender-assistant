# bpy.ops.object.duplicate_move

## Signature
```python
bpy.ops.object.duplicate_move(*, OBJECT_OT_duplicate={}, TRANSFORM_OT_translate={})Â
Description
Duplicate the selected objects and move them
Parameters:
OBJECT_OT_duplicate (dict[str, Any]) â Duplicate Objects, Duplicate selected objects (optional, bpy.ops.object.duplicate() keyword arguments)
TRANSFORM_OT_translate (dict[str, Any]) â Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

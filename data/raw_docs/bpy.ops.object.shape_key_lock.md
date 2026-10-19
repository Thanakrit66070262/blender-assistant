# bpy.ops.object.shape_key_lock

## Signature
```python
bpy.ops.object.shape_key_lock(*, action='LOCK')Â
Description
Change the lock state of all shape keys of active object
Parameters:
action (Literal['LOCK', 'UNLOCK']) â Action, Lock action to execute on vertex groups (optional)
LOCK
Lock â Lock all shape keys.
UNLOCK
Unlock â Unlock all shape keys.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

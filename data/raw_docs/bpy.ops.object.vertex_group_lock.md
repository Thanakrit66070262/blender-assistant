# bpy.ops.object.vertex_group_lock

## Signature
```python
bpy.ops.object.vertex_group_lock(*, action='TOGGLE', mask='ALL')Â
Description
Change the lock state of all or some vertex groups of active object
Parameters:
action (Literal['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT']) â Action, Lock action to execute on vertex groups (optional)
TOGGLE
Toggle â Unlock all vertex groups if there is at least one locked group, lock all in other case.
LOCK
Lock â Lock all vertex groups.
UNLOCK
Unlock â Unlock all vertex groups.
INVERT
Invert â Invert the lock state of all vertex groups.
mask (Literal['ALL', 'SELECTED', 'UNSELECTED', 'INVERT_UNSELECTED']) â Mask, Apply the action based on vertex group selection (optional)
ALL
All â Apply action to all vertex groups.
SELECTED
Selected â Apply to selected vertex groups.
UNSELECTED
Unselected â Apply to unselected vertex groups.
INVERT_UNSELECTED
Invert Unselected â Apply the opposite of Lock/Unlock to unselected vertex groups.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

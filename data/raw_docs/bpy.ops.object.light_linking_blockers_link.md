# bpy.ops.object.light_linking_blockers_link

## Signature
```python
bpy.ops.object.light_linking_blockers_link(*, link_state='INCLUDE')Â
Description
Light link selected blockers to the active emitter object
Parameters:
link_state (Literal['INCLUDE', 'EXCLUDE']) â Link State, State of the shadow linking (optional)
INCLUDE
Include â Include selected blockers to cast shadows from the active emitter.
EXCLUDE
Exclude â Exclude selected blockers from casting shadows from the active emitter.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

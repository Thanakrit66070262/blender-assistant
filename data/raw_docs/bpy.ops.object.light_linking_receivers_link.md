# bpy.ops.object.light_linking_receivers_link

## Signature
```python
bpy.ops.object.light_linking_receivers_link(*, link_state='INCLUDE')Â
Description
Light link selected receivers to the active emitter object
Parameters:
link_state (Literal['INCLUDE', 'EXCLUDE']) â Link State, State of the light linking (optional)
INCLUDE
Include â Include selected receivers to receive light from the active emitter.
EXCLUDE
Exclude â Exclude selected receivers from receiving light from the active emitter.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.object.shaderfx_move_to_index

## Signature
```python
bpy.ops.object.shaderfx_move_to_index(*, shaderfx='', index=0)Â
Description
Change the effectâs position in the list so it evaluates after the set number of others
Parameters:
shaderfx (str) â Shader, Name of the shaderfx to edit (optional, never None)
index (int) â Index, The index to move the effect to (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

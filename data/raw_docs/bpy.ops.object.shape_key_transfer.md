# bpy.ops.object.shape_key_transfer

## Signature
```python
bpy.ops.object.shape_key_transfer(*, mode='OFFSET', use_clamp=False)Â
Description
Copy the active shape key of another selected object to this one
Parameters:
mode (Literal['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE']) â Transformation Mode, Relative shape positions to the new shape method (optional)
OFFSET
Offset â Apply the relative positional offset.
RELATIVE_FACE
Relative Face â Calculate relative position (using faces).
RELATIVE_EDGE
Relative Edge â Calculate relative position (using edges).
use_clamp (bool) â Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object.py:515

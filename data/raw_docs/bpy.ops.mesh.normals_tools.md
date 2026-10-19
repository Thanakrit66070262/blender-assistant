# bpy.ops.mesh.normals_tools

## Signature
```python
bpy.ops.mesh.normals_tools(*, mode='COPY', absolute=False)Â
Description
Custom normals tools using Normal Vector of UI
Parameters:
mode (Literal['COPY', 'PASTE', 'ADD', 'MULTIPLY', 'RESET']) â Mode, Mode of tools taking input from interface (optional)
COPY
Copy Normal â Copy normal to the internal clipboard.
PASTE
Paste Normal â Paste normal from the internal clipboard.
ADD
Add Normal â Add normal vector with selection.
MULTIPLY
Multiply Normal â Multiply normal vector with selection.
RESET
Reset Normal â Reset the internal clipboard and/or normal of selected element.
absolute (bool) â Absolute Coordinates, Copy Absolute coordinates of Normal vector (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

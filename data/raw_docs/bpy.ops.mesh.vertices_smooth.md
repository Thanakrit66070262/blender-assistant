# bpy.ops.mesh.vertices_smooth

## Signature
```python
bpy.ops.mesh.vertices_smooth(*, factor=0.0, repeat=1, xaxis=True, yaxis=True, zaxis=True, wait_for_input=True)Â
Description
Flatten angles of selected vertices
Parameters:
factor (float) â Smoothing, Smoothing factor (in [-10, 10], optional)
repeat (int) â Repeat, Number of times to smooth the mesh (in [1, 1000], optional)
xaxis (bool) â X-Axis, Smooth along the X axis (optional)
yaxis (bool) â Y-Axis, Smooth along the Y axis (optional)
zaxis (bool) â Z-Axis, Smooth along the Z axis (optional)
wait_for_input (bool) â Wait for Input, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

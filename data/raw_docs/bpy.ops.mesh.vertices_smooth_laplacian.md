# bpy.ops.mesh.vertices_smooth_laplacian

## Signature
```python
bpy.ops.mesh.vertices_smooth_laplacian(*, repeat=1, lambda_factor=1.0, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True)Â
Description
Laplacian smooth of selected vertices
Parameters:
repeat (int) â Number of iterations to smooth the mesh, (in [1, 1000], optional)
lambda_factor (float) â Lambda factor, (in [1e-07, 1000], optional)
lambda_border (float) â Lambda factor in border, (in [1e-07, 1000], optional)
use_x (bool) â Smooth X Axis, Smooth object along X axis (optional)
use_y (bool) â Smooth Y Axis, Smooth object along Y axis (optional)
use_z (bool) â Smooth Z Axis, Smooth object along Z axis (optional)
preserve_volume (bool) â Preserve Volume, Apply volume preservation after smooth (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

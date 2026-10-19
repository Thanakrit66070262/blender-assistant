# bpy.types.Object.calc_matrix_camera

## Signature
```python
calc_matrix_camera(depsgraph, *, x=1, y=1, scale_x=1.0, scale_y=1.0)Â
Description
Generate the camera projection matrix of this object (mostly useful for Camera and Light types)
Parameters:
depsgraph (Depsgraph | None) â Depsgraph to get evaluated data from
x (int) â Width of the render area (in [0, inf], optional)
y (int) â Height of the render area (in [0, inf], optional)
scale_x (float) â Width scaling factor (in [1e-06, inf], optional)
scale_y (float) â Height scaling factor (in [1e-06, inf], optional)
Returns:
The camera projection matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
Return type:
mathutils.Matrix

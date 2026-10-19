# bpy.ops.mesh.select_axis

## Signature
```python
bpy.ops.mesh.select_axis(*, orientation='LOCAL', sign='POS', axis='X', threshold=0.0001)Â
Description
Select all data in the mesh on a single axis
Parameters:
orientation (Literal[Transform Orientation Items]) â Axis Mode, Axis orientation (optional)
sign (Literal['POS', 'NEG', 'ALIGN']) â Axis Sign, Side to select (optional)
axis (Literal[Axis Xyz Items]) â Axis, Select the axis to compare each vertex on (optional)
threshold (float) â Threshold, (in [1e-06, 50], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

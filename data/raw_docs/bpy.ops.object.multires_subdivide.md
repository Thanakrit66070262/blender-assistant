# bpy.ops.object.multires_subdivide

## Signature
```python
bpy.ops.object.multires_subdivide(*, modifier='', mode='CATMULL_CLARK')Â
Description
Add a new level of subdivision
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
mode (Literal['CATMULL_CLARK', 'SIMPLE', 'LINEAR']) â Subdivision Mode, How the mesh is going to be subdivided to create a new level (optional)
CATMULL_CLARK
Catmull-Clark â Create a new level using Catmull-Clark subdivisions.
SIMPLE
Simple â Create a new level using simple subdivisions.
LINEAR
Linear â Create a new level using linear interpolation of the sculpted displacement.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

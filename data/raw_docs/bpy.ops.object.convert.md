# bpy.ops.object.convert

## Signature
```python
bpy.ops.object.convert(*, target='MESH', keep_original=False, merge_customdata=True, thickness=5, faces=True, offset=0.01)Â
Description
Convert selected objects to another type
Parameters:
target (Literal['CURVE', 'MESH', 'POINTCLOUD', 'CURVES', 'GREASEPENCIL']) â Target, Type of object to convert to (optional)
CURVE
Curve â Curve from Mesh or Text objects.
MESH
Mesh â Mesh from Curve, Surface, Metaball, Text, or Point Cloud objects.
POINTCLOUD
Point Cloud â Point Cloud from Mesh objects.
CURVES
Curves â Curves from evaluated curve data.
GREASEPENCIL
Grease Pencil â Grease Pencil from Curve or Mesh objects.
keep_original (bool) â Keep Original, Keep original objects instead of replacing them (optional)
merge_customdata (bool) â Merge UVs, Merge UV coordinates that share a vertex to account for imprecision in some modifiers (optional)
thickness (int) â Thickness, (in [1, 100], optional)
faces (bool) â Export Faces, Export faces as filled strokes (optional)
offset (float) â Stroke Offset, Offset strokes from fill (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

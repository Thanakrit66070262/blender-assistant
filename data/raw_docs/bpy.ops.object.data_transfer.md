# bpy.ops.object.data_transfer

## Signature
```python
bpy.ops.object.data_transfer(*, use_reverse_transfer=False, use_freeze=False, data_type='VGROUP_WEIGHTS', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0)Â
Description
Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes
Parameters:
use_reverse_transfer (bool) â Reverse Transfer, Transfer from selected objects to active one (optional)
use_freeze (bool) â Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry (optional)
data_type (Literal['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'COLOR_CORNER', 'UV', 'SMOOTH', 'FREESTYLE_FACE']) â Data Type, Which data to transfer (optional)
VGROUP_WEIGHTS
Vertex Group(s) â Transfer active or all vertex groups.
BEVEL_WEIGHT_VERT
Bevel Weight â Transfer bevel weights.
COLOR_VERTEX
Colors â Color Attributes.
SHARP_EDGE
Sharp â Transfer sharp mark.
SEAM
UV Seam â Transfer UV seam mark.
CREASE
Subdivision Crease â Transfer crease values.
BEVEL_WEIGHT_EDGE
Bevel Weight â Transfer bevel weights.
FREESTYLE_EDGE
Freestyle Mark â Transfer Freestyle edge mark.
CUSTOM_NORMAL
Custom Normals â Transfer custom normals.
COLOR_CORNER
Colors â Color Attributes.
UV
UVs â Transfer UV layers.
SMOOTH
Smooth â Transfer flat/smooth mark.
FREESTYLE_FACE
Freestyle Mark â Transfer Freestyle face mark.
use_create (bool) â Create Data, Add data layers on destination meshes if needed (optional)
vert_mapping (Literal[Dt Method Vertex Items]) â Vertex Mapping, Method used to map source vertices to destination ones (optional)
edge_mapping (Literal[Dt Method Edge Items]) â Edge Mapping, Method used to map source edges to destination ones (optional)
loop_mapping (Literal[Dt Method Loop Items]) â Face Corner Mapping, Method used to map source facesâ corners to destination ones (optional)
poly_mapping (Literal[Dt Method Poly Items]) â Face Mapping, Method used to map source faces to destination ones (optional)
use_auto_transform (bool) â Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects(optional)
use_object_transform (bool) â Object Transform, Evaluate source and destination meshes in global space (optional)
use_max_distance (bool) â Only Neighbor Geometry, Source elements must be closer than given distance from destination one (optional)
max_distance (float) â Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings (in [0, inf], optional)
ray_radius (float) â Ray Radius, âWidthâ of rays (especially useful when raycasting against vertices or edges) (in [0, inf], optional)
islands_precision (float) â Islands Precision, Factor controlling precision of islands handling (the higher, the better the results) (in [0, 10], optional)
layers_select_src (Literal[Dt Layers Select Src Items]) â Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
layers_select_dst (Literal[Dt Layers Select Dst Items]) â Destination Layers Matching, How to match source and destination layers (optional)
mix_mode (Literal[Dt Mix Mode Items]) â Mix Mode, How to affect destination elements with source values (optional)
mix_factor (float) â Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode) (in [0, 1], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

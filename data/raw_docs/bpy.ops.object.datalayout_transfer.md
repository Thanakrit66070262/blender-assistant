# bpy.ops.object.datalayout_transfer

## Signature
```python
bpy.ops.object.datalayout_transfer(*, modifier='', data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE')Â
Description
Transfer layout of data layer(s) from active to selected meshes
Parameters:
modifier (str) â Modifier, Name of the modifier to edit (optional, never None)
data_type (Literal['', 'VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'COLOR_CORNER', 'UV', 'SMOOTH', 'FREESTYLE_FACE']) â Data Type, Which data to transfer (optional)
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
use_delete (bool) â Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source (optional)
layers_select_src (Literal[Dt Layers Select Src Items]) â Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)
layers_select_dst (Literal[Dt Layers Select Dst Items]) â Destination Layers Matching, How to match source and destination layers (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

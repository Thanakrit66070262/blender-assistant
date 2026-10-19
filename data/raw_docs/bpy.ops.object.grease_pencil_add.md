# bpy.ops.object.grease_pencil_add

## Signature
```python
bpy.ops.object.grease_pencil_add(*, type='EMPTY', use_in_front=True, stroke_depth_offset=0.05, use_lights=True, stroke_depth_order='3D', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))Â
Description
Add a Grease Pencil object to the scene
Parameters:
type (Literal[Object Gpencil Type Items]) â Type, (optional)
use_in_front (bool) â Show In Front, Show Line Art Grease Pencil in front of everything (optional)
stroke_depth_offset (float) â Stroke Offset, Stroke offset for the Line Art modifier (in [0, inf], optional)
use_lights (bool) â Use Lights, Use lights for this Grease Pencil object (optional)
stroke_depth_order (Literal['2D', '3D']) â Stroke Depth Order, Defines how the strokes are ordered in 3D space (for objects not displayed âIn Frontâ) (optional)
2D
2D Layers â Display strokes using Grease Pencil layers to define order.
3D
3D Location â Display strokes using real 3D position in 3D space.
radius (float) â Radius, (in [0, inf], optional)
align (Literal['WORLD', 'VIEW', 'CURSOR']) â Align, The alignment of the new object (optional)
WORLD
World â Align the new object to the world.
VIEW
View â Align the new object to the view.
CURSOR
3D Cursor â Use the 3D cursor orientation for the new object.
location (mathutils.Vector | Sequence[float]) â Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
rotation (mathutils.Euler | Sequence[float]) â Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
scale (mathutils.Vector | Sequence[float]) â Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.ops.mesh.rip_edge

## Signature
```python
bpy.ops.mesh.rip_edge(*, location=(0.0, 0.0, 0.0), direction=(0.0, 0.0, 0.0))Â
Description
Extend vertices along the edge closest to the cursor
Parameters:
location (mathutils.Vector | Sequence[float]) â Location, World-space ray origin for extending vertices (array of 3 items, in [-inf, inf], optional)
direction (mathutils.Vector | Sequence[float]) â Direction, World-space direction vector for extending vertices (array of 3 items, in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

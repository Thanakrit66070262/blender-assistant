# bpy.types.Object.crazyspace_displacement_to_deformed

## Signature
```python
crazyspace_displacement_to_deformed(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))Â
Description
Convert displacement vector from non-deformed object space to deformed object space
Parameters:
vertex_index (int) â vertex_index, (in [-inf, inf], optional)
displacement (mathutils.Vector | Sequence[float]) â displacement, (array of 3 items, in [-inf, inf], optional)
Returns:
displacement_deformed, (array of 3 items, in [-inf, inf])
Return type:
mathutils.Vector

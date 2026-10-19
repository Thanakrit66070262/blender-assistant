# bpy.ops.object.quick_fur

## Signature
```python
bpy.ops.object.quick_fur(*, density='MEDIUM', length=0.1, radius=0.001, view_percentage=1.0, apply_hair_guides=True, use_noise=True, use_frizz=True)Â
Description
Add a fur setup to the selected objects
Parameters:
density (Literal['LOW', 'MEDIUM', 'HIGH']) â Density, (optional)
length (float) â Length, (in [0.001, 100], optional)
radius (float) â Hair Radius, (in [0, 10], optional)
view_percentage (float) â View Percentage, (in [0, 1], optional)
apply_hair_guides (bool) â Apply Hair Guides, (optional)
use_noise (bool) â Noise, (optional)
use_frizz (bool) â Frizz, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object_quick_effects.py:103

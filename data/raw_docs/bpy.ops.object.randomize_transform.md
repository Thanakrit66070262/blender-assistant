# bpy.ops.object.randomize_transform

## Signature
```python
bpy.ops.object.randomize_transform(*, random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0))Â
Description
Randomize objects location, rotation, and scale
Parameters:
random_seed (int) â Random Seed, Seed value for the random generator (in [0, 10000], optional)
use_delta (bool) â Transform Delta, Randomize delta transform values instead of regular transform (optional)
use_loc (bool) â Randomize Location, Randomize the location values (optional)
loc (mathutils.Vector | Sequence[float]) â Location, Maximum distance the objects can spread over each axis (array of 3 items, in [-100, 100], optional)
use_rot (bool) â Randomize Rotation, Randomize the rotation values (optional)
rot (mathutils.Euler | Sequence[float]) â Rotation, Maximum rotation over each axis (array of 3 items, in [-3.14159, 3.14159], optional)
use_scale (bool) â Randomize Scale, Randomize the scale values (optional)
scale_even (bool) â Scale Even, Use the same scale value for all axis (optional)
scale (Sequence[float]) â Scale, Maximum scale randomization over each axis (array of 3 items, in [-100, 100], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object_randomize_transform.py:163

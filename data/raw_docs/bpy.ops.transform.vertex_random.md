# bpy.ops.transform.vertex_random

## Signature
```python
bpy.ops.transform.vertex_random(*, offset=0.0, uniform=0.0, normal=0.0, seed=0, wait_for_input=True)Â
Description
Randomize vertices
Parameters:
offset (float) â Amount, Distance to offset (in [-inf, inf], optional)
uniform (float) â Uniform, Increase for uniform offset distance (in [0, 1], optional)
normal (float) â Normal, Align offset direction to normals (in [0, 1], optional)
seed (int) â Random Seed, Seed for the random number generator (in [0, 10000], optional)
wait_for_input (bool) â Wait for Input, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

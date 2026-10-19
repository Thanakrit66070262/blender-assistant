# bpy.ops.object.vertex_group_mirror

## Signature
```python
bpy.ops.object.vertex_group_mirror(*, mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False)Â
Description
Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected
Parameters:
mirror_weights (bool) â Mirror Weights, Mirror weights (optional)
flip_group_names (bool) â Flip Group Names, Flip vertex group names (optional)
all_groups (bool) â All Groups, Mirror all vertex groups weights (optional)
use_topology (bool) â Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

# bpy.types.Object.convert_space

## Signature
```python
convert_space(*, pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD')Â
Description
Convert (transform) the given matrix from one space to another
Parameters:
pose_bone (PoseBone | None) â Bone to use to define spaces (may be None, in which case only the two âWORLDâ and âLOCALâ spaces are usable) (optional)
matrix (mathutils.Matrix | Sequence[Sequence[float]]) â The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
from_space (Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) â The space in which âmatrixâ is currently (optional)
WORLD
World Space â The most global space in Blender.
POSE
Pose Space â The pose space of a bone (its armatureâs object space).
LOCAL_WITH_PARENT
Local With Parent â The rest pose local space of a bone (this matrix includes parent transforms).
LOCAL
Local Space â The local space of an object/bone.
to_space (Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) â The space to which you want to transform âmatrixâ (optional)
WORLD
World Space â The most global space in Blender.
POSE
Pose Space â The pose space of a bone (its armatureâs object space).
LOCAL_WITH_PARENT
Local With Parent â The rest pose local space of a bone (this matrix includes parent transforms).
LOCAL
Local Space â The local space of an object/bone.
Returns:
The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
Return type:
mathutils.Matrix

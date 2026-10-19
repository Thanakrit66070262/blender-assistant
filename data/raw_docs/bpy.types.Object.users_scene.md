# bpy.types.Object.users_scene

## Signature
```python
users_sceneÂ
Description
The scenes this object is in.
Type:
tuple[Scene, â¦]
Note
Takes O(len(bpy.data.scenes) * len(bpy.data.objects)) time.
(readonly)

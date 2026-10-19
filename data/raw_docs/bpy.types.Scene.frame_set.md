# bpy.types.Scene.frame_set

## Signature
```python
frame_set(frame, *, subframe=0.0)Â
Description
Set scene frame updating all objects and view layers immediately
Parameters:
frame (int) â Frame number to set (in [-1048574, 1048574])
subframe (float) â Subframe time, between 0.0 and 1.0 (in [0, 1], optional)

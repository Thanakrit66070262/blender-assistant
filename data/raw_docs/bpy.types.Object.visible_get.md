# bpy.types.Object.visible_get

## Signature
```python
visible_get(*, view_layer=None, viewport=None)Â
Description
Test if the object is visible in the 3D viewport, taking into account all visibility settings
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
viewport (SpaceView3D | None) â Use this instead of the active 3D viewport (optional)
Returns:
Object visible
Return type:
bool

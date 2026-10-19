# bpy.types.Object.is_modified

## Signature
```python
is_modified(scene, settings)Â
Description
Determine if this object is modified from the base mesh data
Parameters:
scene (Scene | None) â Scene in which to check the object (never None)
settings (Literal['PREVIEW', 'RENDER']) â Modifier settings to apply
PREVIEW
Preview â Apply modifier preview settings.
RENDER
Render â Apply modifier render settings.
Returns:
Whether the object is modified
Return type:
bool

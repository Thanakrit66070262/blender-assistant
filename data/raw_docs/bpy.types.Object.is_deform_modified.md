# bpy.types.Object.is_deform_modified

## Signature
```python
is_deform_modified(scene, settings)Â
Description
Determine if this object is modified by a deformation from the base mesh data
Parameters:
scene (Scene | None) â Scene in which to check the object (never None)
settings (Literal['PREVIEW', 'RENDER']) â Modifier settings to apply
PREVIEW
Preview â Apply modifier preview settings.
RENDER
Render â Apply modifier render settings.
Returns:
Whether the object is deform-modified
Return type:
bool

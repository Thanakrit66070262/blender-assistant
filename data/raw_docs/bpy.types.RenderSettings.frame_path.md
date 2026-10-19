# bpy.types.RenderSettings.frame_path

## Signature
```python
frame_path(*, frame=-2147483648, preview=False, view='')Â
Description
Return the absolute path to the filename to be written for a given frame
Parameters:
frame (int) â Frame number to use, if unset the current frame will be used (in [-inf, inf], optional)
preview (bool) â Preview, Use preview range (optional)
view (str) â View, The name of the view to use to replace the â%â chars (optional, never None)
Returns:
File Path, The resulting filepath from the scenes render settings (never None)
Return type:
str

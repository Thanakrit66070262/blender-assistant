# bpy.ops.object.make_links_data

## Signature
```python
bpy.ops.object.make_links_data(*, type='OBDATA')Â
Description
Transfer data from active object to selected objects
Parameters:
type (Literal['OBDATA', 'MATERIAL', 'ANIMATION', 'GROUPS', 'DUPLICOLLECTION', 'FONTS', 'MODIFIERS', 'CONSTRAINTS', 'EFFECTS', 'LIGHT_LINKING', 'SHADOW_LINKING']) â Type, (optional)
OBDATA
Link Object Data â Replace assigned Object Data.
MATERIAL
Link Materials â Replace assigned Materials.
ANIMATION
Link Animation Data â Replace assigned Animation Data.
GROUPS
Link Collections â Replace assigned Collections.
DUPLICOLLECTION
Link Instance Collection â Replace assigned Collection Instance.
FONTS
Link Fonts to Text â Replace Text object Fonts.
MODIFIERS
Copy Modifiers â Replace Modifiers.
CONSTRAINTS
Copy Constraints â Replace Constraints.
EFFECTS
Copy Grease Pencil Effects â Replace Grease Pencil Effects.
LIGHT_LINKING
Copy Light Linking â Replace assigned Light Linking collection.
SHADOW_LINKING
Copy Shadow Linking â Replace assigned Shadow Linking collection.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

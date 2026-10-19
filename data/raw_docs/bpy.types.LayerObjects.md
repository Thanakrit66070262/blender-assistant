# bpy.types.LayerObjects

## Signature
```python
class bpy.types.LayerObjects(bpy_prop_collection)Â
Description
Collections of objects
activeÂ
Active object for this layer
Type:
Object | None
selectedÂ
All the selected objects of this layer (default None, readonly)
Type:
bpy_prop_collection[Object]
classmethod bl_rna_get_subclass(id, default=None, /)Â
Parameters:
id (str) â The RNA type identifier.
default (bpy.types.Struct | None) â The value to return when not found.
Returns:
The RNA type or default when not found.
Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)Â
Parameters:
id (str) â The RNA type identifier.
default (type | None) â The value to return when not found.
Returns:
The class or default when not found.
Return type:
type

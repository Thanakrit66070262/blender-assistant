# bpy.types.ObjectModifiers

## Signature
```python
class bpy.types.ObjectModifiers(bpy_prop_collection)Â
Description
Collection of object modifiers
activeÂ
The active modifier in the list
Type:
Modifier | None
new(name, type)Â
Add a new modifier
Parameters:
name (str) â New name for the modifier (never None)
type (Literal[Object Modifier Type Items]) â Modifier type to add
Returns:
Newly created modifier
Return type:
Modifier
remove(modifier)Â
Remove an existing modifier from the object
Parameters:
modifier (Modifier | None) â Modifier to remove (never None)
clear()Â
Remove all modifiers from the object
move(from_index, to_index)Â
Move a modifier to a different position
Parameters:
from_index (int) â From Index, Index to move (in [-inf, inf])
to_index (int) â To Index, Target index (in [-inf, inf])
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

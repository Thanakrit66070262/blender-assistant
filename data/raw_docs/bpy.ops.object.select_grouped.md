# bpy.ops.object.select_grouped

## Signature
```python
bpy.ops.object.select_grouped(*, extend=False, type='CHILDREN_RECURSIVE')Â
Description
Select all visible objects grouped by various properties
Parameters:
extend (bool) â Extend, Extend selection instead of deselecting everything first (optional)
type (Literal['CHILDREN_RECURSIVE', 'CHILDREN', 'PARENT', 'SIBLINGS', 'TYPE', 'COLLECTION', 'HOOK', 'PASS', 'COLOR', 'KEYINGSET', 'LIGHT_TYPE']) â Type, (optional)
CHILDREN_RECURSIVE
Children.
CHILDREN
Immediate Children.
PARENT
Parent.
SIBLINGS
Siblings â Shared parent.
TYPE
Type â Shared object type.
COLLECTION
Collection â Shared collection.
HOOK
Hook.
PASS
Pass â Render pass index.
COLOR
Color â Object color.
KEYINGSET
Keying Set â Objects included in active Keying Set.
LIGHT_TYPE
Light Type â Matching light types.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

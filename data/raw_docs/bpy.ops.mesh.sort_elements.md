# bpy.ops.mesh.sort_elements

## Signature
```python
bpy.ops.mesh.sort_elements(*, type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0)Â
Description
The order of selected vertices/edges/faces is modified, based on a given method
Parameters:
type (Literal['VIEW_ZAXIS', 'VIEW_XAXIS', 'CURSOR_DISTANCE', 'MATERIAL', 'SELECTED', 'RANDOMIZE', 'REVERSE']) â Type, Type of reordering operation to apply (optional)
VIEW_ZAXIS
View Z Axis â Sort selected elements from farthest to nearest one in current view.
VIEW_XAXIS
View X Axis â Sort selected elements from left to right one in current view.
CURSOR_DISTANCE
Cursor Distance â Sort selected elements from nearest to farthest from 3D cursor.
MATERIAL
Material â Sort selected faces from smallest to greatest material index.
SELECTED
Selected â Move all selected elements in first places, preserving their relative order.
Warning: This will affect unselected elementsâ indices as well.
RANDOMIZE
Randomize â Randomize order of selected elements.
REVERSE
Reverse â Reverse current order of selected elements.
elements (set[Literal['VERT', 'EDGE', 'FACE']]) â Elements, Which elements to affect (vertices, edges and/or faces) (optional)
reverse (bool) â Reverse, Reverse the sorting effect (optional)
seed (int) â Seed, Seed for random-based operations (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

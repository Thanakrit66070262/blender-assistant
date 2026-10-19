# bpy.ops.mesh.intersect

## Signature
```python
bpy.ops.mesh.intersect(*, mode='SELECT_UNSELECT', separate_mode='CUT', threshold=1e-06, solver='EXACT')Â
Description
Cut an intersection into faces
Parameters:
mode (Literal['SELECT', 'SELECT_UNSELECT']) â Source, (optional)
SELECT
Self Intersect â Self intersect selected faces.
SELECT_UNSELECT
Selected/Unselected â Intersect selected with unselected faces.
separate_mode (Literal['ALL', 'CUT', 'NONE']) â Separate Mode, (optional)
ALL
All â Separate all geometry from intersections.
CUT
Cut â Cut into geometry keeping each side separate (Selected/Unselected only).
NONE
Merge â Merge all geometry from the intersection.
threshold (float) â Merge Threshold, (in [0, 0.01], optional)
solver (Literal['FLOAT', 'EXACT']) â Solver, Which Intersect solver to use (optional)
FLOAT
Float â Simple solver with good performance, without support for overlapping geometry.
EXACT
Exact â Slower solver with the best results for coplanar faces.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

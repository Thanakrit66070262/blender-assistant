# bpy.ops.mesh.intersect_boolean

## Signature
```python
bpy.ops.mesh.intersect_boolean(*, operation='DIFFERENCE', use_swap=False, use_self=False, threshold=1e-06, solver='EXACT')Â
Description
Cut solid geometry from selected to unselected
Parameters:
operation (Literal['INTERSECT', 'UNION', 'DIFFERENCE']) â Boolean Operation, Which boolean operation to apply (optional)
use_swap (bool) â Swap, Use with difference intersection to swap which side is kept (optional)
use_self (bool) â Self Intersection, Do self-union or self-intersection (optional)
threshold (float) â Merge Threshold, (in [0, 0.01], optional)
solver (Literal['FLOAT', 'EXACT']) â Solver, Which Boolean solver to use (optional)
FLOAT
Float â Faster solver, some limitations.
EXACT
Exact â Exact solver, slower, handles more cases.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

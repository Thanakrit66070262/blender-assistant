# bpy.ops.mesh.select_mode

## Signature
```python
bpy.ops.mesh.select_mode(*, use_extend=False, use_expand=False, type='VERT', action='TOGGLE')Â
Description
Change selection mode
Parameters:
use_extend (bool) â Extend, (optional)
use_expand (bool) â Expand, (optional)
type (Literal[Mesh Select Mode Items]) â Type, (optional)
action (Literal['DISABLE', 'ENABLE', 'TOGGLE']) â Action, Selection action to execute (optional)
DISABLE
Disable â Disable the selection mode.
ENABLE
Enable â Enable the selection mode.
TOGGLE
Toggle â Toggle the selection mode.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

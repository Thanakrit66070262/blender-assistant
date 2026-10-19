# bpy.ops.object.select_random

## Signature
```python
bpy.ops.object.select_random(*, ratio=0.5, seed=0, action='SELECT')Â
Description
Select or deselect random visible objects
Parameters:
ratio (float) â Ratio, Portion of items to select randomly (in [0, 1], optional)
seed (int) â Random Seed, Seed for the random number generator (in [0, inf], optional)
action (Literal['SELECT', 'DESELECT']) â Action, Selection action to execute (optional)
SELECT
Select â Select all elements.
DESELECT
Deselect â Deselect all elements.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

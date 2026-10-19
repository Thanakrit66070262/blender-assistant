# bpy.ops.object.quick_explode

## Signature
```python
bpy.ops.object.quick_explode(*, style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True)Â
Description
Make selected objects explode
Parameters:
style (Literal['EXPLODE', 'BLEND']) â Explode Style, (optional)
amount (int) â Number of Pieces, (in [2, 10000], optional)
frame_duration (int) â Duration, (in [1, 300000], optional)
frame_start (int) â Start Frame, (in [1, 300000], optional)
frame_end (int) â End Frame, (in [1, 300000], optional)
velocity (float) â Outwards Velocity, (in [0, 300000], optional)
fade (bool) â Fade, Fade the pieces over time (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
File:
startup/bl_operators/object_quick_effects.py:284

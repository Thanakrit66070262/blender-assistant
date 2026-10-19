# bpy.types.Scene.playback_loop_mode

## Signature
```python
playback_loop_modeÂ
Description
What to do when playback reaches the last frame (default 'INFINITE')
INFINITE
Infinite â After the last frame, jump back to the first and keep playing, infinitely.
STOP_END_FRAME
Stop at End Frame â Stop playback at the last frame, without looping.
STOP_START_FRAME
Stop at Start Frame â After the last frame, jump back to the first and stop playback.
RESTORE
Restore Frame â After the last frame, stop at the frame the playback started from.
BOUNCE
Bounce â At the last frame, reverse playback.
Type:
Literal[âINFINITEâ, âSTOP_END_FRAMEâ, âSTOP_START_FRAMEâ, âRESTOREâ, âBOUNCEâ]

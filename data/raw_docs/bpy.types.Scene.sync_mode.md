# bpy.types.Scene.sync_mode

## Signature
```python
sync_modeÂ
Description
How to sync playback (default 'AUDIO_SYNC')
NONE
Play Every Frame â Do not sync, play every frame.
FRAME_DROP
Frame Dropping â Drop frames if playback is too slow.
AUDIO_SYNC
Sync to Audio â Sync to audio playback, dropping frames.
Type:
Literal[âNONEâ, âFRAME_DROPâ, âAUDIO_SYNCâ]

# bpy.ops.object.lightprobe_cache_free

## Signature
```python
bpy.ops.object.lightprobe_cache_free(*, subset='SELECTED')Â
Description
Delete cached indirect lighting
Parameters:
subset (Literal['ALL', 'SELECTED', 'ACTIVE']) â Subset, Subset of probes to update (optional)
ALL
All Light Probes â Delete all light probesâ baked lighting data.
SELECTED
Selected Only â Only delete selected light probesâ baked lighting data.
ACTIVE
Active Only â Only delete the active light probeâs baked lighting data.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

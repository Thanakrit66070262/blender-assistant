# bpy.ops.object.lightprobe_cache_bake

## Signature
```python
bpy.ops.object.lightprobe_cache_bake(*, subset='ALL')Â
Description
Bake irradiance volume light cache
Parameters:
subset (Literal['ALL', 'SELECTED', 'ACTIVE']) â Subset, Subset of probes to update (optional)
ALL
All Volumes â Bake all light probe volumes.
SELECTED
Selected Only â Only bake selected light probe volumes.
ACTIVE
Active Only â Only bake the active light probe volume.
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

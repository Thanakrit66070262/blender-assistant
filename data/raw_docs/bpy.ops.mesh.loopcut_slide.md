# bpy.ops.mesh.loopcut_slide

## Signature
```python
bpy.ops.mesh.loopcut_slide(*, MESH_OT_loopcut={}, TRANSFORM_OT_edge_slide={})Â
Description
Cut mesh loop and slide it
Parameters:
MESH_OT_loopcut (dict[str, Any]) â Loop Cut, Add a new loop between existing loops (optional, bpy.ops.mesh.loopcut() keyword arguments)
TRANSFORM_OT_edge_slide (dict[str, Any]) â Edge Slide, Slide an edge loop along a mesh (optional, bpy.ops.transform.edge_slide() keyword arguments)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

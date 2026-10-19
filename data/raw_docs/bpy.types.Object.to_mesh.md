# bpy.types.Object.to_mesh

## Signature
```python
to_mesh(*, preserve_all_data_layers=False, depsgraph=None)Â
Description
Create a Mesh data-block from the current state of the object. The object owns the data-block. To force free it use to_mesh_clear(). The result is temporary and cannot be used by objects from the main database.
Parameters:
preserve_all_data_layers (bool) â Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)
Returns:
Mesh created from object
Return type:
Mesh

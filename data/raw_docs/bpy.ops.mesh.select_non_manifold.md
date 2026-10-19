# bpy.ops.mesh.select_non_manifold

## Signature
```python
bpy.ops.mesh.select_non_manifold(*, extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True)Â
Description
Select all non-manifold vertices or edges
Parameters:
extend (bool) â Extend, Extend the selection (optional)
use_wire (bool) â Wire, Wire edges (optional)
use_boundary (bool) â Boundaries, Boundary edges (optional)
use_multi_face (bool) â Multiple Faces, Edges shared by more than two faces (optional)
use_non_contiguous (bool) â Non Contiguous, Edges between faces pointing in alternate directions (optional)
use_verts (bool) â Vertices, Vertices connecting multiple face regions (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]

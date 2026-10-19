# bpy.ops.mesh.convex_hull

## Signature
```python
bpy.ops.mesh.convex_hull(*, delete_unused=True, use_existing_faces=True, make_holes=False, join_triangles=True, face_threshold=0.698132, shape_threshold=0.698132, topology_influence=0.0, uvs=False, vcols=False, seam=False, sharp=False, materials=False, deselect_joined=False)Â
Description
Enclose selected vertices in a convex polyhedron
Parameters:
delete_unused (bool) â Delete Unused, Delete selected elements that are not used by the hull (optional)
use_existing_faces (bool) â Use Existing Faces, Skip hull triangles that are covered by a pre-existing face (optional)
make_holes (bool) â Make Holes, Delete selected faces that are used by the hull (optional)
join_triangles (bool) â Join Triangles, Merge adjacent triangles into quads (optional)
face_threshold (float) â Max Face Angle, Face angle limit (in [0, 3.14159], optional)
shape_threshold (float) â Max Shape Angle, Shape angle limit (in [0, 3.14159], optional)
topology_influence (float) â Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads (in [0, 2], optional)
uvs (bool) â Compare UVs, (optional)
vcols (bool) â Compare Color Attributes, (optional)
seam (bool) â Compare Seam, (optional)
sharp (bool) â Compare Sharp, (optional)
materials (bool) â Compare Materials, (optional)
deselect_joined (bool) â Deselect Joined, Only select remaining triangles that were not merged (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
